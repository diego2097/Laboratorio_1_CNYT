from sys import stdin
import math





def multiplicarMatrices(m1,m2):
    if (len(m1) == len(m2) and len(m1[0]) == len(m2[0])):
        matriz = crearMatrizVacia(len(m1),len(m2))    
        for i in range(len(m1)):
            for j in range(len(m1)):
                acumulador = [0,0]
                for k in range(len(m1)):
                    acumulador = suma(acumulador,multiplicacion(m1[i][k],m2[k][j])) 
                matriz[i][j] = acumulador
        return matriz
    return None

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

def productoTensorMatrices(m1,m2):
    matriz = crearMatrizVacia(len(m1)*len(m2),len(m1[0]*len(m2[0])))    
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            temp = multiEscalarMatrices(m1[i][j],m2)
            completarMatrizResultado(temp, matriz, i, j)
    return matriz; 

def transpuesta(m):
    matriz = crearMatrizVacia(len(m[0]),len(m))    
    for i in range (len(m)):
        for j in range (len(m[0])):
            matriz[j][i] = m[i][j]
    return matriz

def multiEscalarMatrices(c,m):
    matriz = crearMatrizVacia(len(m),len(m))    
    for i in range (len(m)):
        matriz[i] = multiEscalarVector(c,m[i])
    return matriz

def inversaMatrices(m):
    matriz = crearMatrizVacia(len(m),len(m))    
    for i in range (len(m)):
        for j in range (len(m)):
            matriz[i][j] = [m[i][j][0]*-1, m[i][j][1]*-1]
    return matriz

def sumaMatrices(m1,m2):
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


def main(): 
    m1 = [[[1,2],[3,4]],[[1,2],[8,4]]]
    c = [8,4]
    rta = multiplicarMatrices(m1,m1) 
    
    # Simulacion de circuito 

    q0 = [[[1,0]],[[0,0]]]       
    q00 = productoTensorMatrices(q0,q0)
    print(q00)
    c = [1/2,0]
    temp = [[[1,0],[1,0]],[[1,0],[-1,0]]]
    H = multiEscalarMatrices(c,temp)

    X = [[[0,0],[1,0]],[[1,0],[0,0]]]

    M1 = productoTensorMatrices(H,H)

    M2 = productoTensorMatrices(H,X)

    """for i in M1:
        print(i)
    print("----------------------")
    for i in M2:
        print(i)
    """

    temp2 = multiplicarMatrices(M1,M2)
    for i in temp2:
        print(i)
main()    