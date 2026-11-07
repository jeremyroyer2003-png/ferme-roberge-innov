#!/usr/bin/env python3
"""Génère les pages HTML du site à partir de data/products.json et data/business.json.

Le site livré est 100 % statique : ce script n'est PAS nécessaire pour l'afficher.
Il sert seulement à régénérer les pages après une modification des données :

    python3 tools/build.py

Aucune dépendance externe (Python 3.8+).
"""
import html
import json
import os
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = ""  # ex. "https://jeremyroyer2003-png.github.io/ferme-roberge-innov/" une fois publié

with open(os.path.join(ROOT, "data", "products.json"), encoding="utf-8") as f:
    PRODUCTS = json.load(f)
with open(os.path.join(ROOT, "data", "business.json"), encoding="utf-8") as f:
    BIZ = json.load(f)

E = html.escape


def money(v):
    s = f"{v:,.2f}".replace(",", " ").replace(".", ",")
    return s + " $"


def price_html(p):
    if p.get("price") is None:
        return '<span class="price-ask">Prix sur demande</span>'
    s = money(p["price"])
    if p.get("price_prefix"):
        s = p["price_prefix"] + " " + s
    if p.get("price_unit"):
        s += " / " + p["price_unit"]
    return E(s)


def price_text(p):
    if p.get("price") is None:
        return "Prix sur demande"
    s = money(p["price"])
    if p.get("price_unit"):
        s += " / " + p["price_unit"]
    return s


# ---------------------------------------------------------------- CTA ----
PHONE = BIZ.get("phone") or ""
PHONE_TEL = "+1" + "".join(c for c in PHONE if c.isdigit()) if PHONE else ""
MESSENGER = BIZ.get("messenger_url") or ""
FB = BIZ.get("socials", {}).get("facebook") or ""

ICON_MSG = ('<svg aria-hidden="true" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.36 2 2 6.13 2 11.7c0 2.91 '
            '1.19 5.44 3.14 7.17V22l3.04-1.67c.86.24 1.76.37 2.82.37 5.64 0 10-4.13 10-9.7S17.64 2 12 2zm1 13.06-2.55-2.72'
            '-4.97 2.72 5.47-5.8 2.6 2.72 4.92-2.72-5.47 5.8z"/></svg>')
ICON_TEL = ('<svg aria-hidden="true" viewBox="0 0 24 24" fill="currentColor"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3'
            '.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 '
            '2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2z"/></svg>')


def cta_primary(label="Commander sur Messenger"):
    return f'<a class="btn" href="{E(MESSENGER)}" target="_blank" rel="noopener" aria-label="{E(label)} (ouvre Messenger)">{ICON_MSG}<span class="btn-label">{E(label)}</span></a>'


def cta_phone():
    return f'<a class="btn btn-ghost" href="tel:{E(PHONE_TEL)}">{ICON_TEL}{E(PHONE)}</a>'


# -------------------------------------------------------------- Gabarit ----
def page(*, title, description, body, base, canonical_path, og_image=None, og_type="website",
         current=None, jsonld=None, extra_scripts=""):
    og_img = (SITE_URL + og_image) if (SITE_URL and og_image) else (og_image and base + og_image)
    canon = f'<link rel="canonical" href="{E(SITE_URL + canonical_path)}">' if SITE_URL else ""
    nav = []
    for href, label, key, cls in (("index.html", "Produits", "home", "nav-home"), ("infos.html", '<span class="lbl-lg">Infos &amp; horaires</span><span class="lbl-sm">Infos</span>', "info", "")):
        cur = ' aria-current="page"' if current == key else ""
        nav.append(f'<a class="{cls}" href="{base}{href}"{cur}>{label}</a>' if cls else f'<a href="{base}{href}"{cur}>{label}</a>')
    ld = f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>' if jsonld else ""
    addr = BIZ.get("address", {})
    addr_line = ", ".join(x for x in (addr.get("street"), addr.get("city"), addr.get("postal_code")) if x)
    return f"""<!DOCTYPE html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(description)}">
{canon}
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="fr_CA">
<meta property="og:site_name" content="{E(BIZ['name'])}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(description)}">
{f'<meta property="og:image" content="{E(og_img)}">' if og_img else ''}
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2f5d3a">
<link rel="icon" href="{base}assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{base}assets/favicon.png">
<link rel="stylesheet" href="{base}css/style.css">
{ld}
</head>
<body>
<a class="skip-link" href="#contenu">Aller au contenu</a>
<header class="site-header">
  <div class="container">
    <a class="brand" href="{base}index.html"><img src="{base}assets/logo.png" alt="" width="40" height="40">{E(BIZ['name'])}</a>
    <nav class="nav" aria-label="Navigation principale">{''.join(nav)}</nav>
    {cta_primary("Commander")}
  </div>
</header>
<main id="contenu">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h2>{E(BIZ['name'])}</h2>
        <p>{E(addr_line)}<br>Kiosque libre-service ouvert 24/7</p>
        <p>{cta_primary()}</p>
      </div>
      <div>
        <h2>Nous joindre</h2>
        <p><a href="tel:{E(PHONE_TEL)}">{E(PHONE)}</a> (appel ou texto)<br>
        <a href="mailto:{E(BIZ.get('email') or '')}">{E(BIZ.get('email') or '')}</a></p>
      </div>
      <div>
        <h2>Suivez-nous</h2>
        <ul class="socials"><li><a href="{E(FB)}" target="_blank" rel="noopener">Facebook</a></li></ul>
        <p><a href="{base}infos.html">Infos & horaires</a></p>
      </div>
    </div>
    <p class="footer-bottom">© {E(BIZ['name'])}. Photos et informations tirées de la page Facebook de la ferme. Prix taxes incluses ; ils peuvent changer selon la saison et les arrivages.</p>
  </div>
</footer>
<script src="{base}js/app.js" defer></script>
{extra_scripts}
</body>
</html>
"""


# ------------------------------------------------------------- Accueil ----
def build_home():
    b = BIZ
    addr = b.get("address", {})
    jsonld = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": b["name"],
        "description": b.get("about"),
        "telephone": b.get("phone"),
        "email": b.get("email"),
        "image": "assets/brand/cover.jpg",
        "logo": "assets/logo.png",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": addr.get("street"),
            "addressLocality": addr.get("city"),
            "postalCode": addr.get("postal_code"),
            "addressRegion": addr.get("region"),
            "addressCountry": "CA",
        },
        "sameAs": [v for v in b.get("socials", {}).values() if v],
        "makesOffer": [
            {"@type": "Offer", "itemOffered": {"@type": "Product", "name": p["name"]},
             **({"price": p["price"], "priceCurrency": "CAD"} if p.get("price") is not None else {})}
            for p in PRODUCTS
        ],
    }
    if b.get("opening_hours_schema"):
        jsonld["openingHours"] = b["opening_hours_schema"]
    jsonld["address"] = {k: v for k, v in jsonld["address"].items() if v}

    body = f"""
<section class="hero" aria-labelledby="titre-accueil">
  <img class="hero-img" src="assets/brand/cover.jpg" alt="Photo de couverture de la {E(b['name'])}" width="1640" height="924" fetchpriority="high">
  <div class="container hero-body">
    <h1 id="titre-accueil">{E(b['name'])}</h1>
    <p>{E(b.get('about') or '')}</p>
    <p class="hero-meta"><span>{E(b.get('category') or '')}</span><span>{E(addr.get('street') or '')}{(', ' + E(addr['city'])) if addr.get('city') else ''}</span><span>Kiosque libre-service 24/7</span></p>
    <p class="product-actions">{cta_primary()}{cta_phone()}</p>
  </div>
</section>
<section class="catalog container" aria-labelledby="titre-produits">
  <h2 id="titre-produits">Nos produits</h2>
  <p class="note">Les produits suivent les saisons : certains ne sont offerts qu'une partie de l'année. Écrivez-nous pour vérifier la disponibilité ou réserver.</p>
  <div class="toolbar">
    <div class="field"><label for="q">Rechercher</label><input id="q" type="search" placeholder="ex. popcorn, pivoine, poulet…" autocomplete="off"></div>
    <div class="field"><span id="prix-label" class="label" style="display:block;font-size:.85rem;font-weight:600;color:var(--muted);margin-bottom:.25rem">Prix ($)</span>
      <div class="price-range" role="group" aria-labelledby="prix-label">
        <label class="visually-hidden" for="pmin">Prix minimum</label><input id="pmin" type="number" inputmode="decimal" min="0" step="0.5" placeholder="min">
        <span aria-hidden="true">–</span>
        <label class="visually-hidden" for="pmax">Prix maximum</label><input id="pmax" type="number" inputmode="decimal" min="0" step="0.5" placeholder="max">
      </div></div>
    <div class="field"><label for="sort">Trier par</label>
      <select id="sort"><option value="newest">Plus récents</option><option value="price-asc">Prix croissant</option><option value="price-desc">Prix décroissant</option><option value="name">Nom (A–Z)</option></select></div>
  </div>
  <div class="chips" id="chips" role="group" aria-label="Filtrer par catégorie"></div>
  <p class="result-count" id="result-count" aria-live="polite"></p>
  <ul class="grid" id="catalog-grid" data-base="">
    {''.join(card_html(p, '', i) for i, p in enumerate(sorted(PRODUCTS, key=lambda p: p.get('date') or '', reverse=True)))}
  </ul>
  <noscript><p class="note">Activez JavaScript pour filtrer et trier les produits.</p></noscript>
</section>
"""
    html_ = page(title=f"{b['name']} — Produits de la ferme", description=(b.get("about") or "")[:155],
                 body=body, base="", canonical_path="index.html", og_image="assets/brand/cover.jpg",
                 current="home", jsonld=jsonld,
                 extra_scripts='<script src="data/products.js"></script>')
    # products.js doit être chargé avant app.js (defer) : on l'insère avant.
    html_ = html_.replace('<script src="js/app.js" defer></script>\n<script src="data/products.js"></script>',
                          '<script src="data/products.js"></script>\n<script src="js/app.js" defer></script>')
    write("index.html", html_)


def card_html(p, base, i):
    img = p.get("thumb") or (p["images"][0] if p["images"] else "")
    lazy = ' loading="lazy"' if i > 3 else ""
    return (f'<li><article class="card"><img class="card-img" src="{base}{E(img)}" alt="{E(p["name"])}" width="600" height="450"{lazy} decoding="async">'
            f'<div class="card-body"><span class="card-cat">{E(p["category"])}</span>'
            f'<h3><a href="{base}produits/{E(p["id"])}.html">{E(p["name"])}</a></h3>'
            f'<p class="card-price">{price_html(p)}</p><span class="card-more" aria-hidden="true">Voir les détails →</span></div></article></li>')


# ------------------------------------------------------- Pages produit ----
def build_product(p):
    base = "../"
    imgs = p["images"]
    main = imgs[0]
    thumbs = ""
    if len(imgs) > 1:
        items = []
        for k, im in enumerate(imgs):
            alt = f'{p["name"]} — photo {k + 1} sur {len(imgs)}'
            items.append(
                f'<li><button type="button" data-full="{base}{E(im)}" data-alt="{E(alt)}" aria-current="{"true" if k == 0 else "false"}" '
                f'aria-label="Afficher la photo {k + 1}"><img src="{base}{E(im)}" alt="" width="72" height="72" loading="lazy"></button></li>')
        thumbs = f'<ul class="thumbs" aria-label="Autres photos">{"".join(items)}</ul>'
    related = [q for q in PRODUCTS if q["category"] == p["category"] and q["id"] != p["id"]][:4]
    if len(related) < 2:
        related += [q for q in PRODUCTS if q["id"] != p["id"] and q not in related][: 4 - len(related)]
    rel_html = "".join(card_html(q, base, 9) for q in related)
    note = f'<p class="note">{E(p["notes"])}</p>' if p.get("notes_public") else ""
    breadcrumb = (f'<nav class="breadcrumb container" aria-label="Fil d’Ariane"><ol>'
                  f'<li><a href="{base}index.html">Accueil</a></li><li>{E(p["category"])}</li>'
                  f'<li aria-current="page">{E(p["name"])}</li></ol></nav>')
    body = f"""{breadcrumb}
<div class="container">
  <p><a href="{base}index.html">← Retour aux produits</a></p>
  <article class="product">
    <div class="gallery">
      <div class="gallery-main"><img id="gallery-main-img" src="{base}{E(main)}" alt="{E(p['name'])}" width="1536" height="2048" fetchpriority="high"></div>
      {thumbs}
    </div>
    <div class="product-info">
      <span class="card-cat">{E(p['category'])}</span>
      <h1>{E(p['name'])}</h1>
      <p class="price">{price_html(p)}</p>
      <div class="desc">{E(p['description'])}</div>
      {note}
      <p class="product-actions">{cta_primary()}{cta_phone()}</p>
      <p class="note">Produit disponible au kiosque libre-service, 177, Rang de la Grande-Ligne, selon la saison et les arrivages.</p>
    </div>
  </article>
</div>
<section class="related container" aria-labelledby="titre-autres">
  <h2 id="titre-autres">Vous aimerez aussi</h2>
  <ul class="grid">{rel_html}</ul>
</section>
"""
    desc = (p["description"] or p["name"]).replace("\n", " ")
    desc = (desc[:150] + "…") if len(desc) > 155 else desc
    jsonld = {"@context": "https://schema.org", "@type": "Product", "name": p["name"], "category": p["category"],
              "description": p["description"], "image": [base + i for i in imgs],
              "brand": {"@type": "Brand", "name": p.get("brand") or BIZ["name"]}}
    if p.get("price") is not None:
        jsonld["offers"] = {"@type": "Offer", "price": p["price"], "priceCurrency": "CAD",
                            "seller": {"@type": "LocalBusiness", "name": BIZ["name"]}}
    write(f"produits/{p['id']}.html",
          page(title=f"{p['name']} — {price_text(p)} | {BIZ['name']}", description=desc, body=body, base=base,
               canonical_path=f"produits/{p['id']}.html", og_image=main, og_type="product", jsonld=jsonld))


# ----------------------------------------------------------- Page infos ----
def build_info():
    b = BIZ
    a = b.get("address", {})
    osm_q = quote(", ".join(x for x in (a.get("street"), a.get("city"), a.get("postal_code"), "Québec", "Canada") if x))
    if b.get("lat") and b.get("lng"):
        osm = f"https://www.openstreetmap.org/?mlat={b['lat']}&mlon={b['lng']}#map=16/{b['lat']}/{b['lng']}"
    else:
        osm = f"https://www.openstreetmap.org/search?query={osm_q}"
    rows = "".join(f"<tr><th scope=\"row\">{E(h['days'])}</th><td>{E(h['hours'])}</td></tr>" for h in b.get("hours", []))
    hours_note = E(b.get("hours_note") or "")
    pay = "".join(f"<li>{E(x)}</li>" for x in b.get("payment_delivery_notes", []))
    body = f"""
<div class="container"><h1 style="margin-top:1.4rem">Infos & horaires</h1></div>
<div class="container info">
  <section class="panel" aria-labelledby="t-adresse">
    <h2 id="t-adresse">Adresse</h2>
    <p>{E(a.get('street') or '')}<br>{E(a.get('city') or '')} {E(a.get('postal_code') or '')}</p>
    <p><a href="{E(osm)}" target="_blank" rel="noopener">Voir sur OpenStreetMap</a></p>
  </section>
  <section class="panel" aria-labelledby="t-heures">
    <h2 id="t-heures">Heures d’ouverture</h2>
    <table><caption class="visually-hidden">Heures d’ouverture du kiosque</caption><tbody>{rows}</tbody></table>
    <p class="note" style="margin-top:.8rem">{hours_note}</p>
  </section>
  <section class="panel" aria-labelledby="t-contact">
    <h2 id="t-contact">Nous joindre</h2>
    <dl>
      <dt>Téléphone</dt><dd><a href="tel:{E(PHONE_TEL)}">{E(PHONE)}</a> (appel ou texto)</dd>
      <dt>Courriel</dt><dd><a href="mailto:{E(b.get('email') or '')}">{E(b.get('email') or '')}</a></dd>
      <dt>Messenger</dt><dd><a href="{E(MESSENGER)}" target="_blank" rel="noopener">Écrire à la ferme</a></dd>
      <dt>Site web</dt><dd>{E(b.get('website') or 'Aucun autre site indiqué')}</dd>
    </dl>
  </section>
  <section class="panel" aria-labelledby="t-commande">
    <h2 id="t-commande">Commandes et paiement</h2>
    <ul>{pay}</ul>
  </section>
  <section class="panel" aria-labelledby="t-apropos" style="grid-column:1/-1">
    <h2 id="t-apropos">À propos</h2>
    <p>{E(b.get('about') or '')}</p>
    {''.join(f'<p>{E(x)}</p>' for x in b.get('about_more', []))}
    <p>Réseaux sociaux : <a href="{E(FB)}" target="_blank" rel="noopener">Facebook</a></p>
  </section>
</div>
"""
    write("infos.html", page(title=f"Infos, adresse et horaires — {b['name']}",
                             description=f"Adresse, heures d’ouverture du kiosque et coordonnées de la {b['name']}.",
                             body=body, base="", canonical_path="infos.html", og_image="assets/brand/cover.jpg",
                             current="info"))


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def build_data_js():
    keep = ("id", "name", "category", "price", "price_raw", "price_prefix", "price_unit", "currency",
            "description", "images", "thumb", "date")
    slim = [{k: p.get(k) for k in keep} for p in PRODUCTS]
    write("data/products.js", "/* Généré par tools/build.py à partir de products.json — ne pas modifier à la main. */\n"
          "window.PRODUCTS = " + json.dumps(slim, ensure_ascii=False, indent=1) + ";\n")


if __name__ == "__main__":
    build_data_js()
    build_home()
    for p in PRODUCTS:
        build_product(p)
    build_info()
    print(f"{len(PRODUCTS)} pages produit + accueil + infos générées.")
