import sys, asyncio
from playwright.async_api import async_playwright
async def main(src,out,w,h):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':w,'height':h})
        await pg.goto('file:///home/claude/v4/'+src); await pg.wait_for_timeout(800)
        await pg.screenshot(path=out); await b.close()
asyncio.run(main(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])))
