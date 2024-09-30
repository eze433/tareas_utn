from funciones_modulo1 import *

almacen_matriz = [[['[1 , 1]', 0, 'nada'], ['[1 , 2]', 3, 'botellas'], ['[1 , 3]', 0, 'nada'], ['[1 , 4]', 8, 'frascos'], ['[1 , 5]', 0, 'nada']],
                  [['[2 , 1]', 0, 'nada'], ['[2 , 2]', 0, 'nada'], ['[2 , 3]', 4, 'fideos'], ['[2 , 4]', 0, 'nada'], ['[2 , 5]', 0, 'nada']],
                  [['[3 , 1]', 0, 'nada'], ['[3, 2]', 0, 'nada'], ['[3, 3]', 0, 'nada'], ['[3, 4]', 0, 'nada'], ['[3, 5]', 6, 'leches']]]



def alta_check_func(alta_check: bool)-> bool:
    if alta_check == False:
        print('ERROR, debe agregar un producto antes de acceder a esta opción')
        return False
    else:
        return True

def alta_producto():
    print('Elija fila y columna para agregar productos \n')
    fila_elegida = input('Elija una fila (1 a 3): ')
    fila_elegida = ValidacionList(['1', '2', '3'], fila_elegida)
    columna_elegida = input('Elija una columna (1 a 5): ')
    columna_elegida = ValidacionList(['1', '2', '3', '4', '5'], columna_elegida)

    if almacen_matriz[int(fila_elegida) - 1][int(columna_elegida) - 1][1] == 0:
        nuevo = input('Ingrese el producto que quiere añadir: ')
        almacen_matriz[int(fila_elegida) - 1][int(columna_elegida) - 1][2] = nuevo
        cant_nuevo = int(input('Ingrese la cantidad del producto que quiere añadir (maximo 20): '))
        cant_nuevo = ValidacionInt(cant_nuevo, 1, 20)
        almacen_matriz[int(fila_elegida) - 1][int(columna_elegida) - 1][1] = cant_nuevo
        print(almacen_matriz[int(fila_elegida) - 1][int(columna_elegida) - 1])

    
    else:
        print('Este espacio ya tiene productos, use la opcion [3] para modificarlos')

def baja_producto():

        confirmacion = 'n'
        while confirmacion == 'n':
            print('Elija fila y columna para sacar productos \n')
            fila_elegida = input('Elija una fila (1 a 3): ')
            fila_elegida = ValidacionList(['1', '2', '3'], fila_elegida)
            columna_elegida = input('Elija una columna (1 a 5): ')
            columna_elegida = ValidacionList(['1', '2', '3', '4', '5'], columna_elegida)

            print(f'¿Estas seguro de que quieres borrar esto {almacen_matriz[int(fila_elegida) - 1][int(columna_elegida) - 1]}? (s / n): ')
            confirmacion = input('>>> ')
            confirmacion = ValidacionList(['s', 'n'], confirmacion)
            
            if confirmacion == 's':
                almacen_matriz[int(fila_elegida) - 1][int(columna_elegida) - 1] = [f'[{int(fila_elegida)} , {int(columna_elegida)}]', 0, 'nada']
                print(almacen_matriz[int(fila_elegida) - 1][int(columna_elegida) - 1])

def modificar_productos():
    print('Elija fila y columna para agregar productos \n')
    fila_elegida = input('Elija una fila (1 a 3): ')
    fila_elegida = ValidacionList(['1', '2', '3'], fila_elegida)
    columna_elegida = input('Elija una columna (1 a 5): ')
    columna_elegida = ValidacionList(['1', '2', '3', '4', '5'], columna_elegida)

    print(f'Va a cambiar {almacen_matriz[int(fila_elegida) - 1][int(columna_elegida) -1]} \n'
        '[1] Cambiar la cantidad \n'
        '[2] Cambiar el producto')
    
    cambio = input('>>> ')
    cambio = ValidacionList(['1', '2'], cambio)

    if cambio == '1':
        cambio_cant = int(input('Ingrese la nueva cantidad: '))
        cambio_cant = ValidacionInt(cambio_cant, 1, 20)
        almacen_matriz[int(fila_elegida) - 1][int(columna_elegida) -1][1] = cambio_cant

    elif cambio == '2':
        cambio_prod = input('Ingrese el nuevo producto: ')
        almacen_matriz[int(fila_elegida) - 1][int(columna_elegida) -1][2] = cambio_prod

    print(almacen_matriz[int(fila_elegida) - 1][int(columna_elegida) -1])

def listar_productos():
    print('Lista de los productos')
    for i in almacen_matriz:
        for j in i:
            if j[1] > 0:
                print(f'{j[0]}: {j[1]} {j[2]}')

def listar_alfa():
    lista = []
    print('Lista de los productos en orden alfabético')
    for i in almacen_matriz:
        for j in i:
            if j[1] > 0:
                lista.append(j[2])
    
    for i in sorted(lista):
        print(i)
            



    



    

            






# alta_producto()