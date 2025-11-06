# Répertoire Static

## Raison d’être du répertoire

Ce répertoire regroupe tous les fichiers statiques de l’application Flask, comme les feuilles de style, images et scripts JavaScript.
Flask les sert lors du rendu de la page.

## Fichier Contenu

**style.css** : définit l’apparence de l’interface utilisateur, incluant la mise en page, les couleurs et le style des boutons.

## Dépendances et hypothèses

Utilisé dans les templates HTML via `<link>` ou `<script>`.

Le répertoire `static/` doit être reconnu par Flask (configuration par défaut).
