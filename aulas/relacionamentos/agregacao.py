"""
Agregação: objetos existem independentemente
Autora: Paola Soares Machado
"""
from typing import List


class Aluno:
    """Representa um aluno."""
    
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self) -> str:
        return self.nome


class Turma:
    """Representa uma turma que agrega alunos."""
    
    def __init__(self, nome: str):
        self.nome = nome
        self.alunos: List[Aluno] = []  # agregação

    def adicionar(self, aluno: Aluno) -> None:
        self.alunos.append(aluno)

    def listar_alunos(self) -> List[str]:
        return [str(aluno) for aluno in self.alunos]


if __name__ == "__main__":
    print("\n💋 Agregação: Turma e Alunos\n")
    
    # alunos existem independente da turma
    a1 = Aluno("Squeruque")
    a2 = Aluno("Major")

    turma = Turma("3º Info")
    turma.adicionar(a1)
    turma.adicionar(a2)

    print(f"Turma: {turma.nome} | Alunos: {turma.listar_alunos()}")

# Feito com glitter e lógica por Paola 💋🎀
