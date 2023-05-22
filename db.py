import psycopg2
from config import config
#conecta e executa consulta
def exec(sql):
    conn = None
    consulta = None
    try:
        params = config()
        print('Conectando')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)

        if cur.pgresult_ptr is not None:
            consulta = cur.fetchall()
       
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
         print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Desconectando')
        return consulta
#cria tabela
def createTable():
    exec('''
         create table tabela(
            id serial primary key,
            a int not null,
            b int not null
        )
        ''')
#deleta tabela
def dropTable():
    exec('drop table if exists tabela')
#insere na tabela
def insert(a, b):
    exec(f'insert into tabela(a, b) values ({a}, {b})')

