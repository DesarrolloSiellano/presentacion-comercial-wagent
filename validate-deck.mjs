import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';
import path from 'node:path';

const root = path.resolve('presentacion-comercial-wagent');
const html = `file://${root}/Wagent-Presentacion-Comercial.html`;
const out = `${root}/assets/deck-preview`;
await mkdir(out, { recursive: true });

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
await page.goto(html, { waitUntil: 'load' });
await page.waitForTimeout(400);

const total = await page.locator('.slide').count();
console.log(`slides: ${total}`);

const report = [];
for (let i = 0; i < total; i += 1) {
  await page.keyboard.press('Home');
  for (let k = 0; k < i; k += 1) await page.keyboard.press('ArrowRight');
  await page.waitForTimeout(250);
  const info = await page.evaluate(() => {
    const slide = document.querySelector('.slide.active');
    const content = slide?.querySelector('.content');
    return {
      title: slide?.dataset.title || '',
      contentScroll: content ? content.scrollHeight : 0,
      contentClient: content ? content.clientHeight : 0,
      slideScroll: slide ? slide.scrollHeight : 0,
      slideClient: slide ? slide.clientHeight : 0,
    };
  });
  const overflow = info.contentScroll > info.contentClient + 2;
  report.push({ ...info, overflow });
  await page.screenshot({ path: `${out}/slide-${String(i + 1).padStart(2, '0')}.png` });
}

console.log(report.map((r) => `${r.overflow ? 'OVERFLOW' : 'ok'}  ${r.title}  (${r.contentScroll}/${r.contentClient})`).join('\n'));
await browser.close();
