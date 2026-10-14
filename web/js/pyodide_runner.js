/**
 * =============================================================================
 * Elysia Code - PYODIDE MANAGER (page side)
 * =============================================================================
 * Runs the student's Python in the BROWSER (WebAssembly) inside a Web Worker.
 *
 *  - Safe for a public website: the code never touches your server.
 *  - Infinite loops are survivable: after `timeoutMs` the worker is terminated and
 *    the student gets a friendly message. (A fresh worker starts on the next Run;
 *    the Python engine is cached by the browser, so this is fast after the first time.)
 *  - HONEST: if the engine cannot be loaded (offline / CDN blocked) we say so.
 *    The old "fallback runner" pretended to run Python by pattern-matching print()
 *    and even returned hard-coded numbers, which showed students WRONG output.
 *
 * Public API (unchanged names):  window.pyodideManager.init()  /  .run(code, stdin, timeoutMs)
 * run() always resolves to { success, stdout, stderr, error, timedOut }
 * =============================================================================
 */

class PyodideManager {
  constructor() {
    this.worker = null;
    this.isReady = false;
    this.isLoading = false;
    this._readyPromise = null;
    this._nextId = 1;
    this._queue = Promise.resolve();   // runs are executed one after another
  }

  _spawn() {
    this.isReady = false;
    this.isLoading = true;
    this.worker = new Worker("js/pyodide_worker.js");
    const worker = this.worker;

    this._readyPromise = new Promise((resolve, reject) => {
      worker.addEventListener("message", (e) => {
        if (e.data && e.data.type === "ready") {
          this.isReady = true;
          this.isLoading = false;
          window.dispatchEvent(new CustomEvent("pyodide:ready"));
          resolve();
        } else if (e.data && e.data.type === "init-error") {
          this.isLoading = false;
          window.dispatchEvent(new CustomEvent("pyodide:error", { detail: e.data.message }));
          reject(new Error(e.data.message));
        }
      });
      // importScripts() failing (no internet / CDN blocked) fires "error" on the worker
      worker.addEventListener("error", (e) => {
        this.isLoading = false;
        window.dispatchEvent(new CustomEvent("pyodide:error", { detail: (e && e.message) || "Failed to load worker" }));
        reject(new Error((e && e.message) || "Python engine failed to load"));
      });
    });
    this._readyPromise.catch(() => {});   // avoid "unhandled rejection" noise
  }

  /** Start loading the engine in the background (safe to call many times). */
  init() {
    if (!this.worker) this._spawn();
    return this._readyPromise;
  }

  _discardWorker() {
    if (this.worker) this.worker.terminate();
    this.worker = null;
    this._readyPromise = null;
    this.isReady = false;
    this.isLoading = false;
  }

  /**
   * Run Python code. stdin = text for input() calls (one answer per line).
   */
  run(code, stdin = "", timeoutMs = 5000) {
    const job = this._queue.then(() => this._runNow(code, stdin, timeoutMs));
    this._queue = job.catch(() => {});
    return job;
  }

  async _runNow(code, stdin, timeoutMs) {
    try {
      await this.init();
    } catch (err) {
      this._discardWorker();
      const msg = "Python engine could not be loaded. Check your internet connection and press Run again.";
      return { success: false, stdout: "", stderr: msg, error: msg, timedOut: false };
    }

    const worker = this.worker;
    const id = this._nextId++;

    return new Promise((resolve) => {
      let finished = false;
      const finish = (result) => {
        if (finished) return;
        finished = true;
        clearTimeout(timer);
        worker.removeEventListener("message", onMessage);
        resolve(result);
      };
      const onMessage = (e) => {
        const m = e.data || {};
        if (m.type === "result" && m.id === id) {
          finish({
            success: !m.stderr,
            stdout: m.stdout || "",
            stderr: m.stderr || "",
            error: m.stderr || null,
            timedOut: false,
          });
        }
      };
      const timer = setTimeout(() => {
        this._discardWorker();   // kills the infinite loop for real
        const secs = Math.round(timeoutMs / 100) / 10;
        const msg = `Execution timed out (>${secs}s)! Infinite loop detected. ` +
                    `Does your while loop change the variable used in its condition?`;
        finish({ success: false, stdout: "", stderr: msg, error: msg, timedOut: true });
      }, timeoutMs);

      worker.addEventListener("message", onMessage);
      worker.postMessage({ type: "run", id: id, code: String(code || ""), stdin: String(stdin || "") });
    });
  }

  /**
   * Run a single line or statement interactively in Pyodide REPL mode.
   * State (assigned variables) is preserved across REPL calls.
   */
  runRepl(code, timeoutMs = 4000) {
    const job = this._queue.then(() => this._runReplNow(code, timeoutMs));
    this._queue = job.catch(() => {});
    return job;
  }

  async _runReplNow(code, timeoutMs) {
    try {
      await this.init();
    } catch (err) {
      this._discardWorker();
      return { success: false, stdout: "", stderr: "Pyodide could not load", result: "" };
    }

    const worker = this.worker;
    const id = this._nextId++;

    return new Promise((resolve) => {
      let finished = false;
      const finish = (result) => {
        if (finished) return;
        finished = true;
        clearTimeout(timer);
        worker.removeEventListener("message", onMessage);
        resolve(result);
      };
      const onMessage = (e) => {
        const m = e.data || {};
        if (m.type === "repl-result" && m.id === id) {
          finish({
            success: !m.stderr,
            stdout: m.stdout || "",
            stderr: m.stderr || "",
            result: m.result || ""
          });
        }
      };
      const timer = setTimeout(() => {
        this._discardWorker();
        finish({ success: false, stdout: "", stderr: "Timed out", result: "" });
      }, timeoutMs);

      worker.addEventListener("message", onMessage);
      worker.postMessage({ type: "repl", id: id, code: String(code || "") });
    });
  }
}

// Global singleton instance
window.pyodideManager = new PyodideManager();
