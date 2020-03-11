# # -*- coding: UTF-8 -*-

# ###### classe

# class Automovel():
#     def __init__(self):
#         self.motor = 'Combustão'
    
# class Carro():
    
#     ###### métodos da classe
#     def __init__(self):
#         Automovel.__init__(self)
#         self.rodas = 4
#         self.porta_mala = 'Normal'
#         self.volante = True
#         self.tanque = True

#     def ligar(self):
#         print('carro ligado')

#     def desligar(self):
#         print('carro desligado')
    
#     def acelerar(self):
#         print('acelerando')
    
#     def frear(self):
#         print('freando')

# class Fiat147(Carro):
#     def __init__(self):
#         super().__init__()
#         self.porta_mala = 'Com água'

# ###### #objeto
# c001 = Fiat147()
# print(c001.ligar())

# # objetoCarro= Carro()
# # objetoCarro.ligar()
# # objetoCarro.acelerar()


class Pai():
    def __init__(self):
        self.profissao = 'Advogado'

class Mae():
    def __init__(self):
        self.profissao = 'Medica'

class Filho():
    def __init__(self):
        Pai.__init__(self)
        self.estudo = 'Programação'

jose = Filho()

#print(jose.profissao)