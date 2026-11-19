import asyncio
from playwright.async_api import async_playwright
from PIL import Image
R="/home/claude/rpt-stories"
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width":1080,"height":1920}, device_scale_factor=1)
        for i in range(1,10):
            await pg.goto(f"file://{R}/render/story{i}.html")
            await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(250)
            await pg.locator(".stage").screenshot(path=f"{R}/out/story{i}.png")
            Image.open(f"{R}/out/story{i}.png").convert("RGB").save(f"{R}/out/rpt-story-{i}.jpg", quality=92)
        await b.close()
asyncio.run(main())
tw,th,gap=216,384,8
strip=Image.new("RGB",(tw*9+gap*8, th),"white")
for i in range(1,10):
    strip.paste(Image.open(f"{R}/out/story{i}.png").convert("RGB").resize((tw,th),Image.LANCZOS),((i-1)*(tw+gap),0))
strip.save(f"{R}/out/rpt-stories-preview.jpg",quality=90)
print("done")
