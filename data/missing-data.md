# Données manquantes ou à vérifier

Tout ce qui n’est pas écrit sur la page Facebook (ou sur une étiquette visible dans une photo) est laissé vide (`null`). Rien n’a été deviné.
Source : https://www.facebook.com/profile.php?id=61561810061615 — extraction du 6 et 7 novembre 2026.

## 1. Entreprise (`data/business.json`)

| Champ | État | Où l’information devrait se trouver |
|---|---|---|
| `lat` / `lng` | **null** — aucune carte ni coordonnée sur la page | À propos > Détails (épingle de carte). Le lien OpenStreetMap du site fait une recherche par adresse. |
| `website` | **null** — aucun site web indiqué | À propos > Coordonnées |
| `reviews` | **null** — aucun onglet Avis/Recommandations visible | Onglet « Avis » de la page |
| `hours` | Pas d’heures dans la section À propos. Les horaires affichés (kiosque 24/7, activités d’automne, autocueillette) viennent des **publications**. | À propos > Détails > Heures d’ouverture |
| `address.city` | « Saint-Isidore » vient des publications ; la section À propos donne seulement la rue et le code postal. | À propos > Détails > Adresse |
| `price_range_raw` | **Ambigu** : Facebook affiche « €€ » (symbole euro automatique), sans montant. Non utilisé sur le site. | — |
| `messenger_url` | `https://m.me/61561810061615` construit à partir de l’identifiant de la page : **à tester** depuis un téléphone. | Bouton « Message » de la page |
| Réseaux sociaux | Seulement Facebook. Le compte Instagram `ferme_roberge_innov` est cité dans une publication (19 juin 2026) mais n’est pas relié à la page : non ajouté. | À propos > Liens |
| Logo « Depuis 1976 » | Lu sur le logo ; aucune autre précision sur l’historique. | À propos > Intro |

## 2. Produits sans prix (affichés « Prix sur demande »)

| Produit | Ce qui manque | Où le prix devrait se trouver |
|---|---|---|
| Viande hachée (`viande-hachee`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : L’étiquette indique seulement « HACHÉ — garder réfrigéré » (Boucherie M. Morin, Saint-Isidore) et un prix de 0,01 $, manifestement une valeur de test. Espèce et prix non indiqués. |
| Chocolat blanc à la pivoine (110 g) (`chocolat-blanc-a-la-pivoine`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Nom et format lus sur l’emballage. Prix non indiqué sur la page. |
| Sel de fleur d’ail et pivoine (125 g) (`sel-de-fleur-d-ail-et-pivoine`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Ingrédients et format lus sur l’étiquette. Prix non indiqué sur la page. |
| Poudre de fleur d’ail (55 g) (`poudre-de-fleur-d-ail`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Ingrédients et format lus sur l’étiquette. Prix non indiqué sur la page. |
| Patates douces (`patates-douces`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Prix non indiqué sur la page. |
| Laitue (`laitue`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Prix non indiqué sur la page. |
| Melon d’eau (`melon-d-eau`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Prix non indiqué sur la page. |
| Petits cantaloups (`cantaloups`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Prix non indiqué sur la page. |
| Concombres (`concombres`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Prix non indiqué sur la page. |
| Courgettes (`courgettes`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Prix non indiqué sur la page. |
| Fèves françaises extra-fines (`feves-francaises`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Prix non indiqué sur la page. |
| Tomates cerises (`tomates-cerises`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Prix non indiqué sur la page. |
| Poivrons verts (`poivrons-verts`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Prix non indiqué sur la page. |
| Citrouilles (`citrouilles`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Prix non indiqué sur la page. Les photos montrent le kiosque et l’étalage de citrouilles ; aucune photo de citrouilles seules n’a été retenue. |
| Épis de maïs ornemental (`mais-ornemental`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Prix non indiqué sur la page. |
| Moutarde et sauce au miel — Le Miel d’Émilie (250 ml) (`miel-d-emilie`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Produit d’un autre artisan vendu au kiosque. Prix non indiqués. |
| Paniers-cadeaux (`paniers-cadeaux`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Publication du 16 décembre 2025. Prix non indiqué. |
| Casquette Ferme Roberge-Innov (`casquette-ferme-roberge-innov`) | Prix | Publication du produit ou étiquette ; voir `notes` dans products.json : Photo seulement ; aucune description ni prix sur la page. |

## 3. Prix ambigus, anciens ou calculés (signalés)

| Produit | Valeur brute (`price_raw`) | Problème |
|---|---|---|
| Smoked meat de dindon | Étiquette : 0,26 kg, total 4,68 $ (prix au kg partiellement caché) | Prix au kg **calculé** (total ÷ poids) : le prix unitaire est caché sur l’étiquette. |
| Mini et petites citrouilles | Les prix varient entre 0,75$ et 2$ chaque | Fourchette « entre 0,75$ et 2$ » : le site affiche « de 0,75 $ ». |
| Maïs sucré | 7,50$ la douzaine | Prix de **2024** (publication du 28 sept. 2024) : à confirmer pour 2026. |
| Pommes de terre nouvelles | 3$ le casseau ou 1,15$ la livre | Prix de **2025** : aucune mention en 2026. |
| Ail | 12,50$ la livre | Prix du 7 mars 2026 (« sur demande ») : à confirmer pour la récolte 2026. |
| Saucisse de dinde traditionnelle | Étiquette : prix 12.00 (au kg), 0,90 kg, total 10,80 $ | Prix **au kg lu sur une étiquette** de photo ; aucun prix publié dans les textes. |
| Steak de dindon | Étiquette : prix 14.00 (au kg), 0,65 kg, total 9,10 $ | Prix **au kg lu sur une étiquette** de photo. |
| Tournedos de dindon | Étiquette : prix 15.25 (au kg), 0,80 kg, total 12,20 $ | Prix **au kg lu sur une étiquette** de photo. |
| Fondue chinoise de dindon | Étiquette : prix 13.00 (au kg), 1,02 kg, total 13,26 $ | Prix **au kg lu sur une étiquette** de photo. |
| Slush à la limonade de pivoine | au prix de 3,50$ | Prix d’été (juillet–août 2026) ; disponibilité hors saison non précisée. |
| Popsicle rhubarbe et pivoine enrobé de chocolat | au prix de 3,50$ | Prix d’été (juillet–août 2026). |
| Limonade à la pivoine (1 L) | 5,00$ pour 1 litre | Bouteille de 1 L « sur demande » (mars 2026) ; en verre ou en slush, 3,50 $ l’été. |

## 4. Noms de produits à confirmer

- **Découpes de dindon** (steak, tournedos, fondue chinoise, smoked meat) : les étiquettes indiquent seulement « steak », « tournedos », etc. ; « de dindon » vient de la publication du 4 novembre 2026, qui présente ces photos comme « nos découpes de dindons ».
- **Viande hachée** : l’étiquette (Boucherie M. Morin) indique « HACHÉ » et un prix de 0,01 $ (valeur de test). Espèce et prix inconnus.
- **Produit non identifié, non publié** : sachet de lanières marinées avec l’étiquette de « La Pivoinerie de Diane » (photo https://www.facebook.com/photo/?fbid=122196251336393668). Nom illisible : peut-être le jerky de dindon annoncé le 4 novembre 2026, mais rien ne le confirme. **Non ajouté au catalogue.**

## 5. Produits mentionnés sans photo (non ajoutés au catalogue)

| Produit | Prix indiqué | Source |
|---|---|---|
| Abats de poulet (cœurs et foies) | 3$ la livre | Publication du 13 novembre 2025 |
| Cornichons sucrés maison | 5,00$ pour 500 ml | Publication du 7 mars 2026 |
| Relish maison | 5,00$ pour 500 ml | Publication du 7 mars 2026 |
| Salsa maison | 10,00$ pour 1000 ml | Publication du 7 mars 2026 |
| Macédoine (conserve maison) | non indiqué | Publication du 4 janvier 2026 |
| Jerky de dindon | non indiqué | Publication du 4 novembre 2026 |
| Miel liquide « toutes fleurs » et miel crémeux (Le Miel d’Émilie) | non indiqué | Publication du 4 novembre 2026 |
| Vinaigrette à la pivoine | non indiqué | Publications du 8 et du 17 juillet 2026 |
| Savons au sorgho (érable, coco, pivoine) — collaboration avec Belles Cosmétiques | non indiqué | Publication du 19 juin 2026 |
| Petites balles de paille | non indiqué | Publication du 4 janvier 2026 |
| Tiges de maïs décoratives | non indiqué | Publications de septembre et octobre 2026 |
| Épis de maïs sucré congelés | 1$ chaque | Publication du 18 avril 2026 (mentionné dans la fiche Maïs sucré) |
| Fleurs de pivoines (autocueillette et bouquets, La Pivoinerie de Diane) | non indiqué | Publications de juin 2026 |

Ces produits peuvent être ajoutés dès qu’une photo existe (voir le README pour la marche à suivre).

## 6. Qualité des photos

| Produit | Fichier | Remarque |
|---|---|---|
| Mini et petites citrouilles | 01.jpg | 720×960 px (basse résolution) |
| Bouquet de narcisses | 03.jpg | 965×1286 px (basse résolution) |
| Citrouilles | 01.jpg, 02.jpg | Photos du kiosque et de l’étalage (pas de citrouille seule). |
| Découpes de dindon, saucisse, viande hachée | 01.jpg | Photos prises sur le comptoir avec l’étiquette de prix visible ; éclairage inégal. |
| Chocolat blanc à la pivoine | 01.jpg, 02.jpg | Photo sombre, reflets sur l’emballage. |
| Ensemble de décorations d’Halloween | 01.jpg | Photo d’exemple de montage, selon la publication. |

Aucune photo retenue n’a de filigrane ni n’est une capture d’écran de texte.

## 7. Limites de l’extraction

- Il n’y a pas d’onglet Boutique ni de Marketplace sur la page : les produits viennent des publications et des photos.
- 686 photos parcourues (juillet 2024 à novembre 2026) ; 91 publications lues en entier dans le fil (octobre 2025 à novembre 2026). Les publications plus anciennes n’ont été lues qu’à travers les légendes de leurs photos, parfois tronquées (« En voir plus »).
- Les vidéos (Reels) n’ont pas été transcrites ; certains prix n’y sont peut-être que mentionnés à l’oral.
