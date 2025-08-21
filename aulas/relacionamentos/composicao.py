class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def __str__(self):
        return f"{self.potencia}cv"

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)  # composição (motor só vive dentro do carro)

    def detalhes(self):
        return f"{self.modelo} com motor {self.motor}"

meu_carro = Carro("fusca tunado", 200)
print(meu_carro.detalhes())
