# -*- coding: utf-8 -*-

# mvc - modelo visão e controle mais adequado
# cria as classes e gera tabelas no banco

from sqlalchemy import create_engine, Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///lab05-ex04.sqlite")
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'Pessoa'
    idPessoa = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)

    def __init__(self,nome):
        self.nome = nome


class Telefone(Base):
    __tablename__ = 'Telefone'
    idTelefone = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(String)
    idPessoa = Column(Integer, ForeignKey('Pessoa.idPessoa'))
    pessoa = relationship('Pessoa', backref='Telefone')

    def __init__(self,numero,pessoa):
        self.numero = numero
        self.pessoa = pessoa




if __name__ == '__main__':
    #gerar schema
    Base.metadata.create_all(engine)

    session = Session()

    pessoa = Pessoa("felipe")
    pessoa.nome = 'Felipe'
    #pessoa.sobrenome = 'Cardoso' #em python é possível

    session.add(pessoa)



    pessoa_telefone  = Telefone('(48) 8888-8888',pessoa)

    session.add(pessoa_telefone)

    session.commit()
    session.close()
