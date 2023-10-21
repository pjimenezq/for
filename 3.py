# Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
x=int(input("Ingrese un número natural: "))#Declarando e inicializando x con la funcion input()
if x%2!=0:#Si el modulo de x dividido entre 2 es diferente a 0, x es impar
    x-=1#Se le resta a x una unidad, para que sea un número par
for i in range(x, 1, -2): print(i)#Para cada número i desde x hasta 2, disminuyendo de dos en dos, imprimir i