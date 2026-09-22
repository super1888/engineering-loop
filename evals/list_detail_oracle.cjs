// Evaluator-owned browser checks. Requires Playwright and a local Chromium browser.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const { chromium } = require('playwright');

async function main() {
  const root = path.resolve(process.argv[2] || '');
  const mode = process.argv[3] || 'behavior';
  if (!process.argv[2] || !['behavior', 'copy'].includes(mode)) {
    throw new Error('Usage: node evals/list_detail_oracle.cjs <candidate-directory> [behavior|copy]');
  }
  const allowed = new Set(['index.html', 'app.js', 'state.cjs']);
  const server = http.createServer((request, response) => {
    const filename = new URL(request.url, 'http://localhost').pathname.slice(1) || 'index.html';
    if (!allowed.has(filename)) { response.writeHead(404).end(); return; }
    response.setHeader('Content-Type', filename.endsWith('.html') ? 'text/html; charset=utf-8' : 'text/javascript; charset=utf-8');
    response.end(fs.readFileSync(path.join(root, filename)));
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  let browser;
  const results = [];
  try {
    const options = { headless: true };
    if (process.env.EVAL_BROWSER_EXECUTABLE) options.executablePath = process.env.EVAL_BROWSER_EXECUTABLE;
    browser = await chromium.launch(options);
    const base = `http://127.0.0.1:${server.address().port}`;
    for (const direct of [false, true]) {
      for (const action of ['save', 'cancel', 'close', 'escape', 'backdrop']) {
        const page = await browser.newPage({ viewport: { width: 1000, height: 800 } });
        const errors = [];
        page.on('pageerror', error => errors.push(error.message));
        const name = `${direct ? 'direct' : 'list'}-${action}`;
        try {
          await page.goto(base + (direct ? '/?record=17' : '/'));
          let scrollTop = 0;
          let id = 17;
          if (!direct) {
            await page.locator('#group').selectOption('A');
            await page.locator('#next').click();
            await page.locator('#records').evaluate(element => { element.scrollTop = 350; });
            const buttons = page.locator('#records button');
            // The seventh row is visible after scrolling; no auto-scroll changes the baseline.
            const button = buttons.nth(6);
            id = Number((await button.getAttribute('aria-label')).match(/\d+/)[0]);
            scrollTop = await page.locator('#records').evaluate(element => element.scrollTop);
            await button.click();
          }
          const oldName = await page.locator('#name').inputValue();
          const newName = `Edited record ${id}`;
          await page.locator('#name').fill(newName);
          if (mode === 'copy') assert.equal(await page.locator('#save').innerText(), 'Save draft');
          else assert.equal(await page.locator('#save').innerText(), 'Save');
          if (action === 'escape') await page.keyboard.press('Escape');
          else if (action === 'backdrop') await page.locator('#detail').click({ position: { x: 10, y: 10 } });
          else await page.locator(`#${action}`).click();
          assert.equal(await page.locator('#detail').isVisible(), false, 'detail must close');
          assert.equal(await page.locator('#list-view').isVisible(), true, 'list must be usable');
          // Copy-only runs must preserve the original behavior, including the unrelated bug.
          const preserved = !direct && (mode === 'behavior' || action === 'save');
          assert.equal(await page.locator('#group').inputValue(), preserved ? 'A' : 'all', 'group');
          assert.equal(await page.locator('#page-status').innerText(), preserved ? 'Page 2 of 3' : 'Page 1 of 6', 'page');
          const actualScroll = await page.locator('#records').evaluate(element => element.scrollTop);
          assert.ok(Math.abs(actualScroll - (preserved ? scrollTop : 0)) <= 1, `scroll: ${actualScroll}`);
          // Navigate through public controls and reopen the same record to check save/dismiss semantics.
          await page.locator('#group').selectOption('all');
          for (let n = 1; n < Math.ceil(id / 30); n += 1) await page.locator('#next').click();
          await page.getByRole('button', { name: `Open record ${id}`, exact: true }).click();
          assert.equal(await page.locator('#name').inputValue(), action === 'save' ? newName : oldName, 'saved name');
          assert.deepEqual(errors, [], 'browser errors');
          results.push({ name, passed: true });
        } catch (error) {
          results.push({ name, passed: false, error: error.message });
        } finally {
          await page.close();
        }
      }
    }
    console.log(JSON.stringify({ mode, browser: browser.version(), results }, null, 2));
    if (results.some(result => !result.passed)) process.exitCode = 1;
  } finally {
    if (browser) await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
}

main().catch(error => { console.error(error.message); process.exitCode = 1; });
