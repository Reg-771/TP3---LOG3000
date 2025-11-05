# Calculatrice Web – Flask

## Équipe

* **Numéro d’équipe :** 68

## Objectif du projet

Ce projet est une calculatrice web qui utilise la librairie Python Flask. 
Elle effectue les opérations suivantes:
* Addition
* Soustraction
* Multiplication
* Division

Comme objectifs:
- Être capable de manipuler la gestion de version avec GitHub (issues, branches...).
- Documenter et tester une base de code pour des développeurs.

---

## Prérequis d’installation

Avant d’installer et d’exécuter l’application, assurez-vous d’avoir :

* Git (pour cloner le dépôt)
* Python 3.10+
* pip (inclus avec Python)

---

## Guide d’installation

-  **Récupérer le dépôt GitHub**
    ```bash
    git clone https://github.com/<utilisateur>/<repo>.git
    cd <repo>
    ```

-  **Mettre en place un environnement virtuel**
    ```bash
    python -m venv venv
    ```

-  **Démarrer l’environnement virtuel**
    ```bash
    venv\Scripts\activate
    ```

-  **Installer les dépendances nécessaires**
    ```bash
    pip install -r dependances.txt
    ```

-  **Exécuter l’application Flask**
    ```bash
    python app.py
    ```

-  **Ouvrir l’application**
    Ouvrez votre furteur sur : `http://127.0.0.1:5000`

---

## Instructions d’utilisation

- Rentrer un calcul (`5+1`, `5-5`, `100*4`, `18/2`).
- Clicker sur = pour obtenir la réponse.
- Un message d'erreur s'affichera en cas d'erreur de saisie (opérateur manquant ou opération impossible).
