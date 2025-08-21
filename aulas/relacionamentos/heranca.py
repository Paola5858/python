class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def bio(self):
        return f"{self.nome}, {self.idade} anos"

# Estudante herda de Pessoa
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)   # pega atributos da classe pai
        self.curso = curso

    def bio(self):
        return super().bio() + f" | Curso: {self.curso}"

aluno = Estudante("paola", 18, "informática")
print(aluno.bio())
