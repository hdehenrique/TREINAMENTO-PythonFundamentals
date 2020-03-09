# Software de folha de pagamento
# Programa para o cálculo de uma folha de pagamento, Os descontos são do Imposto de Renda, que
# depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
# 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.


# Desconto do IR:
# Salário Bruto       Desconto IR
# Até 1.900           isento
# De 1.901 até 2.800  7%
# De 2.801 até 3.700  15%
# de 3.701 até 4.600  22%
# Acima de 4.600      27%

vl_hora = float(input('Digite o valor da sua hora: '))
qtd_hora = float(input('Digite a quantidade de horas trabalhadas: '))

calc_salario = vl_hora*qtd_hora

print('Valor da hora: R$',vl_hora)
print('Total de horas trabalhadas: ',qtd_hora)
print('Salario bruto ({}*{}): R$'.format(vl_hora,qtd_hora), calc_salario)

if calc_salario <= 1900:
    IR = 0
elif calc_salario > 1900 and calc_salario <= 2800:
    IR = 7
elif calc_salario > 2801 and calc_salario <= 3700:
    IR = 15
elif calc_salario > 3701 and calc_salario <= 4600:
    IR = 22
else:
    IR = 27

valorIR = calc_salario*(IR/100)
valorSindicato = calc_salario*(3/100)
valorFGTS = calc_salario*(11/100)

print(f'(-) IR ({IR}%): R${valorIR}')
print(f'(-) Sindicato (3%): R${valorSindicato}')
print(f'FGTS (11%): R${valorFGTS}')