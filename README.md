# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

1. Para que serve o campo `disponivel` em `Livro`?
Para a funcionalidade de emprestar livros. Se tá emprestado, disponivel=False.

2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?
Para enviar o novo status para o banco de dados.

3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?
Listar livros por autor.