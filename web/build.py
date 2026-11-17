#!/usr/bin/env python3
"""Build all four theme sites into web/dist/<theme>/ (each one is a self-contained, deployable website).

    python3 build.py            # build
    python3 build.py serve      # build, then serve on http://localhost:8000
"""
import importlib
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(ROOT))
from common import palette_css, pal_script  # noqa: E402
import concept_config  # noqa: E402
DIST = ROOT / "dist"
THEMES = ["heritage", "modern", "vibrant", "hillstation"]
DOMAIN = "www.anjumaniislam.com"
# Demo-only link back to the chooser and the colour/font picker; remove both at launch.
BACK_LINK = '<a class="demo-back" href="../index.html">&larr; All designs</a>'
# The three scroll-story designs live in web/concepts/ with their own images and sample video.
CONCEPTS = [
    dict(file="01-the-ascent.html", thumb="concepts/thumbs/01.jpg", name="Above the Noise", tagline="Climb through the clouds to the school", palette=["#071631", "#c2a876", "#f4f2ed"], accent="#071631", fonts="DM Serif Display · Montserrat",
         blurb="The site is the drive up the ghat. It opens on the school's front door and, as you scroll, climbs through the clouds to Fajr on the Table Land, with an altimeter on the right edge. It sells escape, and turns Panchgani's altitude into the reason to choose the school."),
    dict(file="02-five-times-a-day.html", thumb="concepts/thumbs/02.jpg", name="Five Times a Day", tagline="Know exactly where your child is", palette=["#0b1220", "#ffc08f", "#ffffff"], accent="#0b1220", fonts="Fraunces · DM Sans",
         blurb="A live clock set to Panchgani time tells a parent what a child at the school is doing right now. One day, ordered by the five salah, with the sky changing as you scroll. It answers the boarding-school worry before anything else."),
    dict(file="03-the-pattern.html", thumb="concepts/thumbs/03.jpg", name="Since 1874", tagline="Heritage and trust, minimal and white", palette=["#ffffff", "#988360", "#071631"], accent="#071631", fonts="Cormorant Garamond · Jost",
         blurb="Minimalist, in the spirit of Repton UK. A full-screen photo carousel under a white crest, a welcome and Chairman's message, five clickable pillars, school news, and the history as a date carousel on a single line."),
]


def manifest(name, start, color, up="../"):
    """Web app manifest so 'Add to Home Screen' / 'Install app' opens the design full screen, without browser chrome."""
    icons = [("app-icon-192.png", "192x192", "any"), ("app-icon-512.png", "512x512", "any"), ("app-icon-maskable-512.png", "512x512", "maskable")]
    return json.dumps(dict(name=name, short_name="Anjuman", description="Anjuman-I-Islam Public School & Jr. College, Panchgani", lang="en", start_url=start, scope="./", display="standalone",
                           background_color="#faf6ec", theme_color=color, icons=[dict(src=f"{up}real/{n}", sizes=s, type="image/png", purpose=p) for n, s, p in icons]), indent=1)


APP_META = '<meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="Anjuman"><meta name="apple-mobile-web-app-status-bar-style" content="default">'


def build():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    metas = []
    for slug in THEMES:
        if not (ROOT / "themes" / slug / "theme.py").exists():
            continue
        mod = importlib.import_module(f"themes.{slug}.theme")
        out = DIST / slug
        (out / "assets").mkdir(parents=True)
        shutil.copytree(ROOT / "assets" / "real", out / "assets" / "real")
        (out / "assets" / "core.js").write_text((ROOT / "core" / "core.js").read_text() + "\n" + (ROOT / "core" / "picker.js").read_text())
        css = (ROOT / "core" / "base.css").read_text() + "\n" + (ROOT / "core" / "picker.css").read_text() + "\n" + (ROOT / "themes" / slug / "style.css").read_text()
        css += "\n" + palette_css(getattr(mod, "PALETTES", []), getattr(mod, "FONTSETS", []))
        (out / "assets" / "style.css").write_text(css)
        pages = mod.build()
        for name, html in pages.items():
            html = html.replace("</body>", BACK_LINK + "</body>", 1)
            (out / f"{name}.html").write_text(html, encoding="utf-8")
        metas.append(mod.META)
        (out / "manifest.webmanifest").write_text(manifest(f'Anjuman-I-Islam Panchgani · {mod.META["name"]}', "./index.html", mod.META["palette"][0]))
        print(f"  {slug:12s} {len(pages)} pages")
    (DIST / "index.html").write_text(chooser(metas), encoding="utf-8")
    shutil.copytree(ROOT / "concepts", DIST / "concepts")
    shutil.copy(ROOT / "core" / "picker.js", DIST / "concepts" / "picker.js")
    picker_css = (ROOT / "core" / "picker.css").read_text()
    for f in CONCEPTS:
        p = DIST / "concepts" / f["file"]
        html = p.read_text(encoding="utf-8")
        head = pal_script(concept_config.style(f["file"])) + "<style>" + concept_config.css(f["file"]) + "\n" + picker_css + "</style>\n"
        stem = f["file"].rsplit(".", 1)[0]
        head += f'<link rel="manifest" href="{stem}.webmanifest"><link rel="apple-touch-icon" href="../real/apple-touch-icon.png">{APP_META}\n'
        (DIST / "concepts" / f"{stem}.webmanifest").write_text(manifest(f'Anjuman-I-Islam Panchgani · {f["name"]}', f"./{f['file']}", f["palette"][0]))
        html = html.replace("</head>", head + "</head>", 1).replace("</body>", BACK_LINK + '<script src="picker.js"></script></body>', 1)
        p.write_text(html, encoding="utf-8")
    print(f"  concepts     {len(CONCEPTS)} designs")
    shutil.copytree(ROOT / "assets" / "real", DIST / "real")
    shutil.copy(ROOT / "core" / "sw.js", DIST / "sw.js")
    (DIST / "manifest.webmanifest").write_text(manifest("Anjuman-I-Islam Panchgani · Website options", "./", "#0d1512", ""))
    (DIST / "CNAME").write_text(DOMAIN + "\n")
    (DIST / ".nojekyll").write_text("")
    # Demo phase: block crawlers. Change to "Allow: /" when the site goes live.
    (DIST / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
    print(f"Built → {DIST}")


def chooser(metas):
    cards = []
    for i, m in enumerate(metas, 1):
        sw = "".join(f'<i style="background:{c}"></i>' for c in m["palette"])
        links = "".join(f'<a href="{m["slug"]}/{p}.html">{l}</a>' for p, l in [("about", "About"), ("academics", "Academics"), ("life", "Campus Life"), ("day", "A Day Here"), ("results", "Results"), ("admissions", "Admissions"), ("contact", "Contact")])
        cards.append(f'''<article class="card" style="--c:{m["palette"][0]};--c2:{m["palette"][1]}">
  <a class="prev" href="{m["slug"]}/index.html" aria-label="Open {m["name"]}"><iframe src="{m["slug"]}/index.html" title="{m["name"]} preview" loading="lazy" tabindex="-1"></iframe></a>
  <div class="body"><span class="n">Option {i}</span><h2>{m["name"]}</h2><p class="tag">{m["tagline"]}</p><p>{m["blurb"]}</p>
  <div class="sw">{sw}</div><p class="meta"><b>Fonts:</b> {m["fonts"]}</p>
  <div class="go"><a class="primary" href="{m["slug"]}/index.html">Open full website</a></div>
  <div class="pages">{links}</div></div></article>''')
    fcards = []
    for j, f in enumerate(CONCEPTS, len(metas) + 1):
        sw = "".join(f'<i style="background:{c}"></i>' for c in f["palette"])
        fcards.append(f'''<article class="card" style="--c:{f["accent"]};--c2:{f["palette"][1]}">
  <a class="prev img" href="concepts/{f["file"]}" aria-label="Open {f["name"]}"><img src="{f["thumb"]}" alt="{f["name"]} preview" loading="lazy"></a>
  <div class="body"><span class="n">Option {j}</span><h2>{f["name"]}</h2><p class="tag">{f["tagline"]}</p><p>{f["blurb"]}</p>
  <div class="sw">{sw}</div><p class="meta"><b>Fonts:</b> {f["fonts"]}</p>
  <div class="go"><a class="primary" href="concepts/{f["file"]}">Open design</a></div></div></article>''')
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Website options — Anjuman-I-Islam Public School &amp; Jr. College, Panchgani</title>
<link rel="icon" href="real/school-favicon.png">
<meta name="theme-color" content="#0d1512"><link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="real/apple-touch-icon.png">{APP_META}
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0}}body{{font-family:Inter,system-ui,sans-serif;background:#0d1512;color:#e8f0ec;line-height:1.6}}
a{{color:inherit;text-decoration:none}}.wrap{{max-width:1280px;margin:0 auto;padding:0 28px}}
header{{padding:72px 0 40px}}header .k{{font-size:.74rem;letter-spacing:.2em;text-transform:uppercase;color:#7fd3b0;font-weight:700}}
h1{{font-size:clamp(2.2rem,5vw,4rem);letter-spacing:-.03em;line-height:1.05;margin:14px 0;max-width:900px}}
header p{{color:#9fb3a9;max-width:720px;font-size:1.05rem}}
.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:28px;padding-bottom:90px}}
.card{{background:#141f1b;border:1px solid #243530;border-radius:22px;overflow:hidden;display:flex;flex-direction:column;transition:transform .35s,border-color .35s}}
.card:hover{{transform:translateY(-6px);border-color:var(--c)}}
.prev{{display:block;position:relative;height:340px;overflow:hidden;background:#fff}}
.prev iframe{{width:1440px;height:1000px;border:0;transform-origin:0 0;pointer-events:none}}
.prev.img img{{width:100%;height:100%;object-fit:cover;object-position:top;display:block;transition:transform .6s}}.card:hover .prev.img img{{transform:scale(1.03)}}
.body{{padding:28px;display:flex;flex-direction:column;gap:10px;flex:1}}
.n{{font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:#7fd3b0;font-weight:700}}
.body h2{{font-size:1.7rem;letter-spacing:-.02em}}.tag{{color:#fff;font-weight:600}}.body p{{color:#9fb3a9;font-size:.95rem}}
.sw{{display:flex}}.sw i{{width:30px;height:30px;border-radius:50%;border:2px solid #141f1b;margin-right:-8px}}
.meta{{margin-top:8px}}.meta b{{color:#cfe0d8}}
.go{{margin-top:12px}}.primary{{display:inline-block;background:var(--c);color:#fff;padding:13px 24px;border-radius:12px;font-weight:700;border:1px solid rgba(255,255,255,.2)}}
.pages{{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}}.pages a{{font-size:.78rem;padding:6px 12px;border:1px solid #2f453e;border-radius:99px;color:#b9cec5}}.pages a:hover{{background:#fff;color:#111}}
footer{{border-top:1px solid #243530;padding:36px 0 60px;color:#6f8a7f;font-size:.85rem}}
@media(max-width:900px){{.grid{{grid-template-columns:1fr}}.prev{{height:260px}}}}
</style></head><body>
<header><div class="wrap"><div class="k">Design proposal · Anjuman-I-Islam Public School &amp; Jr. College, Panchgani</div>
<h1>Seven designs for one school. Pick the one that feels like home.</h1>
<p>Seven complete websites, each with its own layout, typography, motion and story, built on the same verified school content (prospectus and anjumaniislam.org). Open any of them and use the Style button (bottom-left) to try other colours and fonts. Logos and campus photographs are placeholders until real assets arrive.</p></div></header>
<main class="wrap"><div class="grid">{"".join(cards + fcards)}</div></main>
<footer><div class="wrap">Content source: school prospectus and anjumaniislam.org (about, vision &amp; mission, founders &amp; past presidents, institutions, results). Placeholder figures are marked <b>00</b>.</div></footer>
<script>function fit(){{document.querySelectorAll('.prev:not(.img)').forEach(p=>{{const s=p.clientWidth/1440;p.firstElementChild.style.transform='scale('+s+')'}})}}addEventListener('load',fit);addEventListener('resize',fit);</script>
<script>if('serviceWorker' in navigator&&location.protocol!=='file:')navigator.serviceWorker.register('sw.js').catch(function(){{}})</script>
</body></html>'''


if __name__ == "__main__":
    build()
    if len(sys.argv) > 1 and sys.argv[1] == "serve":
        import functools
        import http.server
        port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
        http.server.ThreadingHTTPServer.allow_reuse_address = True
        try:
            server = http.server.ThreadingHTTPServer(("", port), functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DIST)))
        except OSError:
            print(f"\nPort {port} is already in use - most likely an earlier 'serve' is still running.")
            print(f"The site has been rebuilt, so just refresh http://localhost:{port}")
            print(f"(or use another port:  python3 build.py serve {port + 1})")
            sys.exit(0)
        with server:
            print(f"\nServing http://localhost:{port}  (Ctrl+C to stop)")
            server.serve_forever()
