"""
Composição: objeto só existe dentro de outro
Autora: Paola Soares Machado
"""


class Motor:
    """Representa um motor de carro."""
    
    def __init__(self, potencia: int):
        self.potencia = potencia

    def __str__(self) -> str:
        return f"{self.potencia}cv"


class Carro:
    """Representa um carro que compõe um motor."""
    
    def __init__(self, modelo: str, potencia_motor: int):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)  # composição (motor só vive dentro do carro)

    def detalhes(self) -> str:
        return f"{self.modelo} com motor {self.motor}"


if __name__ == "__main__":
    print("\n💋 Composição: Carro e Motor\n")
    meu_carro = Carro("Fusca Tunado", 200)
    print(meu_carro.detalhes())

# Feito com glitter e lógica por Paola 💋🎀
