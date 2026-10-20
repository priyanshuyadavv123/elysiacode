/**
 * Diagnostic script for Phase 7:
 * Measures baseline layout at 390x844 (mobile) and 768x1024 (tablet),
 * captures before screenshots, and benchmarks Fast 3G first-render time.
 */

const { spawn } = require("child_process");
const http = require("http");
const fs = require("fs");
const path = require("path");

const CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const DEBUG_PORT = 9235;
const SCREENSHOT_DIR = path.resolve(__dirname, "../docs/screenshots");

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

class CDPClient {
  constructor(wsUrl) {
    this.wsUrl = wsUrl;
    this.id = 1;
    this.callbacks = new Map();
  }

  async connect() {
    this.ws = new WebSocket(this.wsUrl);
    this.ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.id && this.callbacks.has(data.id)) {
        const cb = this.callbacks.get(data.id);
        this.callbacks.delete(data.id);
        if (data.error) cb.reject(new Error(data.error.message));
        else cb.resolve(data.result);
      }
    };
    return new Promise((resolve) => {
      this.ws.onopen = resolve;
    });
  }

  send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = this.id++;
      this.callbacks.set(id, { resolve, reject });
      this.ws.send(JSON.stringify({ id, method, params }));
    });
  }

  async eval(expr) {
    const res = await this.send("Runtime.evaluate", {
      expression: expr,
      returnByValue: true,
      awaitPromise: true,
    });
    if (res.exceptionDetails) {
      throw new Error("Eval error: " + JSON.stringify(res.exceptionDetails));
    }
    return res.result ? res.result.value : undefined;
  }

  async screenshot(filePath) {
    const res = await this.send("Page.captureScreenshot", { format: "png" });
    fs.writeFileSync(filePath, Buffer.from(res.data, "base64"));
  }
}

async function run() {
  if (!fs.existsSync(SCREENSHOT_DIR)) {
    fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
  }

  console.log("Spawning Chrome headless on port", DEBUG_PORT);
  const chrome = spawn(CHROME_PATH, [
    "--headless=new",
    `--remote-debugging-port=${DEBUG_PORT}`,
    "--disable-gpu",
    "--no-first-run",
    "--no-default-browser-check"
  ]);

  try {
    let targets = null;
    for (let i = 0; i < 25; i++) {
      await sleep(200);
      try {
        targets = await httpGetJson(`http://127.0.0.1:${DEBUG_PORT}/json/list`);
        if (targets && targets.length > 0) break;
      } catch (e) {}
    }

    if (!targets || targets.length === 0) {
      throw new Error("No Chrome targets found");
    }

    const pageTarget = targets.find((t) => t.type === "page") || targets[0];
    console.log("Targets found:", targets.map(t => ({ id: t.id, type: t.type, title: t.title })));
    const wsUrl = pageTarget.webSocketDebuggerUrl;
    const client = new CDPClient(wsUrl);
    await client.connect();

    await client.send("Page.enable");
    await client.send("Runtime.enable");
    await client.send("Network.enable");

    // -------------------------------------------------------------
    // Viewport 1: Mobile (390 x 844)
    // -------------------------------------------------------------
    console.log("\n=== Checking Mobile: 390x844 ===");
    await client.send("Emulation.setDeviceMetricsOverride", {
      width: 390,
      height: 844,
      deviceScaleFactor: 2,
      mobile: true,
      hasTouch: true,
    });

    await client.send("Page.navigate", { url: "http://localhost:8080/" });
    await sleep(2500);

    const mobileBeforePath = path.join(SCREENSHOT_DIR, "mobile_before.png");
    await client.screenshot(mobileBeforePath);
    console.log("Saved mobile_before.png");

    const mobileAudit = await client.eval(`
      (() => {
        const docWidth = document.documentElement.scrollWidth;
        const bodyWidth = document.body.scrollWidth;
        const winWidth = window.innerWidth;
        const hasHorizontalScroll = docWidth > winWidth || bodyWidth > winWidth;

        // Find elements that overflow horizontally
        const overflowingElements = [];
        const allElements = document.querySelectorAll('*');
        for (const el of allElements) {
          const rect = el.getBoundingClientRect();
          if (rect.right > winWidth + 1) {
            overflowingElements.push({
              tag: el.tagName,
              id: el.id,
              className: el.className,
              rectRight: rect.right,
              rectWidth: rect.width
            });
          }
        }

        // Header check
        const header = document.querySelector('.viewport-top-header');
        const headerRect = header ? header.getBoundingClientRect() : null;
        const searchInput = document.querySelector('#hero-global-search');
        const searchRect = searchInput ? searchInput.getBoundingClientRect() : null;

        // Floating AI Tutor button
        const aiFab = document.querySelector('#ai-tutor-fab');
        const aiFabRect = aiFab ? aiFab.getBoundingClientRect() : null;
        const aiFabStyle = aiFab ? window.getComputedStyle(aiFab) : null;

        // Check if CTA buttons covered by AI FAB
        const mainCta = document.querySelector('.hero-primary-cta, #btn-hero-start-learning, .btn-primary-3d');
        const ctaRect = mainCta ? mainCta.getBoundingClientRect() : null;

        // Language & track toggle pills
        const langGroup = document.querySelector('.top-lang-pill-group');
        const langRect = langGroup ? langGroup.getBoundingClientRect() : null;
        const langStyle = langGroup ? window.getComputedStyle(langGroup) : null;

        return {
          winWidth,
          docWidth,
          hasHorizontalScroll,
          overflowCount: overflowingElements.length,
          sampleOverflows: overflowingElements.slice(0, 5),
          header: {
            height: headerRect ? headerRect.height : 0,
            width: headerRect ? headerRect.width : 0
          },
          search: {
            placeholder: searchInput ? searchInput.placeholder : null,
            width: searchRect ? searchRect.width : 0,
            scrollWidth: searchInput ? searchInput.scrollWidth : 0
          },
          aiFab: {
            display: aiFabStyle ? aiFabStyle.display : null,
            position: aiFabStyle ? aiFabStyle.position : null,
            width: aiFabRect ? aiFabRect.width : 0,
            height: aiFabRect ? aiFabRect.height : 0,
            bottom: aiFabStyle ? aiFabStyle.bottom : null,
            right: aiFabStyle ? aiFabStyle.right : null,
            labelVisible: aiFab ? (aiFab.querySelector('.ai-fab-label') ? window.getComputedStyle(aiFab.querySelector('.ai-fab-label')).display : 'none') : 'none'
          },
          langGroup: {
            display: langStyle ? langStyle.display : null,
            visible: langRect ? (langRect.width > 0 && langRect.height > 0) : false
          }
        };
      })()
    `);
    console.log("Mobile Audit Result:", JSON.stringify(mobileAudit, null, 2));

    // -------------------------------------------------------------
    // Viewport 2: Tablet (768 x 1024)
    // -------------------------------------------------------------
    console.log("\n=== Checking Tablet: 768x1024 ===");
    await client.send("Emulation.setDeviceMetricsOverride", {
      width: 768,
      height: 1024,
      deviceScaleFactor: 2,
      mobile: true,
      hasTouch: true,
    });

    await client.send("Page.navigate", { url: "http://localhost:8080/" });
    await sleep(2500);

    const tabletBeforePath = path.join(SCREENSHOT_DIR, "tablet_before.png");
    await client.screenshot(tabletBeforePath);
    console.log("Saved tablet_before.png");

    const tabletAudit = await client.eval(`
      (() => {
        const docWidth = document.documentElement.scrollWidth;
        const winWidth = window.innerWidth;
        const hasHorizontalScroll = docWidth > winWidth;

        const overflowingElements = [];
        const allElements = document.querySelectorAll('*');
        for (const el of allElements) {
          const rect = el.getBoundingClientRect();
          if (rect.right > winWidth + 1) {
            overflowingElements.push({
              tag: el.tagName,
              id: el.id,
              className: el.className,
              rectRight: rect.right
            });
          }
        }

        return {
          winWidth,
          docWidth,
          hasHorizontalScroll,
          overflowCount: overflowingElements.length,
          sampleOverflows: overflowingElements.slice(0, 5)
        };
      })()
    `);
    console.log("Tablet Audit Result:", JSON.stringify(tabletAudit, null, 2));

    // -------------------------------------------------------------
    // Benchmark: Fast 3G Profile First-Render
    // -------------------------------------------------------------
    console.log("\n=== Benchmarking Fast 3G Profile First-Render Time ===");
    // Fast 3G specs: Latency 150ms RTT, Down: 1.6 Mbps = 200 KB/s, Up: 750 kbps = 93.75 KB/s
    await client.send("Network.emulateNetworkConditions", {
      offline: false,
      latency: 150,
      downloadThroughput: 1.6 * 1024 * 1024 / 8, // 200,000 bytes/sec
      uploadThroughput: 750 * 1024 / 8,          // 93,750 bytes/sec
      connectionType: "cellular3g"
    });

    // Clear cache to ensure realistic cold load
    await client.send("Network.clearBrowserCache");

    const startTime = Date.now();
    await client.send("Page.navigate", { url: "http://localhost:8080/" });

    // Wait for first contentful paint or DOM ready
    let renderMetrics = null;
    for (let i = 0; i < 40; i++) {
      await sleep(500);
      try {
        renderMetrics = await client.eval(`
          (() => {
            const nav = performance.getEntriesByType('navigation')[0];
            const paint = performance.getEntriesByType('paint');
            const fcp = paint.find(p => p.name === 'first-contentful-paint');
            if (nav && nav.domInteractive > 0) {
              return {
                domInteractive: Math.round(nav.domInteractive),
                domContentLoaded: Math.round(nav.domContentLoadedEventEnd),
                loadEvent: Math.round(nav.loadEventEnd),
                fcp: fcp ? Math.round(fcp.startTime) : null,
                curriculumTreeJs: performance.getEntriesByName('http://localhost:8080/js/curriculum_tree.js')[0] ? {
                  duration: Math.round(performance.getEntriesByName('http://localhost:8080/js/curriculum_tree.js')[0].duration),
                  transferSize: performance.getEntriesByName('http://localhost:8080/js/curriculum_tree.js')[0].transferSize
                } : null
              };
            }
            return null;
          })()
        `);
        if (renderMetrics && renderMetrics.fcp) {
          break;
        }
      } catch (e) {}
    }
    console.log("Fast 3G Render Metrics (Baseline):", JSON.stringify(renderMetrics, null, 2));

  } finally {
    chrome.kill("SIGTERM");
  }
}

run().catch((err) => {
  console.error("Test failed:", err);
  process.exit(1);
});
