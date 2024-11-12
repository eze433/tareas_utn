from data_stark import lista_is

def promediar(lista:list, key:str, valor:str, a_promediar:str)-> int:
    acumulador = 0
    contador = 0
    
    for personaje in lista:
        if personaje[key] == valor:
            acumulador += int(personaje[a_promediar])
            contador += 1

    return acumulador / contador

def printear_datos(mensaje:str):

    if type(mensaje) == list:
        for i in mensaje:
            print('')
            if type(i) == dict:
                for key, value in i.items():
                    print(f'{key}: {value}')
            else:
                print(i)

    elif type(mensaje) == dict:
        for key, value in mensaje.items():
            print(f'{key}: {value}')

    else:
        print(mensaje)

    print('')

def encontrar_caracteristicas(lista:list, key:str)-> list:
    lista_car = []
    
    for personaje in lista:
        flag = False
        for caracteristica in lista_car:
            if personaje[key] == caracteristica:
                flag = True
        if flag == False:
            lista_car.append(personaje[key])


    return lista_car


def ordenar_listas(lista:list, palabra:str, asc_desc:str)-> list:
    # punto a
    flag = False

    while flag == False: 
        flag = True
        for i in range(len(lista) - 1):
            if asc_desc == 'ascendente':
                if lista[i][palabra] > lista[i + 1][palabra]:
                    aux = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = aux
                    # lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    flag = False

            elif asc_desc == 'descendente':
                if lista[i][palabra] > lista[i + 1][palabra]:
                    aux = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = aux
                    flag = False

    return lista

def encontrar_mas_debil(lista: list, busqueda: str)-> str:
    # punto b
    min = -1

    for personaje in lista:
        for valor in personaje.values():
            if valor == busqueda:
                if int(personaje['fuerza']) < min or min == -1:
                    min = int(personaje['fuerza'])
                    min_nombre = personaje['nombre']
                elif int(personaje['fuerza']) == min:
                    min_nombre = f'{min_nombre} y {personaje['nombre']}'
                
    return f'El personaje {busqueda} mas debll es(son) {min_nombre}, con una fuerza de {min}'


def contar_caracteristicas(lista: list, key: str)-> dict:
    # punto c
    lista_car = encontrar_caracteristicas(lista, key)
    dict_contador = {}
    
    for caracteristica in lista_car:
        contador = 0
        for personaje in lista:
            if personaje[key] == caracteristica:
                contador += 1
        dict_contador[caracteristica] = contador

    return dict_contador
    

def listar_por(lista: list, key: str)-> dict:
    # punto d
    lista_car = encontrar_caracteristicas(lista, key)
    dict_listar = {}

    for caracteristica in lista_car:
        lista_per = []
        for personaje in lista:
            if personaje[key] == caracteristica:
                lista_per.append(personaje['nombre'])
            dict_listar[caracteristica] = lista_per

    return dict_listar

def listar_nombre_peso(lista: list)-> list:
    # punto e 2
    lista_dicts = []
    promedio = promediar(lista, 'genero', 'M', 'fuerza')

    for personaje in lista:
        dict_1 = {}
        if int(personaje['fuerza']) > promedio:
            dict_1['Nombre'] = personaje['nombre']
            dict_1['Peso'] = personaje['peso']
            lista_dicts.append(dict_1)

    return lista_dicts

calcular_imc = lambda peso, altura : float(peso) / ((float(altura) / 100)**2)

def asignar_imc(lista: list)-> dict:

    diccionario_imcs = {}
    for personaje in lista:
        diccionario_imcs[personaje['nombre']] = calcular_imc(personaje['peso'], personaje['altura'])
        personaje['IMC'] = calcular_imc(personaje['peso'], personaje['altura'])

    return diccionario_imcs










# printear_datos(contar_caracteristicas(lista_is, 'inteligencia'))













    




