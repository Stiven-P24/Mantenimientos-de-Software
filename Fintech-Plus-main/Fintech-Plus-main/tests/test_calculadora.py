import pytest
from app.calculadora import sumar, dividir


def test_sumar():
    assert sumar(2, 3) == 5


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
