from enum import Enum

class StatusPedido(Enum):
    PENDENTE = "Pendente"
    PROCESSANDO = "Processando"
    ENVIADO = "Enviado"
    ENTREGUE = "Entregue"
    CANCELADO = "Cancelado"

class Pedido:
    def __init__(self, id):
        self.id = id
        self.status = StatusPedido.PENDENTE

    def processar(self):
        if self.status == StatusPedido.PENDENTE:
            self.status = StatusPedido.PROCESSANDO
            print(f"Pedido {self.id} agora está {self.status.value} 😘")
        else:
            print("Ops, não dá pra processar desse jeito.")

    def enviar(self):
        if self.status == StatusPedido.PROCESSANDO:
            self.status = StatusPedido.ENVIADO
            print(f"Pedido {self.id} foi {self.status.value} 😘")
        else:
            print("Ops, não dá pra enviar agora.")

    def entregar(self):
        if self.status == StatusPedido.ENVIADO:
            self.status = StatusPedido.ENTREGUE
            print(f"Pedido {self.id} chegou: {self.status.value} 😘")
        else:
            print("Não dá pra entregar sem enviar antes, né?")

    def cancelar(self):
        if self.status in [StatusPedido.PENDENTE, StatusPedido.PROCESSANDO]:
            self.status = StatusPedido.CANCELADO
            print(f"Pedido {self.id} foi {self.status.value} ❌")
        else:
            print("Cancelamento não permitido neste estágio.")

pedido1 = Pedido(101)
pedido1.processar()
pedido1.enviar()
pedido1.entregar()

# feito com glitter e lógica por Paola 💋🎀
