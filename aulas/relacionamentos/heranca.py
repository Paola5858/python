"""
Herança: reutilizando código de forma elegante
Autora: Paola Soares Machado
"""


class Pessoa:
    """Classe base representando uma pessoa."""
    
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def bio(self) -> str:
        return f"{self.nome}, {self.idade} anos"


class Estudante(Pessoa):
    """Estudante herda de Pessoa e adiciona curso."""
    
    def __init__(self, nome: str, idade: int, curso: str):
        super().__init__(nome, idade)  # pega atributos da classe pai
        self.curso = curso

    def bio(self) -> str:
        return super().bio() + f" | Curso: {self.curso}"


if __name__ == "__main__":
    aluno = Estudante("Paola", 18, "Informática")
    print(f"💋 {aluno.bio()}")

# Feito com glitter e lógica por Paola 💋🎀
