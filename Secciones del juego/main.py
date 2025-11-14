#Version 1
#main.py
#Librerias ocupadas
import pygame
import sys
import os
import dificultades  # Importar el módulo de la sección de dificultades

#Definimos con os las carpetas y rutas de los archivos
# Usar __file__ es más robusto cuando ejecutas el script desde el IDE
ruta_del_archivo = os.path.dirname(os.path.abspath(__file__))
# Ruta a la carpeta de imágenes

def encontrar_carpeta_imagenes(start_dir, name='Imagenes', max_up=3):
    d = start_dir
    for _ in range(max_up + 1):
        candidate = os.path.join(d, name)
        if os.path.isdir(candidate):
            return os.path.abspath(candidate)
        d = os.path.dirname(d)

# carpeta imagen
carpeta_imagenes = encontrar_carpeta_imagenes(ruta_del_archivo)

#Iniciamos pygame
pygame.init()
pygame.font.init()

#ponemos el primer tamaño de pantalla del juego
tamaño_ancho = 1280
tamaño_largo = 720
pantalla = (tamaño_ancho, tamaño_largo)

screen = pygame.display.set_mode(pantalla)

#Con esto ocultamos el mouse
pygame.mouse.set_visible(False)

#Colores
negro = (0,0,0)
blanco = (255,255,255)
verde = (0,255,0)

#Propiedades del mouse
jugador_tam = 20
jugador_color_hitbox = verde

#variable de la posicion del mouse (inicial)
mouse_x, mouse_y = pygame.mouse.get_pos()

#Creacion de elementos visuales!
pygame.display.set_caption("Que no te atrape") #titulo de la pagina!

# Helper para cargar imágenes con manejo de errores
def cargar_imagen(ruta, alpha=True):
    try:
        img = pygame.image.load(ruta)
        return img.convert_alpha() if alpha else img.convert()
    except Exception as e:
        print(f"No se pudo cargar {ruta}: {e}")
        # retornar una superficie de reemplazo para evitar que el juego se caiga
        surf = pygame.Surface((100, 100), pygame.SRCALPHA)
        surf.fill((255, 0, 255, 128))  # color visible para detectar fallos
        return surf

ruta_inicio_fondo = os.path.join(carpeta_imagenes, 'imagen_de_inicio.png')
inicio_fondo = cargar_imagen(ruta_inicio_fondo, alpha=True)
inicio_fondo_escalada = pygame.transform.scale(inicio_fondo, (tamaño_ancho, tamaño_largo))

#Boton
boton_ancho = 200
boton_largo = 60
ruta_boton_inicio = os.path.join(carpeta_imagenes, 'boton_para_comenzar.png')
boton_inicio = cargar_imagen(ruta_boton_inicio, alpha=True)
boton_inicio_escalada = pygame.transform.scale(boton_inicio, (boton_ancho, boton_largo))

rect_boton = boton_inicio_escalada.get_rect()
rect_boton.center = (tamaño_ancho // 2, tamaño_largo // 2)

#boton hover
ruta_boton_inicio_hover = os.path.join(carpeta_imagenes, 'boton_para_comenzar_hover.png')
boton_inicio_hover = cargar_imagen(ruta_boton_inicio_hover, alpha=True)
boton_inicio_escalada_hover = pygame.transform.scale(boton_inicio_hover, (boton_ancho, boton_largo))
rect_boton_hover = boton_inicio_escalada_hover.get_rect(center=rect_boton.center)

#la estructura para hacer un texto centrado
tipo_texto = pygame.font.Font(None, 50)
color_texto = (255,255,255)

"""
#La forma de preparar el texto para que sea ocupable
texto_surface = tipo_texto.render("HOOOOOOLA MUY BUENAS :D", True, color_texto) #la forma de escribir texto 
texto_rect = texto_surface.get_rect()
texto_rect.center = (tamaño_ancho // 2, tamaño_largo // 2)
"""

#para que no se cierre el juego
reloj = pygame.time.Clock()
FPS = 60
correr = True
while correr:
    #regulacion del tiempo
    reloj.tick(FPS)

    #manejo de eventos posibles!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correr = False #aqui estaria por el momento la salida del programa
    
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos

        if event.type == pygame.MOUSEBUTTONDOWN:
            # comprobar que sea click izquierdo (1)
            if event.button == 1 and rect_boton.collidepoint(event.pos):
                # llamamos a la seccion de dificultades.
                pygame.mouse.set_visible(True)  # mostrar cursor en la nueva sección
                dificultades.start(screen)     # llama a la función de la otra parte
                correr = False  # salir del bucle actual

    # Si no hay movimiento reciente, actualizar con la posición actual del mouse
    # (útil al iniciar)
    if not pygame.mouse.get_rel():  # si no hubo movimiento relativo, mantener última posición
        mouse_x, mouse_y = pygame.mouse.get_pos()

    jugador_rect = pygame.Rect(0, 0, jugador_tam, jugador_tam)
    jugador_rect.center = (mouse_x, mouse_y ) #aqui le damos las propiedades a jugador de nuestro mouse
    
    #parte de los elementos
    #RECOMENDACION: esto va en orden.
    """
    #de esta manera se puede poner texto en pantalla
    screen.blit(texto_surface, texto_rect)#De esta manera porfin logramos escribir algo en pantalla
    """
    screen.blit(inicio_fondo_escalada, (0,0)) #fondo de inicio
    screen.blit(boton_inicio_escalada, rect_boton) #boton en el centro

    if rect_boton.collidepoint(mouse_x, mouse_y):
        screen.blit(boton_inicio_escalada_hover, rect_boton_hover)
    else:
        screen.blit(boton_inicio_escalada, rect_boton)

    pygame.draw.rect(screen, jugador_color_hitbox, jugador_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()