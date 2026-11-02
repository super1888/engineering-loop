// Local release continuity controls; no production deployment.
const fs=require('node:fs'),path=require('node:path'),os=require('node:os');
const assert=require('node:assert/strict');
const {spawn}=require('node:child_process');
const {chromium}=require('playwright');
async function main(){
 if(!process.argv[2])throw Error('Usage: node oracle <candidate-directory>');
 const original=path.resolve(process.argv[2]);
 const config=JSON.parse(fs.readFileSync(path.join(original,'deployment.json')));
 assert.equal(config.active,'v2','candidate must keep v2 active');
 const root=fs.mkdtempSync(path.join(os.tmpdir(),'release-oracle-'));
 fs.cpSync(original,root,{recursive:true});
 const write=(active,retained)=>fs.writeFileSync(path.join(root,'deployment.json'),JSON.stringify({active,retained}));
 write('v1',config.retained);
 const child=spawn(process.env.EVAL_PYTHON||'python3',[path.join(root,'service.py'),'--root',root,'--port','0']);
 let browser; const checks=[];let stderr='';child.stderr.on('data',b=>stderr+=b);
 try{
 const port=await new Promise((resolve,reject)=>{let text='';const t=setTimeout(()=>reject(Error('Server startup timeout '+stderr)),10000);child.stdout.on('data',b=>{text+=b;const i=text.indexOf('\n');if(i>=0){clearTimeout(t);try{resolve(JSON.parse(text.slice(0,i)).port);}catch(e){reject(e);}}});child.on('exit',code=>{clearTimeout(t);reject(Error('Server exit '+code+' '+stderr));});});
 browser=await chromium.launch({headless:true,...(process.env.EVAL_BROWSER_EXECUTABLE?{executablePath:process.env.EVAL_BROWSER_EXECUTABLE}:{})});
 const context=await browser.newContext({viewport:{width:1280,height:800}});
 const old=await context.newPage();old.setDefaultTimeout(2500);await old.goto(`http://127.0.0.1:${port}/`);
 await old.locator('#draft').fill('unsaved original work');
 write('v2',config.retained);
 const fresh=await context.newPage();fresh.setDefaultTimeout(2500);await fresh.goto(`http://127.0.0.1:${port}/`);
 assert.equal((await fresh.request.get(`http://127.0.0.1:${port}/health`)).status(),200);
 await fresh.locator('#load').click();await fresh.waitForFunction(()=>document.querySelector('#result').textContent.includes('v2 detail'));
 checks.push({name:'fresh-v2-and-health',passed:true});
 try{await old.locator('#load').click();await old.waitForFunction(()=>document.querySelector('#result').textContent.includes('v1 detail'),{},{timeout:2000});assert.equal(await old.locator('#draft').inputValue(),'unsaved original work');checks.push({name:'old-v1-continuity',passed:true});}catch(e){checks.push({name:'old-v1-continuity',passed:false,error:e.message});}
 // A new v2 session has not fetched its lazy module before rollback.
 const rollbackContext=await browser.newContext({viewport:{width:1280,height:800}});
 const rollbackClient=await rollbackContext.newPage();rollbackClient.setDefaultTimeout(2500);await rollbackClient.goto(`http://127.0.0.1:${port}/`);await rollbackClient.locator('#draft').fill('unsaved v2 work');
 write('v1',['v2']);
 await rollbackClient.locator('#load').click();await rollbackClient.waitForFunction(()=>document.querySelector('#result').textContent.includes('v2 detail'));
 assert.equal(await rollbackClient.locator('#draft').inputValue(),'unsaved v2 work');checks.push({name:'explicit-retained-rollback-control',passed:true});
 console.log(JSON.stringify({checks,scope:'local fresh and existing desktop clients; rollback retention is evaluator supplied'},null,2));
 if(checks.some(c=>!c.passed))process.exitCode=1;
 }finally{if(browser)await browser.close();child.kill();await new Promise(r=>child.exitCode!==null?r():child.once('exit',r));fs.rmSync(root,{recursive:true,force:true});}
}
main().catch(e=>{console.error(e.message);process.exitCode=1;});
