from data_stark import lista_is
from stark_funciones import *
from funciones_modulo1 import validar_lista

seguir = 's'
while seguir == 's':
    print('''Elija entre una de las opciones 
[1] Listar nombre ordenados
[2] Determinar el superheroe masculino mas debil
[3] Determinar cantidad de superheroes con cada color de ojos
[4] Listar superheroes por color de pelo
[5] Listar superheroes por inteligencia
[6] Mostrar datos de superheroes mas fuertes que el promedio femenino
[7] Calcular y guardar IMCs
[8] Cerrar el programa''')

    opcion = input('>>> ')
    opcion = validar_lista(['1','2','3','4','5','6','7','8'], opcion)
    
    if opcion == '1':
        print('Lista de personajes ordenados por nombre: ')
        printear_datos(ordenar_listas(lista_is, 'nombre', 'ascendente'))
    
    elif opcion == '2':
        printear_datos(encontrar_mas_debil(lista_is, 'M'))

    elif opcion == '3':
        print('Lista de cantidad de personajes por colores de ojos: ')
        printear_datos(contar_caracteristicas(lista_is, 'color_ojos'))

    elif opcion == '4':
        print('Personajes listados por color de pelo: ')
        printear_datos(listar_por(lista_is, 'color_pelo'))

    elif opcion == '5':
        print('Personajes listados por inteligencia: ')
        printear_datos(listar_por(lista_is, 'inteligencia'))

    elif opcion == '6':
        print('Personajes con fuerza mayor al promedio femenino: ')
        printear_datos(listar_nombre_peso(lista_is))

    elif opcion == '7':
        print('IMCs de cada personaje: ')
        printear_datos(asignar_imc(lista_is))
        print('Los datos han sido agregados a la lista')

    elif opcion == '8':
        verificacion = input('¿Está seguro de que quiere cerrar el programa? (s / n): ')
        verificacion = validar_lista(['s', 'n'], verificacion)
        if verificacion == 's':
            print('Gracias por usar el programa')
            seguir = 'n'
