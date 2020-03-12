# def mod():
#     print('Mod')

# def mod2():
#     print('Mod2')

# import os 

# print(dir(os))

# print(os.getenv('HOME'))
# print(os.getenv('USER'))

import sys

for i in range(len(sys.argv)):
    if i == 0:
        print(f'Função:{sys.argv[0]}')
    else:
        print(f'{i}.argumento:{sys.argv[i]}')