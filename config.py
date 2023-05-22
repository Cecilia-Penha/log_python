from configparser import ConfigParser
#ler arquivo database
def config(filename='database.ini', section='postgresql'):
    
    parser = ConfigParser()
    
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('erro')
    return db
