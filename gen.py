#!/usr/bin/env python3
import html, os, json

TEMPLATE = """<!doctype html>
<html><head><meta charset="utf-8"><style>
  *{{margin:0;box-sizing:border-box}}
  html,body{{width:1600px;height:840px;overflow:hidden}}
  body{{background:#0B0D11;color:#E7EAEF;
       font-family:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;position:relative}}
  .grid{{position:absolute;inset:0;
     background-image:linear-gradient(#151922 1px,transparent 1px),linear-gradient(90deg,#151922 1px,transparent 1px);
     background-size:80px 80px;opacity:.35}}
  .glow{{position:absolute;right:-220px;bottom:-220px;width:760px;height:760px;border-radius:50%;
     background:radial-gradient(circle,rgba(232,104,60,.22),transparent 65%)}}
  .wrap{{position:relative;height:100%;padding:96px 100px;display:flex;flex-direction:column;justify-content:space-between}}
  .eyebrow{{font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace;font-size:27px;letter-spacing:.18em;
     text-transform:uppercase;color:#E8683C;font-weight:600;display:flex;align-items:center;gap:20px}}
  .eyebrow::after{{content:"";flex:0 0 130px;height:2px;background:#E8683C;opacity:.75}}
  .title{{font-size:{fs}px;line-height:1.05;font-weight:700;letter-spacing:-.022em;max-width:23ch;text-wrap:balance}}
  .foot{{display:flex;align-items:flex-end;justify-content:space-between}}
  .who{{font-family:ui-monospace,monospace;font-size:25px;color:#8A93A2}}
  .who b{{color:#E7EAEF;font-weight:600}}
  .mark{{width:66px;height:66px;background:#E8683C;clip-path:polygon(0 100%,100% 0,100% 100%)}}
</style></head>
<body>
  <div class="grid"></div><div class="glow"></div>
  <div class="wrap">
    <div class="eyebrow">{tag}</div>
    <div class="title">{title}</div>
    <div class="foot"><div class="who">Andrii Votiakov &middot; dev.to/votiakov</div><div class="mark"></div></div>
  </div>
</body></html>"""

DATA = [
 ("01","WEBSCRAPING","Stop writing a parser per site. Run five and let confidence decide."),
 ("02","WEBSCRAPING","Your scraper probably doesn't need a browser. It needs the right request."),
 ("03","WEBSCRAPING","Anti-bot without melting your budget: the proxy waterfall."),
 ("04","APIFY","Why my Apify actors exit successfully when they scrape zero results"),
 ("05","AT SCALE","Scraping millions of pages a day: what actually breaks"),
 ("06","AWS · LAMBDA","We cut a Lambda bill 96.5% by reading the retry policy."),
 ("07","BIGQUERY","Your BigQuery bill is a query-shape problem. We cut one 72% in three weeks."),
 ("08","DATADOG","Datadog: minus 90% log ingestion without losing a single alert"),
 ("09","MONGODB","MongoDB Atlas minus 40%: unused indexes are write amplification you pay for"),
 ("10","CLOUD COST","The 30-day cloud-cost audit I run on every new client"),
 ("11","CAREER","What competitive programming actually taught me about production code"),
 ("12","AI ENGINEERING","I run an engineering setup where agents write most of the code"),
 ("13","WEBSCRAPING","Your scraper isn't broken. The site changed, and it didn't tell you."),
 ("14","STRUCTURED DATA","Half the web already hands you clean product data. You just have to ask."),
 ("15","TLS · JA3","Why your Python requests get blocked but curl sails through"),
 ("16","PAGINATION","The five ways pagination lies to your scraper"),
 ("17","ENTITY RESOLUTION","Matching the same product across 50 retailers is harder than scraping them"),
 ("18","N8N · APIFY","Build a SHEIN price tracker in 20 minutes with n8n and an Apify actor"),
 ("19","AWS · S3","Your S3 bill is a lifecycle-policy problem"),
 ("20","AWS · NETWORK","The AWS line item nobody understands: data transfer"),
 ("21","KUBERNETES","Your Kubernetes cluster is 60% idle and you're paying for all of it"),
 ("22","AWS · COMMIT","Reserved Instances, Savings Plans, Spot: stop leaving 40% on the table"),
 ("23","CLOUDWATCH","CloudWatch is quietly one of your biggest bills"),
 ("24","AWS · RDS","The RDS instance you provisioned in 2022 is still running 2022's load"),
 ("25","FRACTIONAL CTO","What a fractional CTO actually does in the first 30 days"),
 ("26","ZERO TO ONE","What a £1m MVP actually looked like under the hood"),
 ("27","BUILD IN PUBLIC","I'm building an e-commerce scraping platform. Here's the architecture, minus the secrets."),
 ("28","VECTOR SEARCH","Visual product discovery over 20M items: what actually mattered"),
 ("29","PRODUCTION","Your vibe-coded app works in the demo. Here's what breaks in production."),
 ("30","PAY FOR SAVINGS","Why I only charge when I actually save you money"),
 ("31","NO PROXY","87% of the pages we scrape need no proxy at all"),
 ("32","BENCHMARK","We pay for two unblocking APIs. One unblocked 0% of our pages."),
 ("33","NO BROWSER","A headless browser is needed for only 5% of the pages we scrape"),
 ("34","GENERIC ENGINE","One generic extractor, 30,506 retailers, zero per-site code"),
 ("35","THE WATERFALL","The proxy waterfall, by the numbers: 79.6% never leave hop one"),
 ("36","MESSY DATA","Only 21% of the product URLs people save are actually buyable products"),
 ("37","LLM AT SCALE","Categorizing 800k products with an LLM: 98.7% confidence"),
 ("38","GOOGLE PLACES","Scrape every UK branch of any chain from Google Places"),
 ("39","STORE LOCATORS","Five fingerprints: how UK retail store locators actually work"),
 ("40","YEXT","One GET request returns every Waitrose store in the UK"),
 ("41","STORE APIS","Most chains just hand you their store list as JSON"),
]

outdir = os.path.dirname(os.path.abspath(__file__))
for num, tag, title in DATA:
    # shrink font for long titles so 840px height never overflows
    n = len(title)
    fs = 82 if n <= 55 else (74 if n <= 70 else 66)
    doc = TEMPLATE.format(tag=html.escape(tag), title=html.escape(title), fs=fs)
    with open(os.path.join(outdir, f"cover-{num}.html"), "w") as f:
        f.write(doc)
print("wrote", len(DATA), "html files to", outdir)
