from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Livro


def emprestar_livro(session:Session, titulo):
    """Marque um livro como indisponível."""
    livro = session.execute(select(Livro).where(Livro.titulo == titulo)).scalar_one_or_none()
    if not livro or not livro.disponivel:
        return None
    livro.disponivel = False
    session.commit()
    print(f'Livro {titulo} emprestado com sucesso')

def devolver_livro(session:Session, titulo):
    """Marque um livro como disponível."""
    livro = session.execute(select(Livro).where(Livro.titulo == titulo)).scalar_one_or_none()
    if not livro or livro.disponivel:
        return None
    livro.disponivel = True
    session.commit()
    print(f'Livro {titulo} devolvido com sucesso')
