import unittest
import Lab1
import cmath
import math 
class TestCalculator(unittest.TestCase):
    
    def test_sum(self):
        c = complex(-2,1) + complex(1,2)
        rta = Lab1.suma([-2,1], [1,2])
        c1 = complex(rta[0],rta[1])
        self.assertEqual(c1, c)
    def test_sub(self):
        c = complex(-2,1) - complex(1,2)
        rta = Lab1.resta([-2,1], [1,2])
        c1 = complex(rta[0],rta[1])
        self.assertEqual(c1, c)
    def test_mult(self):
        c = complex(-2,1) * complex(1,2)
        rta = Lab1.multiplicacion([-2,1], [1,2])
        c1 = complex(rta[0],rta[1])
        self.assertEqual(c1, c)
    def test_div(self):
        c = complex(-2,1) / complex(1,2)
        rta = Lab1.division([-2,1], [1,2])
        c1 = complex(rta[0],rta[1])
        self.assertEqual(c1, c)
    def test_modulo(self):
        self.assertEqual(Lab1.modulo([4,-3]), 5)
    def test_conjugado(self):
        self.assertEqual(Lab1.conjugado([4,-3]),[4,3])
    def test_aPolar(self):
        c = cmath.polar(complex(1,1))
        fase = Lab1.fase([1,1])
        rta = Lab1.aPolar([1,1])
        t = (rta[0],fase)
        self.assertEqual(t,c)
    def test_aCartesiano(self):
        c = cmath.rect(2**(1/2),math.radians(45))
        rta = Lab1.aCartesiano([2**(1/2),45.0])
        c1 = complex(rta[0],rta[1])
        self.assertEqual(c1,c)
    def test_fase(self):
        c = cmath.phase(complex(1,4))
        rta = Lab1.fase([1,4])
        self.assertEqual(rta,c)

if __name__ == "__main__":
    unittest.main()
