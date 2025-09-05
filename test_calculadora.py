import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_suma(self):
        self.assertEqual(self.calc.suma(1, 2), 3)

    def test_resta(self):
        self.assertEqual(self.calc.resta(5, 3), 2)

    def test_multiplicacion(self):
        self.assertEqual(self.calc.multiplicacion(2, 3), 6)

    def test_division(self):
        self.assertEqual(self.calc.division(6, 2), 3)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            self.calc.division(1, 0)

if __name__ == '__main__':
    unittest.main()