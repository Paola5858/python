"""
Representa um celular com marca, modelo e armazenamento
Autora: Paola Soares Machado
"""


class Celular:
    """Classe que representa um celular."""
    
    def __init__(self, marca: str, modelo: str, armazenamento: int):
        self.marca = marca
        self.modelo = modelo
        self.armazenamento = armazenamento

    def mostrar_info(self) -> None:
        """Exibe informações do celular."""
        print(f"📱 Celular: {self.marca} {self.modelo}")
        print(f"💾 Armazenamento: {self.armazenamento}GB")
    
    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} ({self.armazenamento}GB)"


if __name__ == "__main__":
    print("\n💋 Meu celular:\n")
    meu_celular = Celular("Samsung", "Galaxy A54", 128)
    meu_celular.mostrar_info()

# Feito com glitter e lógica por Paola 💋🎀
