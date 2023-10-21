#Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

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



