import math 
import operacionesVectores as vectores 
import operacionesBasicasComplejos as complejos

def positionProbability(particlePos,vector,len): 
    normac = complejos.modulo(vector[particlePos])
    normav = vectores.norma(vector)
    numerator = math.pow(normac,2)
    denominator = math.pow(normav,2)
    probability = numerator/denominator
    return probability


def transitionAmplitude(v1,v2): 
    numerator = vectores.productoInterno(v1,v2)
    denominator = [vectores.norma(v1) * vectores.norma(v2),0]
    amplitude = complejos.division(numerator,denominator)
    amplitude = [round(amplitude[0],1),round(amplitude[1],1)]
    return amplitude

