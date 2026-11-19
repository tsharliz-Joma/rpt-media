import sys, json
src=open('/home/claude/scripts/gen_stories.py').read()
exec(src[:src.index("mode = sys.argv[1]")])
stories.clear()
stories.update({
 10: ("#15152B", "#FFFFFF", True,  "Is your Google profile up to date?"),
 11: ("#2F45E0", "#FFFFFF", True,  "No writing needed.<br>We've got it."),
 12: ("#15152B", "#FFFFFF", True,  "Clear beats fancy.<br>Every time."),
 13: ("#2F45E0", "#FFFFFF", True,  "3 photos worth<br>taking this week."),
 14: ("#FFB547", "#15152B", False, "Before and after<br>a gym rebuild."),
 15: ("#C6F432", "#15152B", False, "Why we only<br>work with gyms."),
 16: ("#2F45E0", "#FFFFFF", True,  "Opening a new gym?<br>Launch Kit, $790."),
})
mode=sys.argv[1]
if mode=="render":
    FONT="/home/claude/brand-assets/fonts/node_modules/@fontsource"
    head=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>
@font-face{{font-family:"Space Grotesk";font-weight:700;src:url("file://{FONT}/space-grotesk/files/space-grotesk-latin-700-normal.woff2") format("woff2");}}
@font-face{{font-family:"Inter";font-weight:600;src:url("file://{FONT}/inter/files/inter-latin-600-normal.woff2") format("woff2");}}
html,body{{margin:0}}</style></head><body><div class="stage" style="width:1080px;height:1920px">'''
    for n in stories:
        open(f"{R}/render/story{n}.html","w").write(head+markup(n, f"file://{P}/post{n}.png")+"</div></body></html>")
else:
    urls=json.load(open(f"{R}/asset_urls2.json"))
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
        open(f"/home/claude/rpt-posts/project/Story{n}.dc.html","w").write(head+markup(n, urls[str(n)])+tail)
print("ok", mode)
