from sys import stdin
import operacionesMatrices as matrices
import math
 
def main(): 
    m1 = [[[1,2],[3,4]],[[1,2],[8,4]]]
    
    c = [8,4]
    #rta = multiplicarMatrices(m1,m1) 
    
    # Simulacion de circuito 

    q0 = [[[1,0]],[[0,0]]]       
    q00 = matrices.productoTensorMatrices(q0,q0)

    c = [1/math.sqrt(2),0]
    temp = [[[1,0],[1,0]],[[1,0],[-1,0]]]
    H = matrices.multiEscalarMatrices(c,temp)

    X = [[[0,0],[1,0]],[[1,0],[0,0]]]

    M1 = matrices.productoTensorMatrices(H,H)

    M2 = matrices.productoTensorMatrices(H,X)
    
    temp2 = matrices.multiplicarMatrices(M2,q00)
    rta = matrices.multiplicarMatrices(M1,temp2)

    for i in rta:
        print(i)
main()    