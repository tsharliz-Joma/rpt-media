import asyncio
from playwright.async_api import async_playwright
from PIL import Image
R="/home/claude/rpt-posts"
NS=range(10,17)
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width":1080,"height":1350}, device_scale_factor=1)
        for i in NS:
            await pg.goto(f"file://{R}/render/post{i}.html")
            await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(250)
            await pg.locator(".stage").screenshot(path=f"{R}/out/post{i}.png")
            Image.open(f"{R}/out/post{i}.png").convert("RGB").save(f"{R}/out/rpt-post-{i}.jpg", quality=92)
        await b.close()
asyncio.run(main())
tw,th,gap=360,480,6
order=[16,15,14,13,12,11,10,9,8]
grid=Image.new("RGB",(tw*3+gap*2, th*3+gap*2),"white")
for idx,n in enumerate(order):
    im=Image.open(f"{R}/out/post{n}.png").convert("RGB"); w=int(1350*0.75); x0=(1080-w)//2
    im=im.crop((x0,0,x0+w,1350)).resize((tw,th),Image.LANCZOS); r,c=divmod(idx,3)
    grid.paste(im,(c*(tw+gap),r*(th+gap)))
grid.save(f"{R}/out/rpt-week2-grid-preview.jpg",quality=90)
print("done")
