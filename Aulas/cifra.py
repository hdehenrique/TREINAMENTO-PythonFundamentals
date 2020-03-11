# from __future__ import print_function
# import sys
# import string

# arquivo = open(sys.argv[1], 'r').read().lower()
# rotacao = int(sys.argv[2])

# alfabeto = string.ascii_lowercase
# resultado = ''

# for letra in alfabeto:
#     if letra in alfabeto:
#         posicao = alfabeto.find(letra)
#         posicao = (posicao + rotacao) % 26
#         resultado += alfabeto[posicao]

# print(resultado)

# with open('dados cifrados', 'w') as d:
#     d.write(resultado)

# import module
# print(module.mod2())

from module import mod, mod2
from math import sqrt
import module

mod2()
