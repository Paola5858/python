"""
Sistema de controle de acesso a ambientes
Demonstra associação entre classes
Autora: Paola Soares Machado
"""


class Ambiente:
    """Representa um ambiente físico."""
    
    def __init__(self, id: int, nome: str, descricao: str):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    def __str__(self) -> str:
        return f"Ambiente {self.id}: {self.nome} - {self.descricao}"


class Pessoa:
    """Representa uma pessoa com credenciais de acesso."""
    
    def __init__(self, id: int, nome: str, email: str, rfid: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.rfid = rfid

    def __str__(self) -> str:
        return f"Pessoa {self.id}: {self.nome}, Email: {self.email}, RFID: {self.rfid}"


class AmbientePessoa:
    """Associação entre pessoa e ambiente (controle de acesso)."""
    
    def __init__(self, id: int, pessoa: Pessoa, ambiente: Ambiente):
        self.id = id
        self.pessoa = pessoa
        self.ambiente = ambiente

    def __str__(self) -> str:
        return f"Acesso {self.id}: {self.pessoa.nome} → {self.ambiente.nome}"


if __name__ == "__main__":
    print("💋 Sistema de controle de acesso:\n")
    
    p1 = Pessoa(1, "Paola", "paola@email.com", "RF12345")
    p2 = Pessoa(2, "Squeruque", "squeruque@email.com", "RF67890")

    a1 = Ambiente(1, "Laboratório de Informática", "Acesso restrito")
    a2 = Ambiente(2, "Biblioteca", "Acesso livre")

    acesso1 = AmbientePessoa(1, p1, a1)
    acesso2 = AmbientePessoa(2, p1, a2)
    acesso3 = AmbientePessoa(3, p2, a2)

    print(acesso1)
    print(acesso2)
    print(acesso3)

# Feito com glitter e lógica por Paola 💋🎀
