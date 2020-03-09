#dado o dicionario

dados = {
    'estados': {
        'sp': {
            'nome': 'São Paulo',
            'municipios': 645,
            'populacao': 44.04
        },
        'rj': {
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'populacao': 16.72
        },
        'mg': {
            'nome': 'Minas Gerais',
            'municipios': 31,
            'populacao': 20.87
        }
    }
}
print('Modelo 1')
print('Estado: ',dados['estados']['sp']['nome'])
print(f"Municipios: {dados['estados']['sp']['municipios']}")
print('Populacao: ',dados['estados']['sp']['populacao'])

print('\nModelo 2')
print('Estado: ',dados['estados']['sp']['nome'],
      '\nMunicipios: ',dados['estados']['sp']['municipios'],
      '\nPopulacao: ',dados['estados']['sp']['populacao'] )

print('\nModelo 3')
for estado in dados ['estados'].keys():
    print('Estado: ',dados['estados'][estado]['nome'])
    print(f"Municipios: {dados['estados'][estado]['municipios']}")
    print('Populacao: ',dados['estados'][estado]['populacao'])
    print('  ')

# imprima na tela as seguintes mensagens:

# Estado:<nome_estado>
# Municipios:<qnt_municipios>
# Populacao: <qnt_populacao>