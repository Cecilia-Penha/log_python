
from tabela import table
from ler import metadados

import re

def main():

    #inicia tabela
    start = set()
    commit = set()
    undo = set()
    redo = set()
    #checar linhas
    try:
        with open('C:/Users/cecil/OneDrive/Documentos/files/undo_redo/entrada.txt','r')as file:
            for linha in file:
                linha = re.sub('\n', '', linha).strip()
                #checar inicio transacao
                if (re.match('^<start .+>', linha)):
                    #adiciona transacoes iniciadas
                    t = re.sub('<start|>','',linha).strip()#isola o nome da transacao
                    start.add(t)
                if (re.match('^<commit .+>', linha)):
                    #adiciona transacoes commitadas
                    t = re.sub('<commit|>','',linha).strip()
                    commit.add(t)
            for t in start:
                if t in commit:#se nao tem commit recebe undo
                    redo.add(t)
                else:
                    undo.add(t)
            for i in undo:
                print('Transacao', i ,'recebe undo')
            for i in redo:
                print('Transacao', i ,'recebe redo')
    except Exception:
        print('Erro'+Exception)
        exit()
main()
