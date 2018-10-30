# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, and_ , or_
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("sqlite:///lab05-aula1.sqlite")
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = automap_base()
    Base.prepare(engine,reflect=True)

#https://www.pythonsheets.com/notes/python-sqlalchemy.html

    Contato = Base.classes.Contato

    lista_de_contatos = session.query(Contato).all()

    for contato in lista_de_contatos:
        print("Id: {}\t Nome: {}\t telefone: {}".format(contato.idContato,contato.nome,contato.telefone))


    felipe = session.query(Contato).filter(and_(Contato.nome == 'felipe',Contato.telefone == '8888-8888')).first()

    print("Telefone de {} é {}".format(felipe.nome,felipe.telefone))

    felipe.nome = 'felipe'

    print("Telefone de {} é {}".format(felipe.nome, felipe.telefone))

    #session.commit()