"""
Funções anônimas (lambda) em Python
Autora: Paola Soares Machado
"""
from typing import List, Dict


def demonstrar_lambda_basico() -> None:
    """Demonstra uso básico de lambda."""
    print("💋 Lambda básico:\n")
    
    # Função normal vs lambda
    def quadrado_normal(x: int) -> int:
        return x ** 2
    
    quadrado_lambda = lambda x: x ** 2
    
    print(f"Função normal: quadrado(5) = {quadrado_normal(5)}")
    print(f"Lambda: quadrado(5) = {quadrado_lambda(5)}\n")


def demonstrar_map() -> None:
    """Demonstra lambda com map."""
    print("💋 Lambda com map:\n")
    
    numeros = [1, 2, 3, 4, 5]
    dobrados = list(map(lambda x: x * 2, numeros))
    print(f"Números: {numeros}")
    print(f"Dobrados: {dobrados}\n")


def demonstrar_filter() -> None:
    """Demonstra lambda com filter."""
    print("💋 Lambda com filter:\n")
    
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    print(f"Números: {numeros}")
    print(f"Apenas pares: {pares}\n")


def demonstrar_sorted() -> None:
    """Demonstra lambda com sorted."""
    print("💋 Lambda com sorted:\n")
    
    pessoas: List[Dict[str, any]] = [
        {"nome": "Paola", "idade": 17},
        {"nome": "Major", "idade": 19},
        {"nome": "Squeruque", "idade": 18}
    ]
    
    # Ordenar por idade
    por_idade = sorted(pessoas, key=lambda p: p["idade"])
    print("Pessoas ordenadas por idade:")
    for p in por_idade:
        print(f"  {p['nome']}: {p['idade']} anos")
    print()


if __name__ == "__main__":
    print("\n" + "="*50)
    print("💋 FUNÇÕES ANÔNIMAS (LAMBDA)")
    print("="*50 + "\n")
    
    demonstrar_lambda_basico()
    demonstrar_map()
    demonstrar_filter()
    demonstrar_sorted()

# Feito com glitter e lógica por Paola 💋🎀
