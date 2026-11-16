from html import escape as esc
from common import *
import content as C

META = dict(
    slug="heritage", name="Heritage", palette=["#3a2f1d", "#b8924f", "#f8f3e8"],
    tagline="A century of learning, rooted in values",
    blurb="Ivory and golden beige, arch windows and letterpress detail. A gold line draws itself down the Roll of Honour as you scroll through 150 years of presidents. Also in emerald, navy and burgundy. Dignified, trusted, timeless.",
    fonts="Cormorant Garamond · Lato",
)
PALETTES = [
    dict(id="ivory", name="Ivory and Gold", sw=["#ffffff", "#b8924f", "#3a2f1d"], css="--paper:#fff;--ivory:#f8f3e8;--line:#e7dcc3;--bar-bg:#efe7d3;--emerald:#3a2f1d;--deep:#1c160b;--gold:#b8924f;--gold-l:#dcc28d;--gold-d:#86652a;--ink:#2e281c;--muted:#6f6650;--s1:#fcf9f2;--s2:#f0e4cb;--glow:#fff;--h-on:#1c160b;--on1:#463c28;--on2:#55492f;--on3:#665a3e;--em-on:#86652a;--card-on:rgba(255,255,255,.7);--util-tx:#d9cdb0;--ftr-bg:#241c10;--ftr-tx:#cdbf9f;--sh-rgb:28,22,11;--hb-t:#efe3c9;--hb-b:#fbf6ea;--sc0:#f6eedb;--sc1:#e8d9b4;--sc2:#cfb27a;--sc3:#7a6234;--sc4:#b8924f;--sc5:#f7ebc6"),
    dict(id="emerald", name="Emerald and Gold", sw=["#0f4c3a", "#c9a24b", "#fbf7ec"], css=""),
    dict(id="navy", name="Navy and Steel", sw=["#1d3461", "#7f9cc4", "#f4f7fb"], css="--emerald:#1d3461;--deep:#0e1a38;--gold:#7f9cc4;--gold-l:#c3d3ea;--gold-d:#3f5f90;--paper:#fbfcfe;--ivory:#f1f5fa;--line:#dbe3ee;--bar-bg:#e3eaf3;--ink:#1d2536;--muted:#5d6678;--glow:#2f5099;--on1:#e2e9f6;--on2:#c4d0e8;--on3:#b3c1de;--util-tx:#b9c6e2;--ftr-bg:#09112a;--ftr-tx:#a3b1d1;--sh-rgb:14,26,56;--hb-t:#d3def2;--hb-b:#f1f5fa;--sc0:#e3eaf7;--sc1:#a9bde3;--sc2:#5b7cc0;--sc3:#1d3461;--sc4:#7f9cc4;--sc5:#dbe6f5"),
    dict(id="burgundy", name="Burgundy and Rose", sw=["#6d1f2c", "#d98a9b", "#fdf6f6"], css="--emerald:#6d1f2c;--deep:#3a0e17;--gold:#d98a9b;--gold-l:#f1c4cd;--gold-d:#a23a54;--paper:#fffafa;--ivory:#fbf0f1;--line:#ecd5d9;--bar-bg:#f2dde0;--ink:#2e1f22;--muted:#6e5f62;--glow:#963a48;--on1:#f6e6e8;--on2:#ecd0d4;--on3:#e0bec4;--util-tx:#e4c4ca;--ftr-bg:#2a0a11;--ftr-tx:#c9a2aa;--sh-rgb:58,14,23;--hb-t:#f1d9dc;--hb-b:#fbf0f1;--sc0:#f6e4e6;--sc1:#e8b9c1;--sc2:#c4707f;--sc3:#6d1f2c;--sc4:#d98a9b;--sc5:#f8dce1"),
]
FONTS = "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Lato:wght@400;700;900&display=swap"
GF = "https://fonts.googleapis.com/css2?family="
FONTSETS = [
    dict(id="cormorant", name="Cormorant and Lato"),
    dict(id="playfair", name="Playfair and Source Sans", url=GF + "Playfair+Display:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Source+Sans+3:wght@400;700;900&display=swap", css="--serif:'Playfair Display',Georgia,serif;--sans:'Source Sans 3',system-ui,sans-serif"),
    dict(id="baskerville", name="Baskerville and Work Sans", url=GF + "Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Work+Sans:wght@400;700;900&display=swap", css="--serif:'Libre Baskerville',Georgia,serif;--sans:'Work Sans',system-ui,sans-serif"),
    dict(id="lora", name="Lora and Nunito Sans", url=GF + "Lora:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Nunito+Sans:wght@400;700;900&display=swap", css="--serif:'Lora',Georgia,serif;--sans:'Nunito Sans',system-ui,sans-serif"),
]
STAR = '<svg class="star8" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 1l2.6 6.4L21 4.5l-2.9 6.2L24 12l-5.9 1.3 2.9 6.2-6.4-2.9L12 23l-2.6-6.4L3 19.5l2.9-6.2L0 12l5.9-1.3L3 4.5l6.4 2.9z"/></svg>'
PATTERN = '<svg class="pat" width="100%" height="100%" aria-hidden="true"><defs><pattern id="geo" width="90" height="90" patternUnits="userSpaceOnUse"><path d="M45 0l11 34 34 11-34 11-11 34-11-34L0 45l34-11z" fill="none" stroke="currentColor" stroke-width="1"/><circle cx="45" cy="45" r="16" fill="none" stroke="currentColor" stroke-width="1"/></pattern></defs><rect width="100%" height="100%" fill="url(#geo)"/></svg>'


def orn(): return f'<div class="orn" data-r="zoom"><span></span>{STAR}<span></span></div>'


def sh(eyebrow, title, sub="", center=True):
    c = " center" if center else ""
    return f'<div class="sh{c}"><p class="eyebrow" data-r>{eyebrow}</p><h2 data-split>{title}</h2>{orn() if center else ""}{f"<p class=sub data-r>{sub}</p>" if sub else ""}</div>'


def layout(slug, title, body, hero=""):
    links = "".join(f'<a href="{s}.html"{" class=cur" if s == slug else ""}>{l}</a>' for s, l in PAGES if s != "index")
    left = "".join(f'<a href="{s}.html"{" class=cur" if s == slug else ""}>{l}</a>' for s, l in PAGES[1:5])
    right = "".join(f'<a href="{s}.html"{" class=cur" if s == slug else ""}>{l}</a>' for s, l in PAGES[5:])
    return head(f"{title} — {C.SCHOOL['name']}", "Boarding school and junior college in Panchgani — part of Anjuman-I-Islam, founded 1874.", FONTS, "#3a2f1d", ("heritage", PALETTES, FONTSETS)) + f'''
<body>
<div class="progress"><i></i></div><a class="skip" href="#main">Skip to content</a>
<div class="util"><div class="container"><span>Admissions open · Boarding school &amp; Jr. College</span><span><a href="tel:{C.SCHOOL['phones'][0]}">{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}</a> &nbsp;·&nbsp; <a href="mailto:{C.SCHOOL['email_admissions']}">{C.SCHOOL['email_admissions']}</a></span></div></div>
<header class="hdr" data-header><div class="container hdr-in">
  <nav class="nav nav-l">{left}</nav>
  <a class="brand" href="index.html"><img class="school-logo" src="assets/real/school-logo-sm.png" alt=""><b>Anjuman-I-Islam</b><small>Public School &amp; Jr. College · Panchgani</small></a>
  <nav class="nav nav-r">{right}<a class="btn gold sm" href="admissions.html#enquire">Apply</a></nav>
  <button class="burger" data-nav-toggle aria-label="Menu">{ic("menu")}</button>
</div></header>
<div class="mnav"><a href="index.html">Home</a>{links}<a class="btn gold" href="admissions.html#enquire">Apply now</a></div>
{hero}<main id="main">{body}</main>
<footer class="ftr"><div class="pat-wrap">{PATTERN}</div><div class="container">
  <div class="ftr-top"><img class="school-logo big" src="assets/real/school-logo-sm.png" alt="Anjuman-I-Islam Public School &amp; Jr. College logo"><h3>Anjuman-I-Islam Public School &amp; Jr. College</h3><p>Panchgani, Maharashtra · Part of Anjuman-I-Islam, serving education since 1874</p></div>
  <div class="ftr-grid">
    <div><h5>Explore</h5>{links}</div>
    <div><h5>Contact</h5><p>{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}</p><p>{C.SCHOOL['email_admissions']}</p><p>Panchgani, Maharashtra<br><small>(full address to be added)</small></p></div>
    <div><h5>Anjuman-I-Islam</h5><img class="plogo" src="assets/real/logo.png" alt="Anjuman-I-Islam logo"><p><a href="{C.SCHOOL['parent_url']}" target="_blank" rel="noopener">anjumaniislam.org</a></p></div>
  </div>
  <div class="legal"><span>© <span data-year>2026</span> Anjuman-I-Islam Public School &amp; Jr. College, Panchgani</span><span>Design option 1 · Heritage</span></div>
</div></footer>
{tail()}'''


def page_hero(kicker, title, lead, kind="campus"):
    return f'''<section class="phero"><div class="pat-wrap">{PATTERN}</div><div class="container phero-in">
  <div><p class="eyebrow" data-r>{kicker}</p><h1 data-split>{title}</h1><p class="lead" data-r data-i="3">{lead}</p></div>
  <div class="arch sm" data-r="arch">{scene(kind, "", ratio="1/1", caption=False)}</div></div></section>'''


# --------------------------------------------------------------- pages
def home():
    hero = f'''<section class="hero"><div class="pat-wrap" data-par="-.06">{PATTERN}</div>
<div class="container hero-in">
  <div class="hero-t"><p class="eyebrow" data-r>Boarding school &amp; Jr. College · Panchgani</p>
    <h1 data-split>A century of learning, <em>rooted in values</em></h1>
    <p class="lead" data-r data-i="4">Where education meets compassion. A residential school on 174 acres of the Panchgani hills — one of the family of Anjuman-I-Islam institutions, serving education since 1874.</p>
    <div class="cta" data-r data-i="5"><a class="btn gold" href="admissions.html#enquire">Begin admission {ic("arrow")}</a><a class="btn ghost" href="life.html">Explore the campus</a></div></div>
  <div class="hero-a" data-r="arch"><div class="arch" data-par=".05">{scene("campus", "Main academic block", ratio="3/4")}</div>
    <div class="seal" data-r="zoom" data-i="4"><b data-count="100">100</b><span>years of<br>learning</span></div></div>
</div></section>
{marquee([n for n, _, _ in C.PRESIDENTS] , "mq")}'''
    body = f'''
<section class="sec"><div class="container">{stat_row(C.STATS, "stats")}</div></section>

<section class="sec welcome"><div class="container split">
  <div data-r="arch" class="arch">{scene("hills", "Panchgani hills", ratio="4/5")}</div>
  <div><p class="eyebrow" data-r>Welcome</p><h2 data-split>Where core values and nurturing go hand-in-hand</h2>{orn().replace("center","")}
    <blockquote class="dropcap" data-r>{esc(C.QUOTE)}</blockquote><p class="cite" data-r>— Executive Chairman</p>
    <p data-r>With over a century of quality education, our boarding school empowers every student to explore, discover and excel — fostering academic excellence, character development and global citizenship.</p>
    <a class="link" href="about.html">Read our story {ic("arrow")}</a></div>
</div></section>

<section class="sec emerald"><div class="pat-wrap">{PATTERN}</div><div class="container">
  {sh("Vision &amp; Mission", "What Anjuman-I-Islam stands for")}
  <div class="duo"><div class="panel" data-r="up"><span class="num">I</span><h3>Vision</h3><p>{esc(C.VISION)}</p></div><div class="panel" data-r="up" data-i="2"><span class="num">II</span><h3>Mission</h3><p>{esc(C.MISSION)}</p></div></div>
  <p class="center-link"><a class="link light" href="about.html#goals">Our goals to 2030 {ic("arrow")}</a></p>
</div></section>

<section class="sec"><div class="container">
  {sh("Three stages, one campus", "Primary · High School · Jr. College", "English-medium education from primary through HSC, in one residential community.")}
  <div class="trio" data-stagger>
    {"".join(f'<article class="arc-card" data-r="up"><div class="arch sm">{scene(k, t, ratio="4/5", caption=False)}</div><h3>{t}</h3><p>{esc(d)}</p></article>' for (t, d), k in zip(C.PROGRAMMES, ["books", "lab", "campus"]))}
  </div>
  <p class="center-link"><a class="link" href="academics.html">Academics {ic("arrow")}</a></p>
</div></section>

<section class="sec alt"><div class="container">
  {sh("Roll of Honour", "Twenty-one presidents, one living mission", "From Mr. Cumruddin Tyabji in 1875 to Dr. Zahir Kazi today — the torchbearers of Anjuman-I-Islam.")}
  <p class="center-link"><a class="btn dark" href="about.html#roll">Walk the Roll of Honour</a></p>
</div></section>

<section class="sec"><div class="container">
  {sh("Competitive coaching", "NEET · JEE · CET · NATA · CA", "Entrance coaching on campus alongside the Jr. College timetable.")}
  {exam_tracks("tracks")}
  <p class="center-link"><a class="link" href="results.html">Results &amp; rankings {ic("arrow")}</a></p>
</div></section>

<section class="sec emerald"><div class="pat-wrap">{PATTERN}</div><div class="container">
  {sh("Campus life", "A home away from home")}
  <div class="mosaic" data-stagger>
    <div class="arch m1" data-r="arch">{scene("dorm", "Dormitory", ratio="3/4")}</div>
    <div class="arch m2" data-r="arch">{scene("dining", "Dining hall", ratio="3/4")}</div>
    <div class="arch m3" data-r="arch">{scene("field", "Akbar Peerbhoy Sports Stadium", ratio="3/4")}</div>
    <div class="arch m4" data-r="arch">{scene("prayer", "Prayer hall", ratio="3/4")}</div>
  </div>
  <p class="center-link"><a class="link light" href="life.html">Campus life {ic("arrow")}</a> &nbsp;&nbsp; <a class="link light" href="day.html">Spend a day here {ic("arrow")}</a></p>
</div></section>

<section class="sec"><div class="container">
  {sh("Results", "Anjuman-I-Islam board results, 2026")}
  {ssc_hsc_block()}
</div></section>

<section class="sec alt"><div class="container">
  {sh("From the Anjuman family", "Latest news")}
  {news_cards("news")}
</div></section>

<section class="cta-band"><div class="pat-wrap">{PATTERN}</div><div class="container"><h2 data-split>Come and see the hills for yourself</h2><p data-r>Begin with an enquiry — our admissions office will guide you through every step.</p><div class="cta" data-r><a class="btn gold" href="admissions.html#enquire">Enquire now</a><a class="btn ghost" href="tel:{C.SCHOOL['phones'][0]}">Call {C.SCHOOL['phones'][0]}</a></div></div></section>'''
    return layout("index", "Home", body, hero)


def about():
    body = f'''
<section class="sec"><div class="container narrow center">
  {sh("Our Founders", "A desire to see the community rise")}
  <blockquote class="big" data-r>“…a desire to see the Musalmans rise higher in the moral, social and educational scale.”</blockquote>
  <p data-r>Anjuman-I-Islam was founded in 1874 by a small group of Muslims. As early as 1880 it presented a Memorandum to the Indian Education Commission emphasising vocational, industrial, commercial and agricultural education, physical education and education for girls — a vision it has followed ever since.</p>
</div></section>

<section class="sec alt" id="vision"><div class="container">
  {sh("Vision, Mission &amp; Values", "Our purpose")}
  <div class="quad" data-stagger>
    <div class="panel"><h3>Vision</h3><p>{esc(C.VISION)}</p></div><div class="panel"><h3>Mission</h3><p>{esc(C.MISSION)}</p></div>
    <div class="panel"><h3>Our school’s values</h3><p>{esc(C.SCHOOL_VALUES)}</p></div><div class="panel"><h3>Our school’s mission</h3><p>{esc(C.SCHOOL_MISSION)}</p></div>
  </div>
</div></section>

<section class="sec" id="goals"><div class="container">
  {sh("Our Goals", "Six goals for the decade")}
  <ol class="goals" data-stagger>{"".join(f'<li data-r="up"><span class="num">{r}</span><div><p>{esc(t)}</p><small>{esc(w)}</small></div></li>' for r, t, w in C.GOALS)}</ol>
</div></section>

<section class="sec emerald" id="history"><div class="pat-wrap">{PATTERN}</div><div class="container">
  {sh("Heritage", "From 1874 to today")}
  <div class="tl" data-line><i class="tl-fill"></i>{"".join(f'<div class="tl-i" data-r="up"><b>{y}</b><p>{esc(t)}</p></div>' for y, t in C.HISTORY)}</div>
  <p class="center-note">{esc(C.PIONEER_NOTE)}</p>
</div></section>

<section class="sec" id="roll"><div class="container">
  {sh("Roll of Honour", "Founders &amp; past presidents", "Twenty-one leaders across 150 years. The star marks presidents who contributed funds as philanthropists.")}
  <div class="roll" data-line><i class="roll-fill"></i>{presidents("pres")}</div>
  <div class="center" style="margin-top:40px"><a class="btn dark" href="assets/real/presidents.png" target="_blank" rel="noopener">View the portrait gallery</a></div>
</div></section>

<section class="sec alt" id="leadership"><div class="container split">
  <div data-r="arch" class="arch">{photo("zahir-kazi.png", "Dr. Zahir Kazi", ratio="4/5")}</div>
  <div><p class="eyebrow" data-r>Leadership</p><h2 data-split>Dr. Zahir Kazi</h2>{orn().replace("center","")}<p class="lead" data-r>President, Anjuman-I-Islam since 2009 · Padma awardee</p>
    <p data-r>{esc(C.ZAHIR_BIO)}</p><h4 style="margin-top:28px" data-r>Board of Directors</h4>{board("board")}</div>
</div></section>

<section class="sec" id="network"><div class="container">
  {sh("The Anjuman family", "Institutions across Maharashtra", "Anjuman-I-Islam runs around 90 education institutes from kindergarten to PhD. Our Panchgani campus is highlighted.")}
  {stat_row(C.EDU_STATS, "stats")}
  <div style="margin-top:48px">{institutions_explorer()}</div>
  <div class="objects" style="margin-top:56px"><h3 data-r>Objects of the Anjuman</h3><ul class="list">{"".join(f'<li data-r="up">{esc(o)}</li>' for o in C.OBJECTS)}</ul></div>
</div></section>'''
    return layout("about", "About", body, page_hero("About us", "Rooted in <em>150 years</em> of service", "Part of Anjuman-I-Islam — one of India’s largest minority educational and social institutions.", "campus"))


def academics():
    body = f'''
<section class="sec"><div class="container">
  {sh("Our approach", "Academic progress is a fundamental commitment", "Teachers, advisors and administrators work together to ensure every student thrives.")}
  <div class="quad" data-stagger>{"".join(f'<div class="panel"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in C.ACADEMIC_APPROACH)}</div>
</div></section>
<section class="sec alt" id="programmes"><div class="container">
  {sh("Programmes", "Primary, High School &amp; Jr. College")}
  <div class="trio" data-stagger>{"".join(f'<article class="arc-card" data-r="up"><div class="arch sm">{scene(k, t, ratio="4/5", caption=False)}</div><h3>{t}</h3><p>{esc(d)}</p></article>' for (t, d), k in zip(C.PROGRAMMES, ["books", "lab", "campus"]))}</div>
  <p class="note center">Panchgani: Primary (un-aided), High School (aided), Jr. College (un-aided) — all English medium.</p>
</div></section>
<section class="sec emerald" id="coaching"><div class="pat-wrap">{PATTERN}</div><div class="container">
  {sh("Competitive coaching", "Prepare for the exams that open doors", esc(C.COACHING_NOTE))}
  {exam_tracks("tracks")}
</div></section>
<section class="sec" id="facilities"><div class="container">
  {sh("Facilities", "Labs, classrooms &amp; creative spaces")}
  <div class="fgrid" data-stagger>{"".join(f'<div class="fac" data-r="up">{ic(i)}<h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for t, i, d in C.FACILITIES)}</div>
</div></section>
<section class="sec alt" id="faculty"><div class="container split">
  <div><p class="eyebrow" data-r>Faculty &amp; staff</p><h2 data-split>Mentors, role models and pillars of support</h2>{orn().replace("center","")}
    <p data-r>Teachers with a passion for their subjects lead lively discussions and hands-on activities. Dorm in-charges offer guidance and a listening ear. Administrative and support staff keep the campus safe, clean and welcoming.</p>
    {checklist(["Subject teachers", "Dorm in-charges", "Academic advisors", "Kitchen & maintenance teams"], "checks")}</div>
  <div data-r="arch" class="arch">{scene("portrait", "Faculty portrait", ratio="4/5")}</div>
</div></section>
<section class="cta-band"><div class="pat-wrap">{PATTERN}</div><div class="container"><h2 data-split>Find the right programme for your child</h2><div class="cta" data-r><a class="btn gold" href="admissions.html#enquire">Enquire now</a><a class="btn ghost" href="results.html">See results</a></div></div></section>'''
    return layout("academics", "Academics", body, page_hero("Academics", "Learning that goes <em>beyond the books</em>", "Rigorous academics, personal advising and competitive coaching — on one campus.", "books"))


def life():
    cards = "".join(f'<article class="life-card" data-r="up"><div class="arch sm">{scene(k, t, ratio="4/3", caption=False)}</div><div>{ic(i)}<h3>{t}</h3><p>{esc(d)}</p></div></article>' for t, i, k, d in C.BOARDING)
    acts = "".join(f'<div class="act" data-cat="{c}" data-r="up">{ic(i)}<h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for t, c, i, d in C.ACTIVITIES)
    filt = '<div class="filters center" data-filter-group data-target=".act"><button class="on" data-filter="all">All</button><button data-filter="innov">Innovation</button><button data-filter="outdoor">Outdoors</button><button data-filter="sport">Sports</button><button data-filter="arts">Arts</button><button data-filter="minds">Minds</button></div>'
    day = "".join(f'<div class="day-i" data-r="up"><span>{i + 1}</span><h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(C.DAY))
    jr = "".join(f'<li data-r="up"><b>{esc(t)}</b><p>{esc(d)}</p></li>' for t, d in C.JOURNEY)
    body = f'''
<section class="sec"><div class="container">{sh("Boarding &amp; care", "A home away from home", "Dorm design balances home and school so your child feels safe, happy and welcome.")}<div class="life-grid" data-stagger>{cards}</div></div></section>
<section class="sec emerald" id="day"><div class="pat-wrap">{PATTERN}</div><div class="container">{sh("A day at Panchgani", "The rhythm of boarding life")}<div class="day" data-stagger>{day}</div></div></section>
<section class="sec" id="activities"><div class="container">{sh("Extracurricular activities", "Athletes, artists and leaders in the making", "Teamwork, leadership and time management — learned on the field and in the studio.")}{filt}<div class="acts" style="margin-top:36px">{acts}</div></div></section>
<section class="sec alt" id="journey"><div class="container">{sh("Student journey", "How our students evolve")}<ol class="journey" data-line><i class="jr-fill"></i>{jr}</ol></div></section>
<section class="sec"><div class="container">{sh("Gallery", "Moments from campus")}<div class="mosaic g6" data-stagger>{"".join(f'<div class="arch m{i % 4 + 1}" data-r="arch">{scene(k, l, ratio="3/4")}</div>' for i, (k, l) in enumerate([("hills", "Panchgani hills"), ("field", "Sports Day"), ("arts", "Art studio"), ("garden", "Organic gardens")]))}</div></div></section>
<section class="cta-band"><div class="pat-wrap">{PATTERN}</div><div class="container"><h2 data-split>Plan a campus visit</h2><div class="cta" data-r><a class="btn gold" href="admissions.html#enquire">Enquire now</a></div></div></section>'''
    return layout("life", "Campus Life", body, page_hero("Campus life", "Athletes, artists and <em>leaders in the making</em>", "Boarding, sport, arts, robotics, riding and more across 174 acres.", "field"))


def results():
    ach = "".join(f'<li data-r="up"><b>{esc(y)}</b><div><h4>{esc(t)}</h4><p>{esc(d)}</p></div><em>{esc(k)}</em></li>' for y, t, d, k in C.ACHIEVEMENTS)
    body = f'''
<section class="sec"><div class="container">{sh("Board results", "Anjuman-I-Islam, 2026")}{ssc_hsc_block()}</div></section>
<section class="sec emerald"><div class="pat-wrap">{PATTERN}</div><div class="container">{sh("Entrance exams", "JEE · NEET · CET · NATA · CA")}{exam_tracks("tracks")}<div style="margin-top:36px" class="light-tbl">{exam_table()}</div></div></section>
<section class="sec"><div class="container">{sh("Achievements", "Honours &amp; awards")}<ul class="ach" data-line>{ach}</ul></div></section>
<section class="sec alt"><div class="container">{sh("Recognition", "School rankings")}<div class="trio"><div class="panel"><span class="logo-ph">LOGO</span><h3>Ranking body — <span class="val">#00</span></h3><p>Year · source to be added</p></div><div class="panel"><span class="logo-ph">LOGO</span><h3>Ranking body — <span class="val">#00</span></h3><p>Year · source to be added</p></div><div class="panel"><span class="logo-ph">LOGO</span><h3>Golden School Award</h3><p>2018–19 · Indian Talent Search</p></div></div></div></section>
<section class="sec"><div class="container">{sh("Anjuman in the news", "Stories of excellence")}{news_cards("news")}</div></section>'''
    return layout("results", "Results", body, page_hero("Results &amp; rankings", "Proof that <em>effort is rewarded</em>", "Board outcomes, entrance-exam selections and honours.", "arts"))


def admissions():
    body = f'''
<section class="sec" id="process"><div class="container">{sh("Enrolment process", "Five steps to admission")}{steps("steps")}</div></section>
<section class="sec alt"><div class="container duo">
  <div class="panel" id="important"><h3>Important points</h3>{checklist(C.IMPORTANT, "checks")}</div>
  <div class="panel" id="fees"><h3>Fees policy</h3>{checklist(C.FEES, "checks")}<p class="note">Fee amounts to be added by the school.</p></div>
</div></section>
<section class="sec" id="enquire"><div class="container split"><div><p class="eyebrow" data-r>Admission enquiry</p><h2 data-split>Tell us about your child</h2>{orn().replace("center","")}<p data-r>Our admissions office will contact you within one working day.</p><p data-r><b>{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}</b><br>{C.SCHOOL['email_admissions']}</p></div><div class="formbox" data-r>{enquiry_form()}</div></div></section>
<section class="sec emerald" id="calendar"><div class="pat-wrap">{PATTERN}</div><div class="container">{sh("School calendar", "The academic year at a glance")}<div class="light-cal">{calendar_block()}</div></div></section>
<section class="sec" id="faq"><div class="container narrow">{sh("FAQs", "Questions parents ask")}{faq()}</div></section>'''
    return layout("admissions", "Admissions", body, page_hero("Admissions", "Begin your journey at <em>Panchgani</em>", "A clear five-step enrolment process — and a team to guide you through it.", "hills"))


def contact():
    cards = "".join(f'<div class="panel" data-r="up">{ic("mail")}<h4>{esc(l)}</h4><p>{esc(e)}</p></div>' for l, e in C.SCHOOL["emails"])
    body = f'''
<section class="sec"><div class="container">{sh("Reach the right office", "Get in touch")}<div class="quad five" data-stagger>{cards}</div></div></section>
<section class="sec alt"><div class="container split"><div><p class="eyebrow" data-r>Visit &amp; call</p><h2 data-split>Panchgani campus</h2>{orn().replace("center","")}<p data-r>Panchgani, Maharashtra<br><small>(full postal address and PIN to be added)</small></p><p data-r><b>{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}</b></p><div data-r class="arch sm" style="margin-top:24px">{scene("hills", "Map embed", ratio="16/10")}</div></div>
<div class="formbox" data-r><form class="form" data-demo novalidate><div><label for="c1">Name *</label><input id="c1" required></div><div><label for="c2">Phone *</label><input id="c2" required type="tel"></div><div class="full"><label for="c3">Email *</label><input id="c3" type="email" required></div><div class="full"><label for="c4">Subject</label><select id="c4"><option>Admission enquiry</option><option>Hostel enquiry</option><option>Fees &amp; accounts</option><option>General information</option></select></div><div class="full"><label for="c5">Message *</label><textarea id="c5" required></textarea></div><div class="full"><button class="btn solid" type="submit">Send message {ic("arrow")}</button></div></form></div></div></section>
<section class="sec" id="careers"><div class="container split"><div><p class="eyebrow" data-r>Careers</p><h2 data-split>Join our team</h2>{orn().replace("center","")}<p data-r>Teachers, dorm in-charges, coaching faculty and support staff who care about students.</p><p data-r><b>{C.SCHOOL['emails'][4][1]}</b></p></div><div data-r="arch" class="arch sm">{scene("portrait", "Staff", ratio="4/3")}</div></div></section>
<section class="sec emerald"><div class="pat-wrap">{PATTERN}</div><div class="container center narrow"><p class="eyebrow">Part of a larger family</p><h2 data-split>Anjuman-I-Islam</h2><p data-r>Founded in 1874. Head office enquiries: <b>{C.SCHOOL['parent_email']}</b></p><a class="btn gold" style="margin-top:20px" href="{C.SCHOOL['parent_url']}" target="_blank" rel="noopener">Visit anjumaniislam.org</a></div></section>'''
    return layout("contact", "Contact", body, page_hero("Contact", "We’d love to <em>hear from you</em>", "Reach the right office directly, or send us a message.", "campus"))


def day():
    hero = aerial(f'<div class="container aerial-t"><p class="eyebrow">Panchgani · Maharashtra</p><h1 data-split>174 acres, <em>above the clouds</em></h1><p class="lead" data-r data-i="4">This is where your child will live, learn and grow. Scroll down — and spend a day with us.</p></div>')
    facts = "".join(f'<div class="panel" data-r="up" data-i="{i}"><span class="num">{n}</span><h3>{esc(l)}</h3><p>{esc(t)}</p></div>' for i, (n, l, t) in enumerate(C.PLACE_FACTS))
    band = hills_band('<p class="eyebrow" data-r>Where the day begins</p><h2 data-split>Every morning, the hills lift out of the mist</h2><p class="lead" data-r data-i="3">Rise, pray, learn, play, dine, study, rest — and begin again. Here is a full day in boarding life.</p>')
    body = f'''
<section class="sec"><div class="container">{sh("Where we are", "A hill-station campus", esc(C.PLACE_INTRO))}<div class="trio" data-stagger>{facts}</div></div></section>
{band}
{dayclock(roman=True)}
<section class="sec alt" id="timetable"><div class="container">{sh("The timetable at a glance", "Ten parts of a day")}{daytable()}</div></section>
<section class="sec" id="find-us"><div class="container split"><div><p class="eyebrow" data-r>Find us</p><h2 data-split>Come and see it for yourself</h2>{orn().replace("center","")}<p data-r>Anjuman-I-Islam Public School &amp; Jr. College, Panchgani, Maharashtra.<br><small>Full postal address and directions to be added.</small></p><p data-r><b>{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}</b></p><a class="btn dark" href="admissions.html#enquire">Plan a visit {ic("arrow")}</a></div><div>{map_block()}</div></div></section>
<section class="cta-band"><div class="pat-wrap">{PATTERN}</div><div class="container"><h2 data-split>Spend a day with us</h2><p data-r>Visit the campus, meet the dorm in-charges and see the day unfold first-hand.</p><div class="cta" data-r><a class="btn gold" href="admissions.html#enquire">Enquire now</a><a class="btn ghost" href="life.html">Campus life</a></div></div></section>'''
    return layout("day", "A Day Here", body, hero)

def build():
    return {"index": home(), "about": about(), "academics": academics(), "life": life(), "day": day(), "results": results(), "admissions": admissions(), "contact": contact()}
