from sqlalchemy import update
from core import user_table, engine

con = engine.connect()

atualizacao = input('Digite o nome do usuário: ')

atualizar = update(user_table).where(user_table.c.nome == atualizacao)

novo_nome = input('Digite o novo nome: ')

atualizar = atualizar.values(nome=novo_nome)
resultado = con.execute(atualizar)
print(resultado.rowcount)