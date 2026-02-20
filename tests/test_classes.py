"""
Testes para classes POO
Autora: Paola Soares Machado
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_celular():
    """Testa classe Celular."""
    from exercícios.classe.celular import Celular
    
    cel = Celular("Samsung", "Galaxy A54", 128)
    assert cel.marca == "Samsung"
    assert cel.modelo == "Galaxy A54"
    assert cel.armazenamento == 128
    assert "Samsung" in str(cel)


def test_enum_pedido():
    """Testa Enum de pedidos."""
    from exercícios.classe.enum import Pedido, StatusPedido
    
    pedido = Pedido(1)
    assert pedido.status == StatusPedido.PENDENTE
    
    pedido.processar()
    assert pedido.status == StatusPedido.PROCESSANDO


def test_heranca():
    """Testa herança Pessoa -> Estudante."""
    from aulas.relacionamentos.heranca import Pessoa, Estudante
    
    estudante = Estudante("Paola", 18, "Informática")
    assert estudante.nome == "Paola"
    assert estudante.idade == 18
    assert estudante.curso == "Informática"
    assert "Informática" in estudante.bio()


# Feito com glitter e lógica por Paola 💋🎀
