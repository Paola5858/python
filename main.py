# -*- coding: utf-8 -*-
"""
Menu principal do laboratório Python
Demonstra os principais conceitos estudados
Autora: Paola Soares Machado
"""
import sys
import os

# Configura encoding para UTF-8
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Adiciona os diretórios ao path para importar os módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'exercícios'))


def menu_principal() -> None:
    """Exibe menu interativo com os principais exemplos."""
    while True:
        print("\n" + "="*50)
        print("💋 LABORATÓRIO PYTHON DA PAOLA 💋".center(50))
        print("="*50)
        print("\n📚 Escolha um exemplo para rodar:\n")
        print("  [1] Tabuada")
        print("  [2] Cálculo de média")
        print("  [3] Polimorfismo (formas geométricas)")
        print("  [4] Enum (controle de pedidos)")
        print("  [5] Sistema de controle de acesso")
        print("  [6] Herança (Pessoa → Estudante)")
        print("  [0] Sair")
        print("\n" + "="*50)
        
        try:
            opcao = input("\n✨ Digite sua escolha: ").strip()
            
            if opcao == "0":
                print("\n💋 Até logo, diva! Feito com glitter e lógica por Paola 🎀")
                break
            elif opcao == "1":
                executar_tabuada()
            elif opcao == "2":
                executar_media()
            elif opcao == "3":
                executar_polimorfismo()
            elif opcao == "4":
                executar_enum()
            elif opcao == "5":
                executar_ambiente()
            elif opcao == "6":
                executar_heranca()
            else:
                print("\n❌ Opção inválida! Escolhe uma das opções do menu, gata.")
        except KeyboardInterrupt:
            print("\n\n💋 Até logo! Feito com glitter e lógica por Paola 🎀")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")


def executar_tabuada() -> None:
    """Executa exemplo de tabuada."""
    print("\n" + "─"*50)
    print("📊 TABUADA")
    print("─"*50)
    try:
        numero = int(input("Digite um número: "))
        print(f"\n💋 Tabuada do {numero}:")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    except ValueError:
        print("❌ Digite um número inteiro válido!")


def executar_media() -> None:
    """Executa exemplo de cálculo de média."""
    print("\n" + "─"*50)
    print("📝 CÁLCULO DE MÉDIA")
    print("─"*50)
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        media = (nota1 + nota2) / 2
        print(f"\n📊 Média: {media:.2f}")
        if media >= 7:
            print("💖 APROVADO! Parabéns diva!")
        else:
            print("💔 REPROVADO! Continue estudando!")
    except ValueError:
        print("❌ Digite números válidos!")


def executar_polimorfismo() -> None:
    """Demonstra polimorfismo com formas geométricas."""
    import math
    
    print("\n" + "─"*50)
    print("🔷 POLIMORFISMO - FORMAS GEOMÉTRICAS")
    print("─"*50)
    
    class Forma:
        def calcular_area(self) -> float:
            raise NotImplementedError()
    
    class Retangulo(Forma):
        def __init__(self, largura: float, altura: float):
            self.largura = largura
            self.altura = altura
        
        def calcular_area(self) -> float:
            return self.largura * self.altura
        
        def __str__(self) -> str:
            return f"Retângulo ({self.largura}x{self.altura})"
    
    class Circulo(Forma):
        def __init__(self, raio: float):
            self.raio = raio
        
        def calcular_area(self) -> float:
            return math.pi * (self.raio ** 2)
        
        def __str__(self) -> str:
            return f"Círculo (raio {self.raio})"
    
    formas = [Retangulo(5, 10), Circulo(7)]
    print("\n💋 Calculando áreas:\n")
    for forma in formas:
        print(f"{forma} → Área: {forma.calcular_area():.2f}")


def executar_enum() -> None:
    """Demonstra uso de Enum com controle de pedidos."""
    from enum import Enum
    
    print("\n" + "─"*50)
    print("📦 ENUM - CONTROLE DE PEDIDOS")
    print("─"*50)
    
    class StatusPedido(Enum):
        PENDENTE = "Pendente"
        PROCESSANDO = "Processando"
        ENVIADO = "Enviado"
        ENTREGUE = "Entregue"
    
    class Pedido:
        def __init__(self, id: int):
            self.id = id
            self.status = StatusPedido.PENDENTE
        
        def processar(self) -> None:
            self.status = StatusPedido.PROCESSANDO
            print(f"✅ Pedido {self.id}: {self.status.value}")
        
        def enviar(self) -> None:
            self.status = StatusPedido.ENVIADO
            print(f"✅ Pedido {self.id}: {self.status.value}")
        
        def entregar(self) -> None:
            self.status = StatusPedido.ENTREGUE
            print(f"✅ Pedido {self.id}: {self.status.value}")
    
    print("\n💋 Fluxo de pedido:\n")
    pedido = Pedido(101)
    pedido.processar()
    pedido.enviar()
    pedido.entregar()


def executar_ambiente() -> None:
    """Demonstra associação entre classes."""
    print("\n" + "─"*50)
    print("🏢 SISTEMA DE CONTROLE DE ACESSO")
    print("─"*50)
    
    class Pessoa:
        def __init__(self, nome: str, rfid: str):
            self.nome = nome
            self.rfid = rfid
    
    class Ambiente:
        def __init__(self, nome: str):
            self.nome = nome
    
    class AmbientePessoa:
        def __init__(self, pessoa: Pessoa, ambiente: Ambiente):
            self.pessoa = pessoa
            self.ambiente = ambiente
        
        def __str__(self) -> str:
            return f"✅ {self.pessoa.nome} → {self.ambiente.nome}"
    
    print("\n💋 Registros de acesso:\n")
    p1 = Pessoa("Paola", "RF12345")
    a1 = Ambiente("Laboratório de Informática")
    acesso = AmbientePessoa(p1, a1)
    print(acesso)


def executar_heranca() -> None:
    """Demonstra herança."""
    print("\n" + "─"*50)
    print("👥 HERANÇA - PESSOA E ESTUDANTE")
    print("─"*50)
    
    class Pessoa:
        def __init__(self, nome: str, idade: int):
            self.nome = nome
            self.idade = idade
        
        def bio(self) -> str:
            return f"{self.nome}, {self.idade} anos"
    
    class Estudante(Pessoa):
        def __init__(self, nome: str, idade: int, curso: str):
            super().__init__(nome, idade)
            self.curso = curso
        
        def bio(self) -> str:
            return super().bio() + f" | Curso: {self.curso}"
    
    print("\n💋 Exemplo de herança:\n")
    aluno = Estudante("Paola", 18, "Informática")
    print(f"✨ {aluno.bio()}")


if __name__ == "__main__":
    menu_principal()

# Feito com glitter e lógica por Paola 💋🎀
