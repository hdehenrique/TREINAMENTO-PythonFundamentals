################################
### TRABALHANDO COM EXCEÇÕES 


# Dado o dicionario

# A partir do ID do produto exibir o nome e preço
#Caso produto não exista exibir a mensagem "Produto Inexistente"

# produtos = dict(produtos=dict(p1=dict(nome="Camiseta Star Wars", preco=99.90), 
#                               p2=dict(nome='Caneca Ricky&Morty', preco=49.90), 
#                               p3=dict(nome='Camiseta SpiderMan', preco=69.90)))
# try:
#     produtoID = input('Digite o ID do produto: ')
    
#     if produtoID not in produtos['produtos']:
#         raise ValueError('Produto inexistente!')
#     else:
#         print(f"Produto: {produtos['produtos'][produtoID]['nome']}")
#         print("Preço: {}".format(produtos['produtos'][produtoID]['preco']))
        
# except ValueError as p:
#     print(p)            

###############################
# manipulação de arquivos


# with open('novo arquivo', 'a') as f:
#     f.write('\nMeu primeiro arquivo.')


###############################
# criando funções

# def dobra(valor):
#     return valor * 2

# print(dobra(12))

# produtos = []

# def cadastraProdutos(produto):
#     return produtos.append(produto)

# def listaProdutos():
#     print(produtos)

# def deleteProduto(produto):
#     if produto in produtos:
#         produtos.remove(produto)
#     else:
#         print('Produto inexistente')

# cadastraProdutos('Tenis')
# cadastraProdutos('sapato')
# cadastraProdutos('calca')

# deleteProduto('sapato')

# listaProdutos()


# nome = 'python'

# def linux():
#     global nome # permissão para função alterar nome da variavel global 
#     nome = 'linux'
#     return nome
# linux()
# print(nome)


# def teste(produto: str) -> list:
#     print(var)

# teste()
#usuarios = []

# def cadastra_Pessoa(add=None):
#     #pessoa = dict(nome='Henrique', sobrenome='Santos', idade=32)
#     if  add is None:
#         pass
#     else:
#         usuarios.append(add)

# cadastra_Pessoa('Renato')
# cadastra_Pessoa()
# print(usuarios)


###############################
# *args e **kwargs

# frutas = []

# def inserFrutas(*args):
#     frutas.append(args)

# inserFrutas('abacaxi','laranja','limao','banana')
# print(frutas)

#frutas = []

# def inserFrutas(*args):
#     for f in args:
#         frutas.append(f)
# inserFrutas('abacaxi','laranja','limao','banana')
# print(frutas)

# camisetas = {}
# def insereCamiseta(**kwargs):
#     global camisetas
#     camisetas = kwargs
#     return camisetas

# insereCamiseta(camiseta01='Star Wars',camiseta02='batman')
# print(camisetas)



###############################
# função lambda

# dobro = lambda x: x * 2
# print(dobro(20))

# faca uma função lambida que receba 3 valores e retorne a soma

# soma = lambda n1,n2,n3: n1+n2+n3
# print(soma(10,10,10))

# função MAP - lambda
# numeros = [2,3,4,5,6,7,8,9,10,11]
# dobro = list(map(lambda x: x * 2, numeros))
# print(dobro)

# função FILTER - lambda
# numeros = [2,3,4,5,6,7,8,9,10,11]
# numeros_par = list(filter(lambda x: x % 2 == 0, numeros))
# print(numeros_par)


# função REDUCE - lambda
from functools import reduce

numeros = [2,3,4,5,6,7,8,9,10,11]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)



