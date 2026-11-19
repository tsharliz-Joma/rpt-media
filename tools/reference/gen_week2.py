import json, re
src = open('/home/claude/scripts/gen_posts.py').read()
helpers = src[:src.index("H2 = h(")]
helpers = helpers.replace('ROOT="/home/claude/rpt-posts"', 'ROOT="/home/claude/rpt-posts"')
exec(helpers)
exec(src[src.index("DC_HEAD='''"):src.index("caps={}")])
MINT="#E3F7EE"
def bullets(items, bg="#FFFFFF"):
    return "\n".join(checkrow(t) for t in items)
def col(title, items, bg, fg, tick):
    rows = "".join(f'<div style="display: flex; align-items: center; gap: 16px;"><span style="flex: 0 0 auto; width: 44px; height: 44px; border-radius: 999px; background: {tick}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 24px;">{m}</span><span style="font-size: 32px; font-weight: 600; line-height: 1.2;">{t}</span></div>' for m,t in items)
    return f'<div style="flex: 1 1 0; background: {bg}; color: {fg}; border-radius: 36px; padding: 36px; display: flex; flex-direction: column; gap: 24px;"><span style="{SG} font-weight: 700; font-size: 44px;">{title}</span>{rows}</div>'
X = "&#215;"
week = []
week.append(dict(n=10, title="Google profile tip", bg=MINT, dark=False, fg=INK, foot="#1F6B4A",
 middle=f'''{h("Your Google profile is your second website.", 96, INK)}
<div style="display: flex; flex-direction: column; gap: 20px;">
{checkrow("Hours that are actually right")}
{checkrow("Real photos of your gym")}
{checkrow("A reply to every review")}
</div>''',
 caption="""Before people find your website, they often find your Google profile first. It's free, and it's worth ten minutes this week.

Check your opening hours are right, add a few real photos of your gym, and reply to every review, good or bad.

Small fixes, big first impression.

#gymowner #boxinggym #sydneygyms #gymtips"""))
week.append(dict(n=11, title="Do I need to write anything", bg=INK, dark=True, fg="#FFFFFF", foot="#A9ABC4",
 middle=f'''{h("Do I need to write anything?", 108, "#FFFFFF")}
<div style="align-self: flex-start; background: #FFB547; color: {INK}; border-radius: 999px; padding: 20px 40px; {SG} font-weight: 700; font-size: 64px;">Nope.</div>
{p("Fill in a short form and have a quick chat. We write the words, you check them.", "#C9CBE0")}''',
 caption="""One of the most common worries we hear: I don't have time to write website copy.

You don't have to. Fill in a short form, have a quick chat about your gym, and we write everything. You just check it sounds like you.

#gymowner #boxinggym #personaltrainer #smallbusinesssydney"""))
week.append(dict(n=12, title="Clear beats fancy", bg="#C6F432", dark=False, fg=INK, foot="#2B2B45",
 middle=f'''{h("You don't need a fancy website.", 104, INK)}
{h("You need a clear one.", 104, BLUE)}
{p("Timetable, prices, location and a way to book. Get those right first.", "#2B2B45")}''',
 caption="""You don't need animations, videos or ten pages.

You need your timetable, your prices, where you are, and an easy way to book a first class. Get those four right and your site is already doing its job.

#gymwebsite #boxinggym #gymowner #sydneyfitness"""))
week.append(dict(n=13, title="3 photos every gym needs", bg="#FFF0E3", dark=False, fg=INK, foot="#7A3E00",
 middle=f'''{h("3 photos every gym site needs", 100, INK)}
<div style="display: flex; flex-direction: column; gap: 20px;">
{numrow(1, "The floor, set up and ready", "#E8ECFF", "#1E2FB0")}
{numrow(2, "Your coaches, smiling", "#FFFFFF", "#9A3412", bg="#FFFFFF")}
{numrow(3, "A class in full swing", "#E3F7EE", "#1F6B4A")}
</div>''',
 caption="""Stock photos don't sell a gym. Real ones do.

Three shots worth taking this week:
1. The floor, clean and set up before a class.
2. Your coaches, looking like people someone would want to train with.
3. A class in full swing, so people can picture themselves there.

Phone photos are fine. Good light matters more than a good camera.

#gymowner #boxinggym #gymphotos #sydneygyms"""))
week.append(dict(n=14, title="Before and after", bg="#F6F6FB", dark=False, fg=INK, foot="#4A4A66",
 middle=f'''{h("What changes when we rebuild a gym site", 92, INK)}
<div style="display: flex; gap: 20px; align-items: stretch;">
{col("Before", [(X,"Timetable is a PDF"),(X,"No prices"),(X,"Hard to read on a phone")], "#FFFFFF", INK, "#9A3412")}
{col("After", [("&#10003;","Timetable on the page"),("&#10003;","Clear prices"),("&#10003;","Built for phones")], BLUE, "#FFFFFF", "#1F6B4A")}
</div>''',
 caption="""What actually changes when we rebuild a gym website:

Before: a timetable hidden in a PDF, no prices, and a page that's hard to read on a phone.
After: the timetable right on the page, clear prices, and everything built for phones first, because that's where people look you up.

#gymwebsite #webdesign #boxinggym #gymowner"""))
week.append(dict(n=15, title="Why gyms", bg=INK, dark=True, fg="#FFFFFF", foot="#A9ABC4",
 middle=f'''{h("Why gyms?", 120, "#FFFFFF")}
{h("Because I fought out of them.", 92, "#C6F432")}
<div style="display: flex; flex-wrap: wrap; gap: 16px;">
<span style="background: #FFFFFF; color: {INK}; border-radius: 999px; padding: 16px 28px; {SG} font-weight: 700; font-size: 36px;">66 fights</span>
<span style="background: #FFB547; color: {INK}; border-radius: 999px; padding: 16px 28px; {SG} font-weight: 700; font-size: 36px;">Arafura Games gold</span>
<span style="background: #E8ECFF; color: {INK}; border-radius: 999px; padding: 16px 28px; {SG} font-weight: 700; font-size: 36px;">2x Victorian champion</span>
<span style="background: #E3F7EE; color: {INK}; border-radius: 999px; padding: 16px 28px; {SG} font-weight: 700; font-size: 36px;">3x Queensland Golden Gloves</span>
</div>''',
 caption="""Why do we only work with gyms, fight gyms and PTs?

Because I spent years in them. 66 fights, an Arafura Games gold, two Victorian titles and three Queensland Golden Gloves.

I know what it feels like to walk into a gym for the first time, and what makes people stay. That's what we build every site around.

Charles, Rocket Power Tech

#boxing #boxinggym #gymowner #sydneygyms"""))
week.append(dict(n=16, title="Launch Kit", bg="#E8ECFF", dark=False, fg=INK, foot="#4A4A66",
 middle=f'''{h("Opening a new gym?", 108, INK)}
{p("The Launch Kit gets you ready for opening day.", "#4A4A66")}
<div style="display: flex; flex-direction: column; gap: 20px;">
{checkrow("A brand kit with your colours and logo")}
{checkrow("A one page website")}
{checkrow("9 launch posts")}
</div>
<div style="align-self: flex-start; background: {BLUE}; color: #FFFFFF; border-radius: 999px; padding: 22px 40px; {SG} font-weight: 700; font-size: 44px;">$790 one off</div>''',
 caption="""Opening a new gym, or a new location?

The Launch Kit gets you ready for opening day: a brand kit with your colours and logo, a one page website, and 9 launch posts to build buzz before the doors open.

$790 one off. DM us to chat.

#newgym #boxinggym #gymowner #sydneybusiness"""))
DC_TAIL_W='''
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
caps={}
for post in week:
    n=post["n"]; m = wrap(post["bg"], post["fg"], post["dark"], post["middle"], post["foot"])
    open(f"{ROOT}/project/Post{n}.dc.html","w").write(DC_HEAD.format(title=f"Post {n} {post['title']}") + m + DC_TAIL_W)
    open(f"{ROOT}/render/post{n}.html","w").write(RENDER_HEAD + m + "</div></body></html>")
    caps[n]=dict(title=post["title"], caption=post["caption"])
json.dump(caps, open(f"{ROOT}/out/captions_week2.json","w"), indent=1)
bad=[k for k,v in caps.items() if re.search(r"[\-–—]", v["caption"])]
print("ok", len(week), "dash issues:", bad)
