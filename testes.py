# def somar(x, y):
#     return x + y

# def subtracao(x, y):
#     return x - y

# def multipĺicacao(x, y):
#     return x * y

# # Testar função somar
# assert somar(2,2 ) ==4, f"Obtido: {somar(2, 2)} Esperado: 4"
# assert somar(3, 2) ==5, f"Obtido: {somar(2, 3)} Esperado: 5"

# # Testar subtracao
# assert subtracao(3,2 ) ==1, f"Obtido: {subtracao(3, 2)} Esperado: 1"

from unittest import TestCase, main

def somar(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multipĺicacao(x, y):
    return x * y

class Testes(TestCase):
    
    def test_soma(self):
        self.assertEqual(somar(5,5),10)
        self.assertEqual(type(somar(5,5), int))
        self.assertIsNotNone(somar(5,5), 5)

    def test_sub(self):
        self.assertEqual(subtracao(10,5),5)
        self.assertEqual(type(subtracao(10,5), int))
