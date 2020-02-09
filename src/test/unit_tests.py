from os.path import dirname, join, abspath
import sys 
sys.path.insert(0, abspath(join(dirname(__file__), '..')) + "\main")
import unittest
import operacionesBasicasComplejos as basic
import operacionesVectores as vectores
import operacionesMatrices as matrices
import cmath
import math 
class TestCalculator(unittest.TestCase):
    
    def test_sum(self):
        c = complex(-2,1) + complex(1,2)
        rta = basic.suma([-2,1], [1,2])
        c1 = complex(rta[0],rta[1])
        self.assertEqual(c1, c)

    def test_sub(self):
        c = complex(-2,1) - complex(1,2)
        rta = basic.resta([-2,1], [1,2])
        c1 = complex(rta[0],rta[1])
        self.assertEqual(c1, c)

    def test_mult(self):
        c = complex(-2,1) * complex(1,2)
        rta = basic.multiplicacion([-2,1], [1,2])
        c1 = complex(rta[0],rta[1])
        self.assertEqual(c1, c)

    def test_div(self):
        c = complex(-2,1) / complex(1,2)
        rta = basic.division([-2,1], [1,2])
        c1 = complex(rta[0],rta[1])
        self.assertEqual(c1, c)

    def test_modulo(self):
        self.assertEqual(basic.modulo([4,-3]), 5)

    def test_conjugado(self):
        self.assertEqual(basic.conjugado([4,-3]),[4,3])

    def test_aPolar(self):
        c = cmath.polar(complex(1,1))
        fase = basic.fase([1,1])
        rta = basic.aPolar([1,1])
        t = (rta[0],fase)
        self.assertEqual(t,c)

    def test_aCartesiano(self):
        c = cmath.rect(2**(1/2),math.radians(45))
        rta = basic.aCartesiano([2**(1/2),45.0])
        c1 = complex(rta[0],rta[1])
        self.assertEqual(c1,c)

    def test_fase(self):
        c = cmath.phase(complex(1,4))
        rta = basic.fase([1,4])
        self.assertEqual(rta,c)

    def test_sumaVectores(self):
        v1 = [[4,5],[8,7],[2,1],[3,9]]
        v2 = [[2,1],[1,5],[3,4],[8,9]]
        v3 = []
        for i in range(len(v1)):
            v3.append(complex(v1[i][0],v1[i][1]) + complex(v2[i][0],v2[i][1]))
        vrta = vectores.suma(v1,v2)
        for i in range(len(vrta)):
            vrta[i] = complex(vrta[i][0],vrta[i][1])
        self.assertEqual(v3,vrta)

    def test_inversoVector(self):
        v1 = [[4,5],[8,7],[2,1],[3,9]]
        inverso = [[-4,-5],[-8,-7],[-2,-1],[-3,-9]]
        vrta = vectores.inversa(v1)
        self.assertEqual(inverso,vrta)
        v2 = [[0.5,5],[-5,7],[2,1],[3,9]]
        inverso2 = [[-0.5,-5],[5,-7],[-2,-1],[-3,-9]]
        vrta2 = vectores.inversa(v2)
        self.assertEqual(inverso2,vrta2)

    def test_multiEscalarVector(self):
        v1 = [[4,5],[8,7],[2,1],[3,9]]
        c = [5,8]
        v3 = []
        for i in range(len(v1)):
            v3.append(complex(c[0],c[1]) * complex(v1[i][0],v1[i][1]))
        vrta = vectores.multiplicarPorEscalar(c,v1)
        for i in range(len(vrta)):
            vrta[i] = complex(vrta[i][0],vrta[i][1])
        self.assertEqual(v3,vrta)

    def test_sumaMatrices(self):
        m1 = [[[1,2],[3,4],[2,5]],[[1,2],[8,4],[1,4]],[[3,2],[5,6],[8,1]]]
        m2 = [[[1,2],[3,4],[2,5]],[[1,2],[8,4],[1,4]],[[3,2],[5,6],[8,1]]]
        rta = [[[2,4],[6,8],[4,10]],[[2,4],[16,8],[2,8]],[[6,4],[10,12],[16,2]]]
        vrta = matrices.suma(m1,m2)
        self.assertEqual(rta,vrta)

    

if __name__ == "__main__":
    unittest.main()
