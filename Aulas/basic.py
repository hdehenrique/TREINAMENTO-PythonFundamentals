#!/usr/bin/python3
# Iso é um comentário
# """
# Essa é a documentação do código.
# """
#print("Esse é um código em python")

#endereco = "rua vergueiro,  3057"

# MÉTODOS DE STRING 
#print(endereco.capitalize())
#print(endereco.count('e'))
#print(endereco.upper())
#print(endereco.lower())
#print(endereco.upper())
#print(endereco.split(' '))
#print(endereco.replace('e', 'A'))

# vdd = True
# fal = False
# print(vdd.numerator)
# print(fal.numerator)

# n1 = int(input('Digite o primeiro numero: '))
# n2 = int(input('Digite o segundo numero: '))

# print(n1+n2)

#TRABALHANDO COM LISTAS
# lista = ['a','b','c','12','15','teste','casa']
# #print(lista)
# #print(lista[5])
# #print(len(lista))

# lista[0] = 'cachorro'
# print(lista)


#lista = ['teste','casa',['N1','N2','N3']]
#print(lista)
#print(lista[5])
#print(len(lista))
#print(lista[2][2])

# lista.append(145)
# lista.insert(2,True)
# lista.pop(2)
# print(lista)

#DADO A LISTA

# #EXIBA AS CORES DOS TIMES
# #time: <nome_time>, cores:<cores_time>
# times = [['Corinthians','Palmeiras','São Paulo'],['Preto','Branco','Vermelho','Verde']]
# #time: <nome_time>, cores:<cores_time>
# print(times[0][0], times[1][0]) 
# print(times[0][1], times[1][3]) 
# print(times[0][2], times[1][2]) 

#TUPLA

# linguagens = ('python','java','golang')
# print(linguagens)
# print(linguagens[0])
# print(linguagens[0].upper())

#DICIONARIOS

# carros = {'modelos': {'Fox','Fusca','palio'},
#           'anos': {2003,1978,2002}}
# print(carros['modelos'])
# print(carros['anos'])

# produtos = {'produtos': {'001':{'nome': 'Camiseta SpiderMan',
#                                 'preco': 99.90},
#                          '002':{'nome': 'Camiseta Star Wars',
#                                 'preco': 79.90}          
#                         }
#            }        

# print(produtos['produtos']['002']['preco'])
# print(produtos['produtos']['001']['nome'])

# produtos['produtos']['001']['preco']=29.90
# print(produtos)

# CONVERSÃO DE VALORES

# ano = '2020'

# #print(ano.isnumerc())
# print(int(ano))

# ESTRUTURA DE CONDIÇÃO

# idade = int(input('Digite sua idade: '))

# if idade >= 18:
#     print('Você é maior de idade!')  
# else:
#     print('Você é menor de idade!')



# Faça um programe que receba 4 notas de aluno:
# calcule a média
# caso seja menor que 7 imprima "Reprovado"
# caso seja maior que 5 e menor que 7 imprima "Recuperação"
# caso contrário "Aprovado"

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

media = (n1+n2+n3+n4)/4

if media >= 7:
    print('Aluno aprovado, média igual:', media)
elif media >= 5 and media < 7:
    print('Aluno em recuperação, média igual:',media)
else:
    print('Aluno reprovado, média igual:',media)