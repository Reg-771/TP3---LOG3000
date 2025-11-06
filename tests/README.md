# Répertoire Tests

### Exécution des tests

```bash
pytest
```

### Exécution des tests avec des détails

```bash
pytest -v
```

### Exécution d'un fichier spécifique

```bash
pytest tests/test_operations.py
pytest tests/test_app.py
```

### Exécution d'un test spécifique

```bash
pytest tests/test_operations.py::test_add_basic
pytest tests/test_app.py::TestFlaskRoutes::test_home_get
```

### test_operations.py

Contient les tests unitaires pour les fonctions de `operations.py` :

- **`test_add_*`** : Tests pour l'addition

  - Addition de base
  - Nombres négatifs
  - Nombres décimaux
  - Addition avec zéro

- **`test_subtract_*`** : Tests pour la fonction de soustraction

  - Soustraction de base
  - Ordre des opérandes (a - b)
  - Nombres négatifs
  - Nombres décimaux

- **`test_multiply_*`** : Tests pour la fonction de multiplication

  - Multiplication de base
  - Vérification que ce n'est pas une exponentiation
  - Multiplication par zéro
  - Nombres décimaux

- **`test_divide_*`** : Tests pour la fonction de division
  - Division de base
  - Vérification de la division décimale (pas entière)
  - Division par zéro
  - Nombres négatifs

### test_app.py

Ce fichier contient les **tests d'intégration** pour l'application Flask :

- **Tests des routes** :

  - Route GET `/` : Vérification du rendu de la page d'accueil
  - Route POST `/` : Vérification du traitement des calculs

- **Tests de la fonction `calculate()`** :

  - Expressions valides (avec et sans espaces)
  - Expressions invalides
  - Gestion des erreurs
  - Cas limites

- **Tests du formulaire** :
  - Soumission avec données valides
  - Soumission avec données invalides
  - Affichage des résultats et erreurs
