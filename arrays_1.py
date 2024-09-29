# Los modulos estan guardados en el mismo repo de github

from funciones_paquete.d1.funciones_modulo1 import *
# import listas_personas as ls
from paquete_ejs.funciones_listas import * 
from paquete_ejs.funciones_listas import *


# 1

# def NombreLista()-> list:
#     lista = []
#     for i in range(1, 11):
#         nombre = input(f'Ingrese el {i}° nombre: ')
#         lista.append(nombre)
#     return lista

# for i in NombreLista(): 
#     print(i)


# 2

# def ReemplazarLista()-> list:
#     lista = [0] * 10

#     indice_elegido = int(input('Elija que indice de la lista quiera cambiar(de 0 a 9): '))
#     indice_elegido = ValidacionInt(indice_elegido, 0, 9)
#     cambio = input('Ingrese el valor que quiere ingresar')

#     lista[indice_elegido] = cambio

#     return lista

# for i in ReemplazarLista():
#     print(i)


# 3


# def ListaValidacion()-> list:
#     lista = []
#     for i in range(1, 11):
#         valor = int(input(f'Ingrese el {i}° valor entre 1 y 100: '))
#         valor = ValidacionInt(valor, 1, 100)
#         lista.append(valor)
#     return lista

# for i in ListaValidacion():
#     print(i)


# 4

# def BuscaInt(lista: list, numero: int):
#     for i in lista:
#         if i == numero:
#             return True
#     return False

# lista = [1, 2, 3, 4, 5]
# numero = int(input('Ingrese un numero: '))
# print(BuscaInt(lista, numero))


# 5

# nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro",
#          "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]

# edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

# def EncontrarMenor(nombres: list, edades: list)-> int:
#     menor_edad = edades[0]
#     menor_nombre = nombres[0]
#     for i in range(len(edades)):

#         if edades[i] < menor_edad:
#             menor_edad = edades[i]
#             menor_nombre = nombres[i]

#         elif edades[i] == menor_edad and menor_nombre != nombres[i]:
#             menor_nombre = f'{menor_nombre}, {nombres[i]}'
        
#     return menor_nombre, menor_edad
    
# print(EncontrarMenor(nombres, edades))
# print(f'La(s) personas mas jovenes son {EncontrarMenor(nombres, edades)[0]} con {EncontrarMenor(nombres, edades)[1]} años')


# 6


# lista = []
# def ListaImport():

#     for i in ls.nombres:
#         lista.append(i)

#     return(lista)

# for i in ListaImport():
#     print(i)

# 7

def menu_opciones():
    importado = False
    seguir = 's'
    while seguir == 's':

        print('Elija una de las siguientes opciones: \n'
            '[1] Importar listas \n'
            '[2] Listar los datos de los usuarios de México \n'
            '[3] Listar los nombre, mail y teléfono de los usuarios de Brasil \n'
            '[4] Listar los datos del/los usuario/s más joven/es \n'
            '[5] Obtener un promedio de edad de los usuarios \n'
            '[6] De los usuarios de Brasil, listar los datos del usuario de mayor edad \n'
            '[7] Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 \n'
            '[8] Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.')
        
        opcion_elegida = input('>>> ')
        opcion_elegida = ValidacionList(['1', '2', '3', '4', '5', '6', '7', '8'], opcion_elegida)

        if opcion_elegida == '1':
            from paquete_ejs.listas_personas import nombres, telefonos, mails, address, postalZip, region, country, edades
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

        seguir = input('¿Desea seguir (s, n)?: ')
        seguir = ValidacionList(['s', 'n'], seguir)


menu_opciones()



