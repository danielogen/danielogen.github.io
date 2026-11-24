#!/usr/bin/env node
// Renders scripts/social-card.html to assets/images/social-card.jpg (1200x630).
//
// Usage: node scripts/render_social_card.cjs [path/to/puppeteer-core] [path/to/chrome]
// Needs puppeteer-core (e.g. `npm i -g puppeteer-core`) and a local Chrome. Run it only when
// the card's text or the portrait changes; the JPEG is committed, so CI doesn't run this.
const path = require('path');
const root = path.resolve(__dirname, '..');
const puppeteer = require(process.argv[2] || 'puppeteer-core');
const chrome = process.argv[3] || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

(async () => {
    const browser = await puppeteer.launch({ executablePath: chrome, headless: 'new' });
    const page = await browser.newPage();
    await page.setViewport({ width: 1200, height: 630, deviceScaleFactor: 1 });
    await page.goto('file://' + path.join(root, 'scripts/social-card.html'), { waitUntil: 'networkidle0' });
    await page.evaluate(() => document.fonts.ready);
    const out = path.join(root, 'assets/images/social-card.jpg');
    await page.screenshot({ path: out, type: 'jpeg', quality: 85 });
    await browser.close();
    console.log('Wrote', path.relative(root, out));
})();
