from funciones_modulo1 import validar_lista

def ordenar_alumnos(estudiantes_1):
    flag = False

    while flag == False:
        
        flag = True

        for i in range(len(estudiantes_1) - 1):
        
            if estudiantes_1[i]["apellido"] > estudiantes_1[i + 1]["apellido"]:
                    aux = estudiantes_1[i]["apellido"] 
                    estudiantes_1[i]["apellido"] = estudiantes_1[i + 1]["apellido"]
                    estudiantes_1[i + 1]["apellido"] = aux
                    flag = False

            elif estudiantes_1[i]["apellido"] == estudiantes_1[i + 1]["apellido"]:
                if estudiantes_1[i]["nombre"] > estudiantes_1[i + 1]["nombre"]:
                    aux = estudiantes_1[i]["nombre"]
                    estudiantes_1[i]["nombre"] = estudiantes_1[i + 1]["nombre"]
                    estudiantes_1[i + 1]["nombre"] = aux
                    flag = False

    for info in estudiantes_1:
        for i in info.items():
            print(f'{i[0].capitalize()}: {i[1]}')
        print("")

def promediar_notas(estudiantes_1):
    for info in estudiantes_1:
            notas = 0
            for nota in info['notas']:
                notas += nota
            notas = notas / len(info['notas'])
            print(f'El promedio de {info['nombre']} {info['apellido']} es {notas}')
            print('')

def listar_ingenieria(estudiantes_1):
    print('Lista de cursantes de Ingenieria en Informatica:')
    for info in estudiantes_1:
        for programa in info['programa'].values():
            if programa == "Ingenieria en Informatica":
                print(f'{info['nombre']} {info['apellido']}, con {info['edad']} años')

def promediar_edades(estudiantes_1):
    edades = 0
    for info in estudiantes_1:
        edades += info['edad']
    edades = edades / len(estudiantes_1)
    print(f'El promedio de edades es de {edades}')

def mostrar_mayor_promedio(estudiantes_1):
    max = 0
    for info in estudiantes_1:
        notas = 0
        for nota in info['notas']:
            notas += nota
        notas = notas / len(info['notas'])
        if notas > max:
            max = notas
            max_nombre_completo = f'{info['nombre']} {info['apellido']}'
        elif notas == max:
            max_nombre_completo = f'{max_nombre_completo} y {info['nombre']} {info['apellido']}'

    print(f'El estudiante con mayor promedio de nota es {max_nombre_completo}, con {max}')

def mostrar_club_informatica(estudiantes_1):
    print('Lista de cursantes en el Club de Informatica:')
    for info in estudiantes_1:
        for key in info.keys():
            if key == 'grupos':
                for fila in info['grupos']:
                    for grupo in fila.values():
                        notas = 0
                        if grupo == "Club de Informatica":
                            for nota in info['notas']:
                                notas += nota
                            notas = notas / len(info['notas'])
                            print(f'{info['nombre']} {info['apellido']}, con {notas} de promedio')

def mostrar_mas_jovenes(estudiantes_1):
    print('Lista de legajo, nombre, apellido y programas de los mas jovenes')
    for info in estudiantes_1:
        min = 100
        if info['edad']  < min:
            min = info['edad']
    for info in estudiantes_1:
        if info['edad'] == min:
            print(f"""
Legajo: {info['legajo']}
Nombre: {info['nombre']}
Apellido: {info['apellido']}
Programas: {info['programa']}
""")
            print('')