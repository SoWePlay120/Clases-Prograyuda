opcion=int(input("Digite el numero que quiere que se multiplique: "))
print ("Tabla de multiplicar de ",opcion,":")
limite=12
contador=1
while contador<=limite:
    resultado=contador*opcion
    print (opcion,"x",contador,"=",resultado,)
    contador = contador + 1

