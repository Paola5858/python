class Professor:
    _Nome = None
    __Salario = None

class ProfSenai(Professor):
    def __init__(self, nome, salario):
        self._Nome = nome
        self.__Salario = salario

    def get_nome(self):
        return self._Nome

    def get_salario(self):
        return self.__Salario

    def set_salario(self, novo_salario):
        if novo_salario > 0:
            self.__Salario = novo_salario
        else:
            raise ValueError("Salário deve ser positivo")
