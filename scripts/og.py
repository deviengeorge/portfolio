"""Render OG images (1200x630) with Playwright.
  public/og-image.png            site (light, editorial, like the homepage)
  public/cv/cv-og.png            CV (dodger-blue cover, different from the site)
  public/og/projects/<slug>.png  one per case study
  public/og/blog/<slug>.png      one per post
Run: ~/.venvs/playwright/bin/python scripts/og.py  (needs public/cv/cv-preview.png from `just cvs`)"""
import base64, json, pathlib, re
from html import escape
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
BLUE = "#1e90ff"

def b64(path): return base64.b64encode(path.read_bytes()).decode()

def frontmatter(path):
    """ponytail: flat key: value frontmatter only (what our MDX uses); swap for a YAML parser if it nests."""
    block = path.read_text().split("---")[1]
    out = {}
    for line in block.strip().splitlines():
        k, _, v = line.partition(":")
        v = v.strip()
        try: out[k.strip()] = json.loads(v)
        except ValueError: out[k.strip()] = v.strip('"')
    return out

HEAD = f"""<html><head>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Serif+Display&family=Noto+Naskh+Arabic:wght@600&display=swap" rel="stylesheet">
<style>
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:630px;border-top:6px solid {BLUE};background:#fafaf9;color:#1c1917;font-family:'DM Sans',sans-serif;position:relative;overflow:hidden}}
.bar{{position:absolute;left:0;right:0;top:0;height:76px;border-bottom:1px solid #e7e5e4;display:flex;align-items:center;justify-content:space-between;padding:0 72px}}
.logo{{font-family:'DM Serif Display',serif;font-size:30px;color:{BLUE}}}
.host{{font-size:20px;color:{BLUE};font-weight:500}}
.eyebrow{{font-size:17px;letter-spacing:.14em;text-transform:uppercase;color:#1873cc;font-weight:500}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:96px;line-height:1;letter-spacing:-.01em;margin-top:16px}}
p{{font-size:25px;line-height:1.5;color:#44403c}}
</style></head><body>"""

def site():
    stats = [("Live", "ALReserve, booking platform I lead"), ("24", "churches on one platform"),
             ("4 wks → 3 min", "exam scheduling, Nassaq"), ("99.99%", "API uptime, last 30 days")]
    cells = "".join(f'<div><div style="font-family:\'DM Serif Display\',serif;font-size:42px">{a}</div>'
                    f'<div style="font-size:17px;color:#78716c;margin-top:6px">{b}</div></div>' for a, b in stats)
    return HEAD + f"""
<div class="bar"><span class="logo">DG</span><span class="host">deviengeorge.me</span></div>
<div style="position:absolute;left:72px;top:128px;width:1000px">
 <div class="eyebrow">Full-Stack Software Engineer · Cairo, Egypt</div>
 <h1>Devien George</h1>
 <p style="margin-top:22px">I build and scale production web platforms, used by 1,000+ people daily.</p>
 <div style="margin-top:34px;font-size:19px;color:#44403c;display:flex;align-items:center;gap:12px">
  <span style="width:10px;height:10px;border-radius:50%;background:{BLUE}"></span>Open to remote full-stack roles and contract work</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:150px;border-top:1px solid #e7e5e4;background:#f5f5f4;
 display:grid;grid-template-columns:repeat(4,1fr);align-items:center;text-align:center;padding:0 40px">{cells}</div></body></html>"""

def cv():
    rows = [("ALReserve", "Full-Stack Engineer", "2026 – now"), ("ITI, AMIT, Konecta", "Technical Instructor", "2021 – 2025"),
            ("Evolv", "Frontend Engineer", "2021 – 2022")]
    trs = "".join(f'<div style="display:flex;justify-content:space-between;padding:14px 0;border-bottom:1px solid rgba(255,255,255,.28);font-size:19px">'
                  f'<span><b style="font-weight:700">{a}</b> <span style="opacity:.8">· {b}</span></span><span style="opacity:.8">{c}</span></div>' for a, b, c in rows)
    return f"""<html><head><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Serif+Display&display=swap" rel="stylesheet">
<style>*{{margin:0;box-sizing:border-box}} body{{width:1200px;height:630px;background:{BLUE};color:#fff;font-family:'DM Sans',sans-serif;position:relative;overflow:hidden}}</style></head><body>
<div style="position:absolute;left:72px;top:64px;width:540px">
 <div style="display:flex;align-items:baseline;gap:16px;font-size:17px;letter-spacing:.16em;text-transform:uppercase;font-weight:700">
  <span style="border:2px solid #fff;padding:6px 12px">Curriculum Vitae</span><span style="opacity:.85">PDF · 2 pages</span></div>
 <div style="font-family:'DM Serif Display',serif;font-size:88px;line-height:.95;margin-top:40px">Devien<br>George</div>
 <div style="font-size:26px;margin-top:20px;opacity:.95">Full-Stack Software Engineer, Cairo</div>
 <div style="margin-top:30px;border-top:1px solid rgba(255,255,255,.28)">{trs}</div>
</div>
<div style="position:absolute;left:72px;bottom:40px;font-size:21px;font-weight:700">deviengeorge.me/cv</div>
<div style="position:absolute;right:72px;top:64px;width:470px;height:610px;overflow:hidden;background:#fff;box-shadow:0 0 0 1px rgba(0,0,0,.08)">
 <img src="data:image/png;base64,{b64(PUB / 'cv/cv-preview.png')}" style="width:100%;display:block"></div>
</body></html>"""

def project_hook(fm):
    """Case-study card that leads with the win: ogStat (giant number) and/or ogHook (headline)."""
    logo = fm.get("logo")
    head = (f'<div style="display:flex;align-items:center;gap:16px">'
            f'<img src="data:image/png;base64,{b64(PUB / logo.lstrip("/"))}" style="width:52px;height:52px;border-radius:12px">'
            f'<div><div style="font-size:24px;font-weight:700">{escape(fm["title"])}</div>'
            f'<div class="eyebrow" style="font-size:14px">Case study · {escape(fm.get("period", ""))}</div></div></div>')
    stat = (f'<div style="font-family:\'DM Serif Display\',\'Noto Naskh Arabic\',serif;font-size:{min(112, 2300 // len(fm["ogStat"]))}px;line-height:1.15;margin-top:30px;color:{BLUE};white-space:nowrap">{escape(fm["ogStat"])}</div>'
            if fm.get("ogStat") else "")
    hook_size = 40 if stat else 72
    hook = (f'<div style="font-family:\'DM Serif Display\',serif;font-size:{hook_size}px;line-height:1.1;margin-top:{20 if stat else 40}px">{escape(fm["ogHook"])}</div>')
    sub = f'<div style="font-size:22px;color:#78716c;margin-top:20px">{escape(fm.get("ogSub", ""))}</div>'
    return HEAD + f"""
<div class="bar"><span class="logo">DG</span><span class="host">deviengeorge.me/projects</span></div>
<div style="position:absolute;left:72px;right:72px;top:118px">{head}{stat}{hook}{sub}</div>
<div style="position:absolute;right:72px;bottom:44px;font-size:19px;color:#57534e">by <b style="color:#1c1917;font-weight:500">Devien George</b></div>
</body></html>"""

def page(kind, label, fm, foot):
    logo = fm.get("logo")
    logo_html = (f'<img src="data:image/png;base64,{b64(PUB / logo.lstrip("/"))}" style="width:96px;height:96px;border-radius:20px">'
                 if logo and (PUB / logo.lstrip("/")).exists() else "")
    title = escape(fm["title"])
    size = 84 if len(title) <= 24 else 64 if len(title) <= 44 else 54
    chips = "".join(f'<span style="border:1px solid #d6d3d1;padding:6px 12px;font-size:17px;color:#44403c">{escape(t)}</span>' for t in foot[:5])
    return HEAD + f"""
<div class="bar"><span class="logo">DG</span><span class="host">deviengeorge.me/{kind}</span></div>
<div style="position:absolute;left:72px;right:72px;top:124px">
 <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:40px">
  <div><div class="eyebrow">{escape(label)}</div><h1 style="font-size:{size}px">{title}</h1></div>{logo_html}
 </div>
 <p style="margin-top:22px;font-size:24px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden">{escape(fm['description'])}</p>
</div>
<div style="position:absolute;left:72px;right:72px;bottom:44px;display:flex;justify-content:space-between;align-items:center">
 <div style="display:flex;gap:10px;flex-wrap:wrap">{chips}</div>
 <div style="font-size:19px;color:#57534e;white-space:nowrap">by <b style="color:#1c1917;font-weight:500">Devien George</b></div>
</div></body></html>"""

jobs = [(site(), PUB / "og-image.png"), (cv(), PUB / "cv/cv-og.png")]
for f in sorted((ROOT / "src/content/projects").glob("*.md*")):
    fm = frontmatter(f)
    html = project_hook(fm) if fm.get("ogHook") else page("projects", f"Case study · {fm.get('period', '')}", fm, fm.get("tech", []))
    jobs.append((html, PUB / f"og/projects/{f.stem}.png"))
for f in sorted((ROOT / "src/content/blog").glob("*.md*")):
    fm = frontmatter(f)
    if fm.get("draft") is True: continue
    from datetime import date
    when = date.fromisoformat(str(fm.get("pubDate"))[:10]).strftime("%b %-d, %Y")
    jobs.append((page("blog", f"Article · {when}", fm, fm.get("tags", [])), PUB / f"og/blog/{f.stem}.png"))

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 630})
    for html, out in jobs:
        out.parent.mkdir(parents=True, exist_ok=True)
        pg.set_content(html, wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        pg.screenshot(path=str(out))
        print("wrote", out.relative_to(ROOT))
    b.close()
