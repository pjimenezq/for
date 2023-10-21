# Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
for num in range(1,101):#Para cada número num desde 1 hasta 100, incrementando de uno en uno
    cuadrado=num**2#Hallar el valor de num elevado al cuadrado
    print(num,cuadrado,sep=", ")#Imprimir num y num al cuadrado (separados por una coma)
 
