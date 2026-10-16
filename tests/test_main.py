
import sys
from pathlib import Path

# Agregar la carpeta raíz del proyecto a la ruta de búsqueda
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import main


def test_dni_valido():
    assert main.registrar_asistencia({"dni": "40123456"}) is True


def test_dni_con_espacios():
    assert main.registrar_asistencia({"dni": " 40123456 "}) is True


def test_dni_corto():
    assert main.registrar_asistencia({"dni": "12345"}) is False


def test_dni_con_letras():
    assert main.registrar_asistencia({"dni": "40123ABC"}) is False


def test_dni_vacio():
    assert main.registrar_asistencia({"dni": ""}) is False


def test_materia_personalizada():
    assert main.registrar_asistencia({
        "dni": "40123456",
        "materia": "Programacion III"
    }) is True

