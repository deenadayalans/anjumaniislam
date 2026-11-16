"""Shared HTML helpers used by every theme."""
import json
import math
import random
import urllib.parse
from html import escape as esc
import content as C

PAGES = [  # slug, label
    ("index", "Home"), ("about", "About"), ("academics", "Academics"), ("life", "Campus Life"), ("day", "A Day Here"),
    ("results", "Results"), ("admissions", "Admissions"), ("contact", "Contact"),
]

ICONS = {
    "book": "M4 5c3-1 6-1 8 1 2-2 5-2 8-1v13c-3-1-6-1-8 1-2-2-5-2-8-1zM12 6v13",
    "flask": "M9 3h6M10 3v6l-5 9a2 2 0 002 3h10a2 2 0 002-3l-5-9V3M7 15h10",
    "chip": "M7 7h10v10H7zM10 10h4v4h-4zM9 3v4M15 3v4M9 17v4M15 17v4M3 9h4M3 15h4M17 9h4M17 15h4",
    "bed": "M3 19V6M3 15h18v4M21 15v-3a3 3 0 00-3-3h-7v6",
    "fork": "M7 3v8a2 2 0 002 2v8M5 3v6M9 3v6M17 21V3c-3 2-3 7-3 9h3",
    "dome": "M4 20v-7a8 8 0 0116 0v7M2 20h20M12 2v3M9 20v-4a3 3 0 016 0v4",
    "ball": "M12 3a9 9 0 100 18 9 9 0 000-18zM12 3v18M3 12h18",
    "cross": "M9 3h6v6h6v6h-6v6H9v-6H3V9h6z",
    "plane": "M3 12l18-8-6 16-3-7z",
    "leaf": "M5 20c0-9 5-15 15-16 0 10-6 15-14 15M5 20l7-7",
    "target": "M12 3a9 9 0 100 18 9 9 0 000-18zM12 7a5 5 0 100 10 5 5 0 000-10zM12 11a1 1 0 100 2 1 1 0 000-2z",
    "palette": "M12 3a9 9 0 100 18c1.5 0 2-1 1.5-2-.6-1.2.2-2.5 1.6-2.5H17a4 4 0 004-4c0-5-4-9.5-9-9.5zM7.5 11a1 1 0 100-2 1 1 0 000 2zM11 7.5a1 1 0 100-2 1 1 0 000 2zM15.5 9a1 1 0 100-2 1 1 0 000 2z",
    "mic": "M12 3a3 3 0 00-3 3v5a3 3 0 006 0V6a3 3 0 00-3-3zM5 11a7 7 0 0014 0M12 18v3",
    "trophy": "M8 4h8v6a4 4 0 01-8 0zM8 6H4v2a3 3 0 003 3M16 6h4v2a3 3 0 01-3 3M12 14v4M8 21h8M10 18h4",
    "users": "M9 11a3 3 0 100-6 3 3 0 000 6zM3 20v-1a5 5 0 0110 0v1M17 11a2.5 2.5 0 100-5M16 14a4 4 0 015 4v2",
    "shield": "M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6zM9 12l2 2 4-4",
    "cap": "M2 9l10-5 10 5-10 5zM6 11.5V16c0 1.5 3 3 6 3s6-1.5 6-3v-4.5M22 9v6",
    "cal": "M4 6h16v14H4zM4 10h16M8 3v4M16 3v4",
    "phone": "M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z",
    "mail": "M3 5h18v14H3zM3 6l9 7 9-7",
    "pin": "M12 21s7-6 7-11a7 7 0 10-14 0c0 5 7 11 7 11zM12 12a2 2 0 100-4 2 2 0 000 4z",
    "chat": "M4 5h16v11H9l-5 4z",
    "play": "M8 5v14l11-7z",
    "arrow": "M5 12h14M13 6l6 6-6 6",
    "check": "M5 12l5 5 9-10",
    "sun": "M12 8a4 4 0 100 8 4 4 0 000-8zM12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2",
    "music": "M9 18V6l10-2v12M9 18a3 3 0 11-6 0 3 3 0 016 0zM19 16a3 3 0 11-6 0 3 3 0 016 0z",
    "heart": "M12 20s-8-5-8-11a4.5 4.5 0 018-2.5A4.5 4.5 0 0120 9c0 6-8 11-8 11z",
    "globe": "M12 3a9 9 0 100 18 9 9 0 000-18zM3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18",
    "star": "M12 3l2.7 5.8 6.3.8-4.6 4.4 1.2 6.3L12 17.2 6.4 20.3l1.2-6.3L3 9.6l6.3-.8z",
    "menu": "M4 7h16M4 12h16M4 17h16",
    "x": "M6 6l12 12M18 6L6 18",
    "clock": "M12 3a9 9 0 100 18 9 9 0 000-18zM12 7v5l3 2",
    "download": "M12 4v11M7 11l5 5 5-5M5 20h14",
    "search": "M11 4a7 7 0 100 14 7 7 0 000-14zM21 21l-5-5",
    "moon": "M20 14a8 8 0 11-10-10 6 6 0 0010 10z",
}


def ic(name, cls=""):
    return f'<svg class="ic {cls}" viewBox="0 0 24 24" aria-hidden="true"><path d="{ICONS[name]}"/></svg>'


# ---------- Illustrated photo placeholders (themed via CSS vars --sc0..--sc5) ----------
_SCENES = {
    "hills": '<circle class="s5" cx="300" cy="90" r="34"/><path class="s1" d="M0 190 70 120 130 170 210 100 290 175 350 135 400 170V300H0Z"/><path class="s2" d="M0 220C80 170 150 200 220 180S350 170 400 200V300H0Z"/><path class="s3" d="M0 255C90 225 170 250 250 235S350 230 400 245V300H0Z"/><path class="s4" d="M50 252l12-34 12 34zM80 258l9-27 9 27zM330 250l11-30 11 30z"/>',
    "campus": '<circle class="s5" cx="320" cy="70" r="26"/><path class="s1" d="M0 200C100 160 200 190 300 170S380 160 400 175V300H0Z"/><rect class="s2" x="90" y="150" width="220" height="95"/><path class="s3" d="M80 152 200 108 320 152Z"/><path class="s5" d="M172 108a28 28 0 0156 0Z"/><path class="s4" d="M199 70h2v24h-2z"/><g class="s4"><rect x="108" y="172" width="22" height="34"/><rect x="146" y="172" width="22" height="34"/><rect x="232" y="172" width="22" height="34"/><rect x="270" y="172" width="22" height="34"/></g><rect class="s3" x="180" y="198" width="40" height="47"/><path class="s3" d="M0 245H400V300H0Z"/>',
    "lab": '<rect class="s1" y="0" width="400" height="300"/><rect class="s3" x="0" y="215" width="400" height="85"/><rect class="s2" x="70" y="95" width="110" height="90" rx="18"/><circle class="s5" cx="105" cy="135" r="12"/><circle class="s5" cx="145" cy="135" r="12"/><rect class="s4" x="100" y="160" width="50" height="8" rx="4"/><rect class="s4" x="118" y="60" width="14" height="36"/><circle class="s4" cx="125" cy="56" r="8"/><path class="s5" d="M250 215V150l-26-50h-4v-14h60v14h-4l-26 50v65z" opacity=".85"/><path class="s4" d="M232 190h56v25h-56z"/><circle class="s5" cx="330" cy="185" r="22" opacity=".8"/>',
    "dorm": '<rect class="s1" width="400" height="300"/><rect class="s5" x="260" y="50" width="90" height="100" rx="6" opacity=".6"/><circle class="s4" cx="320" cy="86" r="16"/><rect class="s3" x="0" y="230" width="400" height="70"/><g><rect class="s2" x="30" y="170" width="150" height="60" rx="8"/><rect class="s5" x="38" y="160" width="46" height="22" rx="10"/><rect class="s4" x="30" y="150" width="8" height="82"/><rect class="s2" x="210" y="170" width="150" height="60" rx="8"/><rect class="s5" x="218" y="160" width="46" height="22" rx="10"/><rect class="s4" x="210" y="150" width="8" height="82"/></g>',
    "field": '<circle class="s5" cx="80" cy="70" r="28"/><path class="s1" d="M0 160C100 130 300 130 400 160V300H0Z"/><rect class="s3" y="190" width="400" height="110"/><path class="s2" d="M0 260C120 215 280 215 400 260" fill="none" stroke-width="6" style="stroke:var(--sc2)"/><g class="s5"><rect x="298" y="110" width="5" height="82"/><rect x="352" y="110" width="5" height="82"/><rect x="298" y="110" width="59" height="5"/></g><circle class="s5" cx="180" cy="240" r="12"/><path class="s2" d="M170 240h20" stroke-width="2" style="stroke:var(--sc3)"/>',
    "dining": '<rect class="s1" width="400" height="300"/><path class="s4" d="M200 0v70" stroke-width="3" style="stroke:var(--sc4)"/><path class="s5" d="M170 100a30 30 0 0160 0z"/><path class="s5" d="M90 160l30-20h160l30 20z" opacity=".25"/><rect class="s3" x="40" y="190" width="320" height="22" rx="6"/><rect class="s2" x="70" y="212" width="14" height="70"/><rect class="s2" x="316" y="212" width="14" height="70"/><g class="s5"><ellipse cx="110" cy="188" rx="28" ry="7"/><ellipse cx="200" cy="188" rx="28" ry="7"/><ellipse cx="290" cy="188" rx="28" ry="7"/></g>',
    "prayer": '<circle class="s5" cx="320" cy="64" r="22"/><circle class="s1" cx="332" cy="58" r="20"/><rect class="s2" x="110" y="140" width="180" height="110"/><path class="s2" d="M140 140a60 60 0 01120 0z"/><path class="s3" d="M190 78h20v18h-20z"/><rect class="s2" x="60" y="100" width="26" height="150"/><path class="s2" d="M60 100l13-34 13 34z"/><rect class="s2" x="314" y="100" width="26" height="150"/><path class="s2" d="M314 100l13-34 13 34z"/><path class="s4" d="M180 250v-50a20 20 0 0140 0v50z"/><path class="s3" d="M0 250H400V300H0Z"/>',
    "garden": '<circle class="s5" cx="320" cy="64" r="30"/><path class="s1" d="M0 180C100 150 300 150 400 180V300H0Z"/><rect class="s3" y="215" width="400" height="85"/><g style="stroke:var(--sc4);stroke-width:3;fill:none"><path d="M70 250V170M70 200c-24-6-30-24-30-34 24 0 30 14 30 34zM70 220c24-6 30-24 30-34-24 0-30 14-30 34z"/><path d="M180 250V150M180 190c-26-6-34-26-34-38 26 0 34 16 34 38zM180 215c26-6 34-26 34-38-26 0-34 16-34 38z"/><path d="M290 250V180M290 208c-22-6-28-22-28-30 22 0 28 12 28 30z"/></g>',
    "portrait": '<rect class="s1" width="400" height="300"/><circle class="s2" cx="200" cy="120" r="52"/><path class="s2" d="M80 300c0-70 50-100 120-100s120 30 120 100z"/><circle class="s5" cx="320" cy="60" r="40" opacity=".35"/>',
    "arts": '<rect class="s1" width="400" height="300"/><ellipse class="s5" cx="200" cy="150" rx="120" ry="84"/><circle class="s1" cx="250" cy="170" r="20"/><g><circle class="s4" cx="140" cy="120" r="16"/><circle class="s3" cx="190" cy="92" r="16"/><circle class="s2" cx="248" cy="104" r="16"/><circle class="s4" cx="282" cy="140" r="14"/></g><path class="s3" d="M300 230l60-90 10 8-56 94z"/>',
    "books": '<rect class="s1" width="400" height="300"/><rect class="s3" x="0" y="230" width="400" height="70"/><g><rect class="s2" x="110" y="190" width="180" height="40" rx="4"/><rect class="s4" x="124" y="150" width="152" height="40" rx="4"/><rect class="s5" x="138" y="110" width="124" height="40" rx="4"/><rect class="s2" x="152" y="70" width="96" height="40" rx="4"/></g>',
}
_SCENES["horse"] = _SCENES["field"]


def scene(kind="hills", label="", cls="", ratio=None, caption=True):
    body = _SCENES.get(kind, _SCENES["hills"])
    style = f' style="--ar:{ratio}"' if ratio else ""
    cap = f'<figcaption>Photo placeholder{" · " + esc(label) if label else ""}</figcaption>' if caption else ""
    return (f'<figure class="scene {cls}"{style}><svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
            f'<rect class="s0" width="400" height="300"/>{body}</svg>{cap}</figure>')


def photo(name, alt="", cls="", ratio=None):
    style = f' style="--ar:{ratio}"' if ratio else ""
    return f'<figure class="photo {cls}"{style}><img src="assets/real/{name}" alt="{esc(alt)}" loading="lazy"></figure>'


# ---------- Reusable content blocks (generic classes; each theme's CSS styles them) ----------
def marquee(items, cls=""):
    row = "".join(f"<span>{esc(i)}</span>" for i in items)
    return f'<div class="marquee {cls}" aria-hidden="true"><div class="marquee-track">{row}{row}</div></div>'


def presidents(cls="pres"):
    out = []
    for i, (n, t, star) in enumerate(C.PRESIDENTS):
        s = ' <i class="star" title="Contributed funds as a philanthropist">★</i>' if star else ""
        cur = " is-current" if "till date" in t else ""
        out.append(f'<li class="pres-i{" is-star" if star else ""}{cur}" data-r="up" data-i="{i % 6}"><span class="yrs">{esc(t)}</span><b>{esc(n)}</b>{s}</li>')
    return f'<ol class="{cls}">{"".join(out)}</ol><p class="note"><i class="star">★</i> Presidents who contributed funds as philanthropists.</p>'


def board(cls="board"):
    return f'<ul class="{cls}">' + "".join(f'<li data-r="up" data-i="{i % 4}">{esc(n)}</li>' for i, n in enumerate(C.BOARD)) + "</ul>"


def institutions_explorer():
    cats = list(C.INSTITUTIONS)
    total = sum(len(v) for v in C.INSTITUTIONS.values())
    btns = f'<button class="on" data-filter="all">All <em>{total}</em></button>' + "".join(
        f'<button data-filter="{esc(k)}">{esc(k)} <em>{len(v)}</em></button>' for k, v in C.INSTITUTIONS.items())
    rows = []
    for cat, items in C.INSTITUTIONS.items():
        for area, med, name, aid in items:
            hl = " is-home" if area == "Panchgani" else ""
            rows.append(f'<tr class="{hl}" data-cat="{esc(cat)}" data-text="{esc((name + area + med).lower())}"><td>{esc(name)}</td><td>{esc(area)}</td><td>{esc(med)}</td><td>{esc(aid)}</td></tr>')
    return (f'<div class="explorer" data-explorer><div class="explorer-bar"><div class="filters" data-filter-group>{btns}</div>'
            f'<label class="search">{ic("search")}<input type="search" placeholder="Search institutions or areas" data-search aria-label="Search institutions"></label></div>'
            f'<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Institution</th><th>Area</th><th>Medium</th><th>Type</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>'
            f'<p class="note"><span data-out>{total}</span> institutions shown. Source: anjumaniislam.org</p></div>')


def calendar_block():
    btns = '<button class="on" data-filter="all">All</button>' + "".join(f'<button data-filter="{k}">{v}</button>' for k, v in C.CAL_TYPES.items())
    months = []
    for i, (m, evs) in enumerate(C.CALENDAR):
        li = "".join(f'<li data-cat="{t}"><b>{esc(d)}</b><span>{esc(x)}</span></li>' for d, x, t in evs)
        months.append(f'<div class="month" data-r="up" data-i="{i % 3}"><h4>{m}</h4><ul>{li}</ul></div>')
    return (f'<div class="cal"><div class="filters" data-filter-group data-target=".month li">{btns}</div><div class="months">{"".join(months)}</div>'
            f'<p class="note">{esc(C.CAL_NOTE)}</p></div>')


def faq(n=None):
    items = C.FAQ[:n] if n else C.FAQ
    return '<div class="faq">' + "".join(f'<details class="acc"><summary>{esc(q)}</summary><div class="a">{esc(a)}</div></details>' for q, a in items) + "</div>"


def enquiry_form(confetti=False):
    c = " data-confetti" if confetti else ""
    return f'''<form class="form" data-demo{c} novalidate>
  <div><label for="f-name">Parent / guardian name *</label><input id="f-name" required autocomplete="name"></div>
  <div><label for="f-phone">Phone *</label><input id="f-phone" type="tel" required autocomplete="tel"></div>
  <div><label for="f-mail">Email *</label><input id="f-mail" type="email" required autocomplete="email"></div>
  <div><label for="f-child">Child’s name *</label><input id="f-child" required></div>
  <div><label for="f-class">Class applying for *</label><input id="f-class" required placeholder="e.g. Std VIII"></div>
  <div><label for="f-int">Interested in</label><select id="f-int"><option>Primary</option><option>High School (SSC)</option><option>Jr. College (HSC)</option><option>NEET / JEE / CET coaching</option><option>NATA / CA</option><option>Hifz course</option></select></div>
  <div class="full"><label for="f-msg">Message</label><textarea id="f-msg"></textarea></div>
  <div class="full"><button class="btn solid" type="submit" data-mag>Submit enquiry {ic("arrow")}</button><p class="note">Demo only — nothing is sent.</p></div>
</form>'''


def news_cards(cls="news"):
    out = []
    for i, (d, t, tag, url, img) in enumerate(C.NEWS):
        media = photo(img, t) if img else scene(["hills", "campus", "books", "arts"][i % 4], "", caption=False)
        out.append(f'<a class="news-i" href="{url}" target="_blank" rel="noopener" data-r="up" data-i="{i % 3}" data-spot>{media}<div class="news-b"><span class="tag">{esc(tag)}</span><h4>{esc(t)}</h4><time>{esc(d)}</time></div></a>')
    return f'<div class="{cls}">{"".join(out)}</div>'


def stat_row(items, cls="stats"):
    out = []
    for label, val, suf in items:
        out.append(f'<div class="stat" data-r="up"><b><span data-count="{val}">{val:,}</span>{suf}</b><span>{esc(label)}</span></div>')
    return f'<div class="{cls}">{"".join(out)}</div>'


def ssc_hsc_block():
    s, h = C.SSC_2026, C.HSC_2026
    pass_pct = round(s["passed"] / s["appeared"] * 100, 1)
    rows = "".join(f'<tr><td>{n}</td><td>{a:,}</td><td>{p:,}</td><td>{d}</td><td>{pc}%</td></tr>' for n, a, p, d, pc in h["streams"])
    bars = "".join(
        f'<div class="barrow"><span>{n}</span><div class="bar" style="--w:{pc}%"><i></i></div><b>{pc}%</b></div>' for n, a, p, d, pc in h["streams"])
    return f'''<div class="ssc-hsc">
  <div class="res-card" data-r="up"><h4>SSC 2026 <small>Anjuman-I-Islam network</small></h4>
    <div class="kpis"><div><b data-count="{s['appeared']}">{s['appeared']:,}</b><span>Appeared</span></div><div><b data-count="{s['passed']}">{s['passed']:,}</b><span>Passed</span></div><div><b data-count="{s['distinction']}">{s['distinction']}</b><span>Distinction</span></div><div><b data-count="{s['first_class']}">{s['first_class']}</b><span>First class</span></div></div>
    <div class="barrow"><span>Pass rate</span><div class="bar" style="--w:{pass_pct}%"><i></i></div><b>{pass_pct}%</b></div></div>
  <div class="res-card" data-r="up" data-i="1"><h4>HSC 2026 <small>Anjuman-I-Islam junior colleges</small></h4>
    <div class="kpis"><div><b data-count="{h['appeared']}">{h['appeared']:,}</b><span>Appeared</span></div><div><b data-count="{h['passed']}">{h['passed']:,}</b><span>Passed</span></div><div><b data-count="{h['distinction']}">{h['distinction']}</b><span>Distinction</span></div><div><b>{h['overall']}%</b><span>Overall</span></div></div>
    {bars}
    <div class="tbl-wrap"><table class="tbl"><thead><tr><th>Stream</th><th>Appeared</th><th>Passed</th><th>Distinction</th><th>%</th></tr></thead><tbody>{rows}</tbody></table></div></div>
</div><p class="note">Network-wide figures published by Anjuman-I-Islam for 2026. Panchgani-specific results to be added.</p>'''


def exam_tracks(cls="tracks"):
    ph = '<span class="val" title="Placeholder — replace with verified results">00</span>'
    out = "".join(
        f'<div class="track" data-r="up" data-i="{i}" data-spot><b>{n}</b><span>{esc(full)}</span><div class="trk-meta"><em>{esc(tag)}</em>{ph}<small>selections</small></div></div>'
        for i, (n, full, tag) in enumerate(C.EXAMS))
    return f'<div class="{cls}">{out}</div>'


def exam_table():
    ph = '<span class="val">00</span>'
    heads = "".join(f"<th>{n}</th>" for n, _, _ in C.EXAMS)
    rows = "".join(f'<tr><td><b>{y}</b></td>' + "".join(f"<td>{ph}</td>" for _ in C.EXAMS) + "</tr>" for y in C.YEARS)
    return f'<div class="tbl-wrap"><table class="tbl"><thead><tr><th>Year</th>{heads}</tr></thead><tbody>{rows}</tbody></table></div><p class="note">Placeholder figures (<span class="val">00</span>) — replace with verified Panchgani results before launch.</p>'


def steps(cls="steps"):
    out = "".join(f'<li data-r="up" data-i="{i}"><b>{esc(t)}</b>{f"<small>{esc(s)}</small>" if s else ""}</li>' for i, (t, s) in enumerate(C.STEPS))
    return f'<ol class="{cls}">{out}</ol>'


def checklist(items, cls="checks"):
    return f'<ul class="{cls}">' + "".join(f'<li data-r="up" data-i="{i % 4}">{esc(x)}</li>' for i, x in enumerate(items)) + "</ul>"


def palette_css(pals, fonts=()):
    out = [f'html[data-palette="{p["id"]}"]{{{p["css"]}}}' for p in pals if p.get("css")]
    out += [f'html[data-font="{f["id"]}"]{{{f["css"]}}}' for f in fonts if f.get("css")]
    return "\n".join(out)


def head(title, desc, fonts, theme_color, pal=None):
    pal_js = ""
    if pal:
        slug, lst, fsets = pal
        data = json.dumps(dict(k=slug, list=[dict(id=p["id"], n=p["name"], c=p["sw"]) for p in lst], f=[dict(id=f["id"], n=f["name"], u=f.get("url", "")) for f in fsets]), separators=(",", ":"))
        pal_js = ("<script>(function(){var P=" + data + ",s,f,d=document.documentElement;try{s=localStorage.getItem('pal-'+P.k);f=localStorage.getItem('fnt-'+P.k)}catch(e){}"
                  "if(!P.list.some(function(x){return x.id===s}))s=P.list[0].id;"
                  "var F=P.f.filter(function(x){return x.id===f})[0]||P.f[0];"
                  "window.PAL=P;d.dataset.palette=s;d.dataset.font=F.id;"
                  "if(F.u){var l=document.createElement('link');l.rel='stylesheet';l.href=F.u;document.head.appendChild(l)}})()</script>\n")
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="{theme_color}">
<link rel="icon" href="assets/real/school-favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts}" rel="stylesheet">
{pal_js}<link rel="stylesheet" href="assets/style.css">
<script>document.documentElement.classList.add('js')</script>
</head>'''


def tail():
    return '<script src="assets/core.js"></script>\n</body>\n</html>'


# ---------------------------------------------------------------- Day clock, aerial map, hills band
def map_url(kind="sat", z=17):
    if kind == "sat":
        return f"https://maps.google.com/maps?ll={C.MAP_LL}&z={z}&t=k&output=embed"
    return f"https://maps.google.com/maps?q={urllib.parse.quote_plus(C.MAP_QUERY)}&z={z}&output=embed"


def aerial(inner):
    lat, lng = C.MAP_LL.split(",")
    return f'''<section class="aerial" data-aerial><div class="aerial-stage"><div class="aerial-fallback">{scene("hills", "Aerial view", caption=False)}</div>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"><script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<div class="aerial-map"><div class="aerial-leaflet" data-leaflet data-lat="{lat}" data-lng="{lng}" data-label="Anjuman-I-Islam Public School &amp; Jr. College"></div></div>
<div class="aerial-shade"></div>
<div class="aerial-in">{inner}</div>
<div class="aerial-cap" data-in=".3" data-out=".52"><span class="aerial-k">01 · The campus</span><h3>174 acres of hill country</h3><p>Academic block, dormitories, prayer hall and the Akbar Peerbhoy Sports Stadium — one green campus.</p></div>
<div class="aerial-cap" data-in=".7" data-out="9"><span class="aerial-k">02 · The hill station</span><h3>Panchgani, in the Sahyadri hills</h3><p>Cool mornings, clear night skies and room to roam in the hills of Maharashtra.</p></div>
<div class="aerial-scale" aria-hidden="true"><span data-lv="0">Campus</span><span data-lv="1">Neighbourhood</span><span data-lv="2">Hill station</span></div>
<button class="aerial-toggle" data-map-toggle type="button">Explore the map</button><a class="aerial-cue" href="#after-aerial">Scroll to fly in {ic("arrow")}</a></div></section><span id="after-aerial"></span>'''


def hills_band(inner, cls=""):
    return f'''<section class="hb {cls}"><div class="hb-sky"></div><div class="hb-clouds" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
<svg class="hb-l hb1" data-par=".22" viewBox="0 0 1440 400" preserveAspectRatio="none" aria-hidden="true"><path d="M0 200l150-90 130 60 170-130 160 100 170-80 180 120 140-70 200 90H1440V400H0z"/></svg>
<svg class="hb-l hb2" data-par=".12" viewBox="0 0 1440 360" preserveAspectRatio="none" aria-hidden="true"><path d="M0 190c200-90 380-80 570-10s420 70 870-50V360H0z"/></svg>
<svg class="hb-l hb3" data-par=".04" viewBox="0 0 1440 300" preserveAspectRatio="none" aria-hidden="true"><path d="M0 150c260-70 520-60 760 0s480 20 680-30V300H0z"/></svg>
<div class="hb-in wrap">{inner}</div></section>'''


def _fmt(h):
    h = h % 24
    hh = int(h)
    mm = round((h - hh) * 60)
    ap = "AM" if hh < 12 else "PM"
    h12 = hh % 12 or 12
    return f"{h12}:{mm:02d} {ap}" if mm else f"{h12} {ap}"


def _clock_svg(roman=False):
    rom = ["XII", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]
    ticks = "".join(
        f'<line class="tk{" hr" if i % 5 == 0 else ""}" x1="110" y1="{15 if i % 5 == 0 else 15}" x2="110" y2="{26 if i % 5 == 0 else 21}" transform="rotate({i * 6} 110 110)"/>' for i in range(60))
    nums = "".join(
        f'<text class="num" x="{110 + 70 * math.sin(math.radians(i * 30)):.1f}" y="{110 - 70 * math.cos(math.radians(i * 30)) + 5:.1f}" text-anchor="middle">{rom[i] if roman else (i or 12)}</text>' for i in range(12))
    return (f'''<svg viewBox="0 0 220 220" role="img" aria-label="Analogue clock showing the time of day"><circle class="cf-ring-bg" cx="110" cy="110" r="106"/><circle class="cf-ring" data-ring cx="110" cy="110" r="106" transform="rotate(-90 110 110)" stroke-dasharray="666" stroke-dashoffset="666"/>
<circle class="cf-face" cx="110" cy="110" r="96"/><circle class="cf-rim" cx="110" cy="110" r="96"/>{ticks}{nums}
<g class="hand m" data-hand-m><line x1="110" y1="122" x2="110" y2="34"/></g><g class="hand h" data-hand-h><line x1="110" y1="120" x2="110" y2="58"/></g><circle class="cf-dot" cx="110" cy="110" r="6"/>
<g class="cf-orb" data-orb><circle r="8"/></g></svg>''')


def dayclock(roman=False):
    plan = C.DAYPLAN
    stages = []
    for d in plan:
        o = {"s": d["s"], "e": d["e"], "w": d.get("w", 1)}
        if d.get("subs"):
            o["subs"] = [{"s": b["s"], "e": b["e"], "w": b["w"]} for b in d["subs"]]
        stages.append(o)
    rnd = random.Random(11)
    stars = "".join(f'<circle cx="{rnd.randint(0, 1000)}" cy="{rnd.randint(0, 380)}" r="{rnd.choice([1, 1.2, 1.6, 2.1])}"/>' for _ in range(80))
    panels, segs = [], []
    for i, d in enumerate(plan):
        if d.get("subs"):
            lis = "".join(f'<li data-text="{esc(b["text"])}"><b>{_fmt(b["s"])}</b><span>{esc(b["label"])}</span></li>' for b in d["subs"])
            body = f'<ol class="dc-sub">{lis}</ol><p class="dc-subtext"></p>'
        else:
            body = f'<p>{esc(d["text"])}</p><ul>{"".join(f"<li>{esc(x)}</li>" for x in d["points"])}</ul>'
        panels.append(f'<article class="dc-panel{" on" if i == 0 else ""}" data-panel="{i}"><div class="dc-pic">{scene(d["scene"], "", caption=False, ratio="3/1")}</div><span class="dc-range">{_fmt(d["s"])} – {_fmt(d["e"])}</span><span class="dc-kicker">{esc(d["kicker"])}</span><h3>{esc(d["title"])}</h3>{body}</article>')
        segs.append(f'<button class="seg{" on" if i == 0 else ""}" style="flex:{max(d["e"] - d["s"], 1.2):.2f}" data-seg="{i}" type="button" aria-label="Jump to {esc(d["kicker"])}, {_fmt(d["s"])}"><span>{_fmt(d["s"]) if d["e"] - d["s"] < 6 else _fmt(d["s"]) + " – " + _fmt(d["e"])}</span></button>')
    return f'''<section class="dayclock" data-dayclock data-stages="{esc(json.dumps(stages))}" data-sky="{esc(json.dumps(C.DAYSKY))}" data-mode="light"><div class="dc-stage">
<div class="dc-sky" aria-hidden="true"><svg class="dc-stars" viewBox="0 0 1000 380" preserveAspectRatio="xMidYMid slice">{stars}</svg><i class="dc-orb sun"></i><i class="dc-orb moon"></i>
<svg class="dc-hills" viewBox="0 0 1440 300" preserveAspectRatio="none"><path class="dh1" d="M0 130l140-60 130 40 160-90 150 70 160-50 190 80 140-40 210 60H1440V300H0z"/><path class="dh2" d="M0 200c200-70 360-60 560-10s420 50 880-30V300H0z"/><path class="dh3" d="M0 255c260-50 520-40 760 0s480 20 680-20V300H0z"/></svg></div>
<div class="dc-wrap wrap"><div class="dc-clockbox"><div class="dc-clock">{_clock_svg(roman)}</div><div class="dc-digital"><b data-dc-time>5:00</b><span data-dc-ampm>AM</span></div><p class="dc-label" data-dc-label>{esc(plan[0]["kicker"])}</p></div>
<div class="dc-panels">{"".join(panels)}</div></div>
<div class="dc-bar wrap"><div class="dc-bar-in">{"".join(segs)}<i class="dc-mark" data-mark></i></div><p class="dc-hint">Scroll to move the clock &nbsp;·&nbsp; or tap a time</p></div></div></section>'''


def daytable():
    rows = []
    for d in C.DAYPLAN:
        items = [(b["s"], b["e"], b["label"], b["text"]) for b in d["subs"]] if d.get("subs") else [(d["s"], d["e"], d["title"], d["text"])]
        rows += items
    html = "".join(f'<div class="dt-row" data-r="up" data-i="{i % 3}"><span class="dt-time">{_fmt(s0)} – {_fmt(e0)}</span><b>{esc(t)}</b><p>{esc(x)}</p></div>' for i, (s0, e0, t, x) in enumerate(rows))
    return f'<div class="dtable">{html}</div><p class="note">{esc(C.DAY_NOTE)}</p>'


def map_block():
    url = "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote_plus(C.MAP_QUERY)
    return (f'<div class="mapbox" data-r="zoom"><iframe src="{map_url("road", 13)}" title="Map of Panchgani and the school" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>'
            f'<p style="margin-top:18px"><a class="maplink" href="{url}" target="_blank" rel="noopener">Open in Google Maps {ic("arrow")}</a></p>')
