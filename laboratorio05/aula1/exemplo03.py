# -*- coding: utf-8 -*-
#Mapeamento objeto relacional - ORM
from sqlalchemy import create_engine, and_ , or_
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("sqlite:///lab05-ex01.sqlite")
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = automap_base()
    Base.prepare(engine,reflect=True)

    Pessoa = Base.classes.Pessoa   #tenho que saber nome de cada tabela
    Telefones = Base.classes.Telefones

    lista_pessoas = session.query(Pessoa).join(Telefones).all()  #para inner join [join(Telefones,"comparação")]

    # for linha in lista_pessoas:
    #     print("Nome {}\t".format(linha.nome))
    #     for tel in linha.telefones_collection:  #
    #         print("Telefone: {}".format(tel.numero))

    pessoas = session.query(Pessoa).filter(Pessoa.nome.ilike('J%')).all()
    for linha in pessoas:
        print("Nome {}\t".format(linha.nome))
        for tel in linha.telefones_collection:  #
            print("Telefone: {}".format(tel.numero))





    # lista_de_pessoas = session.query(Pessoa).all();
    #
    # for pessoa in lista_de_pessoas :
    #     print("id: {}\t Nome:{}".format(pessoa.idPessoa,pessoa.nome))
    #
    #
    #
    # lista_de_telefones = session.query(Telefones).all();
    #
    # for telefones in lista_de_telefones:
    #     print("idTelefone: {}\t Telefone:{}\tidPessoa:{}".format(telefones.idTelefone,telefones.numero,telefones.idPessoa))
    #
    #
    #