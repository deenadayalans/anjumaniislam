from html import escape as esc
from common import *
import content as C

META = dict(
    slug="modern", name="Modern Global", palette=["#1d4ed8", "#0d9488", "#0b1f3a"],
    tagline="Learn beyond the classroom",
    blurb="A confident, international look: animated gradient mesh, bento grids with cursor-tracking glow, draggable presidents timeline and live-animating result charts. Reads as a premium global school.",
    fonts="Inter · Instrument Serif",
)
FONTS = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap"
ARROW = ic("arrow")


def sh(tag, title, sub="", dark=False):
    return f'<div class="sh"><p class="tag" data-r>{tag}</p><h2 data-split>{title}</h2>{f"<p class=sub data-r data-i=2>{sub}</p>" if sub else ""}</div>'


def layout(slug, title, body, hero=""):
    nav = "".join(f'<a href="{s}.html"{" class=cur" if s == slug else ""}>{l}</a>' for s, l in PAGES[1:])
    return head(f"{title} — {C.SCHOOL['name']}", "Boarding school and junior college in Panchgani — part of Anjuman-I-Islam, founded 1874.", FONTS, "#0b1f3a") + f'''
<body>
<div class="progress"><i></i></div><a class="skip" href="#main">Skip to content</a>
<header class="hdr" data-header data-hide><div class="wrap hdr-in">
  <a class="brand" href="index.html"><img class="school-logo" src="assets/real/school-logo-sm.png" alt=""><span><b>Anjuman-I-Islam</b><small>Public School &amp; Jr. College · Panchgani</small></span></a>
  <nav class="nav">{nav}</nav>
  <a class="btn grad sm" href="admissions.html#enquire" data-mag>Apply now {ARROW}</a>
  <button class="burger" data-nav-toggle aria-label="Menu">{ic("menu")}</button>
</div></header>
{hero}<main id="main">{body}</main>
<footer class="ftr dark"><div class="wrap">
  <div class="ftr-cta"><h2 data-split>Come and see the hills for yourself.</h2><a class="btn light" href="admissions.html#enquire" data-mag>Start admission {ARROW}</a></div>
  <div class="ftr-grid">
    <div><a class="brand" href="index.html"><img class="school-logo" src="assets/real/school-logo-sm.png" alt=""><span><b>Anjuman-I-Islam</b><small>Public School &amp; Jr. College</small></span></a><p>Panchgani, Maharashtra. A residential school and junior college, part of Anjuman-I-Islam since 1874.</p></div>
    <div><h5>Explore</h5>{"".join(f'<a href="{s}.html">{l}</a>' for s, l in PAGES)}</div>
    <div><h5>Contact</h5><p>{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}</p><p>{C.SCHOOL['email_admissions']}</p></div>
    <div><h5>Network</h5><img class="plogo" src="assets/real/logo.png" alt="Anjuman-I-Islam"><a href="{C.SCHOOL['parent_url']}" target="_blank" rel="noopener">anjumaniislam.org</a></div>
  </div>
  <div class="wordmark" aria-hidden="true">Anjuman</div>
  <div class="legal"><span>© <span data-year>2026</span> Anjuman-I-Islam Public School &amp; Jr. College</span><span>Design option 2 · Modern Global</span></div>
</div></footer>
{tail()}'''


def phero(tag, title, lead):
    return f'''<section class="phero dark"><div class="mesh"><i></i><i></i><i></i></div><div class="grid-bg"></div><div class="wrap">
  <p class="tag" data-r>{tag}</p><h1 data-split>{title}</h1><p class="lead" data-r data-i="3">{lead}</p></div></section>'''


def bento_tile(cls, tag, title, text, kind=None, icon=None):
    media = f'<div class="bt-media">{scene(kind, "", caption=False)}</div>' if kind else ""
    ico = f'<span class="bt-ic">{ic(icon)}</span>' if icon else ""
    return f'<article class="bt {cls}" data-r="up" data-spot>{media}<div class="bt-in">{ico}<span class="tag">{tag}</span><h3>{title}</h3><p>{text}</p></div></article>'


def rail_presidents():
    cards = []
    for i, (n, t, star) in enumerate(C.PRESIDENTS):
        cur = " now" if "till date" in t else ""
        cards.append(f'<div class="pcard{cur}" data-spot><span class="no">{i + 1:02d}</span>{scene("portrait", "", caption=False, ratio="1/1")}<b>{esc(n)}{" <i class=star>★</i>" if star else ""}</b><span class="yrs">{esc(t)}</span></div>')
    return f'<div class="rail prail">{"".join(cards)}</div><p class="note">Drag to explore · <i class="star">★</i> philanthropist presidents.</p>'


def results_tabs():
    h, s = C.HSC_2026, C.SSC_2026
    pp = round(s["passed"] / s["appeared"] * 100, 1)
    ph = '<span class="val">00</span>'
    exams = "".join(f'<div class="ex" data-spot><b>{n}</b><span>{esc(f)}</span>{ph}</div>' for n, f, _ in C.EXAMS)
    return f'''<div class="tabs" data-tabs><div class="filters tabbar"><button data-tab="ssc">SSC 2026</button><button data-tab="hsc">HSC 2026</button><button data-tab="ent">Entrance exams</button></div>
<div data-pane="ssc"><div class="kp"><div><b data-count="{s['appeared']}">{s['appeared']:,}</b><span>Appeared</span></div><div><b data-count="{s['passed']}">{s['passed']:,}</b><span>Passed</span></div><div><b data-count="{s['distinction']}">{s['distinction']}</b><span>Distinction</span></div><div><b data-count="{s['first_class']}">{s['first_class']}</b><span>First class</span></div></div>
 <div class="chart"><div class="barrow"><span>Pass rate</span><div class="bar" style="--w:{pp}%"><i></i></div><b>{pp}%</b></div></div></div>
<div data-pane="hsc"><div class="kp"><div><b data-count="{h['appeared']}">{h['appeared']:,}</b><span>Appeared</span></div><div><b data-count="{h['passed']}">{h['passed']:,}</b><span>Passed</span></div><div><b data-count="{h['distinction']}">{h['distinction']}</b><span>Distinction</span></div><div><b>{h['overall']}%</b><span>Overall</span></div></div>
 <div class="chart">{"".join(f'<div class="barrow"><span>{n}</span><div class="bar" style="--w:{pc}%"><i></i></div><b>{pc}%</b></div>' for n, a, p, d, pc in h['streams'])}</div></div>
<div data-pane="ent"><div class="exs">{exams}</div><p class="note">Placeholder figures — replace with verified Panchgani results.</p></div></div>
<p class="note">Board results are network-wide figures published by Anjuman-I-Islam (2026).</p>'''


# ------------------------------------------------------------- pages
def home():
    hero = f'''<section class="hero dark"><div class="mesh"><i></i><i></i><i></i></div><div class="grid-bg"></div>
<div class="wrap hero-in"><div class="hero-t">
  <p class="pill" data-r><span class="dot"></span> Admissions open · Boarding school &amp; Jr. College</p>
  <h1 data-split>Learn beyond the <em>classroom.</em></h1>
  <p class="lead" data-r data-i="4">A residential school on 174 acres in the hills of Panchgani — robotics, aviation, agriculture and NEET / JEE coaching, grounded in over a century of values and part of Anjuman-I-Islam since 1874.</p>
  <div class="cta" data-r data-i="5"><a class="btn light" href="admissions.html#enquire" data-mag>Start admission {ARROW}</a><a class="btn ghost" href="life.html">Explore campus life</a></div></div>
  <div class="hero-c"><div class="glass fc1" data-par=".12"><b data-count="174">174</b><span>acre campus</span></div><div class="glass fc2" data-par="-.1"><b data-count="100">100</b><span>+ years</span></div><div class="glass fc3" data-par=".18"><span class="mini">Coaching</span><b>NEET · JEE</b></div>
  <div class="hero-img" data-r="zoom" data-par=".06">{scene("campus", "Main academic block", ratio="4/5")}</div></div></div>
<div class="scroll-hint"><i></i>Scroll</div></section>
<section class="strip"><div class="wrap"><span>Part of the Anjuman-I-Islam network</span></div>{marquee(C.MARQUEE_INSTITUTIONS, "mq")}</section>'''
    body = f'''
<section class="sec"><div class="wrap">
  {sh("Programmes &amp; experiences", "Something for every <em>passion.</em>")}
  <div class="bento">
    {bento_tile("b-a", "Academics", "Rigorous learning, personal support", "Advisors, peer tutors and data-driven monitoring from Primary through Jr. College.", "books")}
    {bento_tile("b-b", "Innovation", "Robotics &amp; AI", "A tinkering lab for hands-on building.", None, "chip")}
    {bento_tile("b-c", "New in 2024", "Basic Aviation", "Look up — then learn to fly.", None, "plane")}
    {bento_tile("b-d", "Outdoors", "Horse riding &amp; archery", "On-campus riding, archery and shooting ranges.", "field")}
    {bento_tile("b-e", "Sustainability", "Agriculture &amp; gardening", "Organic gardens and rainwater harvesting.", "garden")}
    {bento_tile("b-f", "Coaching", "NEET · JEE · CET · NATA · CA", "Entrance coaching on campus.", None, "target")}
  </div></div></section>

<section class="sec dark impact"><div class="mesh sm"><i></i><i></i></div><div class="wrap">
  {sh("Part of something bigger", "Anjuman-I-Islam, <em>by the numbers</em>", "Founded in 1874, Anjuman-I-Islam reaches over a hundred thousand learners every year across Maharashtra.")}
  {stat_row(C.NETWORK_STATS, "stats")}
  <p class="center"><a class="link" href="about.html#network">Explore the network {ARROW}</a></p>
</div></section>

<section class="sec"><div class="wrap split"><div data-r="left" class="photo-wrap">{scene("hills", "Panchgani hills", ratio="4/5")}</div>
  <div><p class="tag" data-r>Welcome</p><h2 data-split>Education that meets <em>compassion.</em></h2>
  <blockquote data-r>“{esc(C.QUOTE)}”<cite>Executive Chairman</cite></blockquote>
  <p data-r>{esc(C.SCHOOL_MISSION)}</p><a class="btn dark" href="about.html" data-mag>Our story {ARROW}</a></div></div></section>

<section class="sec alt"><div class="wrap">
  {sh("Results", "Outcomes that <em>speak.</em>", "Published 2026 board results across the Anjuman-I-Islam network, plus entrance-exam tracks at Panchgani.")}
  {results_tabs()}
</div></section>

<section class="sec"><div class="wrap">
  {sh("Legacy", "Twenty-one presidents. <em>One mission.</em>", "From Mr. Cumruddin Tyabji (1875) to Dr. Zahir Kazi today.")}
  {rail_presidents()}
</div></section>

<section class="sec alt"><div class="wrap">
  {sh("Life at Panchgani", "A day in <em>boarding life</em>")}
  <div class="daystrip" data-stagger>{"".join(f'<div class="dd" data-r="up" data-spot><span>{i + 1:02d}</span><h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(C.DAY))}</div>
<p class="center" style="margin-top:36px"><a class="btn dark" href="day.html" data-mag>Scroll through a full day {ARROW}</a></p></div></section>

<section class="sec"><div class="wrap">
  {sh("From the Anjuman family", "Latest <em>news</em>")}
  {news_cards("news")}
</div></section>

<section class="sec dark admit"><div class="mesh sm"><i></i><i></i></div><div class="wrap">
  {sh("Admissions", "Five steps to <em>Panchgani</em>")}
  {steps("steps")}
  <p class="center"><a class="btn light" href="admissions.html#enquire" data-mag>Enquire now {ARROW}</a></p>
</div></section>'''
    return layout("index", "Home", body, hero)


def about():
    toc = '<aside class="toc"><b>On this page</b>' + "".join(f'<a href="#{i}">{t}</a>' for i, t in [("story", "Founders"), ("vision", "Vision &amp; mission"), ("goals", "Goals"), ("history", "History"), ("presidents", "Presidents"), ("leadership", "Leadership"), ("network", "Network")]) + "</aside>"
    hist = "".join(f'<div class="hi"><b>{y}</b><p>{esc(t)}</p></div>' for y, t in C.HISTORY)
    body = f'''
<section class="sec"><div class="wrap aside-layout">{toc}<div class="content">
<div id="story" class="blk"><p class="tag" data-r>Our founders</p><h2 data-split>A desire to see the community <em>rise.</em></h2>
  <p class="lead" data-r>Anjuman-I-Islam was founded in 1874 by a small group of Muslims animated by a “desire to see the Musalmans rise higher in the moral, social and educational scale.”</p>
  <p data-r>In 1880 it presented a Memorandum to the Indian Education Commission emphasising vocational, industrial, commercial and agricultural education, physical education and education for girls. It started the first technical school for artisans in 1936 and its first girls’ school in 1939, and pioneered kindergarten, mid-day meals and subsidised fees for needy students.</p></div>

<div id="vision" class="blk"><p class="tag" data-r>Vision &amp; mission</p><h2 data-split>Our <em>purpose</em></h2>
  <div class="bento two"><article class="bt" data-spot data-r="up"><div class="bt-in"><span class="tag">Vision</span><h3>{esc(C.VISION)}</h3></div></article><article class="bt" data-spot data-r="up" data-i="2"><div class="bt-in"><span class="tag">Mission</span><h3>{esc(C.MISSION)}</h3></div></article>
  <article class="bt" data-spot data-r="up"><div class="bt-in"><span class="tag">School values</span><p>{esc(C.SCHOOL_VALUES)}</p></div></article><article class="bt" data-spot data-r="up" data-i="2"><div class="bt-in"><span class="tag">School mission</span><p>{esc(C.SCHOOL_MISSION)}</p></div></article></div></div>

<div id="goals" class="blk"><p class="tag" data-r>Goals</p><h2 data-split>Six goals for the <em>decade</em></h2>
  <ol class="goals">{"".join(f'<li data-r="up" data-spot><span>{r}</span><p>{esc(t)}</p><em>{esc(w)}</em></li>' for r, t, w in C.GOALS)}</ol></div>

<div id="history" class="blk"><p class="tag" data-r>History</p><h2 data-split>From 1874 to <em>today</em></h2><div class="hist" data-r>{hist}</div></div>

<div id="presidents" class="blk"><p class="tag" data-r>Founders &amp; past presidents</p><h2 data-split>The <em>torchbearers</em></h2>{rail_presidents()}
  <details class="acc list-all"><summary>View as a list</summary><div class="a">{presidents("pres")}</div></details></div>

<div id="leadership" class="blk lead-blk"><div class="split"><div data-r="left">{photo("zahir-kazi.png", "Dr. Zahir Kazi", ratio="4/5")}</div><div><p class="tag" data-r>Leadership</p><h2 data-split>Dr. Zahir <em>Kazi</em></h2><p class="lead" data-r>President, Anjuman-I-Islam since 2009 · Padma awardee</p><p data-r>{esc(C.ZAHIR_BIO)}</p></div></div>
  <h4 style="margin:40px 0 14px">Board of Directors</h4>{board("board")}</div>

<div id="network" class="blk"><p class="tag" data-r>Network</p><h2 data-split>Institutions across <em>Maharashtra</em></h2>{stat_row(C.EDU_STATS, "stats sm")}<div style="margin-top:32px">{institutions_explorer()}</div></div>
</div></div></section>'''
    return layout("about", "About", body, phero("About us", "150 years of <em>service to education</em>", "Part of Anjuman-I-Islam — one of India’s largest minority educational and social institutions."))


def academics():
    ap = "".join(f'<li data-r="up" data-spot><span>{i + 1:02d}</span><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></li>' for i, (t, d) in enumerate(C.ACADEMIC_APPROACH))
    prog = "".join(f'<div data-pane="p{i}"><div class="split"><div><h3>{t}</h3><p class="lead">{esc(d)}</p><p>English medium · {u[2]} · Panchgani campus.</p></div>{scene(k, t, ratio="4/3")}</div></div>' for i, ((t, d), u, k) in enumerate(zip(C.PROGRAMMES, C.PANCHGANI_UNITS, ["books", "lab", "campus"])))
    tabs = "".join(f'<button data-tab="p{i}">{t}</button>' for i, (t, _) in enumerate(C.PROGRAMMES))
    fac = "".join(bento_tile("", "Facility", t, d, None, i) for t, i, d in C.FACILITIES)
    body = f'''
<section class="sec"><div class="wrap">{sh("Our approach", "Academic progress is a <em>fundamental commitment</em>")}<ol class="rows">{ap}</ol></div></section>
<section class="sec alt"><div class="wrap">{sh("Programmes", "Primary to <em>Jr. College</em>")}<div data-tabs><div class="filters tabbar">{tabs}</div>{prog}</div><p class="note">Panchgani: Primary (un-aided), High School (aided), Jr. College (un-aided).</p></div></section>
<section class="sec dark"><div class="mesh sm"><i></i><i></i></div><div class="wrap">{sh("Competitive coaching", "Prepare for the exams that <em>open doors</em>", esc(C.COACHING_NOTE))}{exam_tracks("tracks")}</div></section>
<section class="sec"><div class="wrap">{sh("Facilities", "Spaces built for <em>discovery</em>")}<div class="bento three">{fac}</div></div></section>
<section class="sec alt"><div class="wrap split"><div><p class="tag" data-r>Faculty &amp; staff</p><h2 data-split>Mentors, role models and <em>pillars of support</em></h2><p data-r>Teachers with a passion for their subjects, dorm in-charges offering guidance, and administrative and support staff keeping the campus safe, clean and welcoming.</p>{checklist(["Subject teachers", "Dorm in-charges", "Academic advisors", "Kitchen &amp; maintenance teams"], "checks")}</div>{scene("portrait", "Faculty", ratio="4/3")}</div></section>'''
    return layout("academics", "Academics", body, phero("Academics", "Learning that goes <em>beyond the books</em>", "Rigorous academics, personal advising and competitive coaching on one campus."))


def life():
    bo = "".join(bento_tile(["b-a", "", "", "b-d", "", ""][i], "Boarding", t, d, k) for i, (t, ic_, k, d) in enumerate(C.BOARDING))
    acts = "".join(f'<div class="act" data-cat="{c}" data-spot data-r="up">{ic(i)}<h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for t, c, i, d in C.ACTIVITIES)
    filt = '<div class="filters" data-filter-group data-target=".act"><button class="on" data-filter="all">All</button><button data-filter="innov">Innovation</button><button data-filter="outdoor">Outdoors</button><button data-filter="sport">Sports</button><button data-filter="arts">Arts</button><button data-filter="minds">Minds</button></div>'
    jr = "".join(f'<li data-r="up"><span>{i + 1}</span><h4>{esc(t)}</h4><p>{esc(d)}</p></li>' for i, (t, d) in enumerate(C.JOURNEY))
    body = f'''
<section class="sec"><div class="wrap">{sh("Boarding &amp; care", "A home <em>away from home</em>")}<div class="bento">{bo}</div></div></section>
<section class="sec dark" id="day"><div class="mesh sm"><i></i><i></i></div><div class="wrap">{sh("A day at Panchgani", "The rhythm of <em>boarding life</em>")}<div class="daystrip">{"".join(f'<div class="dd" data-r="up" data-spot><span>{i + 1:02d}</span><h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(C.DAY))}</div></div></section>
<section class="sec" id="activities"><div class="wrap">{sh("Extracurricular activities", "Athletes, artists and <em>leaders in the making</em>")}{filt}<div class="acts">{acts}</div></div></section>
<section class="sec alt" id="journey"><div class="wrap">{sh("Student journey", "How our students <em>evolve</em>")}<ol class="jr" data-stagger>{jr}</ol></div></section>
<section class="sec"><div class="wrap">{sh("Gallery", "Moments from <em>campus</em>")}<div class="masonry">{"".join(f'<div data-r="zoom" class="m{i}">{scene(k, l)}</div>' for i, (k, l) in enumerate([("hills", "Hills"), ("field", "Sports Day"), ("arts", "Art studio"), ("garden", "Gardens"), ("dining", "Dining"), ("lab", "Robotics lab")]))}</div></div></section>'''
    return layout("life", "Campus Life", body, phero("Campus life", "Athletes, artists and <em>leaders in the making</em>", "Boarding, sport, arts, robotics, riding and more across 174 acres."))


def results():
    ach = "".join(f'<article class="ac" data-r="up" data-spot><span class="tag">{esc(k)}</span><b>{esc(y)}</b><h4>{esc(t)}</h4><p>{esc(d)}</p></article>' for y, t, d, k in C.ACHIEVEMENTS)
    body = f'''
<section class="sec"><div class="wrap">{sh("Results", "Board &amp; entrance <em>outcomes</em>")}{results_tabs()}</div></section>
<section class="sec alt"><div class="wrap">{sh("Entrance exams", "Year-wise <em>selections</em>")}{exam_table()}</div></section>
<section class="sec"><div class="wrap">{sh("Achievements", "Honours &amp; <em>awards</em>")}<div class="achs">{ach}</div></div></section>
<section class="sec alt"><div class="wrap">{sh("Recognition", "School <em>rankings</em>")}<div class="bento three"><article class="bt" data-spot><div class="bt-in"><span class="logo-ph">LOGO</span><h3>Ranking body — <span class="val">#00</span></h3><p>Year · source to be added</p></div></article><article class="bt" data-spot><div class="bt-in"><span class="logo-ph">LOGO</span><h3>Ranking body — <span class="val">#00</span></h3><p>Year · source to be added</p></div></article><article class="bt" data-spot><div class="bt-in"><span class="logo-ph">LOGO</span><h3>Golden School Award</h3><p>2018–19 · Indian Talent Search</p></div></article></div></div></section>
<section class="sec"><div class="wrap">{sh("Anjuman in the news", "Stories of <em>excellence</em>")}{news_cards("news")}</div></section>'''
    return layout("results", "Results", body, phero("Results &amp; rankings", "Proof that <em>effort is rewarded</em>", "Board outcomes, entrance-exam selections and honours."))


def admissions():
    body = f'''
<section class="sec" id="process"><div class="wrap">{sh("Enrolment process", "Five steps to <em>admission</em>")}{steps("steps")}
  <div class="duo" style="margin-top:50px"><div class="card" data-spot><h3>Important points</h3>{checklist(C.IMPORTANT, "checks")}</div><div class="card" id="fees" data-spot><h3>Fees policy</h3>{checklist(C.FEES, "checks")}<p class="note">Fee amounts to be added by the school.</p></div></div></div></section>
<section class="sec alt" id="enquire"><div class="wrap split"><div><p class="tag" data-r>Admission enquiry</p><h2 data-split>Tell us about <em>your child</em></h2><p data-r>Our admissions office will contact you within one working day.</p><p data-r><b>{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}</b><br>{C.SCHOOL['email_admissions']}</p></div><div class="card" data-r>{enquiry_form()}</div></div></section>
<section class="sec" id="calendar"><div class="wrap">{sh("School calendar", "The year <em>at a glance</em>")}{calendar_block()}</div></section>
<section class="sec alt" id="faq"><div class="wrap narrow">{sh("FAQs", "Questions parents <em>ask</em>")}{faq()}</div></section>'''
    return layout("admissions", "Admissions", body, phero("Admissions", "Begin your journey at <em>Panchgani</em>", "A clear five-step enrolment process — and a team to guide you."))


def contact():
    cards = "".join(f'<div class="card" data-r="up" data-spot>{ic("mail")}<h4>{esc(l)}</h4><p>{esc(e)}</p></div>' for l, e in C.SCHOOL["emails"])
    body = f'''
<section class="sec"><div class="wrap">{sh("Reach the right office", "Get in <em>touch</em>")}<div class="g3">{cards}</div></div></section>
<section class="sec alt"><div class="wrap split"><div><p class="tag" data-r>Visit &amp; call</p><h2 data-split>Panchgani <em>campus</em></h2><p data-r>Panchgani, Maharashtra<br><small>(full postal address and PIN to be added)</small></p><p data-r><b>{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}</b></p>{scene("hills", "Map embed", ratio="16/10")}</div>
<div class="card" data-r><form class="form" data-demo novalidate><div><label for="c1">Name *</label><input id="c1" required></div><div><label for="c2">Phone *</label><input id="c2" required type="tel"></div><div class="full"><label for="c3">Email *</label><input id="c3" type="email" required></div><div class="full"><label for="c4">Subject</label><select id="c4"><option>Admission enquiry</option><option>Hostel enquiry</option><option>Fees &amp; accounts</option><option>General information</option></select></div><div class="full"><label for="c5">Message *</label><textarea id="c5" required></textarea></div><div class="full"><button class="btn grad" type="submit" data-mag>Send message {ARROW}</button></div></form></div></div></section>
<section class="sec" id="careers"><div class="wrap split"><div><p class="tag" data-r>Careers</p><h2 data-split>Join our <em>team</em></h2><p data-r>Teachers, dorm in-charges, coaching faculty and support staff who care about students.</p><p data-r><b>{C.SCHOOL['emails'][4][1]}</b></p></div>{scene("portrait", "Staff", ratio="4/3")}</div></section>
<section class="sec dark"><div class="mesh sm"><i></i><i></i></div><div class="wrap center"><p class="tag">Part of a larger family</p><h2 data-split>Anjuman-I-Islam</h2><p data-r>Founded in 1874 · head office enquiries: <b>{C.SCHOOL['parent_email']}</b></p><a class="btn light" href="{C.SCHOOL['parent_url']}" target="_blank" rel="noopener" data-mag>Visit anjumaniislam.org {ARROW}</a></div></section>'''
    return layout("contact", "Contact", body, phero("Contact", "We’d love to <em>hear from you</em>", "Reach the right office directly, or send us a message."))


def day():
    hero = aerial(f'<div class="wrap aerial-t"><p class="pill"><span class="dot"></span> Panchgani · Maharashtra</p><h1 data-split>174 acres, <em>above the clouds.</em></h1><p class="lead" data-r data-i="4">This is where your child will live, learn and grow. Scroll down — and spend a day with us.</p></div>')
    facts = "".join(bento_tile("", "Campus", f"{n} · {l}", t, None, ["globe", "fork", "cross"][i]) for i, (n, l, t) in enumerate(C.PLACE_FACTS))
    band = hills_band('<p class="tag" data-r>Where the day begins</p><h2 data-split>Every morning, the hills lift <em>out of the mist.</em></h2><p class="lead" data-r data-i="3">Rise, pray, learn, play, dine, study, rest — and begin again.</p>')
    body = f'''
<section class="sec"><div class="wrap">{sh("Where we are", "A <em>hill-station</em> campus", esc(C.PLACE_INTRO))}<div class="bento three">{facts}</div></div></section>
{band}
{dayclock()}
<section class="sec alt" id="timetable"><div class="wrap">{sh("The timetable", "Ten parts of a <em>day</em>")}{daytable()}</div></section>
<section class="sec" id="find-us"><div class="wrap split"><div><p class="tag" data-r>Find us</p><h2 data-split>Come and <em>see it</em> for yourself</h2><p data-r>Anjuman-I-Islam Public School &amp; Jr. College, Panchgani, Maharashtra.<br><small>Full postal address and directions to be added.</small></p><p data-r><b>{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}</b></p><a class="btn grad" href="admissions.html#enquire" data-mag>Plan a visit {ARROW}</a></div><div>{map_block()}</div></div></section>'''
    return layout("day", "A Day Here", body, hero)

def build():
    return {"index": home(), "about": about(), "academics": academics(), "life": life(), "day": day(), "results": results(), "admissions": admissions(), "contact": contact()}
