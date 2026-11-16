#!/usr/bin/env python3
"""Build all four theme sites into web/dist/<theme>/ (each one is a self-contained, deployable website).

    python3 build.py            # build
    python3 build.py serve      # build, then serve on http://localhost:8000
"""
import importlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(ROOT))
DIST = ROOT / "dist"
THEMES = ["heritage", "modern", "vibrant", "hillstation"]
DOMAIN = "www.anjumaniislam.com"
# Demo-only link back to the theme chooser; set to "" at launch.
BACK_LINK = '<a class="demo-back" href="../index.html">&larr; All themes</a>'


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
        shutil.copy(ROOT / "core" / "core.js", out / "assets" / "core.js")
        css = (ROOT / "core" / "base.css").read_text() + "\n" + (ROOT / "themes" / slug / "style.css").read_text()
        (out / "assets" / "style.css").write_text(css)
        pages = mod.build()
        for name, html in pages.items():
            html = html.replace("</body>", BACK_LINK + "</body>", 1)
            (out / f"{name}.html").write_text(html, encoding="utf-8")
        metas.append(mod.META)
        print(f"  {slug:12s} {len(pages)} pages")
    (DIST / "index.html").write_text(chooser(metas), encoding="utf-8")
    shutil.copytree(ROOT / "assets" / "real", DIST / "real")
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
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Website options — Anjuman-I-Islam Public School &amp; Jr. College, Panchgani</title>
<link rel="icon" href="real/school-favicon.png">
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
<h1>Four complete websites. One school. Pick the one that feels like home.</h1>
<p>Each option is a full 7-page website with its own layout, typography, motion and page designs — all built from the same verified content (school prospectus + anjumaniislam.org). Logos and campus photographs are placeholders until real assets arrive.</p></div></header>
<main class="wrap"><div class="grid">{"".join(cards)}</div></main>
<footer><div class="wrap">Content source: school prospectus and anjumaniislam.org (about, vision &amp; mission, founders &amp; past presidents, institutions, results). Placeholder figures are marked <b>00</b>.</div></footer>
<script>function fit(){{document.querySelectorAll('.prev').forEach(p=>{{const s=p.clientWidth/1440;p.firstElementChild.style.transform='scale('+s+')'}})}}addEventListener('load',fit);addEventListener('resize',fit);</script>
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
