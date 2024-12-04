import pygame as ga

# inicializo los modulos
ga.init()
ga.mixer.init()

# cargo y configuro musica
ga.mixer.music.load('cancion_pokemon.mp3')
ga.mixer.music.set_volume(0.05)
ga.mixer.music.play(-1)

# inicializo valores
running = True
fullscreen = True
puntos_partida = 0
contador_tiempo = 10
entrada_titulo_texto = 'Ingrese su nombre'
slots = []
texto_nombre = ''
hecho = False

# creo colores
color_letras = (255, 255, 255)
color_elementos = (0, 0, 50)
color_fondo = (0, 0, 70)


screen = ga.display.set_mode([0, 0], ga.FULLSCREEN)
ga.display.set_caption('Pokemon Crush')
ventana = 'menu_principal'

# configuro fuentes
fuente_grande = ga.font.SysFont('Arial' , 50)
fuente_chica = ga.font.SysFont('Arial' , 30)

# creo textos
boton_jugar = fuente_grande.render('Jugar', True, color_letras, color_elementos)
boton_tabla = fuente_grande.render('Tabla', True, color_letras, color_elementos)
boton_cerrar = fuente_grande.render('Cerrar', True, color_letras, color_elementos)
boton_salir = fuente_chica.render('Salir', True, color_letras, color_elementos)
tablero_titulo = fuente_grande.render('Tablero de juego', True, color_letras, color_elementos)
tabla_titulo = fuente_grande.render('Tablero', True, color_letras, color_elementos)
boton_salir_juego = fuente_grande.render('Salir', True, color_letras, color_elementos)
puntos_texto = fuente_chica.render('Puntos', True, color_letras, color_elementos)
contador_texto = fuente_chica.render('Tiempo', True, color_letras, color_elementos)

# creo rectangulos
rect_jugar = boton_jugar.get_rect(center = (670, 360))
rect_boton_tabla = boton_tabla.get_rect(center = (670, 450))
rect_cerrar = boton_cerrar.get_rect(center = (670, 540))
rect_salir = boton_salir.get_rect(center = (100, 100))
rect_salir_juego = boton_salir_juego.get_rect(center = (1125, 600))

# cargo fotos
logo = ga.image.load('logo.png')
bulbasaur = ga.image.load('bulbasaur.png')
bulbasaur = ga.transform.smoothscale(bulbasaur, (100, 100))
charmander = ga.image.load('charmander.png')
charmander = ga.transform.smoothscale(charmander, (100, 100))
squirtle = ga.image.load('squirtle.png')
squirtle = ga.transform.smoothscale(squirtle, (100, 100))

# creo el evento para la cuenta regresiva
CUENTA_REGRESIVA = ga.USEREVENT + 1

