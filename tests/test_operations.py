"""
Tests unitaires pour le module operations.py.

Ce fichier regroupe les vérifications des fonctions arithmétiques
de base : addition, soustraction, multiplication et division.

Chaque fonction est testée selon plusieurs scénarios :

- Cas standard avec des nombres positifs

- Utilisation de nombres négatifs

- Utilisation de nombres à virgule flottante

- Cas particuliers (zéro, division par zéro)

"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from operators import add, subtract, multiply, divide

def test_add_basic():
    """
    Vérifie que la fonction d'addition fonctionne correctement
    pour deux entiers positifs.

    Exemple testé : 9 + 2 doit renvoyer 11.
    """
    result = add(9, 2)
    assert result == 11, f"Expected 11, instead obtained {result}"


def test_add_negative_numbers():
    """
    S'assure que l'addition prend correctement en compte
    les nombres négatifs.

    Exemple : -9 + 2 doit retourner -7.
    """
    result = add(-9, 2)
    assert result == -7, f"Expected -7, instead obtained {result}"

def test_add_with_zero():
    """
    Vérifie que l'addition avec zéro renvoie le nombre initial.

    Exemple : 7 + 0 doit retourner 7.
    """
    result = add(7, 0)
    assert result == 7, f"Expected 7, instead obtained {result}"

def test_add_decimals():
    """
    Teste l'addition de nombres à virgule flottante.

    Vérification : 6.5 + 2.5 doit donner 9.0.
    """
    result = add(6.5, 2.5)
    assert result == 9.0, f"Expected 9.0, instead obtained {result}"



def test_subtract_basic():
    """
    Vérifie le fonctionnement de la soustraction pour deux nombres positifs.

    Exemple : 3 - 1 doit donner 2.
    """
    result = subtract(3, 1)
    assert result == 2, f"Expected 2, instead obtained {result}"

def test_subtract_with_zero():
    """
    Vérifie que soustraire zéro n'altère pas le nombre.

    Exemple : 7 - 0 doit retourner 7.
    """
    result = subtract(7, 0)
    assert result == 7, f"Expected 7, instead obtained {result}"

def test_subtract_decimals():
    """
    Vérifie que la soustraction de nombres à virgule flottante
    renvoie un résultat précis.

    Exemple : 7.3 - 7.1 ≈ 0.2
    """
    result = subtract(7.3, 7.1)
    #Perte de résolution possible avec les floats, on utilise une marge d'erreur
    assert abs(result - 0.2) < 0.0001, f"Expected 0.2, instead obtained {result}"


def test_divide_basic():
    """
    Vérifie la division classique entre deux nombres.

    Exemple : 18 / 3 doit renvoyer 6.0
    """
    result = divide(18, 3)
    assert result == 6.0, f"Expected 6.0, instead obtained {result}"

def test_divide_negative_numbers():
    """
    Vérifie la division lorsque l'un des nombres est négatif.

    Exemple : -2 / 4 doit donner -0.5
    """
    result = divide(-2, 4)
    assert result == -0.5, f"Expected -0.5, instead obtained {result}"

def test_divide_by_zero():
    """
    Vérifie que diviser par zéro déclenche une erreur.

    La fonction doit lever une ZeroDivisionError.
    """
    with pytest.raises(ZeroDivisionError):
        divide(7, 0)

def test_divide_decimals():
    """
    Vérifie la division de nombres à virgule flottante.

    Exemple : 14.0 / 4.0 doit donner 3.5
    """
    result = divide(14.0, 4.0)
    assert result == 3.5, f"Expected 3.5, instead obtained {result}"

def test_multiply_basic():
    """
    Vérifie que la multiplication de deux entiers positifs
    retourne le produit attendu.

    Exemple : 2 * 6 = 12
    """
    result = multiply(2, 6)
    assert result == 12, f"Expected 12, instead obtained {result}"

def test_multiply_by_zero():
    """
    Vérifie que multiplier par zéro retourne zéro.

    Exemple : 7 * 0 = 0
    """
    result = multiply(7, 0)
    assert result == 0, f"Expected 0, instead obtained {result}"

def test_multiply_decimals():
    """
    Vérifie la multiplication impliquant des nombres à virgule flottante.

    Exemple : 1.5 * 2 doit donner 3.0
    """
    result = multiply(1.5, 2)
    assert result == 3.0, f"Expected 3.0, instead obtained {result}"

def test_multiply_negative_numbers():
    """
    Vérifie la multiplication impliquant des nombres négatifs.

    Exemple : -8 * 4 = -32
    """
    result = multiply(-8, 4)
    assert result == -8, f"Expected -8, instead obtained {result}"

