def chequeo_import(importado: bool)-> bool:
    if importado == False:
        print('ERROR, debe importar las listas para seleccionar esta opción')
        return False
    else:
        return True

def mexico_usuarios(country: list, nombres: list, telefonos: list, mails: list, 
                    address: list, postalZip: list, region: list, edades: list):
    # 2
    print('Los datos de los usuarios mexicanos son: ')
    for i in range(len(country)):
        if country[i] == 'Mexico':
            print(f'Nombre: {nombres[i]} \n' 
                  f'Telefono: {telefonos[i]} \n' 
                  f'Mail: {mails[i]} \n'
                  f'Direccion: {address[i]} \n'
                  f'ZIP: {postalZip[i]} \n'
                  f'Region: {region[i]} \n'
                  f'Pais: {country[i]} \n' 
                  f'Edad: {edades[i]} \n')
            

def brasil_usuarios(country: list, nombres: list, telefonos: list, mails: list, ):
    # 3
    print('Los nombres, telefonos y mails de los usuarios brasileros son: ')
    for i in range(len(country)):
        if country[i] == 'Brazil':
            print(f'Nombre: {nombres[i]} \n' 
                  f'Telefono: {telefonos[i]} \n' 
                  f'Mail: {mails[i]} \n')
            

def menores(country: list, nombres: list, telefonos: list, mails: list, 
            address: list, postalZip: list, region: list, edades: list)-> str:
    # 4
    min = edades[0]
    lista = []

    for i in range(len(edades)):
        if edades[i] <= min:
            min = edades[i]

    for i in range(len(edades)):
        if edades[i] == min:
            lista.append(i)

    print('Los datos de los menores de edad en la lista son:')
    for i in lista:
        print(f'Nombre: {nombres[i]} \n' 
                f'Telefono: {telefonos[i]} \n' 
                f'Mail: {mails[i]} \n'
                f'Direccion: {address[i]} \n'
                f'ZIP: {postalZip[i]} \n'
                f'Region: {region[i]} \n'
                f'Pais: {country[i]} \n' 
                f'Edad: {edades[i]} \n')

def promedio_edad(edades)-> float:
    # 5
    acumulador = 0
    for i in edades:
        acumulador += i
    return acumulador / len(edades)

def brasil_mayor(country: list, nombres: list, telefonos: list, mails: list, 
            address: list, postalZip: list, region: list, edades: list):
    # 6
        
    max = 0
    lista = []

    for i in range(len(edades)):
        if country[i] == 'Brazil':
            if edades[i] >= max:
                max = edades[i]

    for i in range(len(edades)):
        if edades[i] == max:
            lista.append(i)

    print('Datos del(os) brasilero(s) de mayor edad')
    for i in lista:
        print(f'Nombre: {nombres[i]} \n' 
                f'Telefono: {telefonos[i]} \n' 
                f'Mail: {mails[i]} \n'
                f'Direccion: {address[i]} \n'
                f'ZIP: {postalZip[i]} \n'
                f'Region: {region[i]} \n'
                f'Pais: {country[i]} \n' 
                f'Edad: {edades[i]} \n')
        
def mx_bz_8000(country: list, nombres: list, telefonos: list, mails: list, 
            address: list, postalZip: list, region: list, edades: list):
    # 7
    lista = []
    for i in range(len(country)):
        if country[i] == 'Brazil' or country[i] == 'Mexico':
            if postalZip[i] > 8000:
                lista.append(i)
                
    print('Datos de los Brasileros y Mexicanos con ZIP mayor a 8000: ')

    for i in lista:
        print(f'Nombre: {nombres[i]} \n' 
                f'Telefono: {telefonos[i]} \n' 
                f'Mail: {mails[i]} \n'
                f'Direccion: {address[i]} \n'
                f'ZIP: {postalZip[i]} \n'
                f'Region: {region[i]} \n'
                f'Pais: {country[i]} \n' 
                f'Edad: {edades[i]} \n')
        
def italianos_40(country: list, nombres: list, telefonos: list, mails: list, edades: list):
    # 8

    lista = []
    for i in range(len(country)):
        if country[i] == 'Italy' and edades[i] >= 40:
            lista.append(i)

    print('Nombre, mail y telefono de los italianos mayores a 40: ')

    for i in lista:
        print(f'Nombre: {nombres[i]} \n' 
                f'Telefono: {telefonos[i]} \n' 
                f'Mail: {mails[i]} \n'
                f'Edad: {edades[i]}'
                f'Pais: {country[i]}')
        
