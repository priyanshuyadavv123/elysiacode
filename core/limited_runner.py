"""
Elysia Code - limited Python runner for the optional SERVER-SIDE code execution.

IMPORTANT - what this is and is not
  * It is HARDENING: temp folder, empty environment, CPU/memory/file/process
    limits, output cap and a hard timeout that kills the whole process group.
  * It is NOT a security boundary. The code still runs as the same operating
    system user and can use the network or read files that user can read.
  * So the server only turns it on when it is bound to localhost (your own
    computer), or when you explicitly set ELYSIA_ALLOW_SERVER_EXEC=1.
  * On a public site, run student code in the browser (Pyodide web worker).

Design note: limits are applied by a tiny bootstrap script INSIDE the child
process (not with preexec_fn, which is unsafe in multi-threaded servers).
"""

import os
import shutil
import signal
import subprocess
import sys
import tempfile
import threading

MAX_OUTPUT_BYTES = 100_000     # stdout and stderr together
MAX_CODE_CHARS = 50_000
MAX_STDIN_CHARS = 20_000
MAX_TIMEOUT = 5.0

_BOOTSTRAP = r'''
import sys, traceback
try:
    import resource
    def _limit(which, value):
        try:
            resource.setrlimit(which, (value, value))
        except Exception:
            pass
    _limit(resource.RLIMIT_CPU, int(float(sys.argv[2])) + 1)
    _limit(resource.RLIMIT_AS, 512 * 1024 * 1024)
    _limit(resource.RLIMIT_FSIZE, 1024 * 1024)
    _limit(resource.RLIMIT_NOFILE, 64)
    if hasattr(resource, "RLIMIT_NPROC"):
        _limit(resource.RLIMIT_NPROC, 64)
except ImportError:
    pass                                   # Windows: no resource module

with open(sys.argv[1], encoding="utf-8") as _f:
    _src = _f.read()
sys.argv = ["main.py"]
_g = {"__name__": "__main__", "__builtins__": __builtins__}
try:
    _code = compile(_src, "<string>", "exec")
    exec(_code, _g)
except SystemExit:
    raise
except BaseException:
    _t, _v, _tb = sys.exc_info()
    traceback.print_exception(_t, _v, _tb.tb_next if _tb is not None else None)
    sys.exit(1)
'''


def _kill_group(proc):
    try:
        if os.name == "posix":
            os.killpg(proc.pid, signal.SIGKILL)
        else:
            proc.kill()
    except Exception:
        try:
            proc.kill()
        except Exception:
            pass


def run_python(code, stdin_text="", timeout=3.0, max_output=MAX_OUTPUT_BYTES):
    """Run code and return {"status", "stdout", "stderr", "exit_code"}.

    status is one of: ok, timeout, output_limit, error
    """
    code = str(code or "")
    if len(code) > MAX_CODE_CHARS:
        return {"status": "error", "stdout": "", "exit_code": 1,
                "stderr": "Code exceeds maximum size limit (%d characters)." % MAX_CODE_CHARS}
    try:
        timeout = float(timeout)
    except (TypeError, ValueError):
        timeout = 3.0
    if not (0.1 <= timeout <= MAX_TIMEOUT):          # also rejects nan / inf
        timeout = min(max(timeout if timeout == timeout else 3.0, 0.1), MAX_TIMEOUT)

    stdin_text = str(stdin_text or "")[:MAX_STDIN_CHARS]
    workdir = tempfile.mkdtemp(prefix="elysia_run_")
    try:
        code_path = os.path.join(workdir, "main.py")
        with open(code_path, "w", encoding="utf-8") as f:
            f.write(code)

        env = {"PYTHONIOENCODING": "utf-8", "PYTHONDONTWRITEBYTECODE": "1",
               "LANG": "C.UTF-8", "PATH": "/usr/bin:/bin"}
        if os.name == "nt":                            # Windows needs a few variables
            env["SYSTEMROOT"] = os.environ.get("SYSTEMROOT", "")

        kwargs = {}
        if os.name == "posix":
            kwargs["start_new_session"] = True         # own process group, so we can kill all
        try:
            proc = subprocess.Popen(
                [sys.executable, "-I", "-c", _BOOTSTRAP, code_path, str(timeout)],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                cwd=workdir, env=env, **kwargs)
        except Exception as exc:
            return {"status": "error", "stdout": "", "exit_code": 1,
                    "stderr": "System execution error: %s" % exc}

        state = {"bytes": 0, "over": False}
        chunks = {"out": [], "err": []}
        lock = threading.Lock()

        def reader(stream, key):
            while True:
                data = stream.read1(4096) if hasattr(stream, "read1") else stream.read(4096)
                if not data:
                    break
                with lock:
                    room = max_output - state["bytes"]
                    if room > 0:
                        chunks[key].append(data[:room])
                    state["bytes"] += len(data)
                    if state["bytes"] > max_output and not state["over"]:
                        state["over"] = True
                        _kill_group(proc)

        def feeder():
            try:
                proc.stdin.write(stdin_text.encode("utf-8", "replace"))
                proc.stdin.close()
            except Exception:
                pass                                   # program ended before reading input

        threads = [threading.Thread(target=reader, args=(proc.stdout, "out"), daemon=True),
                   threading.Thread(target=reader, args=(proc.stderr, "err"), daemon=True),
                   threading.Thread(target=feeder, daemon=True)]
        for t in threads:
            t.start()

        status = "ok"
        try:
            proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            status = "timeout"
            _kill_group(proc)
            proc.wait()
        _kill_group(proc)                              # make sure no child survives
        for t in threads[:2]:
            t.join(timeout=1.0)
        for stream in (proc.stdout, proc.stderr, proc.stdin):     # do not leak file descriptors
            try:
                stream.close()
            except Exception:
                pass

        out = b"".join(chunks["out"]).decode("utf-8", "replace")
        err = b"".join(chunks["err"]).decode("utf-8", "replace")
        if state["over"]:
            status = "output_limit"
            err = (err + "\nOutput limit reached (%d KB). Does your loop print forever?" % (max_output // 1000)).strip()
        elif status == "timeout":
            err = "Execution timed out (> %ss)! Infinite loop detected." % timeout
        return {"status": status, "stdout": out, "stderr": err,
                "exit_code": 124 if status == "timeout" else (proc.returncode if proc.returncode is not None else 1)}
    finally:
        shutil.rmtree(workdir, ignore_errors=True)
