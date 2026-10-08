from models import Autor, Livro
from sqlalchemy.orm import Session


def popular_banco(session: Session):
    """Cadastre autores e livros iniciais para testar a aplicação."""

    # 1. Crie os objetos Autor separadamente
    autor1 = Autor(nome='Davi Delon', pais='Pilões')
    autor2 = Autor(nome='Crhis Cahlilok', pais='Pau dos ferros')
    autor3 = Autor(nome='Davi Nego', pais='Volta redonda')

    # 2. Associe os livros diretamente na lista de cada autor
    # O SQLAlchemy preencherá 'autor_id' e 'autor' automaticamente por baixo dos panos.
    autor1.livros = [
        Livro(titulo='O fim de Cris Kalil', ano='2027', autor_id=1, autor=autor1, disponivel=False),
        Livro(titulo='O Reinício de Cris Kalil', ano='2028', autor_id=1, autor=autor1),
    ]

    autor2.livros = [
        Livro(titulo='A queda de Davi Delon', ano='2030', autor_id=2, autor=autor2, disponivel=False),
        Livro(titulo='A cagada trevosa de Delon que assustou o mundo', ano='2026', autor_id=2, autor=autor2),
    ]

    autor3.livros = [
        Livro(titulo='O homem que sobrou na curva...', ano='2026', autor_id=3, autor=autor3),
        Livro(titulo='O menino que descobriu a performance', ano='2027', autor_id=3, autor=autor3),
    ]

    session.add_all([autor1, autor2, autor3])
    session.commit()