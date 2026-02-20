"""
Testando arrays e listas em Python
Autora: Paola Soares Machado
"""
import array
from typing import List


def demonstrar_array() -> None:
    """Demonstra uso de array.array (tipo fixo)."""
    print("💋 Arrays (tipo fixo):")
    numeros = array.array('i', [1, 2, 3, 4, 5])
    print(f"Array de inteiros: {numeros}")
    print(f"Elemento no índice 1: {numeros[1]}")
    print(f"Tamanho: {len(numeros)}\n")


def demonstrar_lista() -> None:
    """Demonstra uso de listas (tipo flexível)."""
    print("💋 Listas (tipo flexível):")
    letras: List[str] = ['a', 'b', 'c']
    print(f"Lista inicial: {letras}")
    print(f"Elemento no índice 2: {letras[2]}")
    
    letras.append('d')
    print(f"Após append('d'): {letras}")
    
    letras.append('nome')
    print(f"Após append('nome'): {letras}")
    
    letras.remove('b')
    print(f"Após remove('b'): {letras}\n")


def demonstrar_tupla() -> None:
    """Demonstra uso de tuplas (imutáveis)."""
    print("💋 Tuplas (imutáveis):")
    teste = (1, 2, 3, 4)
    print(f"Tupla: {teste}\n")


def demonstrar_loops() -> None:
    """Demonstra diferentes formas de loops."""
    print("💋 Loops:")
    
    print("Range de 1 a 10:")
    for i in range(1, 11):
        print(i, end=" ")
    print("\n")
    
    letras = ['a', 'b', 'c', 'd']
    print(f"Iterando sobre lista {letras}:")
    for letra in letras:
        print(letra, end=" ")
    print("\n")
    
    numeros = array.array('i', [1, 2, 3, 4, 5])
    print(f"Iterando sobre array {list(numeros)}:")
    for num in numeros:
        print(num, end=" ")
    print()


if __name__ == "__main__":
    print("\n" + "="*50)
    print("💋 DEMONSTRAÇÃO: ARRAYS, LISTAS E LOOPS")
    print("="*50 + "\n")
    
    demonstrar_array()
    demonstrar_lista()
    demonstrar_tupla()
    demonstrar_loops()

# Feito com glitter e lógica por Paola 💋🎀
