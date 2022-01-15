import unittest

def suma(num_1, num_2):
    #pass
    return num_1 + num_2

class CajaNegraTest(unittest.TestCase):
    def test_suma_dos_positivos(self):
        num_1 = 5
        num_2 = 4

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 9)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)    

if __name__ == '__main__':
    unittest.main()        