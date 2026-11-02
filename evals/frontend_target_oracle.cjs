// Evaluator-owned desktop interactions; requires Playwright and local Chromium.
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const { chromium } = require('playwright');

async function main() {
  if (!process.argv[2]) throw new Error('Usage: node evals/frontend_target_oracle.cjs <candidate> [screenshot-directory]');
  const root = path.resolve(process.argv[2]);
  const screenshots = process.argv[3] && path.resolve(process.argv[3]);
  const server = http.createServer((request, response) => {
    const file = new URL(request.url, 'http://localhost').pathname.slice(1) || 'index.html';
    if (!['index.html', 'app.js'].includes(file)) return response.writeHead(404).end();
    try {
      response.setHeader('Content-Type', file.endsWith('.html') ? 'text/html; charset=utf-8' : 'text/javascript; charset=utf-8');
      response.end(fs.readFileSync(path.join(root, file)));
    } catch { response.writeHead(404).end(); }
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  let browser;
  const results = [];
  const checks = {
    async 'filtered-detail'(page) {
      await page.getByLabel('Filter items').fill('MICRO');
      await page.waitForFunction(() => document.querySelectorAll('#rows tr').length === 1);
      assert.match(await page.locator('#rows').innerText(), /Studio microphone/);
      await page.getByRole('button', {name:'Details', exact:true}).click();
      assert.equal((await page.locator('#details').innerText()).trim(), 'Studio microphone: USB microphone with stand');
    },
    async 'empty-and-clear'(page) {
      await page.getByLabel('Filter items').fill('not-an-inventory-item');
      await page.waitForFunction(() => !document.querySelector('#rows').textContent.includes('Field camera'));
      assert.match(await page.locator('body').innerText(), /no (?:items|results|matching|matches)|nothing (?:found|matches)|0 (?:items|results)/i, 'visible empty feedback');
      if (screenshots) {fs.mkdirSync(screenshots,{recursive:true});await page.screenshot({path:path.join(screenshots,`${page.viewportSize().width}-empty-state.png`),fullPage:true});}
      await page.getByLabel('Filter items').fill('');
      await page.waitForFunction(() => document.querySelectorAll('#rows button').length === 3);
    },
    async 'failure-and-retry'(page) {
      await page.getByLabel('Filter items').fill('MICRO');
      let release;
      const pending = new Promise(resolve => { release = resolve; });
      let calls = 0;
      await page.route('**/api/items', async route => {
        calls += 1;
        if (calls === 1) { await pending; await route.fulfill({status:503,contentType:'application/json',body:JSON.stringify({error:'Service unavailable'})}); }
        else await route.fulfill({status:200,contentType:'application/json',body:JSON.stringify([
          {name:'Studio microphone refreshed',available:7,description:'Updated microphone'},
          {name:'Other camera',available:5,description:'Not a microphone'}
        ])});
      });
      try {
        await page.getByRole('button',{name:'Refresh',exact:true}).click();
        await page.waitForFunction(() => /loading|refreshing/i.test(document.querySelector('#status').textContent));
      } finally { release(); }
      await page.waitForFunction(() => /error|failed|unavailable|unable|could not/i.test(document.querySelector('#status').textContent));
      assert.match(await page.locator('#status').innerText(), /retry|try again|refresh/i, 'actionable error');
      assert.equal(await page.getByLabel('Filter items').inputValue(),'MICRO');
      assert.match(await page.locator('#rows').innerText(),/Studio microphone/);
      assert.doesNotMatch(await page.locator('#rows').innerText(),/Field camera/);
      assert.equal(await page.getByRole('button',{name:/\S/}).evaluateAll(buttons=>buttons.some(button=>button.id==='refresh')),true,'retry has button role and accessible name');
      await page.locator('#refresh').click();
      await page.waitForFunction(() => /updated|success|refreshed/i.test(document.querySelector('#status').textContent));
      assert.equal(await page.getByLabel('Filter items').inputValue(),'MICRO');
      assert.equal(await page.locator('#rows button').count(),1);
      assert.match(await page.locator('#rows').innerText(),/Studio microphone refreshed/);
      assert.doesNotMatch(await page.locator('#rows').innerText(),/Other camera/);
      await page.getByRole('button',{name:'Details',exact:true}).click();
      assert.equal((await page.locator('#details').innerText()).trim(),'Studio microphone refreshed: Updated microphone');
      assert.equal(calls,2);
    },
    async 'keyboard-and-desktop-layout'(page) {
      await page.keyboard.press('Tab');
      assert.equal(await page.locator('#filter').evaluate(el=>el===document.activeElement),true,'filter keyboard focus');
      await page.keyboard.type('MICRO');
      await page.keyboard.press('Tab');
      assert.equal(await page.locator('#refresh').evaluate(el=>el===document.activeElement),true,'refresh keyboard focus');
      await page.keyboard.press('Tab');
      assert.equal(await page.locator('#rows button').count(),1);
      await page.keyboard.press('Enter');
      assert.match(await page.locator('#details').innerText(),/USB microphone with stand/);
      assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth <= innerWidth),true,'desktop horizontal overflow');
    }
  };
  try {
    const options = {headless:true};
    if (process.env.EVAL_BROWSER_EXECUTABLE) options.executablePath=process.env.EVAL_BROWSER_EXECUTABLE;
    browser = await chromium.launch(options);
    for (const width of [1280,1024]) for (const [name,check] of Object.entries(checks)) {
      const page = await browser.newPage({viewport:{width,height:800}});
      page.setDefaultTimeout(2500);
      const errors=[];
      page.on('pageerror',error=>errors.push(error.message));
      try {
        await page.goto(`http://127.0.0.1:${server.address().port}`);
        await check(page);
        assert.deepEqual(errors,[],'browser errors');
        if (screenshots) {fs.mkdirSync(screenshots,{recursive:true});await page.screenshot({path:path.join(screenshots,`${width}-${name}.png`),fullPage:true});}
        results.push({name,width,passed:true});
      } catch(error) {
        if (screenshots) {fs.mkdirSync(screenshots,{recursive:true});await page.screenshot({path:path.join(screenshots,`${width}-${name}-failed.png`),fullPage:true});}
        results.push({name,width,passed:false,error:error.message});
      }
      finally {await page.close();}
    }
    console.log(JSON.stringify({browser:browser.version(),scope:'desktop interaction samples, not mobile or visual-quality proof',results},null,2));
    if(results.some(result=>!result.passed)) process.exitCode=1;
  } finally {if(browser) await browser.close();await new Promise(resolve=>server.close(resolve));}
}
main().catch(error=>{console.error(error.message);process.exitCode=1;});
