import math
import pytest
from Areas import area_cuadrado, area_circulo, area_triangulo

# Pruebas para area_cuadrado
def test_area_cuadrado_valido():
    assert area_cuadrado(4) == 16

def test_area_cuadrado_decimal():
    assert area_cuadrado(2.5) == 6.25

def test_area_cuadrado_invalido():
    with pytest.raises(ValueError, match="El lado debe ser un número positivo."):
        area_cuadrado(0)

# Pruebas para area_circulo
def test_area_circulo_valido():
    assert math.isclose(area_circulo(1), math.pi)

def test_area_circulo_decimal():
    assert math.isclose(area_circulo(2.5), math.pi * 2.5**2)

def test_area_circulo_invalido():
    with pytest.raises(ValueError, match="El radio debe ser un número positivo."):
        area_circulo(-2)

# Pruebas para area_triangulo
def test_area_triangulo_valido():
    assert area_triangulo(4, 3) == 6

def test_area_triangulo_decimal():
    assert area_triangulo(2.5, 4.0) == 5.0

def test_area_triangulo_base_negativa():
    with pytest.raises(ValueError, match="La base y la altura deben ser números positivos."):
        area_triangulo(-3, 4)

def test_area_triangulo_altura_negativa():
    with pytest.raises(ValueError, match="La base y la altura deben ser números positivos."):
        area_triangulo(3, -4)
