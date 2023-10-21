# Reto 8: Ciclo for

**Instrucciones**

Para cada punto cree un programa individual asimismo cree un notebook con la solución a todos los problemas. Al finalizar suba todo a un repo y subalo al canal reto_8 en slack.

## Punto uno
Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

**Código**
```
for num in range(1,101):#Para cada número num desde 1 hasta 100, incrementando de uno en uno
    cuadrado=num**2#Hallar el valor de num elevado al cuadrado
    print(num,cuadrado,sep=", ")#Imprimir num y num al cuadrado (separados por una coma)
```

## Punto dos
Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

**Código**
```
for x in range(1,1000,2): print(x)#Para cada número x desde 1 hasta 999, incrementando de dos en dos, imprimir x

for x in range(2,1001,2): print(x)#Para cada número x desde 2 hasta 1000, incrementando de dos en dos, imprimir x
```

## Punto tres
Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

**Código**
```
x=int(input("Ingrese un número natural: "))#Declarando e inicializando x con la funcion input()
if x%2!=0:#Si el modulo de x dividido entre 2 es diferente a 0, x es impar
    x-=1#Se le resta a x una unidad, para que sea un número par
for i in range(x, 1, -2): print(i)#Para cada número i desde x hasta 2, disminuyendo de dos en dos, imprimir i
```

## Punto cuatro
Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

**Código**
```
x=int(input("Ingrese un número natural: "))#Declarando e inicializando x con la función input()
factorial:int=1 #Declarando factorial como un entero e inicializandolo en 1
for i in range(1,x+1):#Para todo número i desde 1 hasta el x ingresado, incrementando de uno en uno
    factorial=i*factorial#multiplicar el número i por el valor de factorial
    print (i,factorial,sep=",")#Imprimir el número i y el factorial de i (separados por una coma)
```
## Punto cinco
Calcular el valor de 2 elevado a la potencia n usando ciclos for.

**Código**
```
n=int(input("Ingrese el valor del exponente n: "))#Declarando e inicializando n con la función input()
potencia:int=2#Declarando e inicializando ptencia como un entero con valor de 2
for x in range(2,n+1):#Para todo número x desde 2 hasta n, incrementando de uno en uno
    potencia=2*potencia#multiplicar potencia por 2 (haciendo que 2 se multiplique por si mismo n veces)
print("2 elevado a la "+str(n)+" es igual a "+str(potencia))#Imprimir el valor final de potencia
```

## Punto seis
Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).

**Código**
```
n=int(input("Ingrese el valor del exponente n: "))#Declarando e inicializando n con la función input()
x=int(input("Ingrese el valor de la base x: "))#Declarando e inicializando x con la función input()
potencia:int=x#Declarando e inicializando potencia como un entero con el mismo valor que x
for num in range(2,n+1):#Para todo número num desde 2 hasta n, incrementando de uno en uno
    potencia=x*potencia#multiplicar potencia por x (haciendo que x se multiplique por si mismo n veces)
print(str(x)+ " elevado a la "+str(n)+" es igual a "+ str(potencia))#Imprimiendo el valor calculado de la potencia
```
## Punto siete
Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

**Código**
```
for num in range(1,10):#Para todo número num desde 1 hasta 9, incrementando de uno en uno
    for x in range(1,11):#Para todo x desde 1 hasta 10, incrementando de uno en uno
        multiplicacion=num*x#calcular el valor del número num multiplicado por x
        print(num,"x",x,"=",multiplicacion)#Imprimir num por x es igual al resultado de la multiplicación
```

## Punto ocho
Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación. Determine con que valor n se obtiene menos del 0.1% de error.

**Código**
```
def elFactorial(x:int)->int:#Función para calcular el factorial
    factorial:int=1 #Declarando factorial como un entero e inicializandolo en 1
    for i in range(1,x+1):#Para todo número i desde 1 hasta el x ingresado, incrementando de uno en uno
        factorial=i*factorial#multiplicar el número i por el valor de factorial
    return factorial


def funcionExponencial(x:float,n:int)->float:#Función para calcular una aproximación de la función exponencial
    suma : int = 0#Declarando suma como entero e inicializandolo en 0
    for i in range(0, n):#Para todo número i desde 0 hasta n-1, incrementando de uno en uno
        fact=elFactorial(i)#Se halla el factorial de i, llamando la función elFactorial
        calculo=(x**i)/fact#se calcula x^i/i!
        suma += calculo#Se suma los resultados hasta n-1
    return(suma)

if __name__=="__main__":
    n = int(input("Ingrese la cantidad de términos: "))#Declarando e inicializando n con input()
    x = float(input("Ingrese valor x: "))#Declarando e inicializando x con input()
    funcion=funcionExponencial(x,n)#Se llama la función funcionExponencial
    print("La aproximación de la función exponencial de " +str(x)+", con " + str(n) + " términos, es " + str(funcion)) #Se imprime el resultado de la aproximación

import math
potencia=math.exp(x)#Llamando la función exponencial de x
print("El valor real de la función exponencial de " +str(x) +" es "+ str(potencia))#Imprimiendo el valor real de la función exponencial de x

error=((abs(funcion-potencia))/(abs(potencia)))*100#Formula para calcular el error en porcentaje
print("El error es de " +str(error))#Imprimiendo error
```

La siguiente tabla muestra los valores de n con los que se obtiene menos del 0.1% de error, con valores de x desde 1 hasta 10.

|  x  |  n  |error               |
|-----|-----|--------------------|
|  1  |  6  |0.05941848175817597 | 
|  2  |  9  |0.02374473282612521 | 
|  3  |  11 |0.02923369506475417 | 
|  4  |  12 |0.0915229147270035  | 
|  5  |  14 |0.0697989979140001  | 
|  6  |  16 |0.05090982712176348 | 
|  7  |  17 |0.09581831589178165 | 
|  8  |  19 |0.06503681480925541 | 
|  9  |  21 |0.043925185772928046| 
|  10 |  22 |0.06996505123349094 | 


## Punto nueve
Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación. Determine con que valor n se obtiene menos del 0.1% de error.

**Código**
```
def elFactorial(x:int)->int:#Función para calcular el factorial
    factorial:int=1 #Declarando factorial como un entero e inicializandolo en 1
    for i in range(1,x+1):#Para todo número i desde 1 hasta el x ingresado, incrementando de uno en uno
        factorial=i*factorial#multiplicar el número i por el valor de factorial
    return factorial


def funcionSeno(x:float,n:int)->float:#Función para calcular una aproximación de la función seno
    suma : int = 0#Declarando suma como entero e inicializandolo en 0
    for i in range(0, n):#Para todo número i desde 0 hasta n-1, incrementando de uno en uno
        fact=elFactorial(2*i+1)#Se halla el factorial de (2*i+1), llamando la función elFactorial
        calculo=((-1)**i)*((x**(2*i+1))/fact)#se calcula (-1)^i*((x^(2i+1)/(2i+1)!)
        suma += calculo#Se suma los resultados hasta n-1
    return(suma)

if __name__=="__main__":
    n = int(input("Ingrese la cantidad de términos: "))#Declarando e inicializando n con input()
    x = float(input("Ingrese valor x: "))#Declarando e inicializando x con input()
    funcion=funcionSeno(x,n)#Se llama la función funcionSeno
    print("La aproximación de la función seno de " +str(x)+", con " + str(n) + " términos, es " + str(funcion)) #Se imprime el resultado de la aproximación
    

import math
potencia=math.sin(x)#Llamando la función seno de x
print("El valor real de la función seno de " +str(x) +" es "+ str(potencia))#Imprimiendo el valor real de la función seno de x

error=((abs(funcion-potencia))/(abs(potencia)))*100#Formula para calcular el error en porcentaje
print("El error es de " +str(error))#Imprimiendo error
```

La siguiente tabla muestra los valores de n con los que se obtiene menos del 0.1% de error, con valores de x desde 1 hasta 10.

|  x  |  n  |error               |
|-----|-----|--------------------|
|  1  |  3  |0.02325473632520346 | 
|  2  |  5  |0.005500494515743461| 
|  3  |  7  |0.007524890051635531| 
|  4  |  8  |0.006094618980173051| 
|  5  |  9  |0.015424121010932174| 
|  6  |  11 |0.01030909362229034 | 
|  7  |  12 |0.01229386496554245 | 
|  8  |  13 |0.020789417800142904| 
|  9  |  15 |0.01045015598196332 | 
|  10 |  16 |0.019515072875495535| 

## Punto diez
Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación. Determine con que valor n se obtiene menos del 0.1% de error.

**Código**
```
def funcionArcTan(x:float,n:int)->float:#Función para calcular una aproximación de la función arcotangente
    suma : int = 0#Declarando suma como entero e inicializandolo en 0
    for i in range(0, n):#Para todo número i desde 0 hasta n-1, incrementando de uno en uno
        calculo=((-1)**i)*((x**(2*i+1))/(2*i+1))#se calcula (-1)^i*((x^(2i+1)/(2i+1))
        suma += calculo#Se suma los resultados hasta n-1
    return(suma)

if __name__=="__main__":
    n = int(input("Ingrese la cantidad de términos: "))#Declarando e inicializando n con input()
    x = float(input("Ingrese valor x: "))#Declarando e inicializando x con input()
    funcion=funcionArcTan(x,n)#Se llama la función funcionArcTan
    print("La aproximación de la función arcotangente de " +str(x)+", con " + str(n) + " términos, es " + str(funcion)) #Se imprime el resultado de la aproximación
    

import math
arcTan=math.atan(x)#Llamando la función arcotangente de x
print("El valor real de la función arcotangente de " +str(x) +" es "+ str(arcTan))#Imprimiendo el valor real de la función arcotangente de x

error=((abs(funcion-arcTan))/(abs(arcTan)))*100#Formula para calcular el error en porcentaje
print("El error es de " +str(error))#Imprimiendo error
```
La siguiente tabla muestra los valores de n con los que se obtiene menos del 0.1% de error, con valores de x desde -1 hasta 1.

|  x  |  n  |error               |
|-----|-----|--------------------|
|  -1 | 319 |0.09978341824136393 | 
| -0.8|  9  |0.0712837225993695  | 
| -0.6|  5  |0.04684472248010963 | 
| -0.4|  3  |0.05474009552283815 | 
| -0.2|  2  |0.03152376709727691 | 
|  0.2|  2  |0.03152376709727691 | 
|  0.4|  3  |0.05474009552283815 | 
|  0.6|  5  |0.04684472248010963 | 
|  0.8|  9  |0.0712837225993695  | 
|  1  | 319 |0.09978341824136393 | 
