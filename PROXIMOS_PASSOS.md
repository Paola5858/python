# 🎀 PRÓXIMOS PASSOS - EVOLUÇÃO DO REPOSITÓRIO

## 🚀 Sugestões para deixar ainda mais profissional

### 1. Adicionar Testes Unitários
Crie uma pasta `tests/` e adicione testes para suas funções:

```python
# tests/test_tabuada.py
import pytest
from exercícios.intro_python.tabuada import mostrar_tabuada

def test_tabuada():
    # Testa se a função não quebra
    assert mostrar_tabuada(5) is None
```

**Por que?** Mostra que você sabe testar código, habilidade essencial.

---

### 2. Criar um Projeto Integrado
Junte vários conceitos num mini-projeto, tipo:

**Sistema de Biblioteca:**
- Classes: Livro, Usuario, Biblioteca
- Herança: UsuarioComum, UsuarioPremium
- Enum: StatusLivro (DISPONIVEL, EMPRESTADO, RESERVADO)
- Composição: Biblioteca compõe Livros
- Tratamento de erros: validações

**Por que?** Mostra que você sabe aplicar tudo junto, não só conceitos isolados.

---

### 3. Adicionar Documentação com Sphinx
Gere documentação HTML automática do seu código:

```bash
pip install sphinx
sphinx-quickstart docs
sphinx-apidoc -o docs/source .
```

**Por que?** Documentação profissional impressiona muito.

---

### 4. Configurar CI/CD com GitHub Actions
Crie `.github/workflows/python-tests.yml`:

```yaml
name: Python Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install pytest
      - run: pytest
```

**Por que?** Mostra que você entende DevOps básico.

---

### 5. Adicionar Type Checking com mypy
Crie `mypy.ini`:

```ini
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
```

Execute: `mypy .`

**Por que?** Validação de tipos é prática profissional.

---

### 6. Formatar com Black
```bash
pip install black
black .
```

**Por que?** Código formatado consistentemente é mais legível.

---

### 7. Criar um CLI (Command Line Interface)
Use `argparse` ou `click` para criar comandos:

```bash
python main.py --exemplo tabuada --numero 5
python main.py --exemplo media --notas 7 8
```

**Por que?** CLIs são ferramentas profissionais.

---

### 8. Adicionar Logging
Substitua alguns `print()` por logging:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Calculando tabuada...")
logger.error("Erro ao processar entrada")
```

**Por que?** Logging é essencial em aplicações reais.

---

### 9. Criar um requirements-dev.txt
Separe dependências de desenvolvimento:

```txt
# requirements-dev.txt
pytest>=7.0.0
black>=22.0.0
mypy>=0.950
flake8>=4.0.0
```

**Por que?** Organização profissional de dependências.

---

### 10. Adicionar Badges no README
```markdown
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
```

**Por que?** Badges dão credibilidade visual ao projeto.

---

## 🎯 Prioridades

### Curto prazo (1-2 semanas):
1. ✅ Criar um projeto integrado
2. ✅ Adicionar testes básicos
3. ✅ Configurar Black

### Médio prazo (1 mês):
4. ✅ Adicionar CLI
5. ✅ Configurar mypy
6. ✅ Adicionar badges

### Longo prazo (2-3 meses):
7. ✅ Documentação com Sphinx
8. ✅ CI/CD com GitHub Actions
9. ✅ Logging profissional

---

## 💡 Ideias de Projetos Integrados

### 1. Sistema de Gerenciamento de Tarefas
- Classes: Tarefa, Usuario, Projeto
- Enum: StatusTarefa, Prioridade
- Persistência: JSON ou SQLite
- CLI para adicionar/listar/completar tarefas

### 2. Calculadora de Investimentos
- Classes: Investimento, Carteira, Relatorio
- Cálculos: juros compostos, rentabilidade
- Gráficos simples com matplotlib
- Validações e tratamento de erros

### 3. Sistema de Controle de Estoque
- Classes: Produto, Estoque, Venda
- Enum: CategoriaProduto, StatusProduto
- Relatórios: produtos em falta, mais vendidos
- Persistência em arquivo

### 4. Jogo de Adivinhação Avançado
- Classes: Jogo, Jogador, Ranking
- Diferentes níveis de dificuldade
- Sistema de pontuação
- Persistência de ranking

---

## 📚 Recursos para Estudar

### Python Avançado:
- Real Python (realpython.com)
- Python Docs (docs.python.org)
- PEP 8 Style Guide

### Testes:
- Pytest Documentation
- Test-Driven Development (TDD)

### Boas Práticas:
- Clean Code (Robert C. Martin)
- Design Patterns em Python
- SOLID Principles

---

**Lembre-se:** Não precisa fazer tudo de uma vez! Vá evoluindo aos poucos. 
O importante é mostrar evolução constante no GitHub.

**Feito com glitter e lógica por Paola 💋🎀**
