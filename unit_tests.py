import unittest
import Lab1
class TestCalculator(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(Lab1.suma([-2,1], [1,2]), [-1,3])
    def test_sub(self):
        self.assertEqual(Lab1.resta([-2,1], [1,2]), [-3,-1])
    def test_mult(self):
        self.assertEqual(Lab1.multiplicacion([-2,1], [1,2]), [-4,-3])
    def test_div(self):
        self.assertEqual(Lab1.division([-2,1], [1,2]), [0,1])
    def test_modulo(self):
            self.assertEqual(Lab1.modulo([4,-3]), 5)
    def test_conjugado(self):
        self.assertEqual(Lab1.conjugado([4,-3]),[4,3])
    def test_aPolar(self):
        self.assertEqual(Lab1.aPolar([1,1]),[2**(1/2),45.0])
    def test_aCartesiano(self):
        self.assertEqual(Lab1.aCartesiano([2**(1/2),45.0]),[1.0,1.0])



if __name__ == "__main__":
    unittest.main()
