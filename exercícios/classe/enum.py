"""
Enum: representando estados de forma elegante
Autora: Paola Soares Machado
"""
from enum import Enum


class StatusPedido(Enum):
    """Estados possíveis de um pedido."""
    PENDENTE = "Pendente"
    PROCESSANDO = "Processando"
    ENVIADO = "Enviado"
    ENTREGUE = "Entregue"
    CANCELADO = "Cancelado"


class Pedido:
    """Representa um pedido com controle de status."""
    
    def __init__(self, id: int):
        self.id = id
        self.status = StatusPedido.PENDENTE

    def __str__(self) -> str:
        return f"Pedido #{self.id} - Status: {self.status.value}"

    def processar(self) -> None:
        if self.status == StatusPedido.PENDENTE:
            self.status = StatusPedido.PROCESSANDO
            print(f"Pedido {self.id} agora está {self.status.value} 😘")
        else:
            print("Ops, não dá pra processar desse jeito.")

    def enviar(self) -> None:
        if self.status == StatusPedido.PROCESSANDO:
            self.status = StatusPedido.ENVIADO
            print(f"Pedido {self.id} foi {self.status.value} 😘")
        else:
            print("Ops, não dá pra enviar agora.")

    def entregar(self) -> None:
        if self.status == StatusPedido.ENVIADO:
            self.status = StatusPedido.ENTREGUE
            print(f"Pedido {self.id} chegou: {self.status.value} 😘")
        else:
            print("Não dá pra entregar sem enviar antes, né?")

    def cancelar(self) -> None:
        if self.status in [StatusPedido.PENDENTE, StatusPedido.PROCESSANDO]:
            self.status = StatusPedido.CANCELADO
            print(f"Pedido {self.id} foi {self.status.value} ❌")
        else:
            print("Cancelamento não permitido neste estágio.")


if __name__ == "__main__":
    print("💋 Testando fluxo de pedido:\n")
    pedido1 = Pedido(101)
    pedido1.processar()
    pedido1.enviar()
    pedido1.entregar()

# Feito com glitter e lógica por Paola 💋🎀
