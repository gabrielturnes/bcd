# -*- coding: utf-8 -*-

#PEP8

import sqlite3

if __name__ == '__main__':
    print("lab05 bcd")
    conexao = sqlite3.connect('lab05-aula1.sqlite')
    cursor = conexao.cursor()

    nome = ('Cardoso',)
    telefone = ('8888-8888',)
    cursor.execute("SELECT * FROM Contato WHERE telefone = ?",telefone)
    #print(cursor.fetchall())

    for linha in cursor.fetchall():
        print('Id: {}\t Nome: {}\t telefone: {}'.format(linha[0],linha[1],linha[2]))

    cursor.close()
    conexao.close()