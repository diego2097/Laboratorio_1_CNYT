from sys import stdin 
import math 
import operacionesBasicasComplejos as complejos



def norma(vector): 
    norma = 0 
    for i in range(len(vector)): 
        norma = norma + math.pow(complejos.modulo(vector[i]),2)
    norma = math.sqrt(norma)
    return norma 

def productoTensor(v1,v2):
    vector = []
    for i in range (len(v1)):
        for j in range(len(v2)):
            vector.append(complejos.multiplicacion(v1[i],v2[j]))
    return vector

def distancia(v1,v2):
    if (len(v1) == len(v2)):
        rta = 0 
        for i in range (len(v1)):
            rta = rta + math.pow(complejos.distancia(v1[0],v2[0]),2)
        rta = math.sqrt(rta)
        return rta
    return None

def productoInterno(v1,v2):
    if (len(v1) == len(v2)):
        vconj = conjugado(v1)
        rta = [0,0]
        for i in range(len(v1)):
            rta = complejos.suma(rta,complejos.multiplicacion(vconj[i],v2[i]))
        return rta 
    return None

def adjunta(v):
    vector = transpuesta(conjugado(v))
    return vector

def conjugado(v):
    vector = []
    for i in range (len(v)):
        vector.append(complejos.conjugado(v[i]))
    return vector

def transpuesta(v):
    vector = v 
    return vector 

def multiplicarPorEscalar(c,v):
    vector = []
    for i in range  (len(v)):
        vector.append(complejos.multiplicacion(c,v[i]))
    return vector

def inversa(v):
    vector = []
    for i in range (len(v)):
        vector.append([v[i][0]*-1, v[i][1]*-1])
    return vector

def suma(v1,v2):
    if (len(v1)==len(v2)):
        vector = []
        for i in range (len(v1)):
            vector.append(complejos.suma(v1[i], v2[i])) 
        return vector
    return None

def iguales(v1,v2):
    if (len(v1) == (len(v2))):
        for i in range(len(v1)):
            if (complejos.iguales(v1[i],v2[i]) == False):
                return False
        return True 
    return False 