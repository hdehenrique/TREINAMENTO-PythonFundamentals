# -*- coding: UTF-8 -*-

# VERIFICA A VERSAO DO PYTHON QUE O CODIGO É COMPATIVEL E EXECUTA O CODIGO
# from __future__ import print_function

# x = 1

# while x < 10:
#     print(x)
#     x += 1

# usuarios = ['renato','carlos','maria','fabio','paloma']

# while True:
#     login = input('Digite os eu usuário: ')
#     if login not in usuarios:
#         print('usuário não cadastrado!')
#         continue
#     else:
#         print('login efetuado')
#         break


# usuarios = dict(renato='abacaxi123', carlos='fusca123', maria='teste321')

# bloqueados = []
# tentativas = 0

# while True:
#     login = input('Digite o seu usuario: ')
#     if login in usuarios:
#         senha = input('Digite sua senha: ')
#         if senha == usuarios[login]:
#             print('login efetuado!')
#             break
#         elif tentativas < 3:
#             print('Senha Incorreta!')
#             tentativas += 1
#             continue
#         else:
#             print('Usuário bloqueado, contate o administrador')
#             bloqueados.append(login)
#             usuarios.pop(login)
#             break
#     else:
#         print('Usuário não cadastrado')
#         continue


# Exemplo FOR
#frutas = ['uva','banana','laranja']

# modelo 1
# for f in frutas:
#     print(f)

#modelo 2
# for i,f in enumerate(frutas):
#     print(i,f)


# usuarios = dict(renato='teste123',carlos='teste123',maria='teste123')

# for user in usuarios:
#     print(user)

