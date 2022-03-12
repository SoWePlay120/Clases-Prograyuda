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
# 
        

# ciclos for 
# ejemplo c++ 
# for int i > 0:
#     bucle del for

# hacer el contador de letras
palabra=str(input("Digite una palabra"))
letra=str(input("Digite una letra"))

# Esteban
# letras

# for letras in 'Holanda':
#     if letras == 'a':
#         print(f'Letra encontrada:{letras}')
#         break
# else:
#     print("Ciclo acabado")

for letras in palabra: 
    if letras == letra:
        print(f'se encontraron:{letras}')
        break
else:
    print("Ciclo acabado")

#otro for
print("Tabla de mutiplicar for")
for numero in  [0, 1, 2, 3]:
    print(f"{numero} * {numero} = {numero ** 2}")
print("Final")
