# Generates the site pages from shared header/footer. Run: python3 build.py
import re
EMAIL="info@greatlakessitelogic.com"; PHONE_T="+19897802592"; PHONE="(989) 780-2592"
QUOTE=f"mailto:{EMAIL}?subject=Great%20Lakes%20SiteLogic%20Quote%20Request"
NAV=[("/","Home"),("/services","Services"),("/about","About"),("/products","Products")]
import json,glob,html
SCHEMA=open("content/schema.json").read().strip()
def page(slug,title,desc,body):
    links="".join(f'<a href="{h}"{" class=\"active\"" if h==slug else ""}>{t}</a>' for h,t in NAV)
    cta_cls="button active" if slug=="/contact" else "button"
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="{desc}" />
  <link rel="icon" type="image/png" href="/assets/favicon.png" />
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="https://greatlakessitelogic.com/assets/logo.png" />
  <meta name="theme-color" content="#0c2340" />
  <title>{title}</title>
  <link rel="stylesheet" href="/assets/styles.css?v=4" />
  <script type="application/ld+json">{SCHEMA}</script>
</head>
<body>
  <nav id="nav"><div class="container navin"><a class="brand" href="/" aria-label="Great Lakes SiteLogic home"><img class="brand-logo" src="/assets/logo.png" width="1697" height="540" alt="Great Lakes SiteLogic" /></a><div class="navlinks" id="navlinks">{links}<a class="{cta_cls}" href="/contact">Contact Us Today</a></div><button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="navlinks" onclick="var n=document.getElementById('nav');var o=n.classList.toggle('open');this.setAttribute('aria-expanded',o);this.textContent=o?'✕':'☰'">☰</button></div></nav>
  <main id="top">
{body}
  </main>
  <footer><div class="container foot"><span><b>Great Lakes SiteLogic, LLC</b> — Civil Construction Technology</span><span>Email us: <a href="mailto:{EMAIL}">{EMAIL}</a></span><span>© 2026 Great Lakes SiteLogic. All rights reserved.</span></div></footer>
</body>
</html>
'''
CTA=f'''    <section class="cta-band"><div class="container"><div><h2>Ready to talk about your project?</h2><p>Local support in Saginaw, Bay City &amp; Midland. Remote support statewide.</p></div><a class="button navy" href="/contact">Contact Us Today</a></div></section>'''

home=f'''    <section class="hero"><div class="container"><div class="hero-copy"><span class="eyebrow">Mid-Michigan Civil Technology</span><h1>Civil Construction Technology &amp; <span>Machine Grade Control in Mid&#8209;Michigan</span></h1><p class="tagline">Site technology built from the dirt up.</p><p>Practical field mapping, GIS, grade-control workflows, and construction technology support for teams that need the plan to work where the work happens.</p><div class="hero-actions"><a class="button" href="/products">Explore FieldSight</a><a class="button outline" href="/contact">Contact Us Today</a></div><div class="service-line"><strong>Local support:</strong> Saginaw, Bay City &amp; Midland &nbsp;|&nbsp; <strong>Remote support:</strong> Available statewide across Michigan</div></div></div></section>
    <section><div class="container"><span class="eyebrow">What We Do</span><h2>Field experience, built into every workflow.</h2><p class="lead">Great Lakes SiteLogic is a family-owned, Mid-Michigan company helping contractors and project teams get better information from takeoff through construction.</p><div class="cards"><a class="card" href="/products"><h3>FieldSight</h3><p>A field-mapping and GIS app that puts project data, GNSS positioning, and design references in the hands of the crew on site.</p><span class="more">See the product</span></a><a class="card" href="/about"><h3>Our Experience</h3><p>36 combined years across takeoff, civil consulting, contract reporting, Civil 3D grade-control modeling, and machine control — 16 of them boots in the dirt.</p><span class="more">About us</span></a><a class="card" href="/contact"><h3>Get Support</h3><p>Local service in Saginaw, Bay City, and Midland, with remote support available anywhere in Michigan.</p><span class="more">Contact us today</span></a></div></div></section>
    <section class="dark"><div class="container about-grid"><div><span class="eyebrow">By the numbers</span><h2>Mid-Michigan built. Field-tested.</h2><div class="stats"><div class="stat"><strong>36</strong><span>Combined years of experience</span></div><div class="stat"><strong>16</strong><span>Years of firsthand field experience</span></div></div></div><div><p class="lead">We don't approach models, maps, or workflows as office-only deliverables. Every process is built with the operator, foreman, layout crew, superintendent, and project manager in mind.</p><div class="experience"><div>Blueprint Takeoff</div><div>Civil Consulting</div><div>Civil 3D Grade-Control Modeling</div><div>Machine Grade Control</div><div>Survey Equipment Support</div><div>Field Mapping &amp; GIS</div></div></div></div></section>
{CTA}'''

feat=[("Live field positioning","Use GNSS-capable mobile devices to see your position and orient yourself on the jobsite."),("Project data overlays","Bring project information into one visual workspace instead of chasing paper plans, screenshots, texts, and separate map apps."),("Civil file support","Work with common construction and mapping files, including CSV, GeoJSON, KML, XML, and DXF."),("Coordinate-aware workflows","Built with civil coordinate systems in mind, including local and State Plane-based project workflows."),("Office-to-field visibility","Give crews a clearer view of control, boundaries, utilities, design references, and field observations."),("Mobile-first usability","Designed for walking a site, checking layout, verifying conditions, and communicating locations quickly.")]
feats="".join(f'<div class="feature"><span class="num">{i+1:02d}</span><b>{a}</b><p>{b}</p></div>' for i,(a,b) in enumerate(feat))
products=f'''    <section class="page-hero"><div class="container"><span class="eyebrow">Products</span><h1>FieldSight: <span>the jobsite, in your hand.</span></h1><p>A field-mapping and GIS application built for civil construction crews, site-layout teams, and project managers.</p></div></section>
    <section id="fieldsight"><div class="container"><div class="split"><div><div class="product-panel"><span class="product-tag">Construction Field Mapping</span><h2>FieldSight</h2><p>Put the right information in the hands of the people doing the work. FieldSight brings project data, mapping, and location awareness into a mobile-friendly workspace so crews can reference the site while they are standing on it.</p><div class="video-frame"><video controls autoplay muted loop playsinline preload="metadata"><source src="/assets/fieldsight_short.mp4" type="video/mp4">Your browser does not support the video tag.</video></div></div></div><div><h2>Built for practical site workflows.</h2><p class="lead">FieldSight reduces the gap between the office, the model, and the field — turning disconnected files and location data into a clearer jobsite view.</p><div class="features">{feats}</div></div></div></div></section>
    <section class="area"><div class="container story"><div><span class="eyebrow">Why FieldSight exists</span><h2>Critical site information shouldn't be stuck in the office.</h2></div><div><p>The jobsite moves fast, but key information is often trapped inside a CAD file, buried in a text message, or spread across disconnected tools.</p><p>FieldSight was built to close that gap. The focus isn't technology for its own sake — it's giving crews a straightforward way to see where they are, understand what's around them, and make better field decisions.</p><p>FieldSight is actively evolving through real-world construction feedback, with the goal of a dependable workflow for importing project information, reviewing it in the field, and improving office-to-field communication.</p></div></div></section>
{CTA}'''

about=f'''    <section class="page-hero"><div class="container"><span class="eyebrow">About Us</span><h1>Mid-Michigan built. <span>Field-tested experience.</span></h1><p>Family owned and operated, bringing civil construction knowledge and practical technology together for contractors and project teams.</p></div></section>
    <section class="dark" id="about"><div class="container about-grid"><div><span class="eyebrow">Our Background</span><h2>36 years. 16 of them in the dirt.</h2><div class="stats"><div class="stat"><strong>36</strong><span>Combined years of experience</span></div><div class="stat"><strong>16</strong><span>Years of firsthand field experience</span></div></div></div><div><p>Our combined experience spans blueprint takeoff, civil consulting, new civil and building-trades contract reporting, Civil 3D grade-control modeling, machine grade control, and survey-equipment utilization and support.</p><p>Sixteen of those years were spent firsthand with boots in the dirt — operating equipment, managing work, and using machine-control and survey equipment before moving into 3D CAD design.</p><p>That background matters. We use real field experience to optimize processing, modeling, and technology workflows so project information is not only accurate in the office, but practical and useful where the work is actually happening.</p><div class="experience"><div>Blueprint Takeoff</div><div>Civil Consulting</div><div>Civil &amp; Building-Trades Contract Reporting</div><div>Civil 3D Grade-Control Modeling</div><div>Machine Grade Control</div><div>Survey Equipment Support</div></div></div></div></section>
    <section class="area" id="service-area"><div class="container"><span class="eyebrow">Coverage</span><h2>Local support. Statewide reach.</h2><p class="lead">Based in Mid-Michigan, we serve civil construction teams across the Tri-City area and provide remote support throughout Michigan.</p><div class="area-grid"><div class="area-card"><h3>Local service area</h3><p>Saginaw, Bay City, Midland, and surrounding Mid-Michigan civil-construction markets.</p></div><div class="area-card"><h3>Remote support statewide</h3><p>Remote support is available anywhere in Michigan for field mapping, GIS workflows, grade-control coordination, and construction-technology needs.</p></div></div></div></section>
{CTA}'''

contact=f'''    <section class="page-hero"><div class="container"><span class="eyebrow">Contact Us Today</span><h1>Let's make your <span>site data work harder.</span></h1><p>Whether you want to explore FieldSight or need help with a civil construction technology workflow, reach out to discuss the job and the practical path forward.</p></div></section>
    <section><div class="container"><div class="contact-cards"><div class="contact-card"><small>Email</small><a class="big" href="mailto:{EMAIL}">{EMAIL}</a><p>Best for quote requests, plans, and project files.</p></div><div class="contact-card"><small>Send your files</small><span class="big">Plans &amp; project data</span><p>Attach plans, CAD/DXF, LandXML, surfaces, or control points to your email.</p></div><div class="contact-card"><small>Service area</small><span class="big">Saginaw • Bay City • Midland</span><p>Remote support available statewide across Michigan.</p></div></div></div></section>
    <section class="area"><div class="container story"><div><span class="eyebrow">Request a quote</span><h2>What to include in your request.</h2><p class="lead">A few details up front help us give you a faster, more accurate answer.</p><a class="button" style="margin-top:26px" href="{QUOTE}">Email a Quote Request</a></div><ul class="checklist"><li>Project name and location</li><li>Type of work: grade-control modeling, field mapping, FieldSight, or support</li><li>Available files: plans, CAD/DXF, LandXML, surfaces, or control points</li><li>Coordinate system or project datum, if known</li><li>Schedule or needed-by date</li><li>Your name, company, and the best way to reach you</li></ul></div></section>'''

pages={"index.html":("/","Great Lakes SiteLogic | Civil Construction Technology","Civil construction technology for Michigan contractors: grade control, Civil 3D modeling, takeoffs &amp; GIS. Serving Saginaw, Bay City &amp; Midland. Email info@greatlakessitelogic.com.",home),
"about.html":("/about","About | Great Lakes SiteLogic","Family-owned, Mid-Michigan civil construction technology company with 36 years of combined experience.",about),
"products.html":("/products","FieldSight | Great Lakes SiteLogic","FieldSight is a field-mapping and GIS app for civil construction crews, layout teams, and project managers.",products),
"contact.html":("/contact","Contact Us | Great Lakes SiteLogic","Contact Great Lakes SiteLogic for a quote. Serving Saginaw, Bay City, Midland, and remote support statewide.",contact)}

def inline(t):
    t=html.escape(t,quote=False)
    t=re.sub(r"\*\*(.+?)\*\*",r"<strong>\1</strong>",t)
    t=re.sub(r"\[(.+?)\]\((.+?)\)",r'<a href="\2">\1</a>',t)
    t=t.replace("Mid-Michigan","Mid&#8209;Michigan")
    return t.replace("info@greatlakessitelogic.com",f'<a href="{QUOTE}">{EMAIL}</a>')
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
        fs={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
        out+='\n    <script type="application/ld+json">'+json.dumps(fs)+'</script>'
    pages[slugv+".html"]=("/svc:"+slugv,mt,html.escape(md),out)
    services.append((slugv,name,intro[0]))
cards="".join(f'<a class="card" href="/{u}"><h3>{html.escape(n)}</h3><p>{html.escape(re.split(r"(?<=\.) ",d)[0])}</p><span class="more">Learn more</span></a>' for u,n,d in services)
svc=f'''    <section class="page-hero"><div class="container"><span class="eyebrow">Services</span><h1>Civil construction technology <span>services in Mid-Michigan.</span></h1><p>Takeoffs, Civil 3D modeling, machine grade control, survey equipment support, and field mapping for contractors in Saginaw, Bay City, Midland, and statewide.</p></div></section>
    <section><div class="container"><div class="cards">{cards}</div></div></section>
{CTA}'''
pages["services.html"]=("/services","Services | Great Lakes SiteLogic","Blueprint takeoff, Civil 3D grade-control modeling, machine grade control, survey equipment support, and field mapping &amp; GIS for Michigan contractors.",svc)
for f,(slug,t,d,b) in pages.items(): open(f,"w").write(page(slug,t,d,b))
print("built",list(pages))
