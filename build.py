# Generates the site pages from shared header/footer. Run: python3 build.py
import re
EMAIL="info@greatlakessitelogic.com"; PHONE_T="+19897802592"; PHONE="(989) 780-2592"
QUOTE=f"mailto:{EMAIL}?subject=Great%20Lakes%20SiteLogic%20Quote%20Request"
NAV=[("/","Home"),("/services","Services"),("/about","About"),("/products","Products")]
import json,glob,html,datetime
SCHEMA=open("content/schema.json").read().strip()
CURYEAR=datetime.date.today().year
# Year tokens: {{yrs:YYYY}} in copy renders as (current year - YYYY) and stays
# self-updating in the browser via /assets/years.js. Anchors: firsthand field
# experience 2010 (=16 in 2026, +1/yr). Combined experience uses
# {{yrscombined:2010,2006}} = his advertised years (since 2010) + Suzie's years
# (since 2006) = 36 in 2026, advancing +2/yr.
def _yrs_combined(anchors):
    return sum(CURYEAR-int(a) for a in anchors.split(","))
def _yrs_plain(t):
    t=re.sub(r"\{\{yrscombined:([\d,]+)\}\}",lambda m:str(_yrs_combined(m.group(1))),t)
    return re.sub(r"\{\{yrs:(\d{4})\}\}",lambda m:str(CURYEAR-int(m.group(1))),t)
def _yrs_span(t):
    t=re.sub(r"\{\{yrscombined:([\d,]+)\}\}",lambda m:f'<span data-years-combined="{m.group(1)}">{_yrs_combined(m.group(1))}</span>',t)
    return re.sub(r"\{\{yrs:(\d{4})\}\}",lambda m:f'<span data-years-since="{m.group(1)}">{CURYEAR-int(m.group(1))}</span>',t)
def page(slug,title,desc,body):
    desc_html=_yrs_plain(desc)
    desc_tpl=f' data-desc-template="{html.escape(desc,quote=True)}"' if "{{yrs" in desc else ""
    links="".join(f'<a href="{h}"{" class=\"active\"" if h==slug else ""}>{t}</a>' for h,t in NAV)
    cta_cls="button active" if slug=="/contact" else "button"
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="{desc_html}"{desc_tpl} />
  <link rel="icon" type="image/png" href="/assets/favicon.png" />
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc_html}"{desc_tpl} />
  <meta property="og:image" content="https://greatlakessitelogic.com/assets/logo.png" />
  <meta name="theme-color" content="#0c2340" />
  <title>{title}</title>
  <link rel="stylesheet" href="/assets/styles.css?v=5" />
  <script type="application/ld+json">{SCHEMA}</script>
</head>
<body>
  <nav id="nav"><div class="container navin"><a class="brand" href="/" aria-label="Great Lakes SiteLogic home"><img class="brand-logo" src="/assets/logo.png" width="1697" height="540" alt="Great Lakes SiteLogic" /></a><div class="navlinks" id="navlinks">{links}<a class="{cta_cls}" href="/contact">Contact Us Today</a></div><button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="navlinks" onclick="var n=document.getElementById('nav');var o=n.classList.toggle('open');this.setAttribute('aria-expanded',o);this.textContent=o?'✕':'☰'">☰</button></div></nav>
  <main id="top">
{body}
  </main>
  <footer><div class="container foot"><span><b>Great Lakes SiteLogic, LLC</b> — Civil Construction Technology</span><span>Email us: <a href="mailto:{EMAIL}">{EMAIL}</a></span><span>© <span data-copyright-year>2026</span> Great Lakes SiteLogic. All rights reserved.</span></div></footer>
  <script src="/assets/years.js" defer></script>
</body>
</html>
'''
CTA=f'''    <section class="cta-band"><div class="container"><div><h2>Ready to talk about your project?</h2><p>Local support in Saginaw, Bay City &amp; Midland. Remote support statewide.</p></div><a class="button navy" href="/contact">Contact Us Today</a></div></section>'''

home=f'''    <section class="hero"><div class="container"><div class="hero-copy"><span class="eyebrow">Mid-Michigan Civil Technology</span><h1>Civil Construction Technology &amp; <span>Machine Grade Control in Mid&#8209;Michigan</span></h1><p class="tagline">Site technology built from the dirt up.</p><p>Practical field mapping, GIS, grade-control workflows, and construction technology support for teams that need the plan to work where the work happens.</p><div class="hero-actions"><a class="button" href="/services">Explore Our Services</a><a class="button outline" href="/contact">Contact Us Today</a></div><div class="service-line"><strong>Local support:</strong> Saginaw, Bay City &amp; Midland &nbsp;|&nbsp; <strong>Remote support:</strong> Available statewide across Michigan</div></div></div></section>
    <section><div class="container"><span class="eyebrow">What We Do</span><h2>Field experience, built into every workflow.</h2><p class="lead">Great Lakes SiteLogic is a family-owned, Mid-Michigan company helping contractors and project teams get better information from takeoff through construction. Twelve services, one standard: the plan has to work where the work happens.</p><div class="cards"><a class="card" href="/blueprint-takeoff-services-michigan"><h3>Blueprint Takeoff</h3><p>Accurate quantities from the plans, ready for estimating and bidding.</p><span class="more">Learn more</span></a><a class="card" href="/civil-3d-grade-control-modeling-michigan"><h3>Civil 3D Grade-Control Modeling</h3><p>Buildable 3D models that load straight into your machines.</p><span class="more">Learn more</span></a><a class="card" href="/machine-grade-control-michigan"><h3>Machine Grade Control</h3><p>Grade-control setup and support that keeps operators cutting to design.</p><span class="more">Learn more</span></a><a class="card" href="/survey-equipment-support-michigan"><h3>Survey Equipment Support</h3><p>Setup, troubleshooting, and support for the gear your crews run.</p><span class="more">Learn more</span></a><a class="card" href="/field-mapping-gis-michigan"><h3>Field Mapping &amp; GIS</h3><p>Maps and GIS deliverables grounded in field-collected data.</p><span class="more">Learn more</span></a><a class="card" href="/site-technology-consulting-michigan"><h3>Site Technology Consulting</h3><p>The right construction technology, chosen and set up for your operation.</p><span class="more">Learn more</span></a><a class="card" href="/gnss-consulting-team-development-michigan"><h3>GNSS Consulting and Team Development</h3><p>GNSS workflows and crew training that raise everyone's accuracy.</p><span class="more">Learn more</span></a><a class="card" href="/construction-advisement-michigan"><h3>Construction Advisement</h3><p>Straight answers on constructability before problems cost money.</p><span class="more">Learn more</span></a><a class="card" href="/project-management-cost-control-michigan"><h3>Project Management and Cost Control</h3><p>Reporting and controls that keep scope, schedule, and budget honest.</p><span class="more">Learn more</span></a><a class="card" href="/design-consulting-michigan"><h3>Design Consulting</h3><p>Design review and coordination focused on what can actually be built.</p><span class="more">Learn more</span></a><a class="card" href="/pre-construction-consulting-michigan"><h3>Pre-Construction Consulting</h3><p>Early planning that surfaces risk before the first machine rolls.</p><span class="more">Learn more</span></a><a class="card" href="/homeowner-project-advising-michigan"><h3>Homeowner Project Advising</h3><p>Professional guidance for homeowners taking on site and land projects.</p><span class="more">Learn more</span></a></div></div></section>
    <section class="fs-strip"><div class="container fs-strip-in"><div><span class="product-tag">Our Product</span><h2>FieldSight — the jobsite, in your hand.</h2><p>Phone-first field mapping that puts your live position on the plan, with DXF import, CAD-grade editing in the field, and multi-brand GNSS. <strong>Works with Trimble. Works without it.</strong> Now in closed beta on Google Play.</p></div><a class="button" href="/products">See FieldSight</a></div></section>
    <section class="dark"><div class="container about-grid"><div><span class="eyebrow">By the numbers</span><h2>Mid-Michigan built. Field-tested.</h2><div class="stats"><div class="stat"><strong><span data-years-combined="2010,2006">36</span></strong><span>Combined years of experience</span></div><div class="stat"><strong><span data-years-since="2010">16</span></strong><span>Years of firsthand field experience</span></div></div></div><div><p class="lead">We don't approach models, maps, or workflows as office-only deliverables. Every process is built with the operator, foreman, layout crew, superintendent, and project manager in mind.</p><div class="experience"><div>Blueprint Takeoff</div><div>Civil Consulting</div><div>Civil 3D Grade-Control Modeling</div><div>Machine Grade Control</div><div>Survey Equipment Support</div><div>Field Mapping &amp; GIS</div></div></div></div></section>
{CTA}'''

feat=[("Your position, on the plan","FieldSight is phone-first: import the plan and your live position rides on it, so the crew sees where they're standing relative to the design — not a pin dropped on a street map."),("DXF import that respects the plan","Plans import as DXF with per-import layers and text placed in position at its true height. Tap any imported feature to edit it — nothing comes in as a dumb picture."),("Real CAD editing in the field","Node-edit linework with live reshape, snap to endpoints, vertices, and edges, and work with Measure, Offset, 3-point arcs, Join, Break, Close, and Line-by-length tools — plus polygon tracing and undo/redo."),("GNSS your way","Use the phone GPS, plug in a Trimble SPS986 or R780 over USB, or pair an Emlid, Bad Elf, or Ardusimple receiver over Bluetooth — with NTRIP corrections and a live fix-quality readout."),("One Map hub","Basemaps including satellite and a Buildings footprints layer, with Layers and Status panels in a single hub — change what you see without leaving the map."),("Trade-specific toolboxes","Pick your trade — civil, landscape, demolition, forestry, electrical, or plumbing — and get the tools, line types, and symbols that trade actually uses, from APWA utility colors to timber-cruise plots and demo hazard marks."),("Exports crews can use","Export points and linework as GeoJSON, KML, GPX, DXF, or CSV — elevations carried through — for CAD, GIS, Google Earth, and reporting."),("Crew sync","Shared job sites with a live updates feed: the whole crew sees new files, field marks, and updates the moment they're posted.")]
feats="".join(f'<div class="feature"><span class="num">{i+1:02d}</span><b>{a}</b><p>{b}</p></div>' for i,(a,b) in enumerate(feat))
products=f'''    <section class="page-hero"><div class="container"><span class="eyebrow">Products</span><h1>FieldSight by Great Lakes SiteLogic: <span>the jobsite, in your hand.</span></h1><p>Phone-first field mapping that puts your live position on the plan — DXF import, CAD-grade editing in the field, and multi-brand GNSS, built for every trade on the project. <strong>Works with Trimble. Works without it.</strong> Now at version 1.7.31, in closed beta on Google Play.</p></div></section>
    <section id="fieldsight"><div class="container"><div class="split"><div><div class="product-panel"><span class="product-tag">Construction Field Mapping</span><h2>FieldSight</h2><p>Put the right information in the hands of the people doing the work. FieldSight brings the plan, your live position, and the crew's marks into one workspace, so the site makes sense while you're standing on it. Watch the full walk-through:</p><div class="video-frame"><video controls preload="metadata" poster="/assets/fs_shot_map.png"><source src="/assets/fieldsight_walkthrough.mp4" type="video/mp4">Your browser does not support the video tag.</video></div><p style="margin-top:16px"><span class="product-tag">Version 1.7.31</span>&nbsp; <span class="product-tag">Closed Beta — Google Play</span></p></div></div><div><h2>Built for practical site workflows.</h2><p class="lead">FieldSight reduces the gap between the office, the model, and the field — turning disconnected files and location data into a clearer jobsite view.</p><div class="features">{feats}</div></div></div></div></section>
    <section class="area"><div class="container story"><div><span class="eyebrow">Why FieldSight exists</span><h2>Critical site information shouldn't be stuck in the office.</h2></div><div><p>The jobsite moves fast, but key information is often trapped inside a CAD file, buried in a text message, or spread across disconnected tools.</p><p>FieldSight was built to close that gap. The focus isn't technology for its own sake — it's giving crews a straightforward way to see where they are, understand what's around them, and make better field decisions.</p><p>FieldSight is actively evolving through real-world construction feedback, with the goal of a dependable workflow for importing project information, reviewing it in the field, and improving office-to-field communication.</p></div></div></section>
    <section id="screenshots"><div class="container"><span class="eyebrow">Up close</span><h2>See FieldSight in action.</h2><p class="lead">Real screens from the app &mdash; the trade toolboxes, GNSS panel, and map views your crew will use every day.</p><div class="shots">
<div class="shot"><img src="/assets/fs_shot_map.png" alt="FieldSight hybrid map view" loading="lazy"><div><b>Map hub</b><p>Live position on the plan with one-tap switching between basemaps — including satellite and a Buildings footprints layer — plus Layers and Status panels in a single hub.</p></div></div>
<div class="shot"><img src="/assets/fs_shot_toolkit.png" alt="FieldSight trade toolbox picker" loading="lazy"><div><b>Trade toolbox picker</b><p>One tap switches the whole toolkit &mdash; civil, landscape, demolition, forestry, electrical, or plumbing &mdash; each with its own tools and presets.</p></div></div>
<div class="shot"><img src="/assets/fs_shot_forestry.png" alt="FieldSight forestry toolbox" loading="lazy"><div><b>Forestry toolbox</b><p>Skid trails, harvest boundaries, stream buffers, and tree, snag, and landing marks for timber cruising and land clearing.</p></div></div>
<div class="shot"><img src="/assets/fs_shot_demolition.png" alt="FieldSight demolition toolbox" loading="lazy"><div><b>Demolition toolbox</b><p>Demo boundaries, cut-and-cap lines, haul routes, plus ACM and lead hazard marks, debris piles, and exclusion-zone circles.</p></div></div>
<div class="shot"><img src="/assets/fs_shot_electrical.png" alt="FieldSight electrical toolbox" loading="lazy"><div><b>Electrical toolbox</b><p>Primary and secondary runs, trench lines, and panels, transformers, poles, light poles, junction boxes, and meters.</p></div></div>
<div class="shot"><img src="/assets/fs_shot_gnss.png" alt="FieldSight GNSS panel" loading="lazy"><div><b>GNSS panel</b><p>Phone, Bluetooth, or USB receiver with live fix-quality readout, point collection, and NTRIP correction settings.</p></div></div>
</div></div></section>
    <section class="area" id="beta"><div class="container"><span class="eyebrow">Closed Beta &amp; Pricing</span><h2>Now testing with contractor crews.</h2><p class="lead">FieldSight is in closed beta on Google Play, and we're recruiting contractor testers — run it on real jobs and tell us what breaks. When it opens up, pricing is simple, and every plan starts with a 14-day trial.</p><div class="cards"><div class="card"><h3>Solo</h3><p class="price">$29<span>/mo</span></p><p>For the one-person operation putting its own plans in the field.</p></div><div class="card"><h3>Crew</h3><p class="price">$49<span>/user/mo</span></p><p>For crews sharing job sites, files, and live updates across the team.</p></div><div class="card"><h3>Company</h3><p class="price">$99<span>/user/mo</span></p><p>For companies standardizing field mapping across every crew they run.</p></div></div><p style="margin-top:28px"><a class="button navy" href="/contact">Join the Beta</a></p></div></section>
{CTA}'''

about=f'''    <section class="page-hero"><div class="container"><span class="eyebrow">About Us</span><h1>Mid-Michigan built. <span>Field-tested experience.</span></h1><p>Family owned and operated, bringing civil construction knowledge and practical technology together for contractors and project teams.</p></div></section>
    <section class="dark" id="about"><div class="container about-grid"><div><span class="eyebrow">Our Background</span><h2><span data-years-combined="2010,2006">36</span> years. <span data-years-since="2010">16</span> of them in the dirt.</h2><div class="stats"><div class="stat"><strong><span data-years-combined="2010,2006">36</span></strong><span>Combined years of experience</span></div><div class="stat"><strong><span data-years-since="2010">16</span></strong><span>Years of firsthand field experience</span></div></div></div><div><p>Our combined experience spans blueprint takeoff, civil consulting, new civil and building-trades contract reporting, Civil 3D grade-control modeling, machine grade control, and survey-equipment utilization and support.</p><p><span data-years-word="2010">Sixteen</span> of those years were spent firsthand with boots in the dirt — operating equipment, managing work, and using machine-control and survey equipment before moving into 3D CAD design.</p><p>That background matters. We use real field experience to optimize processing, modeling, and technology workflows so project information is not only accurate in the office, but practical and useful where the work is actually happening.</p><div class="experience"><div>Blueprint Takeoff</div><div>Civil Consulting</div><div>Civil &amp; Building-Trades Contract Reporting</div><div>Civil 3D Grade-Control Modeling</div><div>Machine Grade Control</div><div>Survey Equipment Support</div></div></div></div></section>
    <section class="area" id="service-area"><div class="container"><span class="eyebrow">Coverage</span><h2>Local support. Statewide reach.</h2><p class="lead">Based in Mid-Michigan, we serve civil construction teams across the Tri-City area and provide remote support throughout Michigan.</p><div class="area-grid"><div class="area-card"><h3>Local service area</h3><p>Saginaw, Bay City, Midland, and surrounding Mid-Michigan civil-construction markets.</p></div><div class="area-card"><h3>Remote support statewide</h3><p>Remote support is available anywhere in Michigan for field mapping, GIS workflows, grade-control coordination, and construction-technology needs.</p></div></div></div></section>
{CTA}'''

contact=f'''    <section class="page-hero"><div class="container"><span class="eyebrow">Contact Us Today</span><h1>Let's make your <span>site data work harder.</span></h1><p>Whether you want to explore FieldSight or need help with a civil construction technology workflow, reach out to discuss the job and the practical path forward.</p></div></section>
    <section><div class="container"><div class="contact-cards"><div class="contact-card"><small>Email</small><a class="big" href="mailto:{EMAIL}">{EMAIL}</a><p>Best for quote requests, plans, and project files.</p></div><div class="contact-card"><small>Send your files</small><span class="big">Plans &amp; project data</span><p>Attach plans, CAD/DXF, LandXML, surfaces, or control points to your email.</p></div><div class="contact-card"><small>Service area</small><span class="big">Saginaw • Bay City • Midland</span><p>Remote support available statewide across Michigan.</p></div></div></div></section>
    <section class="area"><div class="container story"><div><span class="eyebrow">Request a quote</span><h2>What to include in your request.</h2><p class="lead">A few details up front help us give you a faster, more accurate answer.</p><a class="button" style="margin-top:26px" href="{QUOTE}">Email a Quote Request</a></div><ul class="checklist"><li>Project name and location</li><li>Type of work: grade-control modeling, field mapping, FieldSight, or support</li><li>Available files: plans, CAD/DXF, LandXML, surfaces, or control points</li><li>Coordinate system or project datum, if known</li><li>Schedule or needed-by date</li><li>Your name, company, and the best way to reach you</li></ul></div></section>'''

pages={"index.html":("/","Great Lakes SiteLogic | Civil Construction Technology","Civil construction technology for Michigan contractors: grade control, Civil 3D modeling, takeoffs &amp; GIS. Serving Saginaw, Bay City &amp; Midland. Email info@greatlakessitelogic.com.",home),
"about.html":("/about","About | Great Lakes SiteLogic","Family-owned, Mid-Michigan civil construction technology company with {{yrscombined:2010,2006}} years of combined experience.",about),
"products.html":("/products","FieldSight | Great Lakes SiteLogic","FieldSight by Great Lakes SiteLogic: phone-first field mapping with DXF plan import, CAD editing, and Trimble, Emlid and Bad Elf GNSS support. Works with Trimble. Works without it. Now in closed beta on Google Play.",products),
"contact.html":("/contact","Contact Us | Great Lakes SiteLogic","Contact Great Lakes SiteLogic for a quote. Serving Saginaw, Bay City, Midland, and remote support statewide.",contact)}

def inline(t):
    t=html.escape(t,quote=False)
    t=re.sub(r"\*\*(.+?)\*\*",r"<strong>\1</strong>",t)
    t=re.sub(r"\[(.+?)\]\((.+?)\)",r'<a href="\2">\1</a>',t)
    t=t.replace("Mid-Michigan","Mid&#8209;Michigan")
    return _yrs_span(t.replace("info@greatlakessitelogic.com",f'<a href="{QUOTE}">{EMAIL}</a>'))
services=[]
def render(src):
    lines=src.split("---",1)[1].strip().splitlines()
    h1=lines[0][2:]; intro=[];secs=[];cur=None
    for ln in lines[1:]:
        if ln.startswith("## "): cur={"h":ln[3:],"b":[]}; secs.append(cur)
        elif ln.startswith("### "): cur["b"].append(("q",ln[4:]))
        elif ln.startswith("- "): cur["b"].append(("li",ln[2:]))
        elif re.match(r"\d+\. ",ln): cur["b"].append(("ol",re.sub(r"^\d+\. ","",ln)))
        elif ln.strip(): (cur["b"].append(("p",ln)) if cur else intro.append(ln))
    return h1,intro,secs
def blocks(b):
    out="";faq=[];i=0
    while i<len(b):
        k,v=b[i]
        if k in("li","ol"):
            items=[]
            while i<len(b) and b[i][0]==k: items.append(b[i][1]); i+=1
            out+=('<ul class="checklist">'+"".join(f"<li>{inline(x)}</li>" for x in items)+"</ul>") if k=="li" else ('<ol class="steps">'+"".join(f"<li>{inline(x)}</li>" for x in items)+"</ol>")
            continue
        if k=="q":
            a=b[i+1][1] if i+1<len(b) and b[i+1][0]=="p" else ""
            faq.append((v,a)); out+=f'<details class="faq"><summary>{inline(v)}</summary><p>{inline(a)}</p></details>'; i+=2; continue
        out+=f'<p class="lead">{inline(v)}</p>'; i+=1
    return out,faq
raw=[]
for f in sorted(glob.glob("content/*-page.md")):
    src=open(f).read()
    slugv=re.search(r"slug:\*\* `/(.+?)`",src).group(1)
    raw.append((f,src,slugv,src.splitlines()[0][2:].strip()))
for f,src,slugv,name in raw:
    mt=re.search(r"Meta title:\*\* (.+)",src).group(1).strip()
    md=re.search(r"Meta description:\*\* (.+)",src).group(1).strip()
    h1,intro,secs=render(src)
    out=f'    <section class="page-hero"><div class="container"><span class="eyebrow">Services</span><h1>{inline(h1)}</h1><p>{inline(intro[0])}</p></div></section>\n    <section><div class="container svc-body">'
    faqs=[]
    for c in secs[:-1]:
        html_b,fq=blocks(c["b"]); faqs+=fq
        out+=f'<div class="svc-sec"><h2>{inline(c["h"])}</h2>{html_b}</div>'
    rel="".join(f'<a class="card" href="/{u}"><h3>{html.escape(n)}</h3><span class="more">Learn more</span></a>' for _,_,u,n in raw if u!=slugv)
    out+=f'</div></section>\n    <section class="area"><div class="container"><span class="eyebrow">Related services</span><h2>More ways we can help.</h2><div class="cards rel">{rel}</div></div></section>'
    c=secs[-1]
    out+='\n    <section class="cta-band"><div class="container"><div><h2>'+inline(c["h"])+'</h2>'+"".join(f"<p>{inline(v)}</p>" for k,v in c["b"])+f'</div><a class="button navy" href="{QUOTE}">Email Us</a></div></section>'
    if faqs:
        fs={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":_yrs_plain(q),"acceptedAnswer":{"@type":"Answer","text":_yrs_plain(a)}} for q,a in faqs]}
        out+='\n    <script type="application/ld+json">'+json.dumps(fs)+'</script>'
    pages[slugv+".html"]=("/svc:"+slugv,mt,html.escape(md),out)
    services.append((slugv,name,intro[0]))
cards="".join(f'<a class="card" href="/{u}"><h3>{html.escape(n)}</h3><p>{html.escape(re.split(r"(?<=\.) ",d)[0])}</p><span class="more">Learn more</span></a>' for u,n,d in services)
svc=f'''    <section class="page-hero"><div class="container"><span class="eyebrow">Services</span><h1>Civil construction technology <span>services in Mid-Michigan.</span></h1><p>Takeoffs, Civil 3D modeling, machine grade control, survey equipment support, field mapping, site technology consulting, GNSS and crew development, construction advisement, project management, design consulting, and pre-construction consulting for contractors in Saginaw, Bay City, Midland, and statewide.</p></div></section>
    <section><div class="container"><div class="cards">{cards}</div></div></section>
{CTA}'''
pages["services.html"]=("/services","Services | Great Lakes SiteLogic","Blueprint takeoff, Civil 3D grade-control modeling, machine grade control, survey equipment support, field mapping &amp; GIS, site technology consulting, GNSS training, construction advisement, project management, design consulting, and pre-construction consulting for Michigan contractors.",svc)
for f,(slug,t,d,b) in pages.items(): open(f,"w").write(page(slug,t,d,b))
print("built",list(pages))

# sitemap.xml + robots.txt
import datetime
BASE="https://greatlakessitelogic.com"
today=datetime.date.today().isoformat()
def loc(f): return BASE+("/" if f=="index.html" else "/"+f[:-5])
pri={"index.html":"1.0","services.html":"0.9","contact.html":"0.8"}
urls="".join(f"  <url><loc>{loc(f)}</loc><lastmod>{today}</lastmod><priority>{pri.get(f,'0.8' if 'michigan' in f else '0.6')}</priority></url>\n" for f in pages)
open("sitemap.xml","w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
open("robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
