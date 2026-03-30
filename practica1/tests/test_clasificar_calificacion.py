import pytest
from src.clasificar_calificacion import clasificar_calificacion

# pruebas de particiones válidas
def test_calif_reprobado():
    assert clasificar_calificacion(5.5) == "Reprobado"

def test_calif_aprobado():
    assert clasificar_calificacion(7.5) == "Aprobado"

def test_calif_sobresaliente():
    assert clasificar_calificacion(9.5) == "Sobresaliente"

# LOS CASOS LÍMITE
def test_calif_limite_6():
    assert clasificar_calificacion(6) == "Aprobado"

def test_calif_limite_9():
    assert clasificar_calificacion(9) == "Sobresaliente"

# pruebas de error
def test_calif_error_negativo_Menor_a_cero():
    with pytest.raises(ValueError):
        clasificar_calificacion(-1.0)

def test_calif_error_exceso_mayor_a_diez():
    with pytest.raises(ValueError):
        clasificar_calificacion(11.0)

def test_calif_error_tipo_NO_Numerico():
    with pytest.raises(TypeError):
        clasificar_calificacion("9")