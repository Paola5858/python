# Laboratório de Python da Paola 💻✨

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Tests](https://img.shields.io/badge/tests-pytest-green.svg)
![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)

Repositório onde eu guardo meus experimentos de Python: dos primeiros `print()` até orientação a objetos, enum e relações entre classes.

Não é "aquele" projeto gigante, é mais um raio-x da minha evolução no código.

## O que tem aqui

### 📁 `aulas/`
Exercícios feitos durante as aulas:
- **intro-python/**: primeiros passos com Python
- **array/**: manipulação de listas e loops
- **classe/**: introdução a POO (classes, encapsulamento, funções anônimas)
- **relacionamentos/**: herança, associação, agregação e composição

### 📁 `exercícios/`
Exercícios práticos organizados por tema:

#### `intro-python/`
- Lógica básica: tabuada, média, soma
- Estruturas de controle (`if`, `for`, `while`)

#### `array/`
- Manipulação de listas
- Cálculo de média com `for`
- Filtragem de números pares
- Tabuada usando loops

#### `classe/`
- **POO na veia:**
  - Classes e objetos
  - Herança e polimorfismo
  - Associação, agregação e composição
  - Encapsulamento
  - Uso de `Enum` para representar estados
- **Projetos mini:**
  - Sistema de controle de acesso (ambiente.py)
  - Gerenciamento de pedidos com estados (enum.py)
  - Formas geométricas com polimorfismo (poliformismo.py)

## Como rodar

**Pré-requisitos:**  
- Python 3.x instalado

**Clonar o repositório:**
```bash
git clone https://github.com/Paola5858/python.git
cd python
```

**Rodar alguns exemplos:**

```bash
# Menu interativo (recomendado)
python main.py

# Fundamentos
python exercícios/intro-python/tabuada.py
# Saída: Exibe tabuada de 1 a 10 do número digitado

python exercícios/intro-python/media.py
# Saída: Calcula média e mostra se aprovado (≥7) ou reprovado

# Arrays
python exercícios/array/media_com_for.py
# Saída: 💋 A média dessas notas babadeiras foi: 8.10

python exercícios/array/pares_com_for.py
# Saída: Filtra e exibe apenas números pares da lista

# POO
python exercícios/classe/poliformismo.py
# Saída: Calcula áreas de diferentes formas geométricas

python exercícios/classe/enum.py
# Saída: Demonstra fluxo de pedido com estados (Enum)

python exercícios/classe/ambiente.py
# Saída: Sistema de controle de acesso (associação)

# Herança
python aulas/relacionamentos/heranca.py
# Saída: 💋 Paola, 18 anos | Curso: Informática
```

**Rodar testes:**

```bash
# Instalar dependências de desenvolvimento
pip install -r requirements-dev.txt

# Executar todos os testes
pytest

# Executar com cobertura
pytest --cov=exercícios --cov=aulas
```

## Por que esse repositório existe?

Porque eu não estudo só pra prova. Uso esses exercícios pra:

✨ Treinar raciocínio lógico  
✨ Testar formas diferentes de resolver o mesmo problema  
✨ Brincar com conceitos de POO que vou usar em projetos maiores (APIs, jogos, etc.)  
✨ E claro: pra qualquer pessoa que abrir meu GitHub ver que eu tô construindo base sólida, não só copiando código pronto

## Destaques técnicos

- ✅ Type hints em todas as funções
- ✅ Tratamento de exceções
- ✅ Docstrings explicativas
- ✅ Uso de `if __name__ == "__main__"` para execução direta
- ✅ Padrões de POO aplicados (herança, polimorfismo, encapsulamento)
- ✅ Uso de Enum para estados
- ✅ Código limpo e legível
- ✅ Testes automatizados com pytest
- ✅ Separação de dependências (prod/dev)

---

**Feito com glitter e lógica por Paola 💋🎀**
