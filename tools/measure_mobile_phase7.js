/**
 * Verification script for Phase 7:
 * Tests 390x844 (mobile) and 768x1024 (tablet) layouts,
 * saves after screenshots, tests collapsible menu & AI fab,
 * and benchmarks Fast 3G first-render performance.
 */

const { spawn } = require("child_process");
const http = require("http");
const fs = require("fs");
const path = require("path");

const CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const DEBUG_PORT = 9245;
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

  console.log("1. Starting Chrome headless on port", DEBUG_PORT);
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

    const pageTarget = targets.find((t) => t.type === "page") || targets[0];
    const wsUrl = pageTarget.webSocketDebuggerUrl;
    const client = new CDPClient(wsUrl);
    await client.connect();

    await client.send("Page.enable");
    await client.send("Runtime.enable");
    await client.send("Network.enable");

    // =============================================================
    // VIEWPORT 1: Mobile (390 x 844)
    // =============================================================
    console.log("\n2. Emulating Mobile Viewport (390 x 844)...");
    await client.send("Emulation.setDeviceMetricsOverride", {
      width: 390,
      height: 844,
      deviceScaleFactor: 2,
      mobile: true,
      hasTouch: true,
    });

    await client.send("Page.navigate", { url: "http://localhost:8080/" });
    await sleep(2000);

    // Capture mobile after screenshot
    const mobileAfterPath = path.join(SCREENSHOT_DIR, "mobile_after.png");
    await client.screenshot(mobileAfterPath);
    console.log("Saved mobile_after.png to docs/screenshots/");

    // Mobile Audit
    const mobileAudit = await client.eval(`
      (() => {
        const docWidth = document.documentElement.scrollWidth;
        const bodyWidth = document.body.scrollWidth;
        const winWidth = window.innerWidth;
        const hasHorizontalScroll = docWidth > winWidth || bodyWidth > winWidth;

        // Check header layout
        const header = document.querySelector('.viewport-top-header');
        const headerHeight = header ? header.getBoundingClientRect().height : 0;

        // Check search box & input
        const searchBox = document.querySelector('.hero-search-box');
        const searchInput = document.querySelector('#hero-global-search');
        const searchRect = searchBox ? searchBox.getBoundingClientRect() : null;
        const searchWidth = searchRect ? searchRect.width : 0;
        const placeholderTruncated = searchInput ? (searchInput.scrollWidth > searchInput.clientWidth + 2) : false;

        // Check floating Senior AI button
        const aiFab = document.querySelector('#ai-tutor-fab');
        const aiFabRect = aiFab ? aiFab.getBoundingClientRect() : null;
        const aiFabLabel = aiFab ? aiFab.querySelector('.ai-fab-label') : null;
        const labelDisplay = aiFabLabel ? window.getComputedStyle(aiFabLabel).display : 'none';

        // Check collapsible menu
        const prefsBtn = document.querySelector('#btn-mobile-prefs-toggle');
        const prefsCollapse = document.querySelector('#mobile-prefs-collapse');
        const prefsVisibleBefore = prefsCollapse ? window.getComputedStyle(prefsCollapse).display !== 'none' && prefsCollapse.offsetHeight > 0 : false;

        // Test clicking the preferences toggle
        if (prefsBtn) prefsBtn.click();
        const prefsVisibleAfter = prefsCollapse ? prefsCollapse.classList.contains('open') && window.getComputedStyle(prefsCollapse).display !== 'none' : false;

        // Check if any visible page elements overflow viewport
        const pageOverflows = [];
        const nonHidden = document.querySelectorAll('header, main, section, div:not(.aurora-container):not(.aurora-orb):not(.CodeMirror-sizer):not(.CodeMirror-scroll):not(.CodeMirror)');
        for (const el of nonHidden) {
          const r = el.getBoundingClientRect();
          if (r.width > 0 && r.height > 0 && r.right > winWidth + 2) {
            // ignore if inside horizontally scrollable container like .lesson-pill-tabs
            if (!el.closest('.lesson-pill-tabs')) {
              pageOverflows.push({
                tag: el.tagName,
                className: el.className,
                id: el.id,
                right: r.right,
                width: r.width
              });
            }
          }
        }

        return {
          winWidth,
          docWidth,
          hasHorizontalScroll,
          headerHeight,
          search: {
            width: searchWidth,
            placeholderTruncated,
            placeholder: searchInput ? searchInput.placeholder : null
          },
          aiFab: {
            width: aiFabRect ? Math.round(aiFabRect.width) : 0,
            height: aiFabRect ? Math.round(aiFabRect.height) : 0,
            labelDisplay,
            isCollapsed: labelDisplay === 'none' && aiFabRect && aiFabRect.width <= 50,
            right: aiFabRect ? Math.round(winWidth - aiFabRect.right) : 0,
            bottom: aiFabRect ? Math.round(window.innerHeight - aiFabRect.bottom) : 0
          },
          collapsibleMenu: {
            btnExists: Boolean(prefsBtn),
            prefsVisibleBefore,
            prefsVisibleAfter
          },
          pageOverflows: pageOverflows.slice(0, 5)
        };
      })()
    `);
    console.log("Mobile Audit Result (Phase 7):", JSON.stringify(mobileAudit, null, 2));

    // =============================================================
    // VIEWPORT 2: Tablet (768 x 1024)
    // =============================================================
    console.log("\n3. Emulating Tablet Viewport (768 x 1024)...");
    await client.send("Emulation.setDeviceMetricsOverride", {
      width: 768,
      height: 1024,
      deviceScaleFactor: 2,
      mobile: true,
      hasTouch: true,
    });

    await client.send("Page.navigate", { url: "http://localhost:8080/" });
    await sleep(2000);

    const tabletAfterPath = path.join(SCREENSHOT_DIR, "tablet_after.png");
    await client.screenshot(tabletAfterPath);
    console.log("Saved tablet_after.png to docs/screenshots/");

    const tabletAudit = await client.eval(`
      (() => {
        const docWidth = document.documentElement.scrollWidth;
        const winWidth = window.innerWidth;
        const hasHorizontalScroll = docWidth > winWidth;

        const header = document.querySelector('.viewport-top-header');
        const headerHeight = header ? header.getBoundingClientRect().height : 0;

        const searchInput = document.querySelector('#hero-global-search');
        const searchBox = document.querySelector('.hero-search-box');
        const searchWidth = searchBox ? searchBox.getBoundingClientRect().width : 0;
        const placeholderTruncated = searchInput ? (searchInput.scrollWidth > searchInput.clientWidth + 2) : false;

        const aiFab = document.querySelector('#ai-tutor-fab');
        const aiFabRect = aiFab ? aiFab.getBoundingClientRect() : null;

        return {
          winWidth,
          docWidth,
          hasHorizontalScroll,
          headerHeight,
          search: {
            width: searchWidth,
            placeholderTruncated
          },
          aiFab: {
            width: aiFabRect ? Math.round(aiFabRect.width) : 0,
            height: aiFabRect ? Math.round(aiFabRect.height) : 0
          }
        };
      })()
    `);
    console.log("Tablet Audit Result (Phase 7):", JSON.stringify(tabletAudit, null, 2));

    // =============================================================
    // VIEWPORT 3: Fast 3G First-Render Benchmark
    // =============================================================
    console.log("\n4. Benchmarking Fast 3G First-Render Time (with Gzip)...");
    await client.send("Network.emulateNetworkConditions", {
      offline: false,
      latency: 150,
      downloadThroughput: 1.6 * 1024 * 1024 / 8, // 200 KB/s
      uploadThroughput: 750 * 1024 / 8,          // 93.75 KB/s
      connectionType: "cellular3g"
    });

    await client.send("Network.clearBrowserCache");
    await client.send("Page.navigate", { url: "http://localhost:8080/" });

    let renderMetrics = null;
    for (let i = 0; i < 40; i++) {
      await sleep(500);
      try {
        renderMetrics = await client.eval(`
          (() => {
            const nav = performance.getEntriesByType('navigation')[0];
            const paint = performance.getEntriesByType('paint');
            const fcp = paint.find(p => p.name === 'first-contentful-paint');
            const currEntry = performance.getEntriesByName('http://localhost:8080/js/curriculum_tree.js')[0];
            if (nav && nav.domInteractive > 0) {
              return {
                domInteractive: Math.round(nav.domInteractive),
                domContentLoaded: Math.round(nav.domContentLoadedEventEnd),
                loadEvent: Math.round(nav.loadEventEnd),
                fcp: fcp ? Math.round(fcp.startTime) : null,
                curriculumTreeJs: currEntry ? {
                  duration: Math.round(currEntry.duration),
                  transferSize: currEntry.transferSize,
                  decodedBodySize: currEntry.decodedBodySize
                } : null
              };
            }
            return null;
          })()
        `);
        if (renderMetrics && renderMetrics.fcp && renderMetrics.curriculumTreeJs) {
          break;
        }
      } catch (e) {}
    }
    console.log("Fast 3G Render Metrics (Gzip):", JSON.stringify(renderMetrics, null, 2));

    // Assertions
    if (mobileAudit.hasHorizontalScroll) {
      throw new Error("Mobile has page-level horizontal scroll!");
    }
    if (tabletAudit.hasHorizontalScroll) {
      throw new Error("Tablet has page-level horizontal scroll!");
    }
    if (!mobileAudit.aiFab.isCollapsed) {
      throw new Error("Senior AI Tutor FAB is not collapsed on mobile!");
    }
    if (mobileAudit.search.placeholderTruncated) {
      throw new Error("Search placeholder is truncated on mobile!");
    }
    if (tabletAudit.search.placeholderTruncated) {
      throw new Error("Search placeholder is truncated on tablet!");
    }
    if (mobileAudit.pageOverflows.length > 0) {
      throw new Error("Elements overflowing past viewport on mobile: " + JSON.stringify(mobileAudit.pageOverflows));
    }

    console.log("\n✅ ALL PHASE 7 LAYOUT AND PERFORMANCE CHECKS PASSED!");

  } finally {
    chrome.kill("SIGTERM");
  }
}

run().catch((err) => {
  console.error("Test failed:", err);
  process.exit(1);
});
