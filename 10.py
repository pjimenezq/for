#Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
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