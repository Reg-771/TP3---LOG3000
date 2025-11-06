"""
Tests d'intégration pour l'application Flask définie dans app.py.

Ce fichier regroupe les vérifications suivantes :
- La fonction calculate() pour le traitement et l'évaluation des expressions mathématiques.
- Les routes Flask, incluant les requêtes GET et POST.
- L'intégration avec le formulaire web pour la soumission des calculs.
- La gestion des erreurs et des entrées invalides.

"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app import app, calculate

class TestCalculate:
    """Tests pour valider le moteur de calcul calculate()."""

    def test_simple_addition(self):
        """
        Vérifie qu'une addition simple retourne le résultat attendu.

        Exemple : "3+7" doit donner 10.
        """
        result = calculate("3+7")
        assert result == 10, f"Expected 10, but got {result}"

    def test_addition_with_spaces(self):
        """
        Vérifie qu'une addition avec des espaces est correctement évaluée.

        Exemple : " 4 + 6 " doit donner 10.
        """
        result = calculate(" 4 + 6 ")
        assert result == 10, f"Expected 10, but got {result}"

    def test_decimal_addition(self):
        """
        Vérifie la somme de nombres décimaux.

        Exemple : "1.2+3.4" ≈ 4.6.
        """
        result = calculate("1.2+3.4")
        assert abs(result - 4.6) < 0.0001, f"Expected ~4.6, but got {result}"

    def test_division_zero_error(self):
        """
        Vérifie que diviser par zéro déclenche une exception.

        Exemple : "6/0" doit lever ZeroDivisionError.
        """
        with pytest.raises(ZeroDivisionError):
            calculate("6/0")

    def test_invalid_operand(self):
        """
        Vérifie que les opérandes non numériques déclenchent une exception.

        Exemple : "x+5" doit lever ValueError.
        """
        with pytest.raises(ValueError):
            calculate("x+5")

class TestFlaskRoutes:
    """Tests pour les principales routes de l'application Flask."""

    def test_home_page_loads(self, client):
        """
        Vérifie que la page d'accueil est accessible via GET.

        Contrôle que le code de statut est 200 et que le formulaire est présent.
        """
        response = client.get('/')
        assert response.status_code == 200
        assert b"Flask Calculator" in response.data
        assert b"<form" in response.data

    def test_post_valid_addition(self, client):
        """
        Vérifie qu'une addition valide soumise via POST retourne le bon résultat.

        Exemple : "5+9" doit renvoyer 14.
        """
        response = client.post('/', data={'display': '5+9'})
        assert response.status_code == 200
        assert b"14" in response.data

    def test_post_subtraction(self, client):
        """
        Vérifie qu'une soustraction est évaluée correctement.

        Exemple : "12-3" doit donner 9.
        """
        response = client.post('/', data={'display': '12-3'})
        assert response.status_code == 200
        assert b"9" in response.data

    def test_post_invalid_expression(self, client):
        """
        Vérifie que l'application gère les expressions incorrectes.

        Exemple : "hello" doit afficher un message d'erreur sans planter.
        """
        response = client.post('/', data={'display': 'hello'})
        assert response.status_code == 200
        assert b"Error" in response.data or b"error" in response.data



class TestEndToEnd:
    """Scénarios d'utilisation complets simulant un utilisateur."""

    def test_calculation_workflow(self, client):
        """
        Simule un utilisateur effectuant un calcul complet.

        Exemple : soumettre "20+15" et vérifier que le résultat 35 est affiché.
        """
        # Page d'accueil
        response = client.get('/')
        assert response.status_code == 200

        # Soumission d'un calcul
        response = client.post('/', data={'display': '20+15'})
        assert response.status_code == 200
        assert b"35" in response.data

    def test_error_then_recovery(self, client):
        """
        Simule un utilisateur corrigeant une erreur après soumission.

        Étapes :
        1. Soumettre une expression invalide "oops"
        2. Soumettre ensuite "8+7" pour obtenir 15
        """
        response = client.post('/', data={'display': 'oops'})
        assert response.status_code == 200
        assert b"Error" in response.data or b"error" in response.data

        response = client.post('/', data={'display': '8+7'})
        assert response.status_code == 200
        assert b"15" in response.data


@pytest.mark.parametrize("expression, expected_contains", [
    ("2+3", "5"),
    ("7-2", "5"),
    ("3*4", "12"),
    ("18/3", "6"),
])
def test_various_valid_expressions(client, expression, expected_contains):
    """
    Test paramétré pour plusieurs calculs simples.

    Vérifie que chaque calcul retourne la valeur attendue dans la réponse.
    """
    response = client.post('/', data={'display': expression})
    assert response.status_code == 200
    assert expected_contains.encode() in response.data, \
        f"Expected '{expected_contains}' in response for expression '{expression}'"


@pytest.mark.parametrize("invalid_expression", [
    "",      # vide
    "abc",   # lettres
    "3+4+5", # plusieurs opérateurs
])
def test_various_invalid_inputs(client, invalid_expression):
    """
    Vérifie que plusieurs entrées incorrectes sont gérées.

    Toutes doivent afficher un message d'erreur.
    """
    response = client.post('/', data={'display': invalid_expression})
    assert response.status_code == 200
    assert b"Error" in response.data or b"error" in response.data