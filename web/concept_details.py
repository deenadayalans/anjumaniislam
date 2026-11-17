"""Detail sections for the scroll designs (01, 02): one anchored article per menu item, built from content.py and the prospectus.

build.py replaces the <!--DETAILS--> marker in each concept file with html(), and adds css(file) to its <style>.
"""
from html import escape as e

import content as C

S = C.SCHOOL


def _p(*paras):
    return "".join(f"<p>{p}</p>" for p in paras)


def _ul(items, cls=""):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def _art(id_, kicker, title, body):
    return f'<article class="dt-i" id="{id_}"><small>{kicker}</small><h3>{title}</h3>{body}</article>'


def _group(id_, kicker, title, lead, arts, alt):
    return (f'<section class="dt{" alt" if alt else ""}" id="{id_}"><div class="wrap"><header class="dt-h"><span class="dt-k">{kicker}</span><h2>{title}</h2><p>{lead}</p></header>'
            f'<div class="dt-grid">{"".join(arts)}</div></div></section>')


def _pct(p, a):
    return f"{p / a * 100:.1f}%"


def html():
    tl = _ul([f"<b>{y}</b> {e(t)}" for y, t in C.HISTORY], "dt-tl")
    about = [
        _art("history", "About", "Anjuman-I-Islam since 1874", _p(
            "Anjuman-I-Islam, Mumbai was founded in 1874 by a small group of devout and progressive Muslims led by Justice Badruddin Tyabji, the third President of the Indian National Congress and the first Indian to act as Chief Justice of the Bombay High Court, with a desire to see the community advance in education and social standing.",
            "It began with one school. Today it has ninety-seven institutions from KG to Ph.D., including colleges of engineering, education, commerce, law, hotel management and home science, a polytechnic, a Unani medical college, and schools of pharmacy and architecture.") + tl),
        _art("campus", "About", "The Panchgani campus", _p(
            "With more than 100 years of providing education, the Panchgani school sets out to build a learning community within a boarding school, where every student is empowered to explore, discover and excel.",
            "The campus covers 174 acres, home to a wide variety of flora and fauna. Alongside the school and Junior College, coaching is provided for NEET, JEE, CET and NATA. In 2024 Robotics, Agriculture and Basic Aviation were added, joining horse riding, pottery and archery.")),
        _art("vision", "About", "Vision &amp; mission", _p(
            f"<b>Anjuman vision.</b> {e(C.VISION)}", f"<b>Anjuman mission.</b> {e(C.MISSION)}",
            f"<b>Our school.</b> {e(C.SCHOOL_VALUES)}", f"<b>Our school mission.</b> {e(C.SCHOOL_MISSION)}")),
        _art("preface", "About", "President’s preface", _p(e(C.ZAHIR_BIO),
            "He believes India’s rise to a Vishwa Guru, a world leader, is achievable in the next two to three years with more focus and effort on education.") + '<p class="dt-who"><b>Dr. Zahir Kazi, Padma Shri</b><span>President, Anjuman-I-Islam</span></p>'),
        _art("chairman", "About", "Chairman’s message", f'<blockquote>“Step into a world where education meets compassion, and learning goes beyond the books. Anjuman-I-Islam Public School and Jr. College is a vibrant community where core values and nurturing go hand in hand, creating a supportive environment for every student to thrive. Our boarding school offers a wide variety of extracurricular activities: sports, music, arts, and clubs such as robotics, Artificial Intelligence (AI), horse riding, basic aviation, agriculture, archery, gardening and debate, along with community service. There is something for everyone to explore and develop their passion. Welcome to your new adventure, a place where lifelong friendship begins and the future is bright.”</blockquote><p class="dt-who"><b>[Name to confirm]</b><span>Executive Chairman</span></p>'),
        _art("principal", "About", "Principal’s message", _p("The Principal’s message is not in the prospectus yet. This space is held for it, with a portrait.") + '<p class="dt-who"><b>[Principal’s name]</b><span>Principal</span></p>'),
        _art("faculty", "About", "Faculty &amp; staff", _p(
            "Teachers here are mentors, role models and pillars of support. In class they lead lively discussions, hands-on activities and thought-provoking lectures; in the dormitories the dorm in-charge offers guidance, advice and a listening ear.",
            "Administrative staff manage student records, organise activities and keep the campus safe and secure. Support staff, from the kitchen team preparing nutritious meals to the maintenance crew, keep the campus clean, comfortable and welcoming.") + _ul(["Subject teachers", "Dorm in-charges", "Academic advisors", "Kitchen &amp; maintenance teams"], "dt-chips")),
    ]
    sc, hs = C.SSC_2026, C.HSC_2026
    wins = _ul([f"<b>{y}</b> {e(t)}. {e(d)}" for y, t, d, _ in C.ACHIEVEMENTS], "dt-list")
    acad = [
        _art("curriculum", "Academics", "Curriculum · Primary to Class X", _p(
            "English-medium classes from Primary to Std X. Every classroom has its own projector and AV set-up, and teachers draw on a ready library of e-materials.",
            "Teachers use varied methods for different ways of learning. Academic advisors meet each student regularly to set goals, track progress and offer guidance, and the school reads its own data to find where help is needed. " + e(C.COACHING_NOTE.split(". ", 1)[1]))),
        _art("juniorcollege", "Academics", "Junior College · Classes XI–XII", _p(
            "The Junior College shares the campus, so boarders carry on without changing school. The year follows the board calendar: Prelim exams for Std X and XII in December and January, HSC and SSC practicals in February, and final exams in March.",
            "Students preparing for NEET, JEE, CET, NATA and CA do so in a quiet hill-station setting where wellbeing comes first.")),
        _art("coaching", "Academics", "Entrance coaching", _p(
            "Coaching on campus covers NEET (medicine), JEE (engineering), CET (state entrance), NATA (architecture) and CA (chartered accountancy). Competitive courses carry an additional fee.") + _ul(["NEET", "JEE", "CET", "NATA", "CA"], "dt-chips")),
        _art("labs", "Academics", "Labs &amp; library", _ul([f"<b>{e(t)}.</b> {e(d)}" for t, _, d in C.FACILITIES], "dt-list")),
        _art("results", "Academics", "Results &amp; achievements", wins + _p(
            f"<b>Anjuman network, SSC 2026.</b> {sc['appeared']:,} appeared, {sc['passed']:,} passed ({_pct(sc['passed'], sc['appeared'])}), {sc['distinction']} with distinction, {sc['first_class']} in first class.",
            f"<b>Anjuman network, HSC 2026.</b> {hs['appeared']:,} appeared, {hs['passed']:,} passed ({hs['overall']}%). Science {hs['streams'][0][4]}%, Commerce {hs['streams'][1][4]}%, Arts {hs['streams'][2][4]}%.",
            "<i>Panchgani-only results and entrance-exam selections will be added.</i>")),
    ]
    day = _ul([f"<b>{a}</b> {e(b)}" for a, b in [
        ("05:00", "Rise, pray, breakfast"), ("08:00", "Classes, labs and lunch"), ("16:00", "Play, practise, explore"),
        ("19:00", "Dinner together"), ("20:00", "Supervised study"), ("22:00", "Lights out; dorm in-charge on duty, nurse on campus")]], "dt-tl")
    board = [
        _art("hostels", "Boarding", "Boys’ &amp; girls’ hostels", _p(
            "Every dormitory has been completely renovated, with a design that keeps a balance between home and school so a child feels safe, happy and welcome. The dormitories are spacious and well furnished, with common areas to relax and socialise after a long day.",
            "In the evenings students gather for study sessions supported by peer tutors and resident advisors, and the dorm in-charge is always a first point of contact.")),
        _art("food", "Boarding", "Food &amp; dining", _p(
            "The renovated dining hall seats 300 and serves all five meals of the day. The kitchen is supervised throughout so boarders receive well-balanced, wholesome meals on time, to a menu designed by a dietician. Hygiene and cleanliness come first.")),
        _art("health", "Boarding", "Health &amp; pastoral care", _p(
            "A well-trained and experienced nurse is available on campus 24/7, and a doctor visits for regular check-ups. The sick bay can keep patients in-house for rest and care.",
            "Pastoral care runs through the dorm in-charge, academic advisors and teachers, who watch each child’s progress and wellbeing.")),
        _art("dayhere", "Boarding", "A day at Anjuman", _p("The rhythm of a boarding day, with the five prayers marking its chapters.") + day + f'<p class="dt-note">{e(C.DAY_NOTE)}</p>'),
        _art("safety", "Boarding", "Safety &amp; discipline", _p(
            "The administrative staff look after a safe and secure campus, and a dorm in-charge supports every dormitory. Strict disciplinary action is taken against those who break the rules.") + _ul([e(i) for i in C.IMPORTANT], "dt-list")),
    ]
    life = [
        _art("deen", "Campus life", "Deen &amp; tarbiyah", _p(
            "The call to prayer is given five times a day in the prayer hall, and Muslim students are expected to offer salah. Basic Islamic education and recitation of the Qur’an are emphasised, and a Hifz course is available on request. Islamic quizzes and Eid-e-Milad celebrations are part of the year.")),
        _art("sports", "Campus life", "Sports &amp; riding", _p(
            "The Akbar Peerbhoy Sports Stadium is the largest sports ground in town, with separate grounds for football, kabaddi, volleyball and basketball. Boys and girls are coached in cricket, football, hockey, volleyball and athletics, with PT, gymnastics, yoga and archery.",
            "A well-equipped gymnasium and multipurpose hall keep training going through the rains, under trained and experienced teachers. Horse riding, a skating rink, a shooting range and an open gym are also on campus.")),
        _art("arts", "Campus life", "Arts, clubs &amp; aviation", _p(
            "Extracurricular activities build teamwork, leadership and time management. There is drama, quiz, debate, pottery and ceramics, knitting and sewing, sky gazing and music, and a performing arts centre with music rooms.",
            "Clubs and courses include Robotics &amp; AI, Basic Aviation, Agriculture and Gardening, with inter-house competitions in dramatics, debate, football, badminton and cross-country through the year.")),
        _art("calendar", "Campus life", "Events &amp; calendar", '<div class="dt-cal">' + "".join(
            f"<div><h4>{m}</h4>" + _ul([f"<b>{d}</b> {e(t)}" for d, t, _ in items]) + "</div>" for m, items in C.CALENDAR) + f'</div><p class="dt-note">{e(C.CAL_NOTE)}</p>'),
    ]
    adm = [
        _art("apply", "Admissions", "How to apply", '<ol class="dt-steps">' + "".join(f"<li>{e(t)}{f' <span>({e(s)})</span>' if s else ''}</li>" for t, s in C.STEPS) + "</ol>" + _p(
            "Admission is subject to the written exam, and we meet every family before a place is offered. Use the form below to book a visit.")),
        _art("fees", "Admissions", "Fees", _ul([e(i) for i in C.FEES], "dt-list") + '<p class="dt-note">Fee amounts will be added once confirmed by the school.</p>'),
        _art("faqs", "Admissions", "Frequently asked questions", "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in C.FAQ)),
        _art("contact", "Admissions", "Contact", _ul([f"{e(r)}: <a href=\"mailto:{m}\">{m}</a>" for r, m in S["emails"]], "dt-list") + _p(
            "Phone: " + " · ".join(f'<a href="tel:+91{n}">{n[:5]} {n[5:]}</a>' for n in S["phones"]), "Panchgani, Maharashtra. Full postal address to be added.")),
    ]
    return ("<!-- DETAILS: one anchored article per menu item -->\n"
            + _group("dt-about", "About", "About <i>the school</i>", "Our history, the campus, our leadership and the people who teach here.", about, False)
            + _group("dt-academics", "Academics", "Academics <i>in detail</i>", "What is taught, how children are supported, and where it leads.", acad, True)
            + _group("dt-boarding", "Boarding", "Boarding <i>in detail</i>", "Where children sleep, eat, rest and are looked after.", board, False)
            + _group("dt-life", "Campus life", "Campus life <i>in detail</i>", "Prayer, sport, the arts and the year’s calendar.", life, True)
            + _group("dt-admissions", "Admissions", "Admissions <i>in detail</i>", "How to apply, fees, answers to common questions and how to reach us.", adm, False))


_COMMON = """
.dt{padding:clamp(70px,11vh,120px) 0;scroll-margin-top:80px}
.dt .wrap{width:min(1180px,100% - 2*var(--dt-gutter))}
.dt-h{max-width:760px;margin-bottom:clamp(32px,5vh,56px)}
.dt-k{display:block;font:600 12px var(--sans);letter-spacing:.22em;text-transform:uppercase;color:var(--dt-accent)}
.dt-h h2{font-family:var(--serif);font-weight:400;font-size:var(--dt-h2);line-height:1.05;margin:16px 0 14px;color:inherit}
.dt-h h2 i{color:var(--dt-accent)}
.dt-h p{color:var(--dt-muted);max-width:560px}
.dt-grid{column-count:2;column-gap:clamp(28px,4vw,64px)}
.dt-i{break-inside:avoid;margin-bottom:clamp(36px,4vw,56px);border-top:1px solid var(--dt-line);padding-top:24px;scroll-margin-top:90px;min-width:0}
.dt-i small{display:block;font:600 11px var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--dt-accent)}
.dt-i h3{font-family:var(--serif);font-weight:400;font-size:clamp(24px,2.2vw,32px);line-height:1.15;margin:8px 0 14px;color:inherit}
.dt-i p{font:400 16px/1.75 var(--sans);color:var(--dt-muted);margin-top:12px}
.dt-i p b{color:inherit}
.dt-i a{color:var(--dt-accent);overflow-wrap:anywhere}
.dt-i li{overflow-wrap:anywhere}
.dt-i blockquote{font:italic 400 18px/1.7 var(--serif);color:inherit;border-left:2px solid var(--dt-accent);padding-left:18px}
.dt-who{margin-top:14px}.dt-who b{display:block}.dt-who span{font-size:13px;letter-spacing:.04em}
.dt-note{font-size:13px!important;letter-spacing:.02em}
.dt-tl,.dt-list{list-style:none;margin-top:16px}
.dt-tl li,.dt-list li{padding:9px 0;border-bottom:1px solid var(--dt-line);font:400 15px/1.6 var(--sans);color:var(--dt-muted)}
.dt-tl li b{display:inline-block;min-width:3.4em;color:var(--dt-accent)}
.dt-list li b{color:inherit}
.dt-chips{list-style:none;display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}
.dt-chips li{font:600 12px var(--sans);border:1px solid var(--dt-line);border-radius:999px;padding:7px 14px}
.dt-steps{list-style:none;counter-reset:s;margin-top:16px}
.dt-steps li{counter-increment:s;display:flex;gap:14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--dt-line);font:400 16px var(--sans)}
.dt-steps li::before{content:counter(s);font:italic 400 22px var(--serif);color:var(--dt-accent);min-width:1.2em}
.dt-steps span{color:var(--dt-muted);font-size:14px}
.dt-cal{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px 28px;margin-top:14px}
.dt-cal h4{font:600 12px var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--dt-accent)}
.dt-cal ul{list-style:none;margin-top:6px}
.dt-cal li{display:flex;gap:10px;font:400 14px/1.5 var(--sans);color:var(--dt-muted);padding:4px 0}
.dt-cal li b{flex:0 0 2.6em;color:inherit}
.dt-i details{border-bottom:1px solid var(--dt-line)}
.dt-i summary{cursor:pointer;padding:12px 0;font:500 16px var(--sans);color:inherit}
.dt-i details p{margin:0 0 14px}
@media (max-width:900px){.dt-grid{column-count:1}.dt-cal{grid-template-columns:1fr}}
"""

_PER = {
    "01-the-ascent.html": """
.dt{--dt-gutter:var(--gutter);--dt-h2:clamp(30px,3.4vw,48px);--dt-accent:var(--gold);--dt-line:rgba(11,26,51,.16);--dt-muted:var(--grey);background:var(--paper);color:var(--ink)}
.dt.alt{background:var(--mist)}
""",
    "02-five-times-a-day.html": """
.dt{--dt-gutter:var(--gutter);--dt-h2:var(--t-h2);--dt-accent:var(--accent);--dt-line:var(--line);--dt-muted:var(--muted);position:relative;z-index:1;color:var(--fg)}
.dt.alt{background:color-mix(in srgb,var(--fg) 5%,transparent)}
""",
}


def css(file):
    return _COMMON + _PER[file]
