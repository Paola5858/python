"""representa um celular com marca, modelo e armazenamento."""
class Celular:

    def __init__(self, marca, modelo, armazenamento):
        self.marca = marca
        self.modelo = modelo
        self.armazenamento = armazenamento

    def mostrar_info(self):
        print(f"celular: {self.marca} {self.modelo}")
        print(f"armazenamento: {self.armazenamento}GB")


# criando o objeto
meu_celular = Celular("Samsung", "Galaxy A54", 128)

# exibindo info
meu_celular.mostrar_info()
