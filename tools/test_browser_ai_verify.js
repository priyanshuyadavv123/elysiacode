/**
 * Headless Chrome test for Phase 2:
 * Verifies AI answers in the browser using the Pyodide Web Worker.
 * Tests:
 * 1. Matching AI question updates badge to "Verified in your browser"
 * 2. Mismatched AI question updates badge to "AI answer differs - trust your own run" and displays actual output
 */

const { spawn } = require("child_process");
const http = require("http");

const CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const DEBUG_PORT = 9228;

async function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function httpGetJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, (res) => {
      let data = "";
      res.on("data", (chunk) => (data += chunk));
      res.on("end", () => {
        try {
          resolve(JSON.parse(data));
        } catch (e) {
          reject(e);
        }
      });
    }).on("error", reject);
  });
}

async function runTest() {
  console.log("1. Starting headless Chrome on port", DEBUG_PORT);
  const chrome = spawn(CHROME_PATH, [
    "--headless=new",
    `--remote-debugging-port=${DEBUG_PORT}`,
    "--disable-gpu",
    "--no-first-run",
    "--no-default-browser-check"
  ]);

  chrome.on("error", (err) => {
    console.error("Failed to spawn Chrome:", err);
    process.exit(1);
  });

  try {
    let targets = null;
    for (let i = 0; i < 20; i++) {
      await sleep(300);
      try {
        targets = await httpGetJson(`http://127.0.0.1:${DEBUG_PORT}/json/list`);
        if (targets && targets.length > 0) break;
      } catch (e) {}
    }

    if (!targets || !targets[0] || !targets[0].webSocketDebuggerUrl) {
      throw new Error("Could not connect to Chrome debugging target");
    }

    const wsUrl = targets[0].webSocketDebuggerUrl;
    console.log("2. Connected to Chrome CDP target:", wsUrl);

    const ws = new WebSocket(wsUrl);

    let id = 1;
    const callbacks = new Map();

    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      if (msg.id && callbacks.has(msg.id)) {
        callbacks.get(msg.id)(msg);
        callbacks.delete(msg.id);
      }
    };

    await new Promise((resolve) => (ws.onopen = resolve));

    function sendCmd(method, params = {}) {
      return new Promise((resolve) => {
        const msgId = id++;
        callbacks.set(msgId, resolve);
        ws.send(JSON.stringify({ id: msgId, method, params }));
      });
    }

    await sendCmd("Page.enable");
    await sendCmd("Runtime.enable");

    console.log("3. Navigating to http://127.0.0.1:8080/ ...");
    await sendCmd("Page.navigate", { url: "http://127.0.0.1:8080/" });

    console.log("4. Waiting for ElysiaApp to initialize...");
    for (let i = 0; i < 40; i++) {
      const evalRes = await sendCmd("Runtime.evaluate", {
        expression: "Boolean(window.elysiaApp && document.getElementById('questions-grid'))",
        returnByValue: true
      });
      if (evalRes.result && evalRes.result.result && evalRes.result.result.value) {
        break;
      }
      await sleep(300);
    }

    console.log("5. Injecting matching & mismatched mocked AI questions into QBank...");
    const injectCode = `
      (function() {
        const q_match = {
          id: "mock_ai_match_101",
          subject: "python",
          difficulty: "Beginner",
          title_en: "Add Numbers Match",
          desc_en: "Compute 2 + 3",
          starter_code: "print(2 + 3)",
          solution_code: "print(2 + 3)",
          expected_output: "5",
          output_verified: false,
          ai_generated: true
        };

        const q_diff = {
          id: "mock_ai_diff_102",
          subject: "python",
          difficulty: "Intermediate",
          title_en: "Mismatch Output Test",
          desc_en: "Hallucinated output test",
          starter_code: "print('Actual From Pyodide')",
          solution_code: "print('Actual From Pyodide')",
          expected_output: "Hallucinated AI Output",
          output_verified: false,
          ai_generated: true
        };

        window.elysiaApp.renderQuestions([q_match, q_diff]);
        return true;
      })()
    `;

    await sendCmd("Runtime.evaluate", {
      expression: injectCode,
      returnByValue: true
    });

    console.log("6. Polling for Pyodide worker verification results...");
    let verified = false;
    let matchBadgeText = "";
    let diffBadgeText = "";
    let diffBoxText = "";

    for (let i = 0; i < 40; i++) {
      await sleep(600);
      const checkRes = await sendCmd("Runtime.evaluate", {
        expression: `
          (function() {
            const b1 = document.getElementById("q-verify-badge-mock_ai_match_101");
            const b2 = document.getElementById("q-verify-badge-mock_ai_diff_102");
            const d2 = document.getElementById("q-verify-diff-out-mock_ai_diff_102");
            return {
              b1Text: b1 ? b1.textContent.trim() : "",
              b2Text: b2 ? b2.textContent.trim() : "",
              d2Text: d2 ? d2.textContent.trim() : ""
            };
          })()
        `,
        returnByValue: true
      });

      const val = checkRes.result && checkRes.result.result && checkRes.result.result.value;
      if (val) {
        matchBadgeText = val.b1Text;
        diffBadgeText = val.b2Text;
        diffBoxText = val.d2Text;

        if (
          matchBadgeText.includes("Verified in your browser") &&
          diffBadgeText.includes("AI answer differs") &&
          diffBoxText.includes("Actual From Pyodide")
        ) {
          verified = true;
          break;
        }
      }
    }

    console.log("7. Verification Results:");
    console.log("   - Question 1 (Matching) Badge:", matchBadgeText);
    console.log("   - Question 2 (Mismatched) Badge:", diffBadgeText);
    console.log("   - Question 2 Displayed Output:", diffBoxText);

    if (!verified) {
      throw new Error(`Verification failed! Q1="${matchBadgeText}", Q2="${diffBadgeText}", DiffBox="${diffBoxText}"`);
    }

    console.log("\n✅ SUCCESS: Phase 2 browser verification verified perfectly with matching and mismatched questions!");
    ws.close();
  } finally {
    chrome.kill("SIGTERM");
  }
}

runTest().catch((err) => {
  console.error("Test failed:", err);
  process.exit(1);
});
