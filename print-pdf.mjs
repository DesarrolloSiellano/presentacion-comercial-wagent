import { chromium } from 'playwright';
import path from 'node:path';

const root = path.resolve('presentacion-comercial-wagent');
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
await page.goto(`file://${root}/Wagent-Presentacion-Comercial.html`, { waitUntil: 'load' });
await page.emulateMedia({ media: 'print' });
await page.waitForTimeout(600);
await page.pdf({
  path: `${root}/Wagent-Presentacion-Comercial.pdf`,
  width: '13.333in',
  height: '7.5in',
  printBackground: true,
  margin: { top: '0', right: '0', bottom: '0', left: '0' },
  preferCSSPageSize: true,
});
await browser.close();
console.log('PDF generado');
