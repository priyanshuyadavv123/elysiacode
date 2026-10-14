/**
 * =============================================================================
 * 🔊 ELYSIA AUDIO SYNTHESIZER (WEB AUDIO API)
 * =============================================================================
 * 📌 KYA KAAM HAI IS FILE KA (WHAT IT DOES):
 *   Ye module website ke buttons, code run, aur test cases ke liye realistic
 *   mechanical sound effects (SFX) synthesize karta hai.
 *
 * 👁️ WEB PAGE PE KYA DIKHTA/HOTA HAI:
 *   - Button dabane par mechanical click sound aati hai.
 *   - Code test pass hone par gaming victory chord/chime bajti hai.
 *   - Syntax ya logic error aane par gentle buzzer aati hai.
 *   - Top-right me 🔊/🔇 button se sound on/off ho sakta hai.
 *
 * 💡 KYUN USE KIYA (WHY WE USE THIS):
 *   Bina kisi heavy MP3 file download kiye, browser ka built-in `AudioContext`
 *   use karke sound frequency (Hertz) ke through mathematically audio generate hoti hai.
 *   Zero-lag, 0KB downloads, aur 100% instant playback!
 *
 * ⚠️ AGAR ISKO CHANGE YA DELETE KAREIN TO:
 *   Website mute ho jayegi, par baaki application bina kisi rukawat ke chalti rahegi.
 * =============================================================================
 */

class ElysiaAudio {
  constructor() {
    this.ctx = null;       // AudioContext ka instance yahan store hoga
    this.enabled = true;   // Default sound status: ON (true)
  }

  _init() {
    // 📌 Browser ka native Web Audio API initialize kar rahe hain
    // User jab pehli baar screen par click karta hai tab audio context awake hota hai
    if (!this.ctx && (window.AudioContext || window.webkitAudioContext)) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioCtx();
    }
    // Modern browsers (Chrome/Safari) AudioContext ko initially suspended rakhte hain
    if (this.ctx && this.ctx.state === "suspended") {
      this.ctx.resume().catch(() => {});
    }
  }

  toggle() {
    // 📌 Sound ko Mute / Unmute karne ka function
    // 👁️ Web Page Pe Effect: 🔊 badal kar 🔇 ban jata hai
    this.enabled = !this.enabled;
    return this.enabled;
  }

  playClick() {
    // 📌 Button click par mechanical keyboard jaisa tactile "tick" sound
    if (!this.enabled) return;
    this._init();
    if (!this.ctx) return;

    // Oscillator (Sound Wave Generator) create kiya
    const osc = this.ctx.createOscillator();
    // GainNode (Volume Controller) create kiya
    const gain = this.ctx.createGain();
    
    osc.type = 'sine'; // Smooth sound wave
    // Frequency 600Hz se 120Hz tak 0.04s me drop hoti hai (crisp click effect)
    osc.frequency.setValueAtTime(600, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(120, this.ctx.currentTime + 0.04);

    // Volume fade-out
    gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.04);

    // Audio routing: Oscillator -> Volume Gain -> Speakers
    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.start();
    osc.stop(this.ctx.currentTime + 0.04); // 40 milliseconds me sound finish
  }

  playSuccess() {
    // 📌 Test case pass hone par 4-note victory chord (C5, E5, G5, C6)
    if (!this.enabled) return;
    this._init();
    if (!this.ctx) return;

    const now = this.ctx.currentTime;
    // Music Notes: C5 (523Hz), E5 (659Hz), G5 (784Hz), C6 (1046Hz)
    const notes = [523.25, 659.25, 783.99, 1046.50];

    notes.forEach((freq, idx) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = 'triangle'; // Mellow chime tone
      // Har note 80 millisecond ke gap par bajti hai (arpeggio effect)
      osc.frequency.setValueAtTime(freq, now + idx * 0.08);

      gain.gain.setValueAtTime(0, now + idx * 0.08);
      gain.gain.linearRampToValueAtTime(0.12, now + idx * 0.08 + 0.02);
      gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.08 + 0.35);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now + idx * 0.08);
      osc.stop(now + idx * 0.08 + 0.35);
    });
  }

  playError() {
    // 📌 Syntax ya logic error aane par low buzzer sound (150Hz -> 90Hz)
    if (!this.enabled) return;
    this._init();
    if (!this.ctx) return;

    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    osc.type = 'sawtooth'; // Sharp, rough sound wave (buzzer)
    osc.frequency.setValueAtTime(150, this.ctx.currentTime);
    osc.frequency.linearRampToValueAtTime(90, this.ctx.currentTime + 0.25);

    gain.gain.setValueAtTime(0.12, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.25);

    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.start();
    osc.stop(this.ctx.currentTime + 0.25);
  }
}

// 📌 Global window object me attach kiya taaki baaki scripts isse use kar sakein
window.elysiaAudio = new ElysiaAudio();
