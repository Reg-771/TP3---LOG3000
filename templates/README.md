# Répertoire Templates

## Raison d’être du répertoire

Ce dossier regroupe les fichiers HTML servant à afficher les pages de l’application Flask.
Il permet de séparer le code Python de la présentation visuelle, suivant une approche type MVC.

## Fichier Contenu

**index.html** : Page d’accueil présentant la calculatrice et montrant les résultats des calculs effectués par l’utilisateur.

## Dépendances et hypothèses

La page est générée par la fonction `index()` de `app.py` grâce à `render_template()`.

Elle peut utiliser des fichiers statiques (par ex. `style.css`) pour le style.
