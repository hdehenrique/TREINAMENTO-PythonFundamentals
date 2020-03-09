# Faça um programa que receba 4 notas de aluno:
# calcule a média
# caso seja menor que 7 imprima "Reprovado"
# caso contrário "Aprovado"

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

media = (n1+n2+n3+n4)/4

if media >= 7:
    print('Aluno aprovado, média igual:', media)
else:
    print('Aluno reprovado, média igual:',media)


##################################################

# Faça um programa que receba 4 notas de aluno:
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