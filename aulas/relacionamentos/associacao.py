"""
Associação: relacionamento entre classes independentes
Autora: Paola Soares Machado
"""


class Professor:
    """Representa um professor."""
    
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self) -> str:
        return self.nome


class Disciplina:
    """Representa uma disciplina associada a um professor."""
    
    def __init__(self, nome: str, professor: Professor):
        self.nome = nome
        self.professor = professor  # associação (referência)

    def detalhes(self) -> str:
        return f"{self.nome} | Prof: {self.professor}"


if __name__ == "__main__":
    print("\n💋 Associação entre Disciplina e Professor:\n")
    prof = Professor("Marcelo")
    mat = Disciplina("Banco de Dados", prof)
    print(mat.detalhes())

# Feito com glitter e lógica por Paola 💋🎀
