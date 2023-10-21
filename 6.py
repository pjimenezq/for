#Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
n=int(input("Ingrese el valor del exponente n: "))#Declarando e inicializando n con la función input()
x=int(input("Ingrese el valor de la base x: "))#Declarando e inicializando x con la función input()
potencia:int=x#Declarando e inicializando potencia como un entero con el mismo valor que x
for num in range(2,n+1):#Para todo número num desde 2 hasta n, incrementando de uno en uno
    potencia=x*potencia#multiplicar potencia por x (haciendo que x se multiplique por si mismo n veces)
print(str(x)+ " elevado a la "+str(n)+" es igual a "+ str(potencia))#Imprimiendo el valor calculado de la potencia