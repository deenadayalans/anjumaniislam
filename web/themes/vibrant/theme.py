from html import escape as esc
from common import *
import content as C

META = dict(
    slug="vibrant", name="Vibrant Explorer", palette=["#0e7a5f", "#ffc933", "#ff6b4a", "#4cc9f0"],
    tagline="Your next big adventure starts here",
    blurb="Bold, bright and playful: rotating headline words, spinning badge, sticker cards that wobble, a ‘pick your passion’ filter and confetti when you enquire. Built to win students over as much as parents.",
    fonts="Fraunces · Poppins",
)
FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,800;1,9..144,700&family=Poppins:wght@400;500;600;700&display=swap"
GF = "https://fonts.googleapis.com/css2?family="
FONTSETS = [
    dict(id="fraunces", name="Fraunces and Poppins"),
    dict(id="bricolage", name="Bricolage and Nunito", url=GF + "Bricolage+Grotesque:wght@600;700;800&family=Nunito:wght@400;600;700;800&display=swap", css="--disp:'Bricolage Grotesque',system-ui,sans-serif;--sans:'Nunito',system-ui,sans-serif"),
    dict(id="baloo", name="Baloo and Nunito", url=GF + "Baloo+2:wght@600;700;800&family=Nunito:wght@400;600;700;800&display=swap", css="--disp:'Baloo 2',system-ui,sans-serif;--sans:'Nunito',system-ui,sans-serif"),
    dict(id="fredoka", name="Fredoka and Quicksand", url=GF + "Fredoka:wght@500;600;700&family=Quicksand:wght@500;600;700&display=swap", css="--disp:'Fredoka',system-ui,sans-serif;--sans:'Quicksand',system-ui,sans-serif"),
]
PALETTES = [
    dict(id="sunny", name="Sunny Green", sw=["#0e7a5f", "#ffc933", "#ff6b4a"], css=""),
    dict(id="ivory", name="Ivory and Gold (minimal)", sw=["#faf6ec", "#d9b86a", "#3a342a"], css="--g:#3a342a;--gd:#1f1b14;--y:#d9b86a;--c:#9a7430;--s:#e8e2d4;--l:#cfc7b4;--cream:#faf6ec;--ink:#1f1b14;--muted:#6f6a5c;--mint:#efe9da;--pale1:#f3ecda;--pale2:#e3dbc6;--pale3:#cfc6ad;--pale4:#b9ae92;--confetti:#d9b86a,#9a7430,#e8e2d4,#cfc7b4,#3a342a;--sc0:#f6efdc;--sc1:#e8e2d4;--sc2:#9a8a68;--sc3:#3a342a;--sc4:#9a7430;--sc5:#d9b86a"),
    dict(id="ocean", name="Ocean Pop", sw=["#0369a1", "#fde047", "#fb923c"], css="--g:#0369a1;--gd:#082f49;--y:#fde047;--c:#fb923c;--s:#67e8f9;--l:#a5b4fc;--cream:#f0f9ff;--ink:#0c2233;--muted:#4f6b80;--confetti:#fde047,#fb923c,#67e8f9,#a5b4fc,#0369a1;--sc0:#e0f2fe;--sc1:#67e8f9;--sc2:#0369a1;--sc3:#082f49;--sc4:#fb923c;--sc5:#fde047"),
    dict(id="bubblegum", name="Bubblegum", sw=["#7c3aed", "#ffd84d", "#ff5fa2"], css="--g:#7c3aed;--gd:#2a1052;--y:#ffd84d;--c:#ff5fa2;--s:#5ce1e6;--l:#c4b5fd;--cream:#fff4fb;--ink:#241036;--muted:#6b5a80;--confetti:#ffd84d,#ff5fa2,#5ce1e6,#c4b5fd,#7c3aed;--sc0:#fde7f3;--sc1:#5ce1e6;--sc2:#7c3aed;--sc3:#2a1052;--sc4:#ff5fa2;--sc5:#ffd84d"),
]
ARROW = ic("arrow")
COLS = ["y", "c", "s", "l", "g"]


def sh(title, tag="", sub=""):
    return f'<div class="sh">{f"<span class=pill data-r>{tag}</span>" if tag else ""}<h2 data-split>{title}</h2>{f"<p class=sub data-r>{sub}</p>" if sub else ""}</div>'


def layout(slug, title, body, hero=""):
    nav = "".join(f'<a href="{s}.html"{" class=cur" if s == slug else ""}>{l}</a>' for s, l in PAGES[1:])
    return head(f"{title} — {C.SCHOOL['name']}", "Boarding school and junior college in Panchgani — part of Anjuman-I-Islam, founded 1874.", FONTS, "#0e7a5f", ("vibrant", PALETTES, FONTSETS)) + f'''
<body data-cursor>
<div class="curtain"></div><div class="progress"><i></i></div><a class="skip" href="#main">Skip to content</a>
<header class="hdr" data-header><div class="wrap hdr-in">
  <a class="brand" href="index.html"><img class="school-logo" src="assets/real/school-logo-sm.png" alt=""><span><b>Anjuman-I-Islam</b><small>Public School &amp; Jr. College · Panchgani</small></span></a>
  <nav class="nav">{nav}</nav>
  <a class="btn y sm" href="admissions.html#enquire">Apply!</a>
  <button class="burger" data-nav-toggle aria-label="Menu">{ic("menu")}</button>
</div></header>
{hero}<main id="main">{body}</main>
<footer class="ftr"><div class="wrap">
  <div class="ftr-big"><h2 data-split>Ready to join the adventure?</h2><a class="btn y" href="admissions.html#enquire">Enquire now {ARROW}</a></div>
  <div class="ftr-grid">
    <div><a class="brand" href="index.html"><img class="school-logo" src="assets/real/school-logo-sm.png" alt=""><span><b>Anjuman-I-Islam</b><small>Public School &amp; Jr. College</small></span></a><p>Panchgani, Maharashtra · part of Anjuman-I-Islam, since 1874.</p></div>
    <div><h5>Explore</h5>{"".join(f'<a href="{s}.html">{l}</a>' for s, l in PAGES)}</div>
    <div><h5>Say hello</h5><p>{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}</p><p>{C.SCHOOL['email_admissions']}</p></div>
    <div><h5>Network</h5><img class="plogo" src="assets/real/logo.png" alt="Anjuman-I-Islam"><a href="{C.SCHOOL['parent_url']}" target="_blank" rel="noopener">anjumaniislam.org</a></div>
  </div>
  <div class="legal"><span>© <span data-year>2026</span> Anjuman-I-Islam Public School &amp; Jr. College</span><span>Design option 3 · Vibrant Explorer</span></div>
</div></footer>
{tail()}'''


def phero(title, lead, col="y"):
    return f'''<section class="phero {col}"><div class="wrap"><h1 data-split>{title}</h1><p class="lead" data-r data-i="3">{lead}</p></div>
<svg class="wave" viewBox="0 0 1440 80" preserveAspectRatio="none" aria-hidden="true"><path d="M0 40c240 60 480 60 720 10s480-40 720 0v30H0z"/></svg></section>'''


def hall_cards(items=None):
    items = items if items is not None else list(enumerate(C.PRESIDENTS))
    out = []
    for i, (n, t, star) in items:
        col = COLS[i % 5]
        cur = " now" if "till date" in t else ""
        out.append(f'<div class="pc {col}{cur}" data-r="zoom" data-i="{i % 4}" data-tilt><span class="no">#{i + 1:02d}</span>{"<i class=stk>★ Philanthropist</i>" if star else ""}{scene("portrait", "", ratio="1/1", caption=False)}<b>{esc(n)}</b><span class="yrs">{esc(t)}</span></div>')
    return f'<div class="pcs">{"".join(out)}</div>'


def day_path():
    return '<ol class="path">' + "".join(f'<li data-r="up"><span class="n">{i + 1}</span><div class="bub {COLS[i % 5]}"><h4>{esc(t)}</h4><p>{esc(d)}</p></div></li>' for i, (t, d) in enumerate(C.DAY)) + "</ol>"


def passions(n=None):
    items = C.ACTIVITIES[:n] if n else C.ACTIVITIES
    chips = '<div class="filters chips" data-filter-group data-target=".pa"><button class="on" data-filter="all">Everything</button><button data-filter="innov">Make &amp; build</button><button data-filter="outdoor">Outdoors</button><button data-filter="sport">Play sport</button><button data-filter="arts">Create</button><button data-filter="minds">Think &amp; speak</button></div>'
    cards = "".join(f'<div class="pa {COLS[i % 5]}" data-cat="{c}" data-r="zoom" data-i="{i % 4}" data-tilt>{ic(ico)}<h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for i, (t, c, ico, d) in enumerate(items))
    return f'{chips}<div class="pas">{cards}</div>'


# ---------------------------------------------------------- pages
def home():
    hero = f'''<section class="hero"><div class="wrap hero-in"><div class="hero-t">
  <span class="pill" data-r>Boarding school · Panchgani hills</span>
  <h1 data-r data-i="1">Your next big <span class="word" data-rotate="adventure|breakthrough|friendship|career">adventure</span> starts here.</h1>
  <p class="lead" data-r data-i="3">Robotics, horse riding, aviation, archery and NEET / JEE coaching — on a 174-acre hill campus where lifelong friendships begin and the future is bright.</p>
  <div class="cta" data-r data-i="4"><a class="btn y" href="admissions.html#enquire">Apply for admission {ARROW}</a><a class="btn w" href="life.html">See what we do</a></div></div>
  <div class="collage" data-r="zoom" data-i="2">
    <div class="tile t1" data-par=".05">{ic("chip")}<b>Robotics &amp; AI</b></div><div class="tile t2" data-par="-.06">{ic("plane")}<b>Basic Aviation</b></div><div class="tile t3" data-par=".08">{ic("target")}<b>Archery</b></div><div class="tile t4" data-par="-.04">{ic("star")}<b>Horse riding</b></div>
    <svg class="spin" viewBox="0 0 200 200" aria-hidden="true"><defs><path id="circ" d="M100,100 m-78,0 a78,78 0 1,1 156,0 a78,78 0 1,1 -156,0"/></defs><circle cx="100" cy="100" r="98" fill="#073b30"/><text fill="#ffc933" font-size="14" font-weight="700"><textPath href="#circ" textLength="480" lengthAdjust="spacing">PANCHGANI ★ BOARDING ★ 174 ACRES ★ SINCE 1874 ★ </textPath></text><path d="M100 70l8 20 22 2-17 14 6 22-19-12-19 12 6-22-17-14 22-2z" fill="#ff6b4a"/></svg>
  </div></div><svg class="wave" viewBox="0 0 1440 80" preserveAspectRatio="none" aria-hidden="true"><path d="M0 40c240 60 480 60 720 10s480-40 720 0v30H0z"/></svg></section>
<div class="tick">{marquee(["Robotics", "Aviation", "Agriculture", "Horse riding", "Archery", "Pottery", "Sky gazing", "Debate", "Skating", "Shooting", "Kite flying", "Quiz"], "mq")}</div>'''
    body = f'''
<section class="sec"><div class="wrap">{stat_row(C.STATS, "stats")}</div></section>

<section class="sec"><div class="wrap">{sh("Pick your <em>passion.</em>", "Beyond the classroom", "Teamwork, leadership and time management are learned on the field and in the studio. Tap a chip to explore.")}{passions(8)}<p class="center"><a class="btn g" href="life.html#activities">All 16 activities {ARROW}</a></p></div></section>

<section class="sec band-y"><div class="wrap">{sh("Part of a <em>bigger family</em>", "Anjuman-I-Islam · since 1874", "Our Panchgani campus belongs to one of India’s largest minority educational and social institutions.")}{stat_row(C.NETWORK_STATS, "stats")}<p class="center"><a class="btn g" href="about.html#network">Meet the network {ARROW}</a></p></div></section>

<section class="sec"><div class="wrap">{sh("Hall of <em>fame</em>", "Founders &amp; past presidents", "Twenty-one presidents, 150 years — the last six below.")}{hall_cards(list(enumerate(C.PRESIDENTS))[-5:])}<p class="center"><a class="btn c" href="about.html#presidents">See all 21 {ARROW}</a></p></div></section>

<section class="sec band-g"><div class="wrap">{sh("The <em>scoreboard</em>", "Results 2026", "Board results across the Anjuman-I-Islam network.")}{ssc_hsc_block()}</div></section>

<section class="sec"><div class="wrap">{sh("A day at <em>Panchgani</em>", "Boarding life")}{day_path()}<p class="center"><a class="btn y" href="day.html">Watch the clock turn {ARROW}</a></p></div></section>

<section class="sec alt"><div class="wrap">{sh("What’s <em>happening</em>", "News from the Anjuman family")}{news_cards("news")}</div></section>

<section class="sec"><div class="wrap">{sh("Five steps to <em>join us</em>", "Admissions")}{steps("steps")}<p class="center"><a class="btn y" href="admissions.html#enquire">Start your enquiry {ARROW}</a></p></div></section>'''
    return layout("index", "Home", body, hero)


def about():
    hist = "".join(f'<div class="hcard {COLS[i % 5]}" data-r="up"><b>{y}</b><p>{esc(t)}</p></div>' for i, (y, t) in enumerate(C.HISTORY))
    goals = "".join(f'<li class="{COLS[i % 5]}" data-r="zoom" data-i="{i % 3}"><span>{r}</span><p>{esc(t)}</p><em>{esc(w)}</em></li>' for i, (r, t, w) in enumerate(C.GOALS))
    body = f'''
<section class="sec"><div class="wrap narrow center">{sh("A desire to see the <em>community rise</em>", "Our founders")}<p class="lead" data-r>Anjuman-I-Islam was founded in 1874 by a small group of Muslims animated by a “desire to see the Musalmans rise higher in the moral, social and educational scale.”</p><p data-r>As early as 1880 it urged the Indian Education Commission to support vocational, industrial, commercial and agricultural education, physical education — and education for girls.</p></div></section>
<section class="sec band-y" id="history"><div class="wrap">{sh("From 1874 to <em>today</em>", "History")}<div class="hcards" data-stagger>{hist}</div><p class="center note-b">{esc(C.PIONEER_NOTE)}</p></div></section>
<section class="sec" id="vision"><div class="wrap">{sh("Vision, mission &amp; <em>values</em>", "Our purpose")}<div class="vm"><div class="big y" data-r="zoom"><h3>Vision</h3><p>{esc(C.VISION)}</p></div><div class="big c" data-r="zoom" data-i="1"><h3>Mission</h3><p>{esc(C.MISSION)}</p></div><div class="big s" data-r="zoom" data-i="2"><h3>School values</h3><p>{esc(C.SCHOOL_VALUES)}</p></div><div class="big l" data-r="zoom" data-i="3"><h3>School mission</h3><p>{esc(C.SCHOOL_MISSION)}</p></div></div></div></section>
<section class="sec alt" id="goals"><div class="wrap">{sh("Six goals for the <em>decade</em>", "Goals")}<ol class="goals">{goals}</ol></div></section>
<section class="sec" id="presidents"><div class="wrap">{sh("Hall of <em>fame</em>", "Founders &amp; past presidents", "All twenty-one presidents of Anjuman-I-Islam, 1875 to today.")}{hall_cards()}<p class="note center"><i class="star">★</i> Presidents who contributed funds as philanthropists.</p></div></section>
<section class="sec band-g" id="leadership"><div class="wrap split"><div data-r="zoom" class="frame">{photo("zahir-kazi.png", "Dr. Zahir Kazi", ratio="4/5")}</div><div><span class="pill y" data-r>Leadership</span><h2 data-split>Dr. Zahir Kazi</h2><p class="lead" data-r>President, Anjuman-I-Islam since 2009 · Padma awardee</p><p data-r>{esc(C.ZAHIR_BIO)}</p><h4 style="margin:26px 0 10px">Board of Directors</h4>{board("board")}</div></div></section>
<section class="sec" id="network"><div class="wrap">{sh("Institutions across <em>Maharashtra</em>", "The Anjuman network", "About 90 education institutes from kindergarten to PhD. Panchgani is highlighted.")}{stat_row(C.EDU_STATS, "stats three")}<div style="margin-top:40px">{institutions_explorer()}</div></div></section>'''
    return layout("about", "About", body, phero("A century and a half of <em>education.</em>", "Part of Anjuman-I-Islam — one of India’s largest minority educational and social institutions.", "s"))


def academics():
    ap = "".join(f'<div class="big {COLS[i % 5]}" data-r="zoom" data-i="{i}"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(C.ACADEMIC_APPROACH))
    prog = "".join(f'<article class="pg {COLS[i]}" data-r="up" data-i="{i}" data-tilt>{scene(k, "", ratio="4/3", caption=False)}<div><span class="pill">{u[2]}</span><h3>{t}</h3><p>{esc(d)}</p></div></article>' for i, ((t, d), u, k) in enumerate(zip(C.PROGRAMMES, C.PANCHGANI_UNITS, ["books", "lab", "campus"])))
    fac = "".join(f'<div class="fac {COLS[i % 5]}" data-r="zoom" data-i="{i % 3}" data-tilt>{ic(ico)}<h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for i, (t, ico, d) in enumerate(C.FACILITIES))
    body = f'''
<section class="sec"><div class="wrap">{sh("How we help every <em>student shine</em>", "Our approach")}<div class="vm">{ap}</div></div></section>
<section class="sec alt"><div class="wrap">{sh("Primary to <em>Jr. College</em>", "Programmes", "English-medium · Primary (un-aided), High School (aided), Jr. College (un-aided).")}<div class="pgs">{prog}</div></div></section>
<section class="sec band-g" id="coaching"><div class="wrap">{sh("Dream big. We’ll <em>coach you there.</em>", "Competitive coaching", esc(C.COACHING_NOTE))}{exam_tracks("tracks")}</div></section>
<section class="sec" id="facilities"><div class="wrap">{sh("Spaces for <em>discovery</em>", "Facilities")}<div class="facs">{fac}</div></div></section>
<section class="sec band-y"><div class="wrap split"><div><span class="pill" data-r>Faculty &amp; staff</span><h2 data-split>Mentors, role models and <em>pillars of support</em></h2><p data-r>Teachers with a passion for their subjects, dorm in-charges who offer a listening ear, and staff who keep campus safe, clean and welcoming.</p></div><div class="frame" data-r="zoom">{scene("portrait", "Faculty", ratio="4/3")}</div></div></section>'''
    return layout("academics", "Academics", body, phero("Learning that goes <em>beyond the books.</em>", "Rigorous academics, personal advising and entrance coaching on one campus.", "l"))


def life():
    bo = "".join(f'<article class="pg {COLS[i % 5]}" data-r="up" data-i="{i % 3}" data-tilt>{scene(k, "", ratio="4/3", caption=False)}<div>{ic(ico)}<h3>{t}</h3><p>{esc(d)}</p></div></article>' for i, (t, ico, k, d) in enumerate(C.BOARDING))
    jr = "".join(f'<li data-r="up"><span class="n">{i + 1}</span><div class="bub {COLS[i % 5]}"><h4>{esc(t)}</h4><p>{esc(d)}</p></div></li>' for i, (t, d) in enumerate(C.JOURNEY))
    gal = "".join(f'<div class="g{i}" data-r="zoom" data-i="{i % 3}" data-tilt>{scene(k, l)}</div>' for i, (k, l) in enumerate([("hills", "Hills"), ("field", "Sports Day"), ("arts", "Art studio"), ("garden", "Gardens"), ("dining", "Dining"), ("lab", "Robotics lab")]))
    body = f'''
<section class="sec"><div class="wrap">{sh("A home <em>away from home</em>", "Boarding &amp; care", "Dorm design balances home and school so your child feels safe, happy and welcome.")}<div class="pgs three">{bo}</div></div></section>
<section class="sec band-y" id="day"><div class="wrap">{sh("A day at <em>Panchgani</em>", "Boarding life")}{day_path()}</div></section>
<section class="sec" id="activities"><div class="wrap">{sh("Athletes, artists &amp; <em>leaders in the making</em>", "Extracurricular activities")}{passions()}</div></section>
<section class="sec alt" id="journey"><div class="wrap">{sh("How our students <em>evolve</em>", "Student journey")}<ol class="path">{jr}</ol></div></section>
<section class="sec"><div class="wrap">{sh("Moments from <em>campus</em>", "Gallery")}<div class="gal">{gal}</div></div></section>'''
    return layout("life", "Campus Life", body, phero("Athletes, artists and <em>leaders in the making.</em>", "Boarding, sport, arts, robotics, riding and more across 174 acres.", "c"))


def results():
    ach = "".join(f'<div class="tro {COLS[i % 5]}" data-r="zoom" data-i="{i % 3}" data-tilt>{ic("trophy")}<b>{esc(y)}</b><h4>{esc(t)}</h4><p>{esc(d)}</p><span class="pill">{esc(k)}</span></div>' for i, (y, t, d, k) in enumerate(C.ACHIEVEMENTS))
    body = f'''
<section class="sec"><div class="wrap">{sh("Board <em>scoreboard</em>", "Results 2026")}{ssc_hsc_block()}</div></section>
<section class="sec band-g"><div class="wrap">{sh("Entrance exam <em>tracks</em>", "JEE · NEET · CET · NATA · CA")}{exam_tracks("tracks")}<div class="tw">{exam_table()}</div></div></section>
<section class="sec"><div class="wrap">{sh("Trophy <em>room</em>", "Achievements")}<div class="tros">{ach}</div></div></section>
<section class="sec alt"><div class="wrap">{sh("School <em>rankings</em>", "Recognition")}<div class="vm three"><div class="big y"><span class="logo-ph">LOGO</span><h3>Ranking body — <span class="val">#00</span></h3><p>Year · source to be added</p></div><div class="big c"><span class="logo-ph">LOGO</span><h3>Ranking body — <span class="val">#00</span></h3><p>Year · source to be added</p></div><div class="big s"><span class="logo-ph">LOGO</span><h3>Golden School Award</h3><p>2018–19 · Indian Talent Search</p></div></div></div></section>
<section class="sec"><div class="wrap">{sh("Anjuman in the <em>news</em>", "Stories of excellence")}{news_cards("news")}</div></section>'''
    return layout("results", "Results", body, phero("Proof that <em>effort pays off.</em>", "Board outcomes, entrance-exam selections and honours.", "g"))


def admissions():
    body = f'''
<section class="sec" id="process"><div class="wrap">{sh("Five steps to <em>join us</em>", "Enrolment process")}{steps("steps")}
 <div class="vm" style="margin-top:50px"><div class="big y" data-r="zoom"><h3>Important points</h3>{checklist(C.IMPORTANT, "checks")}</div><div class="big s" id="fees" data-r="zoom" data-i="1"><h3>Fees policy</h3>{checklist(C.FEES, "checks")}<p class="note">Fee amounts to be added by the school.</p></div></div></div></section>
<section class="sec band-c" id="enquire"><div class="wrap split"><div><span class="pill y" data-r>Admission enquiry</span><h2 data-split>Tell us about <em>your child</em></h2><p data-r>Our admissions office will call you within one working day.</p><p data-r><b>{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}</b><br>{C.SCHOOL['email_admissions']}</p></div><div class="formbox" data-r="zoom">{enquiry_form(True)}</div></div></section>
<section class="sec" id="calendar"><div class="wrap">{sh("The year <em>at a glance</em>", "School calendar")}{calendar_block()}</div></section>
<section class="sec alt" id="faq"><div class="wrap narrow">{sh("Questions parents <em>ask</em>", "FAQs")}{faq()}</div></section>'''
    return layout("admissions", "Admissions", body, phero("Begin your journey at <em>Panchgani.</em>", "A clear five-step enrolment process — and a team to guide you.", "y"))


def contact():
    cards = "".join(f'<div class="big {COLS[i % 5]}" data-r="zoom" data-i="{i % 3}">{ic("mail")}<h4>{esc(l)}</h4><p>{esc(e)}</p></div>' for i, (l, e) in enumerate(C.SCHOOL["emails"]))
    body = f'''
<section class="sec"><div class="wrap">{sh("Get in <em>touch</em>", "Reach the right office")}<div class="vm three">{cards}</div></div></section>
<section class="sec alt"><div class="wrap split"><div><span class="pill" data-r>Visit &amp; call</span><h2 data-split>Panchgani <em>campus</em></h2><p data-r>Panchgani, Maharashtra<br><small>(full postal address and PIN to be added)</small></p><p data-r><b>{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}</b></p><div class="frame">{scene("hills", "Map embed", ratio="16/10")}</div></div>
<div class="formbox" data-r="zoom"><form class="form" data-demo data-confetti novalidate><div><label for="c1">Name *</label><input id="c1" required></div><div><label for="c2">Phone *</label><input id="c2" required type="tel"></div><div class="full"><label for="c3">Email *</label><input id="c3" type="email" required></div><div class="full"><label for="c4">Subject</label><select id="c4"><option>Admission enquiry</option><option>Hostel enquiry</option><option>Fees &amp; accounts</option><option>General information</option></select></div><div class="full"><label for="c5">Message *</label><textarea id="c5" required></textarea></div><div class="full"><button class="btn y" type="submit">Send message {ARROW}</button></div></form></div></div></section>
<section class="sec" id="careers"><div class="wrap split"><div><span class="pill" data-r>Careers</span><h2 data-split>Join our <em>team</em></h2><p data-r>Teachers, dorm in-charges, coaching faculty and support staff who care about students.</p><p data-r><b>{C.SCHOOL['emails'][4][1]}</b></p></div><div class="frame" data-r="zoom">{scene("portrait", "Staff", ratio="4/3")}</div></div></section>
<section class="sec band-y"><div class="wrap center narrow"><span class="pill">Part of a larger family</span><h2 data-split>Anjuman-I-Islam</h2><p data-r>Founded in 1874 · head office: <b>{C.SCHOOL['parent_email']}</b></p><a class="btn g" href="{C.SCHOOL['parent_url']}" target="_blank" rel="noopener">Visit anjumaniislam.org {ARROW}</a></div></section>'''
    return layout("contact", "Contact", body, phero("We’d love to <em>hear from you.</em>", "Reach the right office directly, or send us a message.", "s"))


def day():
    hero = aerial(f'<div class="wrap aerial-t"><span class="pill" data-r>Panchgani hills</span><h1 data-split>174 acres, <em>above the clouds!</em></h1><p class="lead" data-r data-i="4">This is where you will live, learn and play. Scroll down — and spend a day with us.</p></div>')
    facts = "".join(f'<div class="big {COLS[i]}" data-r="zoom" data-i="{i}"><h3>{n}</h3><p><b>{esc(l)}</b><br>{esc(t)}</p></div>' for i, (n, l, t) in enumerate(C.PLACE_FACTS))
    band = hills_band('<span class="pill" data-r>Where the day begins</span><h2 data-split>Every morning, the hills lift <em>out of the mist.</em></h2><p class="lead" data-r data-i="3">Rise, pray, learn, play, dine, study, rest — and do it all again!</p>')
    body = f'''
<section class="sec"><div class="wrap">{sh("A <em>hill-station</em> campus", "Where we are", esc(C.PLACE_INTRO))}<div class="vm three">{facts}</div></div></section>
{band}
{dayclock()}
<section class="sec alt" id="timetable"><div class="wrap">{sh("Ten parts of a <em>day</em>", "The timetable")}{daytable()}</div></section>
<section class="sec band-y" id="find-us"><div class="wrap split"><div><span class="pill" data-r>Find us</span><h2 data-split>Come and <em>see it</em> for yourself</h2><p data-r>Anjuman-I-Islam Public School &amp; Jr. College, Panchgani, Maharashtra.<br><small>Full postal address and directions to be added.</small></p><p data-r><b>{C.SCHOOL['phones'][0]} / {C.SCHOOL['phones'][1]}</b></p><a class="btn g" href="admissions.html#enquire">Plan a visit {ARROW}</a></div><div>{map_block()}</div></div></section>'''
    return layout("day", "A Day Here", body, hero)

def build():
    return {"index": home(), "about": about(), "academics": academics(), "life": life(), "day": day(), "results": results(), "admissions": admissions(), "contact": contact()}
