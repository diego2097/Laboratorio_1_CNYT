from sys import stdin
import math
import operacionesVectores as vectores 
import operacionesBasicasComplejos as complejos

def completarMatrizResultado(temp,matriz,a,b):
    m = len(temp)
    n = len(temp[0])
    fila = 0
    col = 0 
    for i in range((m*a),m*(a+1)):
        for j in range((n*b),n*(b+1)):
            matriz[i][j]=temp[fila][col]
            col+=1
        fila+=1
        col=0

def productoTensor(m1,m2):
    matriz = crearMatrizVacia(len(m1)*len(m2),len(m1[0]*len(m2[0])))    
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            temp = multiplicarPorEscalar(m1[i][j],m2)
            completarMatrizResultado(temp, matriz, i, j)
    return matriz; 

def esHermitiana(m):
    adjunta = adjunta(m)
    if (iguales(m,adjunta))
        return True

def esUnitaria(m):
    adjunta = adjunta(m)
    resultado = multiplicar(m,adjunta)
    resultado2 = multiplicar(adjunta,m)
    if (esIdentidad(resultado) and esIdentidad(resultado2)):
        return True 
    return False

def accionSobreVector():
    print("developing")

def multiplicar(m1,m2):
    if (len(m1[0]) == len(m2)):
        matriz = crearMatrizVacia(len(m1),len(m2[0]))    
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                acumulador = [0,0]
                for k in range(len(m1[0])):
                    acumulador = complejos.suma(acumulador,complejos.multiplicacion(m1[i][k],m2[k][j])) 
                matriz[i][j] = acumulador
        return matriz
    return None

def adjunta(m):
    matriz = transpuesta(m)    
    matriz = conjugada(matriz)
    return adjunta

def conjugada(m):
    matriz = crearMatrizVacia(len(m),len(m[0]))    
    for i in range(len(matriz)):
        matriz[i] = vectores.conjugado(m[i])
    return matriz

def transpuesta(m):
    matriz = crearMatrizVacia(len(m[0]),len(m))    
    for i in range (len(m)):
        for j in range (len(m[0])):
            matriz[j][i] = m[i][j]
    return matriz

def multiplicarPorEscalar(c,m):
    matriz = crearMatrizVacia(len(m),len(m))    
    for i in range (len(m)):
        matriz[i] = vectores.multiplicarPorEscalar(c,m[i])
    return matriz

def inversa(m):
    matriz = crearMatrizVacia(len(m),len(m))    
    for i in range (len(m)):
        for j in range (len(m)):
            matriz[i][j] = [m[i][j][0]*-1, m[i][j][1]*-1]
    return matriz

def suma(m1,m2):
    if (len(m1) == len(m2) and len(m1[0]) == len(m2[0])):
        matriz = crearMatrizVacia(len(m1),len(m2))    
        for i in range(len(m1)): 
            for j in range(len(m2)): 
                matriz[i][j] = suma(m1[i][j],m2[i][j])
        return matriz
    return None

def crearMatrizVacia(m,n): 
    matriz = [[[0,0] for col in range(n)] for ren in range(m)]
    return matriz

def esIdentidad(m1):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if (i == j and m1[i][j] != 1): 
                return False
            elif (i != j and m1[i][j] != 0):
                return False
    return True

def iguales(m1,m2):
    if (len(m1) == (len(m2))):
        for i in range(len(m1):
            if (vectores.iguales(m1[i],m2[i]) == False):
                return False
        return True 
    return False 
