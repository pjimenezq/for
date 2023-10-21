#Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

for num in range(1,10):#Para todo número num desde 1 hasta 9, incrementando de uno en uno
    for x in range(1,11):#Para todo x desde 1 hasta 10, incrementando de uno en uno
        multiplicacion=num*x#calcular el valor del número num multiplicado por x
        print(num,"x",x,"=",multiplicacion)#Imprimir num por x es igual al resultado de la multiplicación
