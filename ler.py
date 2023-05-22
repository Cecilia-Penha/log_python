import json
#ler metadados a partir do inicio
def metadados():
    dados = None
    try:
        f = open('metadado.json')
        dados = json.load(f)['INITIAL']
        f.close()
    except:
        print('erro na leitura')
        exit()
    return list(zip(dados['A'], dados['B']))#retorna lista de tuplas