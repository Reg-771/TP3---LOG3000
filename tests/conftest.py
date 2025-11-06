"""
Pytest fixtures pour l'application Flask.

Ce fichier fournit des fixtures réutilisables pour les tests, incluant :
- un client Flask configuré pour les tests HTTP
- un runner CLI pour tester les commandes Flask
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app import app


@pytest.fixture
def client():
    """
    Fournit un client de test Flask configuré.

    Le client permet d'envoyer des requêtes simulées à l'application
    pendant les tests.

    FlaskClient: client Flask prêt pour les tests

    Exemple:
        def test_index(client):
            response = client.get('/')
            assert response.status_code == 200
    """
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # CSRF désactivé pour les tests

    with app.test_client() as test_client:
        yield test_client


@pytest.fixture
def runner():
    """
    Fournit un runner CLI pour tester les commandes Flask.

    Yields:
        FlaskCliRunner: runner CLI pour l'application Flask
    """
    return app.test_cli_runner()