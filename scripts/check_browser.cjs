// Optional browser check: NODE_PATH points at an installed Playwright package.
const {chromium}=require('playwright'),assert=require('node:assert/strict');
const base=process.env.COURSE_URL||'http://127.0.0.1:18781';
(async()=>{const browser=await chromium.launch({headless:true});const page=await browser.newPage({viewport:{width:1440,height:950}});const errors=[];page.on('pageerror',e=>errors.push(e.message));
await page.goto(base+'/curso/trilha1/modulo-1-1.html');assert.equal(await page.locator('[data-ARCKHÉ-topic]').count(),6);
await page.locator('[data-ARCKHÉ-read-toggle]').first().click();assert.equal((await page.evaluate(()=>ARCKHÉ.progress('curso'))).done,1);
await page.locator('[data-ARCKHÉ-doubt-toggle]').first().click();
await page.locator('[data-ARCKHÉ-check-option="1"]').click();assert(await page.locator('[data-ARCKHÉ-check-feedback]').innerText());
// Select a real paragraph, persist a note and restore its highlight after reload.
const note=await page.evaluate(()=>{const node=document.querySelector('[data-ARCKHÉ-block] p').firstChild;const range=document.createRange();range.setStart(node,0);range.setEnd(node,20);return ARCKHÉ.highlight(range,{note:'Rever esta decisão',color:'blue',tags:['piloto']})});assert.equal(typeof note,'string');await page.reload();assert.equal(await page.locator('mark[data-ARCKHÉ-note]').count(),1);
await page.locator('.appearance summary').click();await page.locator('[data-ARCKHÉ-set-theme="claro"]').click();assert(!(await page.locator('html').getAttribute('class')).includes('dark'));await page.locator('[data-ARCKHÉ-set-theme="ARCKHÉ-dark"]').click();
// Save a stable point, then resume from the landing in the same browser context.
await page.locator('#topico-3').scrollIntoViewIfNeeded();await page.waitForTimeout(700);
await page.goto(base+'/');assert.equal((await page.evaluate(()=>ARCKHÉ.progress('curso'))).done,1);
await page.evaluate(()=>ARCKHÉ.resume());await page.waitForURL('**/modulo-1-1.html#*');
// Invalid imports must be atomic; unknown fields must round-trip.
const checks=await page.evaluate(()=>{let a=JSON.parse(ARCKHÉ.exportJSON());a.extension={a:[1,2]};let ok=ARCKHÉ.importJSON(JSON.stringify(a));let b=ARCKHÉ.exportJSON();let bad=ARCKHÉ.importJSON(JSON.stringify({...a,notes:{broken:7}}));return {ok,bad,unchanged:b===ARCKHÉ.exportJSON(),extra:JSON.parse(b).extension}});assert(checks.ok.ok);assert(!checks.bad.ok);assert(checks.unchanged);assert.deepEqual(checks.extra,{a:[1,2]});
await page.getByRole('button',{name:/Minha jornada/}).click();await page.locator('.ARCKHÉ-journey').waitFor({state:'visible'});await page.keyboard.press('Escape');await page.waitForTimeout(400);assert.equal(await page.locator('.ARCKHÉ-journey').count(),0);
await page.goto(base+'/pratica.html');await page.locator('#decisao').fill('Triagem fictícia');await page.locator('button[type=submit]').click();assert.equal(await page.evaluate(()=>JSON.parse(ARCKHÉ.exportJSON()).worksheet.decisao),'Triagem fictícia');await page.reload();assert.equal(await page.locator('#decisao').inputValue(),'Triagem fictícia');await page.locator('#wr').fill('1');await page.locator('#calculate').click();assert.equal(await page.locator('#composite').innerText(),'0,6250');
for(const width of [1440,390]){await page.setViewportSize({width,height:950});for(const url of ['/','/curso/trilha1/index.html','/curso/trilha1/modulo-1-1.html','/pratica.html']){await page.goto(base+url);assert(!(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1)),url+' overflow');}await page.screenshot({path:'/tmp/jev-course-'+width+'.png'});}
await page.goto(base+'/curso/trilha2/index.html');await page.locator('[data-preview]').first().click();assert(await page.locator('dialog iframe').isVisible());await page.keyboard.press('Escape');await page.locator('dialog').waitFor({state:'detached'});
const blocked=await browser.newContext();await blocked.addInitScript(()=>{Object.defineProperty(window,'localStorage',{get(){throw Error('blocked')}})});const p=await blocked.newPage();await p.goto(base+'/curso/trilha1/modulo-1-1.html');await p.locator('[data-ARCKHÉ-read-toggle]').first().click();assert.equal((await p.evaluate(()=>ARCKHÉ.progress('curso'))).done,1);
const nojs=await browser.newContext({javaScriptEnabled:false});const plain=await nojs.newPage();await plain.goto(base+'/curso/trilha1/modulo-1-1.html');assert.equal(await plain.locator('[data-ARCKHÉ-topic]').count(),6);assert(await plain.locator('h1').isVisible());
assert.deepEqual(errors,[]);await browser.close();console.log('Browser OK: progress, resume, doubts, quiz, import, worksheet, dialog, mobile, blocked storage and no JS.');})().catch(e=>{console.error(e);process.exit(1)});
