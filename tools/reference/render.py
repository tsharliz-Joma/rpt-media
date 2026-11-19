import sys, asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        for src, out, w, h in [("cover.html","rpt-facebook-cover.png",1640,720),("profile.html","rpt-profile-picture.png",1080,1080)]:
            pg = await b.new_page(viewport={"width":w,"height":h}, device_scale_factor=1)
            await pg.goto(f"file:///home/claude/brand-assets/{src}")
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(400)
            await pg.locator(".stage").screenshot(path=f"/home/claude/brand-assets/{out}")
            await pg.close()
        await b.close()
asyncio.run(main())
