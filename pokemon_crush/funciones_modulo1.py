def es_par(a):
    if a % 2 == 0:
        par = True

    else: 
        par = False

    return(par)

def descuento(a_descontar: int, descuento: float)-> float:
    # Ingresa el valor iniciado seguido por el descuento
    # Devuelve el valor descontado

    descontado = a_descontar - a_descontar * descuento
    return(descontado)

def validar_int(a: int, b: int, c: int)-> int:
    # Ingresa el valor a verificar seguido por los numeros que definen el rango
    # Valida que el numero este dentro del rango y devuelve el numero ingresado

    while a < b or a > c:
        a = int(input(f'Ingrese un número entre {b} y {c}: '))
    
    return(a)


def validar_str(a, b, c):
    # Ingresa lo ingresado por el usuario y las opciones
    # Valida el ingreso y devuelve la opcion elegida
    
    while a.lower() != b and a.lower() != c:
        print(f'Elija entre {b} y {c}: ')
        operacion = input('>>> ')

    return(a.lower())


def validar_lista(opciones: list, opcion: any)-> str:
    # Se ingresan las opciones
    # Valida que lo elegido esté dentro de las opciones
    # Devuelve la opción elegida

    validacion = False

    for i in opciones:
        if i == opcion:
            validacion = True

    while validacion == False:
        print(f'Ingrese entre una de las opciones {opciones}: ')

        if type(opcion) == int:
            opcion = int(input('>>> '))

        else:
            opcion = input('>>> ')
        
        for i in opciones:
            if i == opcion:
                validacion = True

    return opcion


def bub_sort(lista: list)-> list:
    # Regresa una lista ordenada de menor a mayor
    bandera = False

    while bandera == False:
        bandera = True
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                bandera = False

    return lista

# print(bub_sort([100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]))




