"""
Testes para funções fundamentais
Autora: Paola Soares Machado
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercícios.intro_python import soma, media


def test_somar():
    """Testa função de soma."""
    # Importa dinamicamente para evitar problemas de path
    assert soma.somar(2, 3) == 5
    assert soma.somar(-1, 1) == 0
    assert soma.somar(0, 0) == 0


def test_calcular_media():
    """Testa função de média."""
    assert media.calcular_media(8, 6) == 7
    assert media.calcular_media(10, 10) == 10
    assert media.calcular_media(0, 10) == 5


# Feito com glitter e lógica por Paola 💋🎀
