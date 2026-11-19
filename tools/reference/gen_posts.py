import json, os
ROOT="/home/claude/rpt-posts"
INK="#15152B"; BLUE="#2F45E0"; LIME="#C6F432"
SG="font-family: 'Space Grotesk', sans-serif;"
def rocket(size, body, window_fill="#FFFFFF"):
    return f'''<svg width="{size}" height="{size}" viewBox="-20 -20 240 240" aria-hidden="true"><g transform="rotate(42 100 105)"><path d="M100 160 C114 174 113 190 100 204 C87 190 86 174 100 160 Z" fill="#FF7A1A"></path><path d="M100 168 C107 177 107 187 100 196 C93 187 93 177 100 168 Z" fill="#FFB547"></path><rect x="82" y="146" width="36" height="14" rx="5" fill="#15152B"></rect><path d="M64 108 L38 136 Q32 144 40 150 L64 150 Z" fill="#15152B"></path><path d="M136 108 L162 136 Q168 144 160 150 L136 150 Z" fill="#15152B"></path><path d="M100 16 C130 34 140 70 140 108 L140 142 Q140 150 132 150 L68 150 Q60 150 60 142 L60 108 C60 70 70 34 100 16 Z" fill="{body}"></path><circle cx="100" cy="88" r="19" fill="{window_fill}" stroke="#15152B" stroke-width="7"></circle></g></svg>'''
def chip(dark_bg):
    if dark_bg:
        bg, fg, disc, body, win = "#FFFFFF", BLUE, BLUE, "#FFFFFF", BLUE
    else:
        bg, fg, disc, body, win = BLUE, "#FFFFFF", "#FFFFFF", BLUE, "#FFFFFF"
    return f'''<div style="align-self: flex-start; display: flex; align-items: center; gap: 14px; background: {bg}; color: {fg}; border-radius: 999px; padding: 12px 28px 12px 12px; {SG} font-weight: 700; font-size: 24px; letter-spacing: 3px;"><span style="width: 48px; height: 48px; border-radius: 999px; background: {disc}; display: flex; align-items: center; justify-content: center;">{rocket(40, body, win)}</span>ROCKET POWER TECH</div>'''
def footer(color):
    return f'<div style="font-size: 26px; font-weight: 600; color: {color};">@rocketpowertech</div>'
def wrap(bg, fg, dark, middle, foot_color):
    return f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 96px; background: {bg}; color: {fg}; display: flex; flex-direction: column; justify-content: space-between; gap: 40px; font-family: Inter, sans-serif; overflow: hidden;">
{chip(dark)}
<div style="display: flex; flex-direction: column; gap: 40px;">
{middle}
</div>
{footer(foot_color)}
</div>'''
def h(text, size=104, color=None):
    c = f" color: {color};" if color else ""
    return f'<h1 style="margin: 0; {SG} font-weight: 700; font-size: {size}px; line-height: 1.0; letter-spacing: -3px;{c}">{text}</h1>'
def p(text, color, size=40):
    return f'<p style="margin: 0; font-size: {size}px; line-height: 1.35; color: {color}; max-width: 860px;">{text}</p>'
def row(label, right, bg, fg, extra=""):
    return f'''<div style="display: flex; align-items: center; justify-content: space-between; gap: 24px; background: {bg}; color: {fg}; border-radius: 32px; padding: 34px 40px;"><span style="{SG} font-weight: 700; font-size: 44px;">{label}{extra}</span><span style="font-size: 36px; font-weight: 600;">{right}</span></div>'''
def numrow(n, text, badge_bg, badge_fg, bg="#FFFFFF"):
    return f'''<div style="display: flex; align-items: center; gap: 32px; background: {bg}; border-radius: 32px; padding: 30px 36px;"><span style="flex: 0 0 auto; width: 84px; height: 84px; border-radius: 26px; background: {badge_bg}; color: {badge_fg}; {SG} font-weight: 700; font-size: 44px; display: flex; align-items: center; justify-content: center;">{n}</span><span style="{SG} font-weight: 700; font-size: 44px; line-height: 1.15; color: {INK};">{text}</span></div>'''
def checkrow(text):
    return f'''<div style="display: flex; align-items: center; gap: 30px; background: #FFFFFF; border-radius: 32px; padding: 30px 36px;"><span style="flex: 0 0 auto; width: 84px; height: 84px; border-radius: 999px; background: #1F6B4A; display: flex; align-items: center; justify-content: center;"><svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg></span><span style="{SG} font-weight: 700; font-size: 44px; line-height: 1.15; color: {INK};">{text}</span></div>'''

H2 = h('Great gym.<br><span style="color: #C6F432;">Quiet website?</span>', 120, "#FFFFFF")
H3 = h('A website plus<br>12 fresh posts.<br><span style="color: #2F45E0;">Every month.</span>', 100, INK)
H8 = h('Built with AI.<br><span style="color: #FFB547;">Checked by<br>a fighter.</span>', 108, "#FFFFFF")
posts = []
# 1 Intro
posts.append(dict(title="Post 1 Intro", bg=BLUE, dark=True, middle=f'''<div style="width: 300px; height: 300px; border-radius: 999px; background: #FFFFFF; display: flex; align-items: center; justify-content: center;">{rocket(250, BLUE)}</div>
{h("Hi, we're<br>Rocket Power Tech.", 90, "#FFFFFF")}
{p("Websites and monthly posts for boxing gyms and PTs in Sydney.", "#DCE2FF")}''', fg="#FFFFFF", foot="#DCE2FF",
caption="""Hi, we're Rocket Power Tech.

We make websites and monthly social posts for boxing gyms, fight gyms and personal trainers around Sydney. One simple monthly price, no upfront build fee.

Run by Charles, a former fighter who builds websites. Say hi in the DMs.

#sydneygyms #boxinggym #personaltrainer #gymmarketing #smallbusinesssydney"""))
# 2 Problem
posts.append(dict(title="Post 2 Problem", bg=INK, dark=True, middle=f'''{H2}
{p("People look you up online before they ever walk through the door. Let's make that first look count.", "#C9CBE0")}''', fg="#FFFFFF", foot="#A9ABC4",
caption="""Your coaching is sharp. Your community is tight. But if your website hasn't been touched in years, that's the first thing a new member sees.

We build clean, fast gym websites and keep them fresh, so your online first impression matches the real thing.

#boxinggym #gymowner #sydneyfitness #gymmarketing"""))
# 3 What you get
posts.append(dict(title="Post 3 What you get", bg="#E8ECFF", dark=False, middle=f'''<div style="display: flex; gap: 24px; align-items: stretch;">
<div style="flex: 1 1 0; min-height: 300px; background: #0E0E11; border-radius: 36px; padding: 36px; display: flex; flex-direction: column; justify-content: space-between; gap: 16px;"><span style="{SG} font-weight: 700; color: {LIME}; font-size: 22px; letter-spacing: 3px;">YOUR GYM</span><span style="{SG} font-weight: 700; color: #F4F4F5; font-size: 44px; line-height: 1.05;">Train like a fighter.</span><span style="align-self: flex-start; background: {LIME}; color: #0E0E11; font-weight: 600; font-size: 20px; padding: 10px 18px; border-radius: 999px;">Book a free class</span></div>
<div style="flex: 0 0 300px; display: flex; flex-direction: column; gap: 24px;"><div style="flex: 1 1 0; background: #FFB547; border-radius: 30px; padding: 24px; display: flex; align-items: flex-end;"><span style="{SG} font-weight: 700; font-size: 28px; line-height: 1.1; color: {INK};">Saturday sparring</span></div><div style="flex: 1 1 0; background: #FFFFFF; border-radius: 30px; padding: 24px; display: flex; align-items: flex-end;"><span style="{SG} font-weight: 700; font-size: 28px; line-height: 1.1; color: {INK};">New timetable</span></div></div>
</div>
{H3}''', fg=INK, foot="#4A4A66",
caption="""What you actually get:

A custom website for your gym, hosted and looked after.
12 branded posts with captions, ready on the 1st of every month.

You run the gym. We keep you looking sharp online.

#gymmarketing #boxinggym #sydneygyms #socialmediaforgyms"""))
# 4 Pricing
posts.append(dict(title="Post 4 Pricing", bg="#FFF0E3", dark=False, middle=f'''{h("Simple monthly plans.", 104, INK)}
{p("No upfront build fee.", "#7A3E00")}
<div style="display: flex; flex-direction: column; gap: 20px;">
{row("Site", "$149 a month", "#FFFFFF", INK)}
{row("Site + Content", "$499 a month", BLUE, "#FFFFFF")}
{row("Content", "$399 a month", "#FFFFFF", INK)}
</div>''', fg=INK, foot="#7A3E00",
caption="""Three plans, no surprises.

Site: $149 a month. Custom website, hosting and domain, plus 30 minutes of edits a month.
Content: $399 a month. 12 branded posts with captions every month.
Site + Content: $499 a month. Both, and you save $49.

No upfront build fee. Opening a new gym? Ask about the Launch Kit.

#gymowner #boxinggym #sydneybusiness #gymmarketing"""))
# 5 How it works
posts.append(dict(title="Post 5 How it works", bg="#F6F6FB", dark=False, middle=f'''{h("How it works", 110, INK)}
<div style="display: flex; flex-direction: column; gap: 20px;">
{numrow(1, "Tell us about your gym", "#E8ECFF", "#1E2FB0")}
{numrow(2, "Approve your new site", "#FFF0E3", "#9A3412")}
{numrow(3, "Fresh posts land every month", "#E3F7EE", "#1F6B4A")}
</div>''', fg=INK, foot="#4A4A66",
caption="""How it works, start to finish:

1. Fill in a short form and have a 15 minute chat about your gym.
2. We build your site. You check it, we fix anything, it goes live.
3. 12 fresh posts and captions land on the 1st of every month.

That's it. No tech headaches on your end.

#gymowner #boxinggym #personaltrainer #sydneygyms"""))
# 6 Demo
posts.append(dict(title="Post 6 Demo", bg="#0E0E11", dark=True, middle=f'''<div style="background: #1A1A20; border-radius: 40px; padding: 48px; display: flex; flex-direction: column; gap: 24px;">
<div style="display: flex; align-items: center; justify-content: space-between; gap: 16px;"><span style="{SG} font-weight: 700; color: {LIME}; font-size: 26px; letter-spacing: 4px;">NORTHPAW</span><span style="border: 2px solid #3F3F46; color: #D4D4D8; font-size: 22px; font-weight: 600; padding: 8px 18px; border-radius: 999px;">Demo</span></div>
<span style="{SG} font-weight: 700; color: #F4F4F5; font-size: 72px; line-height: 1.0;">Train like a fighter.</span>
<span style="align-self: flex-start; background: {LIME}; color: #0E0E11; font-weight: 700; font-size: 26px; padding: 14px 26px; border-radius: 999px;">Book a free class</span>
</div>
{h("Meet Northpaw.", 110, "#FFFFFF")}
{p("A demo gym site we built to show what yours could look like.", "#A1A1AA")}''', fg="#FFFFFF", foot="#A1A1AA",
caption="""Meet Northpaw, a demo boxing gym we made up to show what a Rocket Power Tech site looks like.

A clickable weekly timetable, clear membership prices, and a free class signup front and centre.

Want to see your own gym like this? DM us MOCKUP.

#boxinggym #gymwebsite #webdesign #sydneygyms"""))
# 7 Tip
posts.append(dict(title="Post 7 Tip", bg="#E3F7EE", dark=False, middle=f'''{h("3 things every gym site needs", 100, INK)}
<div style="display: flex; flex-direction: column; gap: 20px;">
{checkrow("Your timetable, up to date")}
{checkrow("Clear prices")}
{checkrow("A free class button that's easy to find")}
</div>''', fg=INK, foot="#1F6B4A",
caption="""Quick check for gym owners. Does your website have these three?

1. Your timetable, up to date. People want to know when they can come.
2. Clear prices. Hidden prices make people click away.
3. A free class button that's easy to find. Make the first step simple.

Missing one? We can help.

#gymowner #boxinggym #gymtips #sydneyfitness"""))
# 8 Built with AI
posts.append(dict(title="Post 8 Built with AI", bg=BLUE, dark=True, middle=f'''{H8}
{p("I'm Charles. 66 fights taught me to sweat the details, so nothing goes live that I wouldn't put my name on.", "#DCE2FF")}''', fg="#FFFFFF", foot="#DCE2FF",
caption="""Honest answer to a fair question: yes, we use AI.

It helps us design and build fast, which is how we keep prices low. But every site and every post gets checked by me before it goes anywhere. 66 fights taught me to sweat the details, so wrong class times or made up claims don't get past me.

Charles, Rocket Power Tech

#boxing #gymmarketing #smallbusinesssydney #webdesign"""))
# 9 Offer
posts.append(dict(title="Post 9 Offer", bg="#FFB547", dark=False, middle=f'''{h("Free homepage mockup for your gym.", 108, INK)}
{p("Send us a DM with the word MOCKUP and we'll design one for you. No strings attached.", "#5C2E00")}
<div style="align-self: flex-start; background: {INK}; color: #FFFFFF; border-radius: 999px; padding: 26px 44px; {SG} font-weight: 700; font-size: 44px; letter-spacing: 2px;">DM us MOCKUP</div>''', fg=INK, foot="#5C2E00",
caption="""Want to see what your gym could look like online?

Send us a DM with the word MOCKUP and we'll design a homepage mockup for your gym, free. If you like it, we can talk. If not, no worries.

Boxing gyms, fight gyms and PTs around Sydney.

#boxinggym #sydneygyms #personaltrainer #gymowner"""))

DC_HEAD='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Space+Grotesk:wght@500;600;700&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0}}
</style>
</helmet>
'''
DC_TAIL='''
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1080,"height":1350}}'>
class Component extends DCLogic {
  renderVals() {
    return {};
  }
}
</script>
</body>
</html>
'''
FONT=f"{ROOT}/../brand-assets/fonts/node_modules/@fontsource"
RENDER_HEAD=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><style>
@font-face{{font-family:"Space Grotesk";font-weight:700;src:url("file://{FONT}/space-grotesk/files/space-grotesk-latin-700-normal.woff2") format("woff2");}}
@font-face{{font-family:"Space Grotesk";font-weight:500;src:url("file://{FONT}/space-grotesk/files/space-grotesk-latin-500-normal.woff2") format("woff2");}}
@font-face{{font-family:"Inter";font-weight:400;src:url("file://{FONT}/inter/files/inter-latin-400-normal.woff2") format("woff2");}}
@font-face{{font-family:"Inter";font-weight:500;src:url("file://{FONT}/inter/files/inter-latin-500-normal.woff2") format("woff2");}}
@font-face{{font-family:"Inter";font-weight:600;src:url("file://{FONT}/inter/files/inter-latin-600-normal.woff2") format("woff2");}}
@font-face{{font-family:"Inter";font-weight:700;src:url("file://{FONT}/inter/files/inter-latin-600-normal.woff2") format("woff2");}}
html,body{{margin:0;padding:0}}
</style></head><body><div class="stage" style="width:1080px;height:1350px">
'''
caps={}
for i,post in enumerate(posts,1):
    m = wrap(post["bg"], post["fg"], post["dark"], post["middle"], post["foot"])
    open(f"{ROOT}/project/Post{i}.dc.html","w").write(DC_HEAD.format(title=post["title"]) + m + DC_TAIL)
    open(f"{ROOT}/render/post{i}.html","w").write(RENDER_HEAD + m + "</div></body></html>")
    caps[i]=post["caption"]
json.dump(caps, open(f"{ROOT}/out/captions.json","w"), indent=1)
print("ok", len(posts))
