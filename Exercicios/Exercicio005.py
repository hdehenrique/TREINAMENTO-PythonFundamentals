# Faça umprograma que recebe dois valores e retorne o maior valor
# Caso sejam iguais imprima "Valores iguais"

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

# if n1 > n2:
#     print('Valor maior',n1)
# elif n1 < n2:
#     print('Valor maior',n2)
# else:
#     print('Valores iguais')

## modo 2
if n1==n2:
    print('Valores iguais')
else:
    print(max(n1,n2))