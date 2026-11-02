"""Browser-oracle controls; no model trial is performed by these tests."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

CORRECT = r"""
let items = [
 {name:'Field camera',available:4,description:'Weather-resistant camera kit'},
 {name:'Studio microphone',available:2,description:'USB microphone with stand'},
 {name:'Conference projector with extended installation kit',available:1,description:'HDMI projector and mounting kit'}
];
const filter=document.querySelector('#filter'), rows=document.querySelector('#rows'), status=document.querySelector('#status');
let shown=[];
function render(){
 shown=items.filter(item=>item.name.toLowerCase().includes(filter.value.toLowerCase()));
 rows.innerHTML=shown.map((item,index)=>`<tr><td>${item.name}</td><td>${item.available}</td><td><button data-index="${index}">Details</button></td></tr>`).join('');
 if(!shown.length) status.textContent='No matching items';
}
filter.addEventListener('input',render);
rows.addEventListener('click',event=>{if(event.target.matches('button')){const item=shown[Number(event.target.dataset.index)];document.querySelector('#details').textContent=item.name+': '+item.description;}});
document.querySelector('#refresh').addEventListener('click',async()=>{
 const button=document.querySelector('#refresh');button.disabled=true;status.textContent='Loading…';
 try {const response=await fetch('/api/items');if(!response.ok)throw new Error('Unavailable');items=await response.json();render();status.textContent='Updated';}
 catch(error){status.textContent='Refresh failed. Try again.';}
 finally{button.disabled=false;}
});
render();
"""

class FrontendTargetOracleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not shutil.which('node'):
            raise unittest.SkipTest('Node is unavailable')
        result = subprocess.run(['node', '-e',
            "const fs=require('node:fs');const {chromium}=require('playwright');"
            "process.exit(fs.existsSync(process.env.EVAL_BROWSER_EXECUTABLE||chromium.executablePath())?0:1)"],
            capture_output=True, timeout=10)
        if result.returncode:
            raise unittest.SkipTest('Playwright and local Chromium must be configured')

    def test_rejects_original_and_data_loss_but_accepts_valid_behavior(self):
        fixture=ROOT/'evals/fixtures/frontend-target-runtime'
        with tempfile.TemporaryDirectory() as directory:
            candidate=Path(directory)/'candidate'
            shutil.copytree(fixture,candidate)
            original=(candidate/'app.js').read_text(encoding='utf-8')
            variants=[('original',original,False),('valid',CORRECT,True),
                ('lose-data-on-error',CORRECT.replace("catch(error){status.textContent=", "catch(error){items=[];render();status.textContent="),False)]
            for name,source,passed in variants:
                with self.subTest(variant=name):
                    (candidate/'app.js').write_text(source,encoding='utf-8')
                    before={p.name:p.read_bytes() for p in candidate.iterdir() if p.is_file()}
                    result=subprocess.run(['node',str(ROOT/'evals/frontend_target_oracle.cjs'),str(candidate)],
                        capture_output=True,text=True,timeout=90)
                    report=json.loads(result.stdout)
                    self.assertEqual(len(report['results']),8)
                    self.assertEqual(result.returncode,0 if passed else 1,result.stdout+result.stderr)
                    self.assertEqual(all(row['passed'] for row in report['results']),passed)
                    if name=='lose-data-on-error':
                        self.assertTrue(any(not row['passed'] and row['name']=='failure-and-retry' for row in report['results']))
                    self.assertEqual(before,{p.name:p.read_bytes() for p in candidate.iterdir() if p.is_file()})

if __name__=='__main__':
    unittest.main()
