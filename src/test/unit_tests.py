from os.path import dirname, join, abspath
import sys 
sys.path.insert(0, abspath(join(dirname(__file__), '..')) + "\main")
import unittest
import operacionesBasicasComplejos as basic
import operacionesVectores as vectores
import operacionesMatrices as matrices
import cmath
import math 
import random

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

    # test vectores

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

    def test_conjugadoVectores(self):
        N = 4
        vector = []  
        for i in range(N): 
            vector.append([random.randint(-100, 100),random.randint(-100, 100)])
        conjugado = vectores.conjugado(vector)

        for i in range(N): 
            self.assertEqual((vector[i][1])*-1 ,conjugado[i][1])
        

    def test_adjuntaVectores(self):
        N = 4
        vector = []  
        for i in range(N): 
            vector.append([random.randint(-100, 100),random.randint(-100, 100)])
        adjunta = vectores.conjugado(vector)
        adjunta = vectores.transpuesta(adjunta)

        for i in range(N): 
            self.assertEqual((vector[i][1])*-1 ,adjunta[i][1])

    def test_productoInterno(self): 
        N = 100
        vector = []  
        vector2 = []
        for i in range(N): 
            vector.append([random.randint(-100, 100),random.randint(-100, 100)])
            vector2.append([random.randint(-100, 100),random.randint(-100, 100)])

        rta = vectores.productoInterno(vector,vector2)
        conjugado = vectores.conjugado(vector)
        suma = [0,0]
        for i in range(N): 
            suma = basic.suma(suma, basic.multiplicacion(conjugado[i],vector2[i]))
    
        self.assertEqual(suma,rta)
    
    def test_productoTensorVectores(self):
        N = 100
        vector = []  
        vector2 = []
        for i in range(N): 
            vector.append([random.randint(-100, 100),random.randint(-100, 100)])
            vector2.append([random.randint(-100, 100),random.randint(-100, 100)])
        rta = vectores.productoTensor(vector,vector2)

        tensor = []
        for i in range(N):
            for j in range(N):
                 tensor.append(basic.multiplicacion(vector[i],vector2[j]))

        self.assertEqual(rta,tensor)
        
    # test matrices 

    def test_sumaMatrices(self):
        m1 = [[[1,2],[3,4],[2,5]],[[1,2],[8,4],[1,4]],[[3,2],[5,6],[8,1]]]
        m2 = [[[1,2],[3,4],[2,5]],[[1,2],[8,4],[1,4]],[[3,2],[5,6],[8,1]]]
        rta = [[[2,4],[6,8],[4,10]],[[2,4],[16,8],[2,8]],[[6,4],[10,12],[16,2]]]
        vrta = matrices.suma(m1,m2)
        self.assertEqual(rta,vrta)

    def test_inversaMatrices(self):
        N = 4
        matriz = [[[random.randint(-100, 100),random.randint(-100, 100)] for j in range(N)]for i in range(N)]  
        inversa = [[]]
        inversa = matrices.inversa(matriz)
        for i in range(N):
            for j in range(N):
                self.assertEqual(matriz[i][j][0]*-1,inversa[i][j][0])                
                self.assertEqual(matriz[i][j][1]*-1,inversa[i][j][1])

    def test_multplicarEscalarPorMatriz(self):
        N = 4
        matriz = [[[random.randint(-100, 100),random.randint(-100, 100)] for j in range(N)]for i in range(N)]  
        inversa = [[]]
        escalar = [random.randint(-100, 100),random.randint(-100, 100)]
        matriz_resultado = matrices.multiplicarPorEscalar(escalar,matriz)
        for i in range(N):
            for j in range(N):
                self.assertEqual(basic.multiplicacion(matriz[i][j],escalar),matriz_resultado[i][j])                

    def test_transpuesta(self):  
        m1 = [[[1,2],[3,4],[2,5]],[[1,2],[8,4],[1,4]],[[3,2],[5,6],[8,1]]]
        transpuesta = matrices.transpuesta(m1)
        rta = [[[1,2],[1,2],[3,2]],[[3,4],[8,4],[5,6]],[[2,5],[1,4],[8,1]]]
        self.assertEqual(transpuesta,rta)

    def test_conjugadaMatriz(self):
        N = 4
        matriz = [[[random.randint(-100, 100),random.randint(-100, 100)] for j in range(N)]for i in range(N)]  
        conjugada = matrices.conjugada(matriz)
        for i in range(N):
            for j in range(N):
                self.assertEqual(matriz[i][j][1]*-1,conjugada[i][j][1])

    def test_adjuntaMatriz(self):
        m1 = [[[1,2],[3,4],[2,5]],[[1,2],[8,4],[1,4]],[[3,2],[5,6],[8,1]]]
        adjunta = matrices.adjunta(m1)
        rta = [[[1,-2],[1,-2],[3,-2]],[[3,-4],[8,-4],[5,-6]],[[2,-5],[1,-4],[8,-1]]]
        self.assertEqual(adjunta,rta)

    def test_multiplicarMatriz(self):
        m1 = [[[11,5],[3,5]],[[7,5],[11,5]]]
        m2 = [[[8,5],[0,5],[1,5]],[[0,5],[3,5],[5,5]]]
        matriz = matrices.multiplicar(m1,m2)
        rta = [[[38,110],[-41,85],[-24,100]],[[6,130],[-17,105],[12,120]]]
        self.assertEqual(matriz,rta)

    def test_accionSobreVector(self):
        m1 = [[[-3,5],[5,5],[-6,5]],[[7,5],[10,5],[-1,5]]]

        v = [[-6,5],[-2,5],[5,5]]
        accion = matrices.accionSobreVector(m1,v)
        rta = [[-97,-35],[-142,65]]
        self.assertEqual(accion,rta)

    def test_eshermitiana(self):
        m1 = [[[7,0],[6,5]],[[6,-5],[-3,0]]]
        self.assertTrue(matrices.esHermitiana(m1))
        m1 = [[[-3,5],[5,5],[-6,5]],[[7,5],[10,5],[-1,5]]]
        self.assertFalse(matrices.esHermitiana(m1))
    

if __name__ == "__main__":
    unittest.main()
