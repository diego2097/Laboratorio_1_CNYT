from os.path import dirname, join, abspath
import sys 
sys.path.insert(0, abspath(join(dirname(__file__), '..')) + "\main")
import unittest
import operacionesBasicasComplejos as basic
import operacionesVectores as vectores
import operacionesMatrices as matrices
import QuantumStates as quantum 
import cmath
import math 
import random

class QuantumTestCalculator(unittest.TestCase):
    
    def test_particleProbability(self):
        vector = [[-3,-1],[0,-2],[0,1],[2,0]]
        pos = 2 
        rta = round(quantum.positionProbability(pos,vector,len(vector)),3)
        self.assertEqual(rta,0.053)
        vector = [[2,1],[-1,2],[0,1],[1,0],[3,-1],[2,0],[0,-2],[-2,1],[1,-3],[0,-1]]
        pos = 7
        rta = round(quantum.positionProbability(pos,vector,len(vector))*100,2)
        self.assertEqual(rta,10.87)

    def test_transitionAmplitude(self): 
         v1 = [[1,0],[0,-1]]
         v2 = [[0,1],[1,0]]
         rta =quantum.transitionAmplitude(v2,v1)
         self.assertEqual(rta,[0,-1])

if __name__ == "__main__":
    unittest.main()
