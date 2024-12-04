from inicializaciones import *
import pygame as ga
import random as ra

def generar_tabla(slots: list)-> list:
    lista = [
    {'piezas':[]},
    {'piezas':[]},
    {'piezas':[]},
    {'piezas':[]}
    ]

    # lleno la tabla con valores de 1 a 3
    for fila in range(len(lista)):
        for i in range(0, 7):
            lista[fila]['piezas'].append(ra.randint(1, 3))

    # ordeno los rectangulos para ponerlos en la tabla
    posicion_x = 160
    posicion_y = 260
    suma_x = 112
    suma_y = 112
    indice_x = 0
    indice_y = 0

    for fila in lista:
        for numero in fila['piezas']:
        # depende del valor del numero generado asigna un pokemon
            if numero == 1:
                pokemon = bulbasaur
            elif numero == 2:
                pokemon = charmander
            elif numero == 3:
                pokemon = squirtle

            slot_rect = pokemon.get_rect(center= (posicion_x, posicion_y))
            # guardo la configuracion de los slots
            slots.append({'pokemon': pokemon, 'rect': slot_rect, 'indice_x': indice_x, 'indice_y': indice_y})
            posicion_x += suma_x
            indice_x += 1

        posicion_x = 160
        posicion_y += suma_y
        indice_x = 0
        indice_y += 1

    return lista


def verificar_eleccion(x:int, y:int, lista:list)-> list:
    # chequea si hay tres numeros seguidos iguales horizontal o verticalmente
    # x = columna elegida
    # y = fila elegida

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
    
    # verifico una vez mas por si la secuencia está al final de una fila/columna
    if len(lista_x) == 3:
        for i in lista_x:
            if x == i:
                flag_x = True

    if len(lista_y) == 3:
        for i in lista_y:
            if y == i:
                flag_y = True

    puntos = False
    
    # creo una variable final
    if flag_x or flag_y:
        puntos = True
    
    return puntos


def ordenar_listas(lista_1:list, lista_2:list, asc_desc:str)-> list:
    # ordena ascendentement o descendentemente depende lo pasado
    bandera = False
    while bandera == False:
        bandera = True
        for i in range(len(lista_1) - 1):
            if asc_desc == 'asc':
                if lista_1[i] > lista_1[i + 1]:
                    lista_1[i], lista_1[i + 1] = lista_1[i + 1], lista_1[i]
                    lista_2[i], lista_2[i + 1] = lista_2[i + 1], lista_2[i]
                    bandera = False

            elif asc_desc == 'desc':
                if lista_1[i] < lista_1[i + 1]:
                    lista_1[i], lista_1[i + 1] = lista_1[i + 1], lista_1[i]                        
                    lista_2[i], lista_2[i + 1] = lista_2[i + 1], lista_2[i]
                    bandera = False

    return lista_1, lista_2

def escribir_puntos(nombre:str, puntos:int)-> None:
    # recorre linea por linea y chequea si el nombre coincide
    # si coincide cambia los puntos, si no coincide crea una nueva linea con ese nombre y puntos
    with open('puntos.csv', 'r+') as archivo:
        primero = True
        guardado = False

        for linea in archivo:
            
            posicion = linea.find(':')

            if linea[:posicion] == nombre.lower():
                if puntos > int(linea[posicion + 1:]):
                    linea = f'{linea[:posicion]}:{puntos}\n'
                guardado = True

            if primero:
                string = linea
                primero = False
            
            else:
                string = f'{string}{linea}'

        if guardado == False:
            string = f'{string}{nombre.lower()}:{puntos}\n'

    
        archivo.seek(0)
        archivo.write(string)