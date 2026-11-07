# Ferme Roberge-Innov — site vitrine

Site statique (HTML, CSS et JavaScript, sans framework ni étape de build) qui présente les produits de la **Ferme Roberge-Innov** (177, rang de la Grande-Ligne, Saint-Isidore). Il a été construit à partir de la page Facebook publique de la ferme.

- **48 produits**, **9 catégories**, **100 photos** en résolution d’origine
- Accueil avec recherche, filtres par catégorie et par prix, et tri
- Une page par produit, avec galerie, prix, description et bouton de commande Messenger
- Page Infos : adresse, horaires, coordonnées et modes de paiement

## Voir le site

Ouvrez `index.html` dans un navigateur : le site fonctionne directement depuis le disque.

Pour le mettre en ligne avec GitHub Pages : *Settings → Pages → Deploy from a branch → `main` / root*. N’importe quel hébergeur statique fonctionne aussi (Netlify, Cloudflare Pages, etc.), sans configuration.

## Structure

```
index.html, infos.html, produits/<id>.html   pages générées
css/style.css, js/app.js                      style et interactivité
data/business.json                            infos de l’entreprise
data/products.json                            catalogue (source de vérité)
data/products.js                              copie de products.json pour le navigateur (générée)
data/missing-data.md                          données manquantes ou à vérifier
assets/products/<id>/01.jpg, 02.jpg, …         photos originales ; thumb.jpg = vignette 800 px
assets/logo.png, assets/favicon.png, assets/brand/
build-log.md                                  journal d’extraction (source de chaque produit)
tools/build.py                                régénère les pages à partir des données
```

## Modifier un produit ou un prix

1. Modifiez `data/products.json`. Pour un produit sans prix, laissez `"price": null` : le site affiche alors « Prix sur demande ».
2. Pour un nouveau produit, ajoutez ses photos dans `assets/products/<id>/` (01.jpg, 02.jpg, …) et une vignette `thumb.jpg`.
3. Lancez `python3 tools/build.py` (Python 3, aucune dépendance) pour régénérer les pages.

Une fois le site publié, indiquez son adresse dans `SITE_URL` (en haut de `tools/build.py`), puis relancez le script : les balises canoniques et Open Graph utiliseront des URL absolues.

Les prix sont en dollars canadiens, taxes incluses.
