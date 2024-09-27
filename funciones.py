

def EsPar(a):
    if a % 2 == 0:
        par = True
    else: 
        par = False
    return(par)

def RealizarDescuento(a_descontar: int, descuento: float)-> float:
    # Ingresa el valor iniciado seguido por el descuento
    # Devuelve el valor descontado

    descontado = a_descontar - a_descontar * descuento
    return(descontado)

def ValidacionInt(a: int, b: int, c: int)-> int:
    # Ingresa el valor a verificar seguido por los numeros que definen el rango
    # Valida que el numero este dentro del rango y devuelve el numero ingresado

    while a < b or a > c:
        print(f'Ingrese un número entre {b} y {c}')
        a = int(input(f'Ingrese un número(entre {b} y {c}): '))
    
    return(a)


def ValidacionStr(a, b, c):
    # Ingresa lo ingresado por el usuario y las opciones
    # Valida el ingreso y devuelve la opcion elegida
    
    while a.lower() != b and a.lower() != c:
        print(f'Elija entre {b} y {c}: ')
        operacion = input('>>> ')

    return(a.lower())


def ValidacionList(opciones: list, a_validar: str)-> str:
    # Se ingresan las opciones seguidas por lo ingresado por el usuario
    # Valida que lo elegido esté dentro de las opciones
    # Devuelve la opción elegida

    validacion = False
    a_validar = a_validar.lower()

    for i in opciones:
            if str(i) == a_validar:
                validacion = True

    while validacion == False:
        print(f'Ingrese entre una de las opciones {opciones}: ')
        a_validar = input('>>> ')

        for i in opciones:
            if str(i) == a_validar:
                validacion = True

    return(a_validar)
        
# entrado = input('Ingrese una opcion (si, no, blanco, negro): ')
# print(f'La opcion elegida fue: {ValidacionList([4, 5, 2], entrado)}')





