#!/usr/bin/env python3
"""Regenerate the animated README banners: python3 scripts/make_banner.py (run from repo root)."""
THEMES = {
  "light": dict(bg="#FAFAF7", border="#E6E4DD", text="#16181D", muted="#6A6F7A", faint="#C9CCD2", card="#FFFFFF", accent="#6E56CF", chip="#EEEAFB", on_chip="#4B36A8"),
  "dark":  dict(bg="#0D1117", border="#262C36", text="#E6EDF3", muted="#8B949E", faint="#3A414C", card="#161B22", accent="#A594F9", chip="#2A2250", on_chip="#D4CCFF"),
}
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

def banner(t, animated=True):
    c = THEMES[t]
    def anim(attr, frm, to, begin, dur="0.4s"):
        return f'<animate attributeName="{attr}" from="{frm}" to="{to}" begin="{begin}" dur="{dur}" fill="freeze"/>' if animated else ""
    chips = [("+ Context", 1, True), ("+ Tone", 2, True), ("+ Length", 3, True), ("Role · skipped", 4, False)]
    out = []
    y0 = 105
    for i, (label, n, add) in enumerate(chips):
        y = y0 + i * 50
        w = 150 if add else 170
        begin = f"{0.6 + i*0.35:.2f}s"
        fill = c["chip"] if add else "none"
        stroke = c["accent"] if add else c["faint"]
        tcol = c["on_chip"] if add else c["muted"]
        strike = "" if add else f'<line x1="{1070}" y1="{y+1}" x2="{1070+110}" y2="{y+1}" stroke="{c["muted"]}" stroke-width="1.5"/>'
        out.append(f'''
  <g opacity="{0 if animated else 1}">{anim("opacity", 0, 1, begin)}
    <rect x="1052" y="{y-19}" width="{w}" height="38" rx="19" fill="{fill}" stroke="{stroke}" stroke-width="1.5" {'stroke-dasharray="4 4"' if not add else ''}/>
    <text x="1070" y="{y+6}" font-size="16" font-weight="{600 if add else 500}" fill="{tcol}">{label.replace('·','&#183;')}</text>{strike}
  </g>''')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="360" viewBox="0 0 1280 360" font-family="{FONT}">
  <title>just-enough-prompt — Fix what your prompt is missing. Nothing more.</title>
  <rect x="1" y="1" width="1278" height="358" rx="18" fill="{c['bg']}" stroke="{c['border']}" stroke-width="2"/>
  <text x="72" y="112" font-size="15" font-weight="600" letter-spacing="3" fill="{c['muted']}">AGENT SKILL</text>
  <text x="70" y="178" font-size="56" font-weight="800" letter-spacing="-1.5" fill="{c['text']}">just-enough-prompt</text>
  <text x="72" y="228" font-size="28" font-weight="600" fill="{c['accent']}">Fix what your prompt is missing.</text>
  <text x="72" y="262" font-size="28" font-weight="600" fill="{c['accent']}">Nothing more.</text>
  <text x="72" y="306" font-size="18" fill="{c['muted']}">Adds only the practices it needs, and shows why.</text>
  <rect x="724" y="86" width="290" height="188" rx="14" fill="{c['card']}" stroke="{c['border']}" stroke-width="1.5"/>
  <circle cx="746" cy="110" r="5" fill="{c['faint']}"/><circle cx="764" cy="110" r="5" fill="{c['faint']}"/><circle cx="782" cy="110" r="5" fill="{c['faint']}"/>
  <text x="746" y="164" font-family="{MONO}" font-size="17" fill="{c['text']}">write an email</text>
  <text x="746" y="190" font-family="{MONO}" font-size="17" fill="{c['text']}">about the project</text>
  <text x="746" y="216" font-family="{MONO}" font-size="17" fill="{c['text']}">delay<tspan fill="{c['accent']}">▍</tspan></text>
  <path d="M1016,180 L1040,180" stroke="{c['faint']}" stroke-width="2" stroke-linecap="round"/>
  {''.join(out)}
</svg>
'''
if __name__ == "__main__":
    import sys
    for t in THEMES:
        open(f".github/assets/banner-{t}.svg", "w").write(banner(t))
    if "--static" in sys.argv:
        for t in THEMES:
            open(f"/tmp/banner-{t}-static.svg", "w").write(banner(t, animated=False))
