from sys import stdin 
import math 



def distancia(c1,c2):
    rta = modulo(resta(c1,c2))
    return rta 

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
    rta.append(math.atan2(c[1],c[0]))
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

def iguales(c1,c2):
    rta = (c1[0] == c2[0] and c1[1] == c2[1])
    return rta 

