import json, sys
R="/home/claude/rpt-stories"; P="/home/claude/rpt-posts/out"
SG="font-family: 'Space Grotesk', sans-serif;"
stories = {
 1: ("#15152B", "#FFFFFF", True,  "We're live!<br>Come say hi."),
 2: ("#2F45E0", "#FFFFFF", True,  "Is your website as good as your gym?"),
 3: ("#2F45E0", "#FFFFFF", True,  "A site plus 12 posts, every month."),
 4: ("#15152B", "#FFFFFF", True,  "Plans from<br>$149 a month."),
 5: ("#2F45E0", "#FFFFFF", True,  "Three steps.<br>That's it."),
 6: ("#C6F432", "#15152B", False, "Take a look at Northpaw."),
 7: ("#15152B", "#FFFFFF", True,  "Does your gym site have all three?"),
 8: ("#FFB547", "#15152B", False, "Built with AI.<br>Checked by a fighter."),
 9: ("#2F45E0", "#FFFFFF", True,  "Free mockup<br>for your gym.<br>DM us MOCKUP."),
}
def markup(n, img_src):
    bg, fg, dark, line = stories[n]
    pill_bg, pill_fg = ("#FFFFFF", "#2F45E0") if dark else ("#15152B", "#FFFFFF")
    sub = "#DCE2FF" if fg=="#FFFFFF" else "#2B2B45"
    return f'''<div style="width: 1080px; height: 1920px; box-sizing: border-box; padding: 260px 96px 360px; background: {bg}; color: {fg}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 64px; font-family: Inter, sans-serif; overflow: hidden; text-align: center;">
<div style="background: {pill_bg}; color: {pill_fg}; border-radius: 999px; padding: 16px 34px; {SG} font-weight: 700; font-size: 30px; letter-spacing: 4px;">NEW POST</div>
<img src="{img_src}" alt="Today's post from Rocket Power Tech" style="width: 620px; height: 775px; object-fit: cover; border-radius: 44px; border: 10px solid #FFFFFF; box-sizing: border-box; transform: rotate(-4deg); box-shadow: 0 40px 80px rgba(10, 14, 40, 0.35);">
<h1 style="margin: 0; {SG} font-weight: 700; font-size: 84px; line-height: 1.04; letter-spacing: -2px; max-width: 860px;">{line}</h1>
<p style="margin: 0; font-size: 34px; font-weight: 600; color: {sub};">@rocketpowertech</p>
</div>'''
mode = sys.argv[1]
if mode == "render":
    FONT="/home/claude/brand-assets/fonts/node_modules/@fontsource"
    head=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>
@font-face{{font-family:"Space Grotesk";font-weight:700;src:url("file://{FONT}/space-grotesk/files/space-grotesk-latin-700-normal.woff2") format("woff2");}}
@font-face{{font-family:"Inter";font-weight:600;src:url("file://{FONT}/inter/files/inter-latin-600-normal.woff2") format("woff2");}}
@font-face{{font-family:"Inter";font-weight:400;src:url("file://{FONT}/inter/files/inter-latin-400-normal.woff2") format("woff2");}}
html,body{{margin:0}}</style></head><body><div class="stage" style="width:1080px;height:1920px">'''
    for n in stories:
        open(f"{R}/render/story{n}.html","w").write(head+markup(n, f"file://{P}/post{n}.png")+"</div></body></html>")
else:
    urls=json.load(open(f"{R}/asset_urls.json"))
    tail='''
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1080,"height":1920}}'>
class Component extends DCLogic {
  renderVals() {
    return {};
  }
}
</script>
</body>
</html>
'''
    for n in stories:
        head=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Story {n}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&amp;family=Space+Grotesk:wght@700&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0}}
</style>
</helmet>
'''
        open(f"/home/claude/rpt-posts/project/Story{n}.dc.html","w").write(head+markup(n, urls[str(n)])+tail)
print("ok", mode)
