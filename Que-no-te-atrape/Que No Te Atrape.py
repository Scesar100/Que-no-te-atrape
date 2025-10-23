#Version 0.2
#Librerias ocupadas
import pygame
import numpy
import sys


#Iniciamos pygame
pygame.init()

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

#variable de la posicion del mouse
mouse_x = tamaño_ancho // 2
mouse_y = tamaño_largo // 2
#Creacion de elementos visuales!

pygame.display.set_caption("Bienvenido :D") #titulo de la pagina!
inicio_fondo = pygame.image.load('Imagenes/imagen_de_inicio.png').convert_alpha() #Aqui estaria la imagen del inicio
inicio_fondo_escalada = pygame.transform.scale(inicio_fondo, (tamaño_ancho, tamaño_largo)) #asi la imagen se calibra al tamaño en 'px' ocupados

#Boton
boton_ancho = 200
boton_largo = 60
boton_inicio = pygame.image.load('Imagenes/boton_para_comenzar.png').convert()
boton_inicio_escalada = pygame.transform.scale(boton_inicio, (boton_ancho, boton_largo))

rect_boton = boton_inicio_escalada.get_rect() #le damos la hitbox al boton para que pueda recibir clicks
rect_boton.center = (tamaño_ancho // 2, tamaño_largo // 2) #con esto conseguimos hacer que el boton este centrado

#la estructura para hacer un texto centrado
tipo_texto = pygame.font.Font(None, 50) #el tipo de texto que se ocupara como su color
color_texto = (255,255,255)

"""
#La forma de preparar el texto para que sea ocupable
texto_surface = tipo_texto.render("HOOOOOOLA MUY BUENAS :D", True, color_texto) #la forma de escribir texto 
texto_rect = texto_surface.get_rect()
texto_rect.center = (tamaño_ancho // 2, tamaño_largo // 2)
"""

#para que no se cierre el juego
reloj = pygame.time.Clock() #creamos un reloj
FPS = 60 #la velocidad que va a ir el juego
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

    
    #la parte logica del programa
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

    pygame.draw.rect(screen, jugador_color_hitbox, jugador_rect) #le ponemos la hitbox al mouse
    pygame.display.flip() #actualiza la pantalla!



    

    


pygame.quit()
sys.exit()