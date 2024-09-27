from funciones_paquete.d1.funciones_modulo1 import *

# resultado = 0

# def Recursiva(numero):
#     if numero == 0:
#         resultado = 1
#     else:
#         resultado = numero * Recursiva(numero - 1)
    
#     return(resultado)

# numero = int(input('Ingrese un numero: '))

# print(Recursiva(numero))

# 1

# total = 0

# def sumarNaturales(numero: int)-> int:

#     if numero != 0:
#         total = numero + sumarNaturales(numero - 1)
#     else:
#         total = 0

#     return(total)

# print(sumarNaturales(5))


# 2

# resultado = 1

# def calcular_potencia(numero: int, exponente: int)-> int:
#     if exponente != 0:
#         resultado = numero * potencia(numero, exponente - 1)
#     else:
#         resultado = 1

#     return(resultado)

# print(calcular_potencia(10, 4))

# 3

# resultado = 0


# def suma_digitos(numero: int)-> int:
#     if numero == 0:
#         resultado = 0
#     else:
#         resultado = numero % 10 + suma_digitos(numero // 10)
    
#     return(resultado)

# print(suma_digitos(12345))

# 4

def fibonacci(numero: int)-> int:
    if numero == 0:
        resultado = 0
    elif numero == 1:
        resultado = 1
    else:
        resultado = fibonacci(numero - 1) + fibonacci(numero - 2)

    return resultado

numero = int(input("Ingrese un número: "))
ValidacionInt(numero, 1, 100)
print(fibonacci(numero))

