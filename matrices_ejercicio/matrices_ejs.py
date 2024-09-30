from funciones_modulo1 import *
from ejs_matrices import *

# 1


seguir = 's'

alta_check = False

while seguir == 's':

    print('\n¿Que quiere hacer? \n'
          f'[1] Agregar producto \n'
          f'[2] Sacar producto \n'
          f'[3] Modificar producto \n'
          f'[4] Listar productos \n'
          f'[5] Listar productos por nombre \n'
          f'[6] Salir')
    
    elegida = input('>>> ')
    elegida = ValidacionList(['1', '2', '3', '4', '5', '6'], elegida)

    if elegida == '1':
            alta_producto()
            alta_check = True
    
    if elegida == '2':
        if alta_check_func(alta_check) == True:
            baja_producto()

    if elegida == '3':
        if alta_check_func(alta_check) == True:
            modificar_productos()

    if elegida == '4':
        listar_productos()

    if elegida == '5':
        listar_alfa()

    if elegida == '6':
        print('Gracias por usar el programa')
        break
        
        



    

# fila_elegida = int(input('Elija una fila (1 a 3): '))
# fila_elegida = int(ValidacionList([1, 2, 3], fila_elegida))
# columna_elegida = int(input('Elija una columna (1 a 5): '))
# columna_elegida = int(ValidacionList([1, 2, 3, 4, 5], columna_elegida))

# print(almacen_matriz[fila_elegida - 1][columna_elegida - 1])




