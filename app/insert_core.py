from core import user_table, engine

con = engine.connect()
insert = user_table.insert()

# new = insert.values(idade=25, nome='Caio', senha='abacaxi123')
# con.execute(new)

con.execute(user_table.insert(),[
    {'nome':'marcio 2', 'idade':20, 'senha':'limao123'},
    {'nome':'gustavo 2', 'idade':18, 'senha':'goiaba123'},
    {'nome':'guilherme 2', 'idade':31, 'senha':'melancia123'}
] )