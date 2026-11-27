"""Render OG images (1200x630): public/og-image.png and public/cv/cv-og.png.
Run: ~/.venvs/playwright/bin/python scripts/og.py  (needs public/cv/cv-preview.png from `just cvs`)"""
import base64, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
cv_png = base64.b64encode((PUB / "cv/cv-preview.png").read_bytes()).decode()

BASE = """<html><head>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Serif+Display&display=swap" rel="stylesheet">
<style>
*{margin:0;box-sizing:border-box}
body{width:1200px;height:630px;background:#1c1917;color:#fafaf9;font-family:'DM Sans',sans-serif;
 position:relative;overflow:hidden;border-top:6px solid #d97706}
.glow{position:absolute;right:-180px;top:-180px;width:620px;height:620px;border-radius:50%;
 background:radial-gradient(circle,rgba(217,119,6,.22),transparent 65%)}
.l{position:absolute;left:80px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;width:%W%px}
.chip{align-self:flex-start;color:#1c1917;background:#f59e0b;font-weight:700;font-size:20px;letter-spacing:3px;
 padding:8px 16px;border-radius:6px;margin-bottom:28px}
h1{font-family:'DM Serif Display',serif;font-weight:400;font-size:84px;line-height:1}
.role{font-size:32px;color:#d6d3d1;margin-top:18px}
.stack{font-size:22px;color:#a8a29e;margin-top:28px;line-height:1.5}
.facts{display:flex;gap:12px;margin-top:30px;flex-wrap:wrap}
.facts span{border:1px solid #44403c;color:#e7e5e4;font-size:19px;padding:7px 14px;border-radius:999px}
.url{position:absolute;left:80px;bottom:44px;font-size:22px;color:#f59e0b;font-weight:500}
</style></head><body><div class="glow"></div>%BODY%</body></html>"""

portfolio = BASE.replace("%W%", "760").replace("%BODY%", """
<div class="l">
 <h1>Devien George</h1>
 <div class="role">Full-Stack Software Engineer · Cairo, Egypt</div>
 <div class="stack">Node.js · TypeScript · React · Next.js · Laravel · AWS</div>
 <div class="facts"><span>4+ years in production</span><span>Building ALReserve</span><span>ITI instructor</span></div>
</div>
<div class="url">deviengeorge.me</div>
<div style="position:absolute;right:90px;top:50%;transform:translateY(-50%);width:260px;height:260px;border-radius:28px;
 border:2px solid #d97706;display:flex;align-items:center;justify-content:center;background:rgba(28,25,23,.6);
 font-family:'DM Serif Display',serif;font-size:130px;color:#f59e0b">DG</div>""")

cv = BASE.replace("%W%", "640").replace("%BODY%", f"""
<div class="l">
 <div class="chip">CV · PDF</div>
 <h1>Devien George</h1>
 <div class="role">Full-Stack Software Engineer</div>
 <div class="stack">Node.js · TypeScript · React · Next.js<br>Laravel · AWS · Docker</div>
</div>
<div class="url">deviengeorge.me/cv · always the latest version</div>
<img src="data:image/png;base64,{cv_png}" style="position:absolute;right:90px;top:70px;width:400px;
 transform:rotate(3deg);border-radius:4px;box-shadow:0 30px 60px rgba(0,0,0,.55),0 0 0 1px rgba(255,255,255,.08)">""")

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 630})
    for html, out in [(portfolio, PUB / "og-image.png"), (cv, PUB / "cv/cv-og.png")]:
        pg.set_content(html, wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        pg.screenshot(path=str(out))
        print("wrote", out)
    b.close()
