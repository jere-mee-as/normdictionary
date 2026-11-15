import sys, asyncio
from playwright.async_api import async_playwright
ROOT = '/home/claude/samerule/'
async def run(page_name, w, h):
    async with async_playwright() as p:
        b = await p.chromium.launch(); ctx = await b.new_context(viewport={'width': w, 'height': h}); pg = await ctx.new_page()
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto('file://' + ROOT + page_name); await pg.wait_for_timeout(600)
        tag = f'{page_name}@{w}'
        # outline: open first level, first group, first claim
        for mode in ['outline', 'sentence', 'stems']:
            await pg.click(f'#sw button:text-is("{mode}")'); await pg.wait_for_timeout(400)
            sec = {'outline': '#outl', 'sentence': '#sent', 'stems': '#stem'}[mode]
            sel = {'outline': '#outl .orow', 'sentence': '#sent .ch', 'stems': '#stem .sit:not(.off)'}[mode]
            for depth in range(3):
                rows = pg.locator(sel)
                if mode == 'outline': rows = pg.locator(f'#outl .d{depth}')
                if mode == 'stems': rows = pg.locator(f'#stem .scol').nth(depth).locator('.sit')
                await rows.first.click(); await pg.wait_for_timeout(700)
            n = await pg.locator(f'{sec} .fact:visible').count()
            print(tag, mode, 'facts visible:', n)
            await pg.screenshot(path=f'{ROOT}shots/{page_name}-{w}-{mode}.png')
        # fold + copy
        f = pg.locator('#stem .fact').first; await f.click(); await pg.wait_for_timeout(300)
        print(tag, 'fold open:', await f.evaluate('e => e.classList.contains("open")'))
        await ctx.grant_permissions(['clipboard-read', 'clipboard-write'])
        await f.locator('.cp').click(); await pg.wait_for_timeout(200)
        print(tag, 'copied:', (await pg.evaluate('navigator.clipboard.readText()'))[:120])
        await pg.fill('#find', 'teacher'); await pg.wait_for_timeout(400)
        print(tag, 'search note/nohits:', await pg.evaluate('document.documentElement.classList.contains("nohits")'))
        await pg.screenshot(path=f'{ROOT}shots/{page_name}-{w}-search.png'); await pg.fill('#find', '')
        await pg.click('#theme'); await pg.wait_for_timeout(200); print(tag, 'themes:', await pg.locator('#themes button').count())
        print(tag, 'foot:', '-', 'ERRORS:', errs)
        await b.close()
async def main():
    for pn in ['index.html']:
        for w, h in [(1280, 800), (390, 844)]: await run(pn, w, h)
asyncio.run(main())
