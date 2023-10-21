#Calcular el valor de 2 elevado a la potencia n usando ciclos for.
n=int(input("Ingrese el valor del exponente n: "))#Declarando e inicializando n con la función input()
potencia:int=2#Declarando e inicializando ptencia como un entero con valor de 2
for x in range(2,n+1):#Para todo número x desde 2 hasta n, incrementando de uno en uno
    potencia=2*potencia#multiplicar potencia por 2 (haciendo que 2 se multiplique por si mismo n veces)
print("2 elevado a la "+str(n)+" es igual a "+str(potencia))#Imprimir el valor final de potencia
