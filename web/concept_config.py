"""Colour palettes and font pairings for the three scroll-story designs in web/concepts/.

Each design already drives its look from CSS variables, so a palette is just a set of overrides
(plus, for 02, one colour set per time-of-day phase).
"""
from common import palette_css

GF = "https://fonts.googleapis.com/css2?family="
_FONTS = {
    "playfair": dict(id="playfair", name="Playfair and Inter", url=GF + "Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@300;400;500;600&display=swap",
                     css="--serif:'Playfair Display',Georgia,serif;--sans:'Inter',system-ui,sans-serif"),
    "cormorant": dict(id="cormorant", name="Cormorant and Jost", url=GF + "Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Jost:wght@200;300;400;500&display=swap",
                      css="--serif:'Cormorant Garamond',Georgia,serif;--sans:'Jost',system-ui,sans-serif"),
    "fraunces": dict(id="fraunces", name="Fraunces and DM Sans", url=GF + "Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,600;1,9..144,300;1,9..144,400&family=DM+Sans:wght@400;500;600;700&display=swap",
                     css="--serif:'Fraunces',Georgia,serif;--sans:'DM Sans',system-ui,sans-serif"),
    "dmserif": dict(id="dmserif", name="DM Serif and Montserrat", url=GF + "DM+Serif+Display:ital@0;1&family=Montserrat:wght@400;500;600;700&display=swap",
                    css="--serif:'DM Serif Display',Georgia,serif;--sans:'Montserrat',system-ui,sans-serif"),
}


def fonts(default):
    """The design's own pairing first (no extra download), then the other three."""
    own = dict(_FONTS[default], css="", url="")
    return [own] + [f for k, f in _FONTS.items() if k != default]


def _phase_css(pid, rows):
    """02 repaints the whole page per time of day: rows = {phase: (bg, fg, accent)}."""
    out = []
    sel = {"now": 'body[data-phase="now"]', "rhythm": 'body[data-phase="rhythm"]', "fajr": 'body[data-phase="fajr"]', "dhuhr": 'body[data-phase="dhuhr"]',
           "asr": 'body[data-phase="asr"]', "maghrib": 'body[data-phase="maghrib"]', "night": f'body[data-phase="isha"],html[data-palette="{pid}"] body[data-phase="night"]', "ledger": 'body[data-phase="ledger"]'}
    for k, (bg, fg, ac) in rows.items():
        out.append(f'html[data-palette="{pid}"] {sel[k]}{{--bg:{bg};--fg:{fg};--muted:color-mix(in srgb,{fg} 74%,transparent);--accent:{ac};--line:color-mix(in srgb,{fg} 22%,transparent)}}')
    return "\n".join(out)


STYLE = {
    "01-the-ascent.html": dict(
        slug="ascent", font="dmserif",
        pals=[
            dict(id="navy", name="Navy and Bronze", sw=["#071631", "#c2a876", "#f4f2ed"], css=""),
            dict(id="ivory", name="Ivory and Gold (minimal)", sw=["#ffffff", "#b8924f", "#231f18"], css="--night:#231f18;--ink:#2e2a21;--ghat:#4a4334;--moss:#a39a82;--mist:#f6f1e7;--paper:#fffdf8;--dawn:#dcc48f;--ember:#a8822f;--gold:#b8924f;--grey:#6b665a"),
            dict(id="forest", name="Forest and Clay", sw=["#0e2a22", "#c0743a", "#f3f1e7"], css="--night:#0e2a22;--ink:#12332a;--ghat:#1f4a3c;--moss:#7fa893;--mist:#f3f1e7;--paper:#fbfaf4;--dawn:#e0a36f;--ember:#b5651d;--gold:#c0743a;--grey:#55605a"),
            dict(id="plum", name="Plum and Rose", sw=["#2a1230", "#c9627f", "#f7f0f4"], css="--night:#2a1230;--ink:#331a3a;--ghat:#4a2a55;--moss:#b48fc0;--mist:#f7f0f4;--paper:#fffafc;--dawn:#f0b6c4;--ember:#b04a6a;--gold:#c9627f;--grey:#6a5a66"),
        ]),
    "02-five-times-a-day.html": dict(
        slug="fivetimes", font="fraunces",
        pals=[
            dict(id="dawn", name="Dawn to Dusk", sw=["#0b1220", "#ffc08f", "#eef2ea"], css=""),
            dict(id="ivory", name="Ivory and Gold (minimal)", sw=["#faf6ec", "#d9b86a", "#1c1914"], css="", rules=_phase_css("ivory", {
                "now": ("#1c1914", "#ffffff", "#d9b86a"), "rhythm": ("#2a251d", "#f6f1e7", "#d9b86a"), "fajr": ("#3a3328", "#f6f1e7", "#e3c98f"),
                "dhuhr": ("#faf6ec", "#1f1b14", "#a8822f"), "asr": ("#efe6d0", "#2a210f", "#9a7430"), "maghrib": ("#4a3d2a", "#f6f1e7", "#e3c98f"),
                "night": ("#14110c", "#efe8d8", "#d9b86a"), "ledger": ("#fbf8f1", "#1f1b14", "#8a6a2f")})),
            dict(id="forest", name="Forest and Mint", sw=["#08201a", "#8fe0c4", "#eef6f0"], css="", rules=_phase_css("forest", {
                "now": ("#08201a", "#ffffff", "#8fe0c4"), "rhythm": ("#14372d", "#f0fbf6", "#7fd6b5"), "fajr": ("#1f4a3c", "#effaf4", "#a6e6cb"),
                "dhuhr": ("#eef6f0", "#10261d", "#1f7a5a"), "asr": ("#e8efd0", "#1f2a10", "#5a7a1f"), "maghrib": ("#2f5a4a", "#f0fbf5", "#ffcf9a"),
                "night": ("#06120f", "#e6f2ec", "#8fe0c4"), "ledger": ("#f4f8f2", "#14231c", "#2f7a5a")})),
            dict(id="plum", name="Plum and Rose", sw=["#160d22", "#ff9fb2", "#f8eef3"], css="", rules=_phase_css("plum", {
                "now": ("#160d22", "#ffffff", "#ff9fb2"), "rhythm": ("#2a1a44", "#fbeef4", "#f59ab5"), "fajr": ("#4a2f6b", "#fff0f6", "#ffb3c7"),
                "dhuhr": ("#f8eef3", "#2a1028", "#b02a63"), "asr": ("#f8dfe6", "#3a1020", "#c2386f"), "maghrib": ("#6e2a4f", "#fff0f4", "#ffc0cf"),
                "night": ("#0e0716", "#efe6f5", "#e0a8ff"), "ledger": ("#fbf3f6", "#2a1a22", "#b02a63")})),
        ]),
    "03-the-pattern.html": dict(
        slug="pattern", font="cormorant",
        pals=[
            dict(id="white", name="White and Navy", sw=["#ffffff", "#988360", "#071631"], css=""),
            dict(id="ivory", name="Ivory and Gold (minimal)", sw=["#fffdf8", "#b8924f", "#26221a"], css="--white:#fffdf8;--grey:#f6f1e7;--text:#5b564a;--soft:#8a8473;--ink:#1f1b14;--navy:#26221a;--gold:#b8924f;--rule:#e3dbc7"),
            dict(id="slate", name="Slate and Sky", sw=["#ffffff", "#3f84a8", "#1c2b3a"], css="--white:#fff;--grey:#f1f4f7;--text:#4d5a66;--soft:#7d8a96;--ink:#101820;--navy:#1c2b3a;--gold:#3f84a8;--rule:#d5dde5"),
            dict(id="burgundy", name="Burgundy and Rose", sw=["#fffafa", "#c2607a", "#4a1420"], css="--white:#fffafa;--grey:#faf1f3;--text:#5a4a4e;--soft:#8c7a7e;--ink:#2a0e16;--navy:#4a1420;--gold:#c2607a;--rule:#ecd5da"),
        ]),
}


def style(file):
    s = STYLE[file]
    return s["slug"], s["pals"], fonts(s["font"])


def css(file):
    slug, pals, fs = style(file)
    # Form controls ignore the page font by default, so they would stay on Arial whatever pairing is chosen.
    return "button,input,select,textarea{font-family:inherit}\n" + palette_css(pals, fs) + "\n" + "\n".join(p.get("rules", "") for p in pals)
