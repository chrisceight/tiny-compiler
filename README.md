# tiny-compiler
Tiny Compiler: Mini compilador em Python que integra análise léxica, sintática e geração de bytecode com uma VM simples.

---

### Funcionalidades principais
- **Linguagem**: números inteiros, identificadores, operadores `+ - * /`, atribuição `=`, `print(expr)` e `;` como separador.  
- **Pipeline**: lexer → parser recursivo descendente → AST → gerador de bytecode → VM.  
- **Testes**: exemplos e testes de integração com `pytest`.  
- **CI**: workflow GitHub Actions para rodar testes em pushes e pull requests.

---

### Requisitos
- **Python 3.8+**  
- Opcional: `virtualenv`, `pytest`, `flake8` para lint e testes

---

### Instalação rápida
```bash
git clone git@github.com:SEU_USUARIO/tiny-compiler.git
cd tiny-compiler
python -m venv .venv
# Linux macOS
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

### Uso básico
1. Crie um arquivo `program.tiny` com um programa tiny, por exemplo:
```tiny
a = 2 + 3 * (4 + 1);
print(a);
```
2. Rode o compilador e a VM:
```bash
python main.py
```
3. Saída esperada:
```
17
```

---

### Estrutura do projeto
- **`lexer.py`** — tokenizador simples.  
- **`ast.py`** — definições de nós da AST.  
- **`parser.py`** — parser recursivo descendente que produz AST.  
- **`codegen.py`** — gera bytecode a partir da AST.  
- **`vm.py`** — máquina virtual que executa o bytecode.  
- **`main.py`** — pipeline de compilação e execução.  
- **`program.tiny`** — exemplo de programa.  
- **`tests/`** — testes com `pytest`.  
- **`.github/workflows/ci.yml`** — workflow de CI para testes.

---

### Testes e CI
- Execute testes localmente:
```bash
pytest -q
```
- O repositório já inclui um workflow GitHub Actions que roda `pytest` em pushes e pull requests. Basta fazer push para que a CI valide o código.

---

### Boas práticas e próximos passos
- Separe responsabilidades por módulos e mantenha commits pequenos e atômicos.  
- Adicione mais instruções à linguagem, tratamento de erros sintáticos e semânticos, e otimizações simples.  
- Experimente gerar C ou LLVM IR em vez de bytecode para estudar geração de código real.

---

### Contribuição
- **Fork** o repositório, crie uma branch de feature e abra um pull request.  
- Escreva testes para novas funcionalidades e garanta que a CI passe antes do merge.  
- Use mensagens de commit claras como `feat: lexer`, `fix: parser precedence`, `test: add integration test`.

---

### Licença
**MIT** — sinta‑se livre para estudar, modificar e redistribuir com atribuição.
