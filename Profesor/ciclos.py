#ciclos while 


# while condicon:
#     cuerpo del while

# ejemplo:

contador=1 #INTERADORES
pare=10
while contador<=pare:
    print(contador)
    contador+=1

# grado intermedio tabla de multiplicar
# ver practica tabla de multiplicar

#grado avanzado
# menu de opciones
print("Elija una opcion para acceder a ella: \n\n 1- Suma\n 2-Resta\n 3-Multiplicar")
op=int(input("Opcion: "))
numero1=int(input("Ingrese un valor: "))
numero2=int(input("Ingrese un valor: "))
resultado=0
    
while op!=0:
    if op==1:
        resultado=numero1+numero2
        print(f'El valor de la suma es {resultado}')
        break
    else:
        if op==2:
            resultado=numero1-numero2
            print(f'El valor de la resta es {resultado}')
            break
        else:
            if op==3:
                resultado=numero1*numero2
                print(f'El valor de la multiplicacion es {resultado}')
                break
else:
    print("Fin de la calculadora")
        

# ciclos for 
# ejemplo c++ 
# for int i > 0:
#     bucle del for
# for 



