from funciones_modulo1 import validar_int
import random as ra
 
lista = [
{"piezas":[]},
{"piezas":[]},
{"piezas":[]},
{"piezas":[]}
]

for fila in range(len(lista)):
    for i in range(0, 7):
        lista[fila]['piezas'].append(ra.randint(1, 3))

for fila in lista:
    print(fila['piezas'])

def verificar_eleccion(x:int, y:int)-> None:
    # chequea si hay tres numeros seguidos iguales horizontal o verticalmente
    # x = fila elegida
    # y = columna elegida

    lista_x = []
    lista_y = []
    flag_x = False
    flag_y = False
    check = 0

    for i in range(len(lista[y]['piezas'])):
        # i es el indice de los numeros en horizontal

        if len(lista_x) == 3 and x in lista_x:
            break

        elif lista[y]['piezas'][i] == check:
            lista_x.append(i)

        else:
            lista_x = [i]
            check = lista[y]['piezas'][i]

    check = 0

    for i in range(len(lista)):
        # i es el indice de los numeros en vertical
        
        if len(lista_y) == 3 and y in lista_y:
            break

        elif lista[i]['piezas'][x] == check:
            lista_y.append(i)

        else:
            lista_y = [i]
            check = lista[i]['piezas'][x]
    
    if len(lista_x) == 3:
        for i in lista_x:
            if x == i:
                flag_x = True

    if len(lista_y) == 3:
        for i in lista_y:
            if y == i:
                flag_y = True
        
    if flag_x == True or flag_y == True:
        print('HA GANADO 10 PUNTOS')
    else:
        print('SEGUI PARTICIPANDO')


columna = int(input('Ingrese la columna: '))
columna = validar_int(columna, 0, 6)
fila = int(input('Ingrese la fila: '))
fila = validar_int(fila, 0, 3)


verificar_eleccion(columna, fila) 
