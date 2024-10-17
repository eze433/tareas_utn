#strings
#1

def check(cadena:str, caracter:str)->int:
    contador = 0
    for letra in cadena:
        if letra.lower() == caracter:
            contador += 1
    return contador


#2

def range_index(indice1:int, indice2:int, cadena:str):   
    while indice1 + 1 > len(cadena) or indice1 < len(cadena) * -1:
        indice1 = int(input('Ingrese un indice en el rango del string: '))

    while indice2 + 1 > len(cadena) or indice2 < len(cadena) * -1:
        indice2 = int(input('Ingrese un indice en el rango del string: '))

    return cadena[indice1:indice2]

# print(range_index(3,-5,'Holas'))


# 3

def index_check(indice1:int, cadena:str):

    while indice1 + 1 > len(cadena) or indice1 < len(cadena) * -1:
        indice1 = int(input('Ingrese un indice en el rango del string: '))

    return cadena[indice1]

# print(index_check(5,'Holas'))

# documento 2

# 1

def matriz_cadena(cadena:str)->list:
    matriz = [['a', 0],
              ['e', 0],
              ['i', 0],
              ['o', 0],
              ['u', 0]]
    
    cadena = cadena.lower()
    for letra in cadena:

        if letra == 'a':
            matriz[0][1] += 1

        elif letra == 'e':
            matriz[1][1] += 1

        elif letra == 'i':
            matriz[2][1] += 1

        elif letra == 'o':
            matriz[3][1] += 1

        elif letra == 'u':
            matriz[4][1] += 1

    return matriz

# print(matriz_cadena('AeIOue'))

# 2

def check_esta(caracter:str, cadena:str)-> int:
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            return i
        
    return -1

# print(check_esta('a', 'holas'))

# 3

def pal_check(cadena:str)->bool:
    cadena = cadena.lower()
    for i in range(len(cadena)):
        if cadena[i] != cadena[-(i + 1)]:
            return False
    
    return True

# print(pal_check('rottor'))

#4

def no_repite(cadena:str):
    cadena_2 = ''
    for i in range(len(cadena)):
        flag = True
        for letra in cadena_2:
            if cadena[i] == letra:
                flag = False
                break
        if flag == True:
            cadena_2 += cadena[i]

    return cadena_2

# print(no_repite('Hoooolljllaaalillaaaeaa'))

# 5

def sin_vocales(cadena:str)->str:
    vocales = ('a','e','i','o','u')
    cadena_2 = ''
    for letra in cadena:
        flag = True
        for vocal in vocales:
            if letra.lower() == vocal:
                flag = False
        if flag == True:
            cadena_2 += letra

    return cadena_2

# print(sin_vocales('adepoiurfu'))

# 6

def subcadenas(cadena, subcadena):
    contador = 0
    for i in range(len(cadena)):
        if cadena[i : i + len(subcadena)] == subcadena:
            contador += 1

    return contador

# print(subcadenas('panEl pan del panaderopan', 'pan'))


            
                    

                
            
                    

        



        



