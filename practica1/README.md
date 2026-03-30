Práctica 1: Testing con Particiones de Equivalencia

Esta práctica contiene la implementación y pruebas unitarias de dos funciones: clasificar_temperatura y clasificar_calificacion. Se aplicó la técnica de Particiones de Equivalencia (PE) para garantizar la cobertura de distintos escenarios de entrada.

Estructura del Proyecto
src/: Contiene la implementación de las funciones.
tests/: Contiene los casos de prueba con pytest.

Problema 1: Clasificación de Temperatura
Especificación
Clasifica una temperatura en:
Frío: ≤ 15°C
Templado: 16°C a 25°C
Caliente: > 25°C
Particiones de Equivalencia (PE)

Se definieron particiones válidas e inválidas considerando:
Rangos permitidos
Valores fuera del dominio (-273 a 10000)
Tipos de datos no numéricos


Problema 2: Clasificación de Calificación
Especificación
Clasifica una calificación en:
Reprobado: < 6
Aprobado: 6 a 8
Sobresaliente: 9 a 10
Particiones de Equivalencia (PE)

Se definieron particiones válidas e inválidas considerando:
Rango válido de 0 a 10
Valores fuera del rango
Tipos de datos incorrectos

Ejecución de Pruebas

Para ejecutar las pruebas:
pytest -v
Ejemplo de salida:
tests/test_calcular_temperatura.py::test_temp_frio PASSED
tests/test_calcular_temperatura.py::test_temp_templado PASSED
tests/test_clasificar_calificacion.py::test_calif_aprobado PASSED


Tecnologías
Python 3.10
Pytest
Visual Studio Code / VSCodium
Miniconda

Configuración del Entorno
Crear entorno:
conda create --prefix  TSP 

Activar entorno:
conda activate TSP

Instalar dependencias:
pip install pytest