from paquete.funciones_listas import *
from paquete.funciones_modulo1 import *

# 1

# nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia",
#            "Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]

# edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

# band = False
# while band == False:
#     band = True
#     for i in range(len(nombres) - 1):
#         if nombres[i] > nombres[i + 1]:
#             nombres[i], nombres[i + 1] = nombres[i + 1], nombres[i]
#             edades[i], edades[i + 1] = edades[i + 1], edades[i]
#             band = False
    
# print(nombres)
# print(edades)


# 2

# nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales"
#            ,"Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
#            "Base de Datos", "Ergonomia", "Naturaleza"]

# puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]


# bandera = False
# while bandera == False:
#     bandera = True
#     for i in range(len(nombres) - 1):
#         if nombres[i] > nombres[i + 1]:
#             nombres[i], nombres[i + 1] = nombres[i + 1], nombres[i]
#             puntos[i], puntos[i + 1] = puntos[i + 1], puntos[i]
#             bandera = False
#         elif nombres[i] == nombres[i + 1]:
#             print(True)
#             if puntos[i] < puntos[i + 1]:
#                 puntos[i], puntos[i + 1] = puntos[i + 1], puntos[i]
#                 bandera = False


# print(nombres)
# print(puntos)


# 3

# estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
# apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
# nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]


# bandera = False
# while bandera == False:

#     bandera = True
#     for i in range(len(apellidos) - 1):
#         if apellidos[i] > apellidos[i + 1]:
#             apellidos[i], apellidos[i + 1] = apellidos[i + 1], apellidos[i]
#             estudiantes[i], estudiantes[i + 1] = estudiantes[i + 1], estudiantes[i]
#             nota[i], nota[i + 1] = nota[i + 1], nota[i]
#             bandera = False

#         elif apellidos[i] == apellidos[i + 1]:
            
#             if estudiantes[i] > estudiantes[i + 1]:
#                 estudiantes[i], estudiantes[i + 1] = estudiantes[i + 1], estudiantes[i]
#                 nota[i], nota[i + 1] = nota[i + 1], nota[i]
#                 bandera = False

#             elif estudiantes[i] == estudiantes[i + 1]:
                
#                 if nota[i] < nota[i + 1]:
#                     nota[i], nota[i + 1] = nota[i + 1], nota[i]
#                     bandera = False

# print(apellidos)
# print(estudiantes)
# print(nota)

# 4

def menu_opciones():
    importado = False
    seguir = 's'
    while seguir == 's':

        print(
            'Elija una de las siguientes opciones: \n'
            '[1] Importar listas \n'
            '[2] Listar los datos de los usuarios de México \n'
            '[3] Listar los nombre, mail y teléfono de los usuarios de Brasil \n'
            '[4] Listar los datos del/los usuario/s más joven/es \n'
            '[5] Obtener un promedio de edad de los usuarios \n'
            '[6] De los usuarios de Brasil, listar los datos del usuario de mayor edad \n'
            '[7] Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 \n'
            '[8] Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años \n'
            '[9] Listar nombres de mexicanos en orden alfabético \n'
            '[10] Listar los usuario de menor a mayor \n'
            '[11] Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 ordenados\n'
            )
        
        opcion_elegida = ValidacionList(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])

        if opcion_elegida == '1':
            from paquete.listas_personas import nombres, telefonos, mails, address, postalZip, region, country, edades
            importado = True
        
        if opcion_elegida == '2':
            if chequeo_import(importado) == True:
                mexico_usuarios(country, nombres, telefonos, mails, 
                    address, postalZip, region, edades)
                
        if opcion_elegida == '3':
            if chequeo_import(importado) == True:
                brasil_usuarios(country, nombres, mails, telefonos)

        if opcion_elegida == '4':
            if chequeo_import(importado) == True:
                menores(country, nombres, telefonos, mails, 
                        address, postalZip, region, edades)
        
        if opcion_elegida == '5':
            if chequeo_import(importado) == True:
                print(f'El promedio de edad de los contactos es: {promedio_edad(edades)}')

        if opcion_elegida == '6':
            if chequeo_import(importado) == True:
               brasil_mayor(country, nombres, telefonos, mails, 
                            address, postalZip, region, edades)
               
        if opcion_elegida == '7':
            if chequeo_import(importado) == True:
                mx_bz_8000(country, nombres, telefonos, mails, 
                            address, postalZip, region, edades)

        if opcion_elegida == '8':
            if chequeo_import(importado) == True:
                italianos_40(country, nombres, telefonos, mails, edades)

        if opcion_elegida == '9':
            if chequeo_import(importado) == True:
                mexico_sort(country, nombres)

        if opcion_elegida == '10':
            if chequeo_import(importado) == True:
                orden_edad(edades, nombres)

        if opcion_elegida == '11':
            if chequeo_import(importado) == True:
                mx_bz_sort(country, postalZip, edades, nombres)

        print('¿Desea seguir (s, n)?: ')
        seguir = ValidacionList(['s', 'n'])


menu_opciones()


