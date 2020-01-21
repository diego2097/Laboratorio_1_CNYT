from sys import stdin
import math

def Transpuesta(m):
    matriz = [[]]
    for i in range (len(m)):
        for j in range (len(m)):
            matriz[j][i] = m[i][j]
    return matriz

def multiEscalarMatrices(c,m):
    matriz = [[]]
    for i in range (len(m1)):
        for j in range (len(m2)):
            matriz[i][j] = multiplicacion[c,m[i][j]]
    return matriz

def inversaMatrices(m):
    matriz = [[]]
    for i in range (len(m1)):
        for j in range (len(m2)):
            matriz[i][j] = [m[i][j][0]*-1, m[i][j][1]*-1]
    return matriz

def sumaMatrices(m1,m2):
    if (len(m1) == len(m2) and len(m1[0]) == len(m2[0])):
        matriz = [[]]
        for i in range (len(m1)):
            for j in range (len(m2)):
                matriz[i][j] = suma(m1[i][j],m2[i][j])
        return matriz
    return None

def multiEscalarVector(c,v):
    vector = []
    for i in range  (len(v)):
        vector.append(multiplicacion(c,v[i]))
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
            vector.append(suma(v1[i], v2[i])) 
        return vector
    return None

def fase(c):
    rta = math.atan2(c[1],c[0])
    return rta

def aCartesiano(c):
    rta = []
    rta.append(c[0] * math.cos(math.radians(c[1])))
    rta.append(c[0] * math.sin(math.radians(c[1])))
    return rta

def aPolar(c):
    rta = []
    rta.append(modulo(c))
    rta.append(math.atan(c[1]/c[0]))
    return rta

def conjugado(c):
    rta = []
    rta.append(c[0])
    rta.append(c[1] * -1)
    return rta

def modulo(c):
    rta = ((c[0]**2) + (c[1]**2))**(1/2)
    return rta

def division(c1,c2):
    rta = []
    deno = c2[0]**2 + c2[1]**2
    temp = c1[0]*c2[0] + c1[1]*c2[1]
    temp2 = c2[0]*c1[1] - c1[0]*c2[1]
    rta.append(temp/deno)
    rta.append(temp2/deno)
    return rta

def multiplicacion(c1,c2):
    rta = []
    rta.append(c1[0]*c2[0] - c1[1]*c2[1])
    rta.append(c1[0]*c2[1] + c2[0]*c1[1])
    return rta


def resta(c1,c2):
    rta = []
    rta.append(c1[0] - c2[0])
    rta.append(c1[1] - c2[1])
    return rta

def suma(c1,c2):
    rta = []
    rta.append(c1[0] + c2[0])
    rta.append(c1[1] + c2[1])
    return rta 


