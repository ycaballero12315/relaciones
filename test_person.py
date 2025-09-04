import unittest
from relaciones.persona import calcular

class TestCalcAvg(unittest.TestCase):
    def test_1(self):
        result = calcular(10,10,10)
        self.assertEqual(result, 10)
    
    def test_2(self):
        result = calcular(7,7,3, 3)
        self.assertEqual(result,5)


if __name__ == "__main__":
    unittest.main()
