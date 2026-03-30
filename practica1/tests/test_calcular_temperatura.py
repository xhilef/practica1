import pytest
from src.calcular_temperatura import clasificar_temperatura

# pruebas de particiones válidas
def test_temp_frio():
    assert clasificar_temperatura(10) == "Frío"

def test_temp_templado():
    assert clasificar_temperatura(20) == "Templado"

def test_temp_caliente():
    assert clasificar_temperatura(30) == "Caliente"

# LOOS CASOS LÍMITE 
def test_temp_limite_15():
    assert clasificar_temperatura(15) == "Frío"

def test_temp_limite_16():
    assert clasificar_temperatura(16) == "Templado"

def test_temp_limite_25():
    assert clasificar_temperatura(25) == "Templado"

# pruebas de error
def test_temp_error_min_Menor_a_Menos273():
    with pytest.raises(ValueError):
        clasificar_temperatura(-300)

def test_temp_error_max_Mayor_a_10000():
    with pytest.raises(ValueError):
        clasificar_temperatura(12000)

def test_temp_error_tipo_NO_numerico():
    with pytest.raises(TypeError):
        clasificar_temperatura("calorcito")