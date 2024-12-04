from funciones import *
from funciones_modulo1 import validar_lista, validar_int

seguir = 's'

while seguir == 's':
    lista = generar_tablero()

    for fila in lista:
        print(fila['piezas'])

    columna = int(input('Ingrese la columna: '))
    columna = validar_int(columna, 0, 6)
    fila = int(input('Ingrese la fila: '))
    fila = validar_int(fila, 0, 3)

    verificacion = verificar_eleccion(columna, fila, lista)

    if verificacion == True:
        print('HA GANADO 10 PUNTOS')
    else:
        print('INTENTELO DE NUEVO')

    nombre = input('Ingrese su nombre: ')

    while nombre.isalnum() == False:
        print('Su nombre debe contener solo letras o numeros')
        nombre = input('Ingrese su nombre: ')

    escribir_puntos(nombre, verificacion)

    seguir = input('¿Quiere seguir jugando? (s / n): ')
    seguir = validar_lista(['s', 'n'], seguir)

