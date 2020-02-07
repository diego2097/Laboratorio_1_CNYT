from sys import stdin 
import math 
import operacionesBasicasComplejos as complejos

def productoTensorVectores():
    print("developing")

def distanciaVectores():
    print("developing")

def normaVector():
    print("developing")

def productoInterno():
    print("developing")

def adjuntaVector():
    print("developing")

def conjugadaVector():
    print("developing")

def transpuestaVector():
    print("developing")

def multiEscalarVector(c,v):
    vector = []
    for i in range  (len(v)):
        vector.append(complejos.multiplicacion(c,v[i]))
    return vector

def inversoVector(v):
    vector = []
    for i in range (len(v)):
        vector.append([v[i][0]*-1, v[i][1]*-1])
    return vector

def sumaVectores(v1,v2):
    if (len(v1)==len(v2)):
        vector = []
        for i in range (len(v1)):
            vector.append(complejos.suma(v1[i], v2[i])) 
        return vector
    return None
