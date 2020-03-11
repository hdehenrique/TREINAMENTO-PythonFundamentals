# crie uma classe Mamifero com os atributos: Bebe Leite

# crie uma classe Homosapiens com os atributos: polegares = true / formaCaminhar = Bipede

# métodos: caça, comer, dormir e construir

class Human():
    def __init__(self):
        self.alimentacao = 'bebe leite'

class Homosapiens(Human):
    def __init__(self):
        Human.__init__(self)
        self.polegares = True
        self.formaCaminhar = 'bipede'
    
    def cacar(self):
        print('caçando...')
    
    def comer(self):
        print('comendo...')

    def dormir(self):
        print('dormindo...')
    
    def construir(self):
        print('construindo...')

teste = Homosapiens()
print(teste.alimentacao)
teste.dormir()