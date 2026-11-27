"""Render OG images (1200x630) in the site's own style (light, editorial, DM Serif + DM Sans).
Outputs public/og-image.png and public/cv/cv-og.png.
Run: ~/.venvs/playwright/bin/python scripts/og.py  (needs public/cv/cv-preview.png from `just cvs`)"""
import base64, pathlib
from playwright.sync_api import sync_playwright

PUB = pathlib.Path(__file__).resolve().parent.parent / "public"
cv_png = base64.b64encode((PUB / "cv/cv-preview.png").read_bytes()).decode()

HEAD = """<html><head>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&family=DM+Serif+Display&display=swap" rel="stylesheet">
<style>
*{margin:0;box-sizing:border-box}
body{width:1200px;height:630px;border-top:6px solid #1e90ff;background:#fafaf9;color:#1c1917;font-family:'DM Sans',sans-serif;position:relative;overflow:hidden}
.bar{position:absolute;left:0;right:0;top:0;height:76px;border-bottom:1px solid #e7e5e4;display:flex;align-items:center;
 justify-content:space-between;padding:0 72px}
.logo{font-family:'DM Serif Display',serif;font-size:30px;color:#1e90ff}
.host{font-size:20px;color:#1e90ff;font-weight:500}
.eyebrow{font-size:17px;letter-spacing:.14em;text-transform:uppercase;color:#1873cc;font-weight:500}
h1{font-family:'DM Serif Display',serif;font-weight:400;font-size:96px;line-height:1;letter-spacing:-.01em;margin-top:16px}
p{font-size:25px;line-height:1.5;color:#44403c}
</style></head><body>"""

portfolio = HEAD + """
<div class="bar"><span class="logo">DG</span><span class="host">deviengeorge.me</span></div>
<div style="position:absolute;left:72px;top:128px;width:900px">
 <div class="eyebrow">Full-Stack Software Engineer · Cairo, Egypt</div>
 <h1>Devien George</h1>
 <p style="margin-top:22px;width:1000px">I build and scale production web platforms, used by 1,000+ people daily.</p>
 <div style="margin-top:34px;font-size:19px;color:#44403c;display:flex;align-items:center;gap:12px">
  <span style="width:10px;height:10px;border-radius:50%;background:#1e90ff"></span>Open to remote full-stack roles and contract work</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:150px;border-top:1px solid #e7e5e4;background:#f5f5f4;
 display:grid;grid-template-columns:repeat(4,1fr);align-items:center;text-align:center;padding:0 40px">
 %STATS%
</div></body></html>"""
stats = [("Live", "ALReserve, booking platform I lead"), ("24", "churches on one platform"),
         ("4 wks → 3 min", "exam scheduling, Nassaq"), ("99.99%", "API uptime, last 30 days")]
portfolio = portfolio.replace("%STATS%", "".join(
    f'<div><div style="font-family:\'DM Serif Display\',serif;font-size:42px">{a}</div>'
    f'<div style="font-size:17px;color:#78716c;margin-top:6px">{b}</div></div>' for a, b in stats))

cv = HEAD + f"""
<div class="bar"><span class="logo">DG</span><span class="host">deviengeorge.me/cv</span></div>
<div style="position:absolute;left:72px;top:128px;width:560px">
 <div class="eyebrow">Curriculum Vitae · PDF</div>
 <h1 style="font-size:84px">Devien George</h1>
 <p style="margin-top:14px">Full-Stack Software Engineer</p>
 <div style="margin-top:34px;border-top:1px solid #e7e5e4">
  %ROWS%
 </div>
</div>
<div style="position:absolute;right:72px;top:128px;width:440px;height:520px;overflow:hidden;border:1px solid #d6d3d1;border-bottom:0;background:#fff">
 <img src="data:image/png;base64,{cv_png}" style="width:100%;display:block">
</div></body></html>"""
rows = [("ALReserve", "Full-Stack Engineer", "2026 – now"), ("ITI, AMIT, Konecta", "Technical Instructor", "2021 – 2025"),
        ("Evolv", "Frontend Engineer", "2021 – 2022")]
cv = cv.replace("%ROWS%", "".join(
    f'<div style="display:flex;justify-content:space-between;padding:13px 0;border-bottom:1px solid #e7e5e4;font-size:19px">'
    f'<span><b style="font-weight:500">{a}</b> <span style="color:#78716c">· {b}</span></span><span style="color:#78716c">{c}</span></div>'
    for a, b, c in rows))

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 630})
    for html, out in [(portfolio, PUB / "og-image.png"), (cv, PUB / "cv/cv-og.png")]:
        pg.set_content(html, wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        pg.screenshot(path=str(out))
        print("wrote", out)
    b.close()
