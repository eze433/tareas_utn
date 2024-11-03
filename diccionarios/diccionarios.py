from estudiantes import estudiantes_1
from funciones_modulo1 import validar_lista
from funciones_dict import *


seguir = 's'
while seguir == 's':
    print("""
[1] Listar alumnos
[2] Promedios de nota
[3] Información Ingenieria en informática
[4] Promedios de edad
[5] Alumno mayor promedio
[6] Club de informática
[7] Info mas jovenes
[8] Salir""")

    eleccion = validar_lista(['1', '2', '3', '4', '5', '6', '7', '8'])

    if eleccion == '1':
        ordenar_alumnos(estudiantes_1)
    
    elif eleccion == '2':
        promediar_notas(estudiantes_1)
        
    elif eleccion == '3':
        listar_ingenieria(estudiantes_1)

    elif eleccion == '4':
        promediar_edades(estudiantes_1)

    elif eleccion == '5':
        mostrar_mayor_promedio(estudiantes_1)

    elif eleccion == '6':
        mostrar_club_informatica(estudiantes_1)

    elif eleccion == '7':
        mostrar_mas_jovenes(estudiantes_1)

    elif eleccion == '8':
        print('Gracias por usar el programa')
        seguir = 'n'

            
