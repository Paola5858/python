class Professor:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor  # associação (referência)

    def detalhes(self):
        return f"{self.nome} | Prof: {self.professor}"

prof = Professor("marcelo")
mat = Disciplina("banco de dados", prof)

print(mat.detalhes())
