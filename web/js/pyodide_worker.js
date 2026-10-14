/**
 * Elysia Code - Python engine that runs inside a Web Worker (Pyodide WebAssembly).
 *
 * Runs isolated in a background Web Worker so student code (and infinite loops)
 * never freezes the browser UI.
 * Loaded via high-speed jsDelivr CDN and cached by the browser.
 */

importScripts("https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js");

let pyodide = null;
let stdoutBuf = [];
let stderrBuf = [];
let stdinLines = [];

/** Remove Pyodide's internal stack frames so students only see THEIR code in the traceback. */
function cleanTraceback(message) {
  const text = String(message || "");
  const idx = text.indexOf('File "<exec>"');
  if (idx === -1) return text.trim();
  const lineStart = text.lastIndexOf("\n", idx) + 1;
  return "Traceback (most recent call last):\n" + text.slice(lineStart).trim();
}

async function init() {
  try {
    pyodide = await loadPyodide({
      indexURL: "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/",
      stdout: (t) => stdoutBuf.push(t),
      stderr: (t) => stderrBuf.push(t),
    });

    pyodide.setStdin({
      stdin: () => {
        const line = stdinLines.length ? stdinLines.shift() : "";
        stdoutBuf.push("> " + line);
        return line;
      },
    });
    self.postMessage({ type: "ready" });
  } catch (err) {
    self.postMessage({ type: "init-error", message: String((err && err.message) || err) });
  }
}

let replDict = null;

self.onmessage = async (event) => {
  const msg = event.data || {};
  if (!pyodide) return;

  if (msg.type === "repl") {
    if (!replDict) {
      replDict = pyodide.globals.get("dict")();
      replDict.set("__name__", "__main__");
    }
    stdoutBuf = [];
    stderrBuf = [];
    let resultVal = "";
    let stderr = "";
    try {
      const val = await pyodide.runPythonAsync(String(msg.code || ""), { globals: replDict });
      if (val !== undefined && val !== null) {
        resultVal = String(val);
        if (typeof val.destroy === "function") val.destroy();
      }
      stderr = stderrBuf.join("\n");
    } catch (err) {
      stderr = cleanTraceback(err && err.message);
    }
    self.postMessage({
      type: "repl-result",
      id: msg.id,
      stdout: stdoutBuf.join("\n"),
      stderr: stderr,
      result: resultVal
    });
    return;
  }

  if (msg.type !== "run") return;

  stdoutBuf = [];
  stderrBuf = [];
  stdinLines = String(msg.stdin || "").split("\n");
  if (stdinLines.length && stdinLines[stdinLines.length - 1] === "") stdinLines.pop();

  const ns = pyodide.globals.get("dict")();
  ns.set("__name__", "__main__");
  let stderr = "";
  try {
    await pyodide.runPythonAsync(String(msg.code || ""), { globals: ns });
    stderr = stderrBuf.join("\n");
  } catch (err) {
    stderr = cleanTraceback(err && err.message);
  } finally {
    ns.destroy();
  }
  self.postMessage({ type: "result", id: msg.id, stdout: stdoutBuf.join("\n"), stderr: stderr });
};

init();
