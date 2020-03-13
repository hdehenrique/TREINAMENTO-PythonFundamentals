
### conexão PostgreSQL

# import psycopg2

# def insert_in_table(nome, conteudo):    
#     try:
#         con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")
#         cur = con.cursor()

#         cur.execute(f"insert into scripts(nome, conteudo) values('{nome}', '{conteudo}')")
#         con.commit()
#         #print(f"O primeiro registro é {cur.fetchone()}")
#         #print(f"Todos os outros {cur.fetchall()}")
#         print('Registro criado com sucesso!')

#     except Exception as e:
#         print(f'Erro: {e}')
#         print('\nFazendo rollback')
#         con.rollback()

#     finally:
#         print('\nFinalizando a conexão')
#         cur.close()
#         con.close()

# insert_in_table('mongoDB_1','TesteInsert_1')

### conexao com MongoDB

from pymongo import MongoClient

client = MongoClient('localhost')
db = client['dexterops']

def insert_dados():
    db.fila.insert({
        "_id":13, 
        "empresa":"4linux",
        "cursos": [
            {"nome":"InfraAgil",
            "carga horaria":40},
            {"nome":"Continuos monitoring",
            "carga horaria":40}
        ]})

def select_dados():

    for r in db.fila.find():
        print(f"Empresa: {r['empresa']}")
        for c in r['cursos']:
            print('===========')
            print(f"Nome: {c['nome']}, \nCarga horaria:{c['carga horaria']}\n")

insert_dados()
