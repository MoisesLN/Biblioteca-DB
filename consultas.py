from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Autor, Livro


def listar_livros(session:Session):
    livros = session.execute(select(Livro)).scalars().all()
    livrosArray = []
    for livro in livros:
        livrosArray.append(f'Titulo: {livro.titulo} | Autor: {livro.autor.nome} | Disponivel: {livro.disponivel}')
    print(livrosArray)


def listar_livros_disponiveis(session:Session):
    livros = session.execute(select(Livro)).scalars().all()
    livrosArray = []
    for livro in livros:
        if livro.disponivel:
            livrosArray.append(f'Titulo: {livro.titulo} | Autor: {livro.autor.nome}')
    print(livrosArray)


def buscar_livros_por_titulo(session:Session, trecho):
    livros = session.execute(select(Livro).where(Livro.titulo.contains(trecho))).scalars().all()
    livrosArray = []
    for livro in livros:
        livrosArray.append(f'Titulo: {livro.titulo} | Autor: {livro.autor.nome}')
    print(livrosArray)


def listar_livros_por_autor(session:Session, nome_autor):
    autor = session.execute(select(Autor).where(Autor.nome == nome_autor)).scalar_one_or_none()
    if autor:
        print(f'Livros de {autor.nome}')
        for livro in autor.livros:
            print(f'titulo: {livro.titulo} - Disponivel: {livro.disponivel}')