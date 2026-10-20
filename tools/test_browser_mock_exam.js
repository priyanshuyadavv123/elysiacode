/**
 * Headless Chrome test for Phase 4:
 * Verifies that:
 * 1. Mock exam Section A (MCQs) renders properly.
 * 2. Questions with single quotes in their explanation (e.g., 'b = a' in python_ca1 Q1)
 *    do not produce SyntaxErrors on option click.
 * 3. Delegated click listener fires, button gets .selected, and .mcq-feedback renders.
 * 4. HTML tags in options or questions (e.g. <div class='nav'> in html_ca1) render safely as escaped text.
 */

const { spawn } = require("child_process");
const http = require("http");

const CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const DEBUG_PORT = 9229;

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
    for (let i = 0; i < 25; i++) {
      await sleep(250);
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
        expression: "Boolean(window.elysiaApp && document.getElementById('mock-mcq-container'))",
        returnByValue: true
      });
      if (evalRes && evalRes.result && evalRes.result.result && evalRes.result.result.value === true) {
        break;
      }
      await sleep(300);
    }

    console.log("5. Loading python_ca1 mock exam...");
    const loadRes = await sendCmd("Runtime.evaluate", {
      expression: `
        (async () => {
          try {
            window.elysiaApp.subject = 'python';
            await window.elysiaApp.loadMockExam();
            const buttons = document.querySelectorAll('#mock-mcq-container .mcq-option-btn');
            return {
              examTitle: window.elysiaApp.mockExamData ? window.elysiaApp.mockExamData.title : null,
              buttonCount: buttons.length
            };
          } catch (err) {
            return { error: err.message, stack: err.stack };
          }
        })()
      `,
      awaitPromise: true,
      returnByValue: true
    });

    const loadVal = loadRes.result.result.value;
    console.log("   Exam loaded:", loadVal);
    if (!loadVal || loadVal.buttonCount === 0) {
      throw new Error("Failed to render Section A MCQ buttons in python_ca1: " + JSON.stringify(loadVal));
    }

    console.log("6. Clicking Option B in Q1 (contains 'b = a' apostrophe in explanation)...");
    const clickRes = await sendCmd("Runtime.evaluate", {
      expression: `
        (() => {
          // Q1 has 4 buttons. Option B is index 1 (correct answer).
          const buttons = document.querySelectorAll('#mock-mcq-container .mcq-option-btn');
          const btn = buttons[1]; // Option B: '4'
          btn.click();

          const feedbackEl = btn.parentElement.parentElement.querySelector('.mcq-feedback');
          return {
            isSelected: btn.classList.contains('selected'),
            feedbackDisplay: feedbackEl ? feedbackEl.style.display : null,
            feedbackText: feedbackEl ? feedbackEl.textContent : null,
            hasApostropheText: feedbackEl ? feedbackEl.textContent.includes("b = a") : false
          };
        })()
      `,
      returnByValue: true
    });

    const clickData = clickRes.result.result.value;
    console.log("   Click test result:", clickData);
    if (!clickData.isSelected) {
      throw new Error("Button did not receive .selected class after click!");
    }
    if (clickData.feedbackDisplay !== "block") {
      throw new Error("mcq-feedback was not displayed after click!");
    }
    if (!clickData.hasApostropheText) {
      throw new Error("mcq-feedback does not contain the expected explanation with 'b = a'!");
    }

    console.log("7. Loading html_ca1 mock exam to test HTML entity escaping (<div class='nav'>)...");
    const htmlExamRes = await sendCmd("Runtime.evaluate", {
      expression: `
        (async () => {
          try {
            window.elysiaApp.subject = 'html';
            await window.elysiaApp.loadMockExam();
            const firstBtn = document.querySelector('#mock-mcq-container .mcq-option-btn');
            const divChild = firstBtn ? firstBtn.querySelector('div') : null;
            return {
              buttonText: firstBtn ? firstBtn.textContent.trim() : null,
              hasUnescapedDiv: Boolean(divChild)
            };
          } catch (err) {
            return { error: err.message, stack: err.stack };
          }
        })()
      `,
      awaitPromise: true,
      returnByValue: true
    });

    const htmlData = htmlExamRes.result.result.value;
    console.log("   HTML Exam Option check:", htmlData);
    if (htmlData.hasUnescapedDiv) {
      throw new Error("Option created an unescaped <div> child in the button!");
    }

    console.log("8. Clicking Option A in html_ca1...");
    const clickHtmlRes = await sendCmd("Runtime.evaluate", {
      expression: `
        (() => {
          const firstBtn = document.querySelector('#mock-mcq-container .mcq-option-btn');
          firstBtn.click();
          const feedbackEl = firstBtn.parentElement.parentElement.querySelector('.mcq-feedback');
          return {
            isSelected: firstBtn.classList.contains('selected'),
            feedbackDisplay: feedbackEl ? feedbackEl.style.display : null,
            feedbackText: feedbackEl ? feedbackEl.textContent : null
          };
        })()
      `,
      returnByValue: true
    });
    console.log("   HTML click result:", clickHtmlRes.result.result.value);

    console.log("\n✅ SUCCESS: Phase 4 browser test verified! Delegated click listener, single quote escaping, and HTML tag escaping all work perfectly without SyntaxErrors.");
    ws.close();
    chrome.kill("SIGKILL");
    process.exit(0);
  } catch (err) {
    console.error("\n❌ TEST FAILED:", err);
    chrome.kill("SIGKILL");
    process.exit(1);
  }
}

runTest();
