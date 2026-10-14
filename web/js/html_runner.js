/**
 * =============================================================================
 * 🌐 HTML & CSS LIVE SANDBOX RUNNER
 * =============================================================================
 * 📌 KYA KAAM HAI IS FILE KA (WHAT IT DOES):
 *   Ye module user ke likhe huye HTML aur CSS code ko ek isolated <iframe>
 *   (browser ke andar ek mini-browser window) me inject karke live render karta hai,
 *   aur check karta hai ki user ne saare required HTML tags (jaise <h1>, <form>) likhe hain ya nahi.
 *
 * 👁️ WEB PAGE PE KYA DIKHTA/HOTA HAI:
 *   Jab user "HTML & CSS" track select karta hai aur "Run Code" ya "Submit" dabata hai,
 *   to right side par white color ka live web preview box dikhta hai jisme unka
 *   button, form, headings, cards live render ho jate hain (bilkul CodePen jaisa!).
 *
 * 💡 KYUN USE KIYA (WHY WE USE THIS):
 *   Agar hum user ke HTML code ko seedha main web page ke andar daal denge,
 *   to user ka CSS humari website ki styling ko bigaad sakta hai (CSS leak).
 *   `<iframe>` use karne se user ka code 100% isolated rehta hai aur safe rehta hai!
 *
 * ⚠️ AGAR ISKO CHANGE YA DELETE KAREIN TO:
 *   HTML track me live preview band ho jayega aur HTML test cases validate nahi honge.
 * =============================================================================
 */

class HtmlRunner {
  constructor(iframeElement) {
    // 📌 Target <iframe> element jisme web page draw karna hai
    this.iframe = iframeElement;
  }

  setIframe(iframeElement) {
    // 📌 Iframe element ka reference update karne ke liye
    this.iframe = iframeElement;
  }

  render(htmlCode) {
    // 📌 User ka code lekar use ek clean HTML document ke andar wrap karta hai aur iframe me inject karta hai
    if (!this.iframe) return;

    // Iframe ka internal document object access kiya
    const doc = this.iframe.contentDocument || this.iframe.contentWindow.document;
    
    // 📌 Clean default CSS styling provide kar rahe hain taaki user ka code sundar dikhe
    const styledHtml = `
      <!DOCTYPE html>
      <html>
      <head>
        <meta charset="utf-8">
        <style>
          /* 📌 Basic Typography & Layout Defaults */
          body {
            font-family: system-ui, -apple-system, sans-serif;
            padding: 16px;
            color: #1e293b;
            background: #ffffff;
            line-height: 1.5;
          }
          h1 { color: #0f172a; margin-bottom: 8px; font-size: 1.5rem; }
          h2 { color: #334155; margin-bottom: 6px; font-size: 1.2rem; }
          p { margin-bottom: 12px; color: #475569; }
          ul { padding-left: 20px; margin-bottom: 12px; }
          li { margin-bottom: 4px; }
          
          /* 📌 Forms Styling */
          form {
            display: flex;
            flex-direction: column;
            gap: 10px;
            max-width: 320px;
          }
          input, textarea, button {
            padding: 8px 12px;
            border-radius: 6px;
            border: 1px solid #cbd5e1;
            font-size: 14px;
          }
          button {
            background: #2563eb;
            color: white;
            border: none;
            cursor: pointer;
            font-weight: bold;
          }
          button:hover {
            background: #1d4ed8;
          }
          
          /* 📌 Reusable Card Classes for Exercises */
          .fest-card, .profile-card {
            border: 1px solid #e2e8f0;
            padding: 16px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            background: #f8fafc;
          }
        </style>
      </head>
      <body>
        <!-- 📌 User ka code yahan live inject hota hai -->
        ${htmlCode}
      </body>
      </html>
    `;

    // Document stream open karke fresh content write kiya aur close kiya
    doc.open();
    doc.write(styledHtml);
    doc.close();
  }

  validateElements(expectedElements) {
    /**
     * 📌 DOM VALIDATOR (TEST CASE CHECKER):
     * Check karta hai ki kya user ne saare zaroori tags code me daale hain.
     * e.g., expectedElements = ['form', 'input', 'button']
     * Agar koi tag missing hua (jaise <button>), to error return karega.
     */
    if (!this.iframe) return { valid: false, missing: expectedElements };

    const doc = this.iframe.contentDocument || this.iframe.contentWindow.document;
    const missing = [];

    // Har expected tag ke liye document me querySelector chalaya
    expectedElements.forEach(tag => {
      const el = doc.querySelector(tag);
      if (!el) {
        missing.push(`<${tag}>`); // Missing tag ko list me record kiya
      }
    });

    return {
      valid: missing.length === 0, // Agar koi tag missing nahi hai to True
      missing: missing
    };
  }
}

// 📌 Global singleton instance banaya
window.htmlRunner = new HtmlRunner(null);
