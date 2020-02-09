## Calculadora de complejos  

### Objetivo 

Libreria para hacer operaciones entre numeros complejos. 

### Descripcion 

La libreria utiliza vectores para simular los numeros complejos. En el vector [a,b] a representa la parte real del numero complejo y b la parte imaginaria. La libreria soporta las siguientes operaciones: 

### Funcionalidades 

### Operaciones entre complejos

- Suma(c1, c2): Recibe dos numeros complejos en forma de vector, y retorna un vector con la suma entre ambos.  

- Resta(c1, c2): Recibe dos numeros complejos en forma de vector, y retorna un vector con la resta entre ambos. 

- Multiplicacion(c1, c2): Recibe dos numeros complejos en forma de vector, y retorna un vector con la multiplicacion entre ambos.  

- Division(c1, c2): Recibe dosnumeros complejos en forma de vector, y retorna un vector con la division entre ambos.  

- Modulo(c): Recibe un complejo en forma de vector, y retorna el modulo del mismo. 

- Conjugado(c): Recibe un complejo en forma de vector, y retorna el conjugado del complejo.

- aPolar(c): Recibe un complejo en forma de vector y coordenadas cartesianas, retorna un complejo en coordenadas polares.

- aCartesiano(c): Recibe un complejo en forma de vector y coodenadas polares, retorna un complejo en coordenadas cartesianas. 

- fase(c): Retorna la fase del numero complejo con coordenadas cartesianas.  

### Operaciones entre vectores de complejos

- suma(vector1[c1,c2...cn],vector2[c1,c2...cn]): Recibe dos vectores de complejos, y retorna un vector con la suma entre ambos

- inversa(vector[c1,c2...cn]): Recibe un vector de complejos, y retorna un vector con el inverso de este

- multiplicarPorEscalar(complejo[a,b], vector[c1,c2...cn]): Recibe un numero complejo y un vector. Retorna un vector con la multiplicacion entre estos. 

- transpuesta(vector[c1,c2...cn]): Recibe un vector de complejos y retorna el transpuesto de este. 

- conjugado(vector[c1,c2...cn]): Recibe un vector de complejos y retorna el conjugado de este. 

- adjunta(vector[c1,c2...cn]):  Recibe un vector de complejos y retorna la adjunta de este.

- productoInterno(vector1[c1,c2...cn],vector2[c1,c2...cn]): Recibe dos vectores de complejos, y retorna un complejo con el resultado del producto interno entre ambos.

- distancia(vector1[c1,c2...cn],vector2[c1,c2...cn]): Recibe dos vectores de complejos, y retorna un entero con la distancia entre ambos vectores.

- productoTensor(vector1[c1,c2...cn],vector2[c1,c2...cn]): Recibe dos vectores de complejos, y retorna un vector con el resultado del producto tensor entre ambos.

### Operaciones entre matrices de complejos

- suma(matriz1[v1,v2...vn],matriz2[v1,v2...vn]): Recibe dos matrices de complejos, y retorna una matriz con la suma entre ambos.

- inversa(matriz[v1,v2...vn]): Recibe una matriz de complejos, y retorna una matriz con la inversa de esta. 

- multiplicarPorEscalar(complejo[a,b],matriz[v1,v2...vn]): Recibe un vector y una matriz. Retorna el producto entre ambos.

- transpuesta(matriz[v1,v2...vn]): Recibe una matriz de complejos, y retorna una matriz con la transpuesta de esta. 

- conjugada(matriz[v1,v2...vn]): Recibe una matriz de complejos, y retorna una matriz con la conjugada de esta. 

- adjunta(matriz[v1,v2...vn]): Recibe una matriz de complejos, y retorna una matriz con la adjunta de esta.

- multiplicar(matriz1[v1,v2...vn],matriz2[v1,v2...vn]): Recibe dos matrices. Retorna el producto entre ambas.

- accionSobreVector(matriz[v1,v2...vn],vector[c1,c2...cn]): Recibe un vector y una matriz. Retorna la accion de la matriz sobre el vector, es decir el producto entre ambos. 

- esUnitaria(matriz[v1,v2...vn]): Recibe una matriz y retorna True si esta es unitaria, de lo contrario retorna False

- esHermitiana(matriz[v1,v2...vn]): Recibe una matriz y retorna True si esta es hermitiana, de lo contrario retorna False

- productoTensor(matriz1[v1,v2...vn],matriz2[v1,v2...vn]): Recibe dos matrices. Retorna el producto tensor entre ambas.

### Prerequisitos 

Para poder ejecutar esta libreria se necesita tener instalado python 3.7 o superior. Para descargar, puede hacerlo directamente de la 
[pagina oficial de python](https://www.python.org/downloads/)


### Uso de la libreria 

Luego de tener instalado python, debe clonar el repositorio 

```
git clone https://github.com/diego2097/Laboratorio_1_CNYT.git
```

Recuerde que para utilizar la libreria en su proyecto debe importarla 

```python
import operacionesVectores  
import operacionesBasicasComplejos 
import operacionesMatrices
```

### Ejecutar las pruebas  

Para ejecutar las pruebas desde el directorio del proyecto ejecutar
```
python src/test/unit_tests.py
```

### Construido con

- [Python](https://www.python.org/downloads/)

### Author 

- [Diego Alejandro Corredor Tolosa](https://github.com/diego2097)

### License 

- GNU General Public License v3.0