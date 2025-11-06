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

La portée du projet s'épand comme tel:
- **HTML/CSS** sont utilisés pour l'interface utilisateur.
- **Flask** est utilisé pour le routage et la logique en Python.
- Un module de tests (un ajout futur) sera utilisé pour faire des tests unitaires automatiques.

---

## Prérequis d’installation

Avant de faire l'installation et de passer à exécuter l’application, assurez-vous que vous avec déjà :

* Git (pour obtenir le dépôt)
* Python 3.10+
* pip (vient avec Python)

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

---

## Module Tests

Un dossier `tests/` contiendra les tests unitaires pour vérifier le bon fonctionnement des opérations mathématiques et de la logique de l’application Flask.

### Lancement des tests
Une fois `pytest` installé, les tests peuvent être exécutés avec la commande :

```bash
pytest
```

### Organisation prévue des tests
```
tests/
│
├── test_app.py         # Tests des routes Flask et intégration
└── test_operators.py   # Tests unitaires des fonctions add, subtract, multiply et plus...
```

---

## Processus de contribution (branches, PR, issues)

### 🧩 Règles de contribution

- Ouvrir une issue pour signaler un bug ou proposer une nouvelle fonctionnalité.

- Créer une branche dédiée à cette issue :
   ```bash
   git checkout -b fix/<nom-issue>
   ```

- Apporter les modifications nécessaires, puis committer avec un message explicite:
   ```bash
   git commit -m "Corrige la fonction subtract pour inverser les opérandes"
   ```

- Envoyer la branche sur le dépôt distant:
   ```bash
   git push origin fix/<issue>
   ```

- Créer une Pull Request (PR) vers la branche principale (main ou master).

- Soumettre la PR à la revue par un membre de l’équipe avant fusion.

---

### Gestion des issues GitHub

Pour chaque issue:
- Fournir une description précise du problème ou de la fonctionnalité.

- Indiquer les étapes pour reproduire un bug, si applicable.

- Expliquer le résultat attendu et le résultat observé.

- Assigner un responsable pour la résolution.