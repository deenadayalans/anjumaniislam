from html import escape as esc
from common import *
import content as C

META = dict(
    slug="hillstation", name="Hill Station Editorial", palette=["#1f3a2e", "#b5651d", "#efe7d6"],
    tagline="Above the clouds, a place to grow",
    blurb="Immersive and magazine-like: a parallax mountain-range hero, full-screen menu, custom cursor, giant type, draggable campus rail and a presidents’ roll set like a newspaper masthead. It sells the place — Panchgani itself.",
    fonts="DM Serif Display · DM Sans",
)
FONTS = "https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@400;500;700&display=swap"
ARROW = ic("arrow")

RANGES = '''<svg class="ly l1" data-par=".26" viewBox="0 0 1440 500" preserveAspectRatio="none" aria-hidden="true"><path d="M0 290l140-110 120 70 170-150 150 110 160-100 190 150 140-90 170 130H1440v400H0z" fill="#d79a73" opacity=".6"/></svg>
<svg class="ly l2" data-par=".17" viewBox="0 0 1440 460" preserveAspectRatio="none" aria-hidden="true"><path d="M0 250l180-90 150 60 200-120 180 100 170-70 210 130 150-70H1440v320H0z" fill="#8c7a63" opacity=".8"/></svg>
<svg class="ly l3" data-par=".09" viewBox="0 0 1440 420" preserveAspectRatio="none" aria-hidden="true"><path d="M0 210l160 60 190-110 220 90 210-80 190 70 270-60H1440v250H0z" fill="#4a6654"/></svg>
<svg class="ly l4" data-par=".02" viewBox="0 0 1440 360" preserveAspectRatio="none" aria-hidden="true"><path d="M0 150c180-80 360-70 540-10s360 50 520-20 260-20 380 20v220H0z" fill="#1f3a2e"/></svg>'''


def layout(slug, title, body, hero=""):
    menu = "".join(f'<a href="{s}.html"><span>{i + 1:02d}</span>{l}</a>' for i, (s, l) in enumerate(PAGES))
    return head(f"{title} — {C.SCHOOL['name']}", "Boarding school and junior college in Panchgani — part of Anjuman-I-Islam, founded 1874.", FONTS, "#1f3a2e") + f'''
<body data-cursor>
<div class="curtain"></div><div class="progress"><i></i></div><a class="skip" href="#main">Skip to content</a>
<header class="hdr" data-header data-hide><div class="wrap hdr-in">
  <a class="brand" href="index.html"><span class="logo-ph">LOGO</span><span><b>Anjuman-I-Islam</b><small>Public School &amp; Jr. College · Panchgani</small></span></a>
  <div class="hdr-r"><a class="apply" href="admissions.html#enquire">Apply</a><button class="menu-btn" data-nav-toggle aria-label="Menu" aria-expanded="false"><span>Menu</span><i></i><i></i></button></div>
</div></header>
<div class="nav"><div class="wrap nav-in"><nav>{menu}</nav><div class="nav-side"><p class="kick">Contact</p><p>{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}<br>{C.SCHOOL['email_admissions']}</p><p class="kick">Part of</p><img class="plogo" src="assets/real/logo.png" alt="Anjuman-I-Islam"></div></div></div>
{hero}<main id="main">{body}</main>
<footer class="ftr"><div class="wrap">
  <p class="kick">Admissions</p><a class="huge" href="admissions.html#enquire" data-hover>Come and see<br>the hills <em>for yourself</em> {ARROW}</a>
  <div class="ftr-grid">
    <div><a class="brand" href="index.html"><span class="logo-ph">LOGO</span><span><b>Anjuman-I-Islam</b><small>Public School &amp; Jr. College</small></span></a><p>Panchgani, Maharashtra · a unit of Anjuman-I-Islam, serving education since 1874.</p></div>
    <div><h5>Explore</h5>{"".join(f'<a href="{s}.html">{l}</a>' for s, l in PAGES)}</div>
    <div><h5>Contact</h5><p>{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}</p><p>{C.SCHOOL['email_admissions']}</p></div>
    <div><h5>Network</h5><a href="{C.SCHOOL['parent_url']}" target="_blank" rel="noopener">anjumaniislam.org</a><a href="mailto:{C.SCHOOL['parent_email']}">{C.SCHOOL['parent_email']}</a></div>
  </div>
  <div class="legal"><span>© <span data-year>2026</span> Anjuman-I-Islam Public School &amp; Jr. College</span><span>Design option 4 · Hill Station Editorial</span></div>
</div></footer>
{tail()}'''


def phero(kick, title, lead=""):
    return f'''<section class="phero"><div class="sky"><div class="sun" data-par=".3"></div></div>
<svg class="ly l2" data-par=".12" viewBox="0 0 1440 460" preserveAspectRatio="none" aria-hidden="true"><path d="M0 250l180-90 150 60 200-120 180 100 170-70 210 130 150-70H1440v320H0z" fill="#8c7a63" opacity=".8"/></svg>
<svg class="ly l4" viewBox="0 0 1440 360" preserveAspectRatio="none" aria-hidden="true"><path d="M0 150c180-80 360-70 540-10s360 50 520-20 260-20 380 20v220H0z" fill="#1f3a2e"/></svg>
<div class="wrap phero-in"><p class="kick" data-r>{kick}</p><h1 data-split>{title}</h1>{f'<p class="lead" data-r data-i="3">{lead}</p>' if lead else ""}</div></section>'''


def chap(num, title, body, id="", cls=""):
    idattr = f' id="{id}"' if id else ""
    return f'<section class="chap {cls}"{idattr}><div class="wrap chap-in"><div class="chap-h"><span class="no" data-r>{num}</span><h2 data-split>{title}</h2></div><div class="chap-b">{body}</div></div></section>'


def rail_campus():
    cards = [("Academic block", "campus", "A vintage building with projectors, labs and a library."), ("Akbar Peerbhoy Sports Stadium", "field", "The largest sports ground in town."),
             ("Dormitories", "dorm", "Fully renovated; home away from home."), ("Dining hall", "dining", "Seats 300; five meals a day."), ("Prayer hall", "prayer", "Five calls to prayer daily."),
             ("Robotics & AI lab", "lab", "Tinker, build, program."), ("Organic gardens", "garden", "Rainwater harvesting and farming."), ("Arts centre", "arts", "Music rooms and studios.")]
    return '<div class="rail crail">' + "".join(f'<figure class="cc" data-hover>{scene(k, "", ratio="3/4", caption=False)}<figcaption><b>{esc(t)}</b><span>{esc(d)}</span></figcaption></figure>' for t, k, d in cards) + "</div>"


# ----------------------------------------------------------------- pages
def home():
    hero = f'''<section class="hero"><div class="sky"><div class="sun" data-par=".35"></div></div>{RANGES}
<div class="wrap hero-copy"><p class="kick" data-r>Panchgani · Maharashtra · over a century of learning</p>
<h1 data-split>Above the clouds, <em>a place to grow.</em></h1>
<p class="lead" data-r data-i="5">A residential school and junior college across 174 acres of hill country — part of Anjuman-I-Islam, serving education since 1874.</p></div>
<div class="wrap hero-foot"><div><b data-count="174">174</b><span>acres of campus</span></div><div><b data-count="100">100</b><span>+ years of education</span></div><div><b data-count="5">5</b><span>entrance-exam tracks</span></div><a class="scrollcue" href="#intro" data-hover>Scroll {ic("arrow")}</a></div></section>'''
    chapters = "".join(f'<a class="chapter-link" href="{u}.html" data-hover data-r="up" data-i="{i}"><span>{i + 1:02d}</span><h3>{t}</h3><p>{d}</p>{ARROW}</a>' for i, (u, t, d) in enumerate([
        ("about", "The School &amp; its story", "1874 to today, vision, mission and the twenty-one presidents."), ("academics", "Academics", "Primary to Jr. College, coaching for NEET, JEE, CET, NATA and CA."),
        ("life", "Campus life", "Boarding, sport, arts, robotics, riding and the student journey."), ("day", "A day at Panchgani", "Scroll through 5 am to 5 am — the clock turns, the sky changes."), ("results", "Results", "Board results, entrance tracks, achievements and rankings."),
        ("admissions", "Admissions", "Five steps, fee policy, calendar and FAQs.")]))
    body = f'''
<section class="intro" id="intro"><div class="wrap"><p class="manifesto" data-split>“{esc(C.QUOTE)}”</p><p class="cite" data-r>— Executive Chairman</p></div></section>

<section class="chapters"><div class="wrap">{chapters}</div></section>

<section class="sec sand"><div class="wrap"><div class="sec-top"><p class="kick" data-r>The campus</p><h2 data-split>Spaces to wander</h2><a class="tlink" href="life.html" data-hover>Explore campus life {ARROW}</a></div></div>{rail_campus()}<p class="drag wrap">Drag to explore →</p></section>

<section class="sec"><div class="wrap split"><div class="sticky"><p class="kick" data-r>Beyond the classroom</p><h2 data-split>Athletes, artists &amp; leaders in the making</h2><p data-r>Teamwork, leadership and time management are learned as much on the field and in the studio as in the classroom.</p><a class="tlink" href="life.html#activities" data-hover>All 16 activities {ARROW}</a></div>
<ul class="acts-list">{"".join(f'<li data-r="up" data-hover><span>{i + 1:02d}</span><b>{esc(t)}</b><em>{esc(d)}</em></li>' for i, (t, c, ico, d) in enumerate(C.ACTIVITIES[:8]))}</ul></div></section>

<section class="sec forest"><div class="wrap"><p class="kick" data-r>Heritage</p><h2 data-split>Twenty-one presidents. One living mission.</h2></div>{marquee([n for n, _, _ in C.PRESIDENTS], "mq")}<div class="wrap"><p class="center-link"><a class="tlink light" href="about.html#presidents" data-hover>Read the roll {ARROW}</a></p></div></section>

<section class="sec"><div class="wrap"><div class="sec-top"><p class="kick" data-r>Anjuman-I-Islam</p><h2 data-split>Reach &amp; impact</h2></div>{stat_row(C.NETWORK_STATS, "stats")}</div></section>

<section class="sec sand"><div class="wrap"><div class="sec-top"><p class="kick" data-r>Results · 2026</p><h2 data-split>Across the Anjuman family</h2></div>{ssc_hsc_block()}</div></section>

<section class="sec"><div class="wrap"><div class="sec-top"><p class="kick" data-r>Journal</p><h2 data-split>Latest news</h2></div>{news_cards("news")}</div></section>'''
    return layout("index", "Home", body, hero)


def about():
    hist = "".join(f'<li data-r="up"><b>{y}</b><p>{esc(t)}</p></li>' for y, t in C.HISTORY)
    goals = "".join(f'<li data-r="up"><span>{r}</span><p>{esc(t)}</p><em>{esc(w)}</em></li>' for r, t, w in C.GOALS)
    body = chap("01", "Our founders", f'<p class="big-p" data-r>Founded in 1874 by a small group of Muslims, “animated by a desire to see the Musalmans rise higher in the moral, social and educational scale.”</p><p data-r>As early as 1880, Anjuman-I-Islam presented a Memorandum to the Indian Education Commission urging vocational, industrial, commercial and agricultural education, physical education and education for girls. It opened its first technical school for artisans in 1936 and its first girls’ school in 1939, and pioneered kindergarten, mid-day meals and subsidised fees for the needy.</p>', "story") \
        + chap("02", "Vision &amp; mission", f'<div class="vm"><div data-r="up"><span class="kick">Vision</span><p class="big-p">{esc(C.VISION)}</p></div><div data-r="up" data-i="1"><span class="kick">Mission</span><p class="big-p">{esc(C.MISSION)}</p></div><div data-r="up"><span class="kick">Our school’s values</span><p>{esc(C.SCHOOL_VALUES)}</p></div><div data-r="up" data-i="1"><span class="kick">Our school’s mission</span><p>{esc(C.SCHOOL_MISSION)}</p></div></div>', "vision", "sand") \
        + chap("03", "Six goals", f'<ol class="goals">{goals}</ol>', "goals") \
        + chap("04", "History", f'<ol class="hist">{hist}</ol><p class="pull" data-r>{esc(C.PIONEER_NOTE)}</p>', "history", "forest") \
        + chap("05", "Founders &amp; past presidents", f'<p data-r class="lead">Twenty-one presidents across 150 years — from Mr. Cumruddin Tyabji in 1875 to Dr. Zahir Kazi today. <i class="star">★</i> marks presidents who contributed funds as philanthropists.</p>{presidents("pres")}<p><a class="tlink" href="assets/real/presidents.png" target="_blank" rel="noopener" data-hover>View the portrait gallery {ARROW}</a></p>', "presidents") \
        + chap("06", "Leadership", f'<div class="lead-grid"><div data-r="up">{photo("zahir-kazi.png", "Dr. Zahir Kazi", ratio="4/5")}</div><div><h3 class="big-name" data-r>Dr. Zahir Kazi</h3><p class="kick" data-r>President since 2009 · Padma awardee</p><p data-r>{esc(C.ZAHIR_BIO)}</p><p class="kick" style="margin-top:30px">Board of Directors</p>{board("board")}</div></div>', "leadership", "sand") \
        + chap("07", "The Anjuman network", f'{stat_row(C.EDU_STATS, "stats three")}<div style="margin-top:44px">{institutions_explorer()}</div><h4 style="margin:56px 0 12px">Objects of the Anjuman</h4><ul class="objs">{"".join(f"<li data-r=up>{esc(o)}</li>" for o in C.OBJECTS)}</ul>', "network")
    return layout("about", "About", body, phero("The school &amp; its story", "150 years of <em>service to education</em>", "Anjuman-I-Islam Public School &amp; Jr. College, Panchgani is a unit of Anjuman-I-Islam, founded in Mumbai in 1874."))


def academics():
    ap = "".join(f'<li data-r="up"><span>{i + 1:02d}</span><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></li>' for i, (t, d) in enumerate(C.ACADEMIC_APPROACH))
    prog = "".join(f'<div class="prog" data-r="up" data-i="{i}">{scene(k, "", ratio="4/3", caption=False)}<div><span class="kick">{u[2]} · {u[1]}</span><h3>{t}</h3><p>{esc(d)}</p></div></div>' for i, ((t, d), u, k) in enumerate(zip(C.PROGRAMMES, C.PANCHGANI_UNITS, ["books", "lab", "campus"])))
    fac = "".join(f'<div class="fac" data-r="up" data-i="{i % 3}">{ic(ico)}<h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for i, (t, ico, d) in enumerate(C.FACILITIES))
    body = chap("01", "Our approach", f'<ol class="rows">{ap}</ol>') \
        + chap("02", "Primary, High School &amp; Jr. College", f'<div class="progs">{prog}</div>', "programmes", "sand") \
        + chap("03", "Competitive coaching", f'<p class="lead" data-r>{esc(C.COACHING_NOTE)}</p>{exam_tracks("tracks")}', "coaching", "forest") \
        + chap("04", "Facilities", f'<div class="facs">{fac}</div>', "facilities") \
        + chap("05", "Faculty &amp; staff", f'<p class="big-p" data-r>Mentors, role models and pillars of support.</p><p data-r>Teachers with a passion for their subjects, dorm in-charges offering a listening ear, administrative staff who keep the campus safe, and support staff who keep it clean and welcoming.</p><div class="ph3">{scene("portrait", "Faculty", ratio="16/9")}</div>', "faculty", "sand")
    return layout("academics", "Academics", body, phero("Academics", "Learning that goes <em>beyond the books</em>", "Rigorous academics, personal advising and entrance coaching on a single campus."))


def life():
    bo = "".join(f'<article class="bo" data-r="up" data-i="{i % 2}">{scene(k, "", ratio="3/2", caption=False)}<div>{ic(ico)}<h3>{t}</h3><p>{esc(d)}</p></div></article>' for i, (t, ico, k, d) in enumerate(C.BOARDING))
    day = "".join(f'<li data-r="up"><span>{i + 1:02d}</span><b>{esc(t)}</b><em>{esc(d)}</em></li>' for i, (t, d) in enumerate(C.DAY))
    acts = "".join(f'<li data-cat="{c}" data-r="up" data-hover><span>{ic(ico)}</span><b>{esc(t)}</b><em>{esc(d)}</em></li>' for t, c, ico, d in C.ACTIVITIES)
    filt = '<div class="filters" data-filter-group data-target=".acts-list li"><button class="on" data-filter="all">All</button><button data-filter="innov">Innovation</button><button data-filter="outdoor">Outdoors</button><button data-filter="sport">Sports</button><button data-filter="arts">Arts</button><button data-filter="minds">Minds</button></div>'
    jr = "".join(f'<li data-r="up"><span>{i + 1}</span><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></li>' for i, (t, d) in enumerate(C.JOURNEY))
    body = f'<section class="sec"><div class="wrap"><div class="sec-top"><p class="kick">The campus</p><h2 data-split>Spaces to wander</h2></div></div>{rail_campus()}<p class="drag wrap">Drag to explore →</p></section>' \
        + chap("01", "Boarding &amp; care", f'<div class="bos">{bo}</div>') \
        + chap("02", "A day at Panchgani", f'<ol class="acts-list day">{day}</ol>', "day", "forest") \
        + chap("03", "Activities", f'{filt}<ul class="acts-list" style="margin-top:30px">{acts}</ul>', "activities") \
        + chap("04", "The student journey", f'<ol class="rows">{jr}</ol>', "journey", "sand") \
        + f'<section class="sec"><div class="wrap"><div class="sec-top"><p class="kick">Gallery</p><h2 data-split>Moments from campus</h2></div><div class="gal">{"".join(f"<div class=g{i} data-r=zoom>{scene(k, l)}</div>" for i, (k, l) in enumerate([("hills", "Hills"), ("field", "Sports Day"), ("arts", "Art studio"), ("garden", "Gardens"), ("dining", "Dining"), ("lab", "Robotics lab")]))}</div></div></section>'
    return layout("life", "Campus Life", body, phero("Campus life", "Athletes, artists and <em>leaders in the making</em>", "Boarding, sport, arts, robotics, riding and more across 174 acres."))


def results():
    ach = "".join(f'<li data-r="up"><b>{esc(y)}</b><div><h4>{esc(t)}</h4><p>{esc(d)}</p></div><em>{esc(k)}</em></li>' for y, t, d, k in C.ACHIEVEMENTS)
    body = chap("01", "Board results · 2026", ssc_hsc_block()) \
        + chap("02", "Entrance exams", f'{exam_tracks("tracks")}<div style="margin-top:40px">{exam_table()}</div>', "entrance", "forest") \
        + chap("03", "Achievements", f'<ol class="ach">{ach}</ol>', "achievements") \
        + chap("04", "Rankings", '<div class="rk"><div data-r="up"><span class="logo-ph">LOGO</span><h4>Ranking body — <span class="val">#00</span></h4><p>Year · source to be added</p></div><div data-r="up" data-i="1"><span class="logo-ph">LOGO</span><h4>Ranking body — <span class="val">#00</span></h4><p>Year · source to be added</p></div><div data-r="up" data-i="2"><span class="logo-ph">LOGO</span><h4>Golden School Award</h4><p>2018–19 · Indian Talent Search</p></div></div>', "", "sand") \
        + chap("05", "Anjuman in the news", news_cards("news"))
    return layout("results", "Results", body, phero("Results", "Proof that <em>effort is rewarded</em>", "Board outcomes, entrance-exam selections and honours."))


def admissions():
    stp = "".join(f'<li data-r="up"><span>{i + 1:02d}</span><b>{esc(t)}</b>{f"<em>{esc(s)}</em>" if s else ""}</li>' for i, (t, s) in enumerate(C.STEPS))
    body = chap("01", "Enrolment process", f'<ol class="acts-list day">{stp}</ol>', "process") \
        + chap("02", "Important points &amp; fees", f'<div class="vm"><div><span class="kick">Important points</span>{checklist(C.IMPORTANT, "checks")}</div><div id="fees"><span class="kick">Fees policy</span>{checklist(C.FEES, "checks")}<p class="note">Fee amounts to be added by the school.</p></div></div>', "", "sand") \
        + chap("03", "Admission enquiry", f'<p class="lead" data-r>Our admissions office will contact you within one working day. <b>{C.SCHOOL["phones"][0]} / {C.SCHOOL["phones"][1]}</b> · {C.SCHOOL["email_admissions"]}</p><div class="formbox" data-r>{enquiry_form()}</div>', "enquire") \
        + chap("04", "School calendar", calendar_block(), "calendar", "forest") \
        + chap("05", "Questions", faq(), "faq")
    return layout("admissions", "Admissions", body, phero("Admissions", "Begin your journey at <em>Panchgani</em>", "A clear five-step process — and a team to guide you."))


def contact():
    cards = "".join(f'<div data-r="up"><span class="kick">{esc(l)}</span><p class="big-p small">{esc(e)}</p></div>' for l, e in C.SCHOOL["emails"])
    body = chap("01", "Reach the right office", f'<div class="mails">{cards}</div>') \
        + chap("02", "Visit &amp; call", f'<p class="big-p" data-r>Panchgani, Maharashtra</p><p data-r>Full postal address and PIN to be added.<br><b>{C.SCHOOL["phones"][0]} / {C.SCHOOL["phones"][1]}</b></p><div class="ph3">{scene("hills", "Map embed", ratio="16/9")}</div>', "", "sand") \
        + chap("03", "Send a message", '<div class="formbox" data-r><form class="form" data-demo novalidate><div><label for="c1">Name *</label><input id="c1" required></div><div><label for="c2">Phone *</label><input id="c2" required type="tel"></div><div class="full"><label for="c3">Email *</label><input id="c3" type="email" required></div><div class="full"><label for="c4">Subject</label><select id="c4"><option>Admission enquiry</option><option>Hostel enquiry</option><option>Fees &amp; accounts</option><option>General information</option></select></div><div class="full"><label for="c5">Message *</label><textarea id="c5" required></textarea></div><div class="full"><button class="btn solid" type="submit">Send message ' + ARROW + '</button></div></form></div>') \
        + chap("04", "Careers", f'<p class="big-p" data-r>Join our team.</p><p data-r>Teachers, dorm in-charges, coaching faculty and support staff who care about students.<br><b>{C.SCHOOL["emails"][4][1]}</b></p>', "careers", "forest") \
        + chap("05", "Anjuman-I-Islam", f'<p data-r>Founded in 1874. Head office enquiries: <b>{C.SCHOOL["parent_email"]}</b></p><p><a class="tlink" href="{C.SCHOOL["parent_url"]}" target="_blank" rel="noopener" data-hover>Visit anjumaniislam.org {ARROW}</a></p>')
    return layout("contact", "Contact", body, phero("Contact", "We’d love to <em>hear from you</em>", "Reach the right office directly, or send us a message."))


def day():
    hero = aerial(f'<div class="wrap aerial-t"><p class="kick" data-r>Panchgani · Maharashtra</p><h1 data-split>174 acres, <em>above the clouds.</em></h1><p class="lead" data-r data-i="4">This is where your child will live, learn and grow. Scroll down — and spend a day with us.</p></div>')
    facts = "".join(f'<div class="fact" data-r="up" data-i="{i}"><b>{n}</b><span>{esc(l)}</span><p>{esc(t)}</p></div>' for i, (n, l, t) in enumerate(C.PLACE_FACTS))
    band = hills_band('<p class="kick" data-r>Where the day begins</p><h2 data-split>Every morning, the hills lift <em>out of the mist.</em></h2>')
    body = chap("01", "Where we are", f'<p class="big-p" data-r>{esc(C.PLACE_INTRO)}</p><div class="facts">{facts}</div>', "where") \
        + band + dayclock() \
        + chap("02", "The timetable", daytable(), "timetable", "sand") \
        + chap("03", "Find us", f'<p class="big-p" data-r>Come and see it for yourself.</p><p data-r>Anjuman-I-Islam Public School &amp; Jr. College, Panchgani, Maharashtra.<br><small>Full postal address and directions to be added.</small><br><b>{C.SCHOOL["phones"][0]} / {C.SCHOOL["phones"][1]}</b></p>{map_block()}', "find-us")
    return layout("day", "A Day Here", body, hero)

def build():
    return {"index": home(), "about": about(), "academics": academics(), "life": life(), "day": day(), "results": results(), "admissions": admissions(), "contact": contact()}
