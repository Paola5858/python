"""
Encapsulamento: protegendo dados sensíveis
Autora: Paola Soares Machado
"""


class Professor:
    """Classe que demonstra encapsulamento."""
    
    def __init__(self, nome: str, salario: float):
        self._nome = nome  # protegido (convenção)
        self.__salario = salario  # privado (name mangling)
    
    @property
    def nome(self) -> str:
        """Getter para nome."""
        return self._nome
    
    @nome.setter
    def nome(self, valor: str) -> None:
        """Setter para nome."""
        if valor and len(valor) > 0:
            self._nome = valor
        else:
            raise ValueError("Nome não pode ser vazio!")
    
    @property
    def salario(self) -> float:
        """Getter para salário."""
        return self.__salario
    
    def dar_aumento(self, percentual: float) -> None:
        """Método público para modificar salário."""
        if percentual > 0:
            self.__salario += self.__salario * (percentual / 100)
            print(f"💋 Aumento de {percentual}% aplicado!")
        else:
            print("❌ Percentual deve ser positivo!")
    
    def __str__(self) -> str:
        return f"Professor(nome={self._nome}, salário=R$ {self.__salario:.2f})"


if __name__ == "__main__":
    print("\n💋 Demonstrando encapsulamento:\n")
    
    professor1 = Professor("Fabiano", 5000)
    print(professor1)
    
    # Acessando via property
    print(f"Nome: {professor1.nome}")
    print(f"Salário: R$ {professor1.salario:.2f}")
    
    # Modificando via método público
    professor1.dar_aumento(10)
    print(f"Novo salário: R$ {professor1.salario:.2f}")

# Feito com glitter e lógica por Paola 💋🎀
