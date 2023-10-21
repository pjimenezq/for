#Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
x=int(input("Ingrese un número natural: "))#Declarando e inicializando x con la funcion input()
factorial:int=1 #Declarando factorial como un entero e inicializandolo en 1
for i in range(1,x+1):#Para todo número i desde 1 hasta el x ingresado, incrementando de uno en uno
    factorial=i*factorial#multiplicar el número i por el valor de factorial
    print (i,factorial,sep=",")#Imprimir el número i y el factorial de i (separados por una coma)

