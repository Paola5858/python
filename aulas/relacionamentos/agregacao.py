class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []   # agregação

    def adicionar(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        return [str(aluno) for aluno in self.alunos]

# alunos existem independente da turma
a1 = Aluno("squeruque")
a2 = Aluno("major")

turma = Turma("3º info")
turma.adicionar(a1)
turma.adicionar(a2)

print(f"Turma: {turma.nome} | Alunos: {turma.listar_alunos()}")
