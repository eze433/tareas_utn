import pygame as ga
from inicializaciones import *
from funciones import *

while running:
    screen.fill(color_fondo)

    if ventana == 'menu_principal':
        screen.blit(logo, (433, 100))
        screen.blit(boton_tabla, rect_boton_tabla)
        screen.blit(boton_jugar, rect_jugar)
        screen.blit(boton_cerrar, rect_cerrar)

    elif ventana == 'tabla_puntos':
        if hecho == False: #ocurre solo una vez
            # encuentra los nombres y los puntos y los ordena
            lista_nombres = []
            lista_puntos = []
            with open('puntos.csv', 'r') as archivo:
                for linea in archivo:
                    fin = linea.find(':')
                    lista_nombres.append(linea[:fin])
                    lista_puntos.append(linea[fin + 1:])

            listas = ordenar_listas(lista_nombres, lista_puntos, 'asc')
            lista_nombres = listas[0]
            lista_puntos = listas[1]

            hecho = True

        ga.draw.rect(screen, color_elementos, (533, 200, 330, 500))
        suma = 210
        posicion = 0

        # lista los primeros 10 nombres ordenados por nombre

        for i in range(len(lista_puntos)):
            if posicion == 10:
                break
            posicion += 1
            string = f'{posicion}. {lista_nombres[i]}'
            tabla = fuente_chica.render(string, True, color_letras, color_elementos)
            tabla_puntos = fuente_chica.render(lista_puntos[i].strip(), True, color_letras, color_elementos)
            screen.blit(tabla, (540, suma))
            screen.blit(tabla_puntos, (800, suma))
            
            suma += 50

        screen.blit(boton_salir, rect_salir)
        screen.blit(tabla_titulo, (533, 100))

    elif ventana == 'juego_principal':
        ga.draw.rect(screen, color_elementos, (100, 150, 800, 550))
        ga.draw.rect(screen, color_elementos, (975, 250, 300, 300))

        if hecho == False: # se hace solo una vez
            lista = generar_tabla(slots)
            ga.time.set_timer(CUENTA_REGRESIVA, 1000)
        hecho = True

        for slot in slots: # recorre y muestra todos los slots
            screen.blit(slot['pokemon'], slot['rect'])
        
        # creo la info
        texto_contador_tiempo = fuente_grande.render(str(contador_tiempo), True, color_letras, color_elementos)
        contador_puntos_texto = fuente_grande.render(str(puntos_partida), True, color_letras, color_elementos)
        
        # muestro los elementos
        screen.blit(tablero_titulo, (200, 90))
        screen.blit(boton_salir_juego, rect_salir_juego)

        screen.blit(puntos_texto, (1090, 275))
        screen.blit(contador_puntos_texto, (1115, 325))
        screen.blit(contador_texto, (1090, 400))
        screen.blit(texto_contador_tiempo, (1115, 450))

    elif ventana == 'entrar_nombre':
        ga.draw.rect(screen, color_elementos, (433, 200, 550, 200))

        # creo la info
        entrada_titulo = fuente_chica.render(entrada_titulo_texto, True, color_letras, color_elementos)
        entrada_texto = fuente_grande.render(texto_nombre, True, color_letras, color_elementos)

        # muestro la info
        screen.blit(entrada_titulo, (433, 200))
        screen.blit(entrada_texto, (433, 300))

    # manejo eventos
    for event in ga.event.get():

        if event.type == ga.MOUSEBUTTONDOWN:
            # maneja todas las colisiones de mouse con rects, mueve a traves de los menues
            if event.button == 1:
                if ventana == 'menu_principal':
                    # checkea clicks a las opciones
                    if rect_jugar.collidepoint(event.pos):
                        ventana = 'juego_principal'

                    elif rect_boton_tabla.collidepoint(event.pos):
                        ventana = 'tabla_puntos'

                    elif rect_cerrar.collidepoint(event.pos):
                        running = False

                elif ventana == 'tabla_puntos':

                    if rect_salir.collidepoint(event.pos):
                        ventana = 'menu_principal'
                        hecho = False

                elif ventana == 'juego_principal':
                    # chequea las posibles colisiones con todos los slots
                    for i in range(len(slots)):
                        if slots[i]['rect'].collidepoint(event.pos):
                            verificacion = verificar_eleccion(slots[i]['indice_x'], slots[i]['indice_y'], lista)
                            # vuelve a generar una tabla
                            slots = []
                            lista = generar_tabla(slots)
                            # suma puntos o resta
                            if verificacion == True:
                                puntos_partida += 10
                            else:
                                contador_tiempo -= 1
                                puntos_partida -= 1

                    
                    if rect_salir_juego.collidepoint(event.pos):
                        ventana = 'entrar_nombre'
                        # resetea todos los valores
                        puntos_partida = 0
                        slots = []
                        hecho = False
                        contador_tiempo = 10

        if event.type == CUENTA_REGRESIVA and ventana == 'juego_principal':
            # resta el tiempo cuando pasa 1 segundo en la ventana de juego
            if contador_tiempo > 0:
                contador_tiempo -= 1
            

            else:
                ventana = 'entrar_nombre'
                # pausa el evento y resetea los valores
                ga.time.set_timer(CUENTA_REGRESIVA, 0)
                slots = []
                hecho = False
                contador_tiempo = 10

        if ventana == 'entrar_nombre':
            if event.type == ga.KEYDOWN:
                if event.key == ga.K_RETURN:
                    # verifica nombre valido
                    if (texto_nombre.isalnum() == False or len(texto_nombre) > 12) or len(texto_nombre) < 3:
                        texto_nombre = ''
                        entrada_titulo_texto = 'Ingrese un nombre válido(>3, <12, alfanumerico)'

                    else:
                        ventana = 'menu_principal'
                        escribir_puntos(texto_nombre, puntos_partida)
                        texto_nombre = ''
                        puntos_partida = 0
                        hecho = False

                elif event.key == ga.K_BACKSPACE:
                    # borra
                    texto_nombre = texto_nombre[:-1]

                else:
                    # agrega
                    texto_nombre += event.unicode

        if ventana != 'entrar_nombre': 
            # k para alternar entre pantalla completa
            if event.type == ga.KEYDOWN:
                if event.key == ga.K_f:
                    fullscreen = not fullscreen
                    if fullscreen == True:
                        screen = ga.display.set_mode((0, 0), ga.FULLSCREEN)
                    else:
                        screen = ga.display.set_mode((600, 600))
        
        if event.type == ga.QUIT:
            running = False

    # actualizo la pantalla
    ga.display.flip()


# resolucion = 1366x768