import ler
import db 
from db import exec
#colocar dados na tabela
def criaTabela():
    dados = ler.metadados()
    for i in dados:
        db.insert(i[0], i[1])
    for i in dados:
        print(i)
#criar tabela e popular
def table():
    db.dropTable()

    db.createTable()

    criaTabela()
table()
