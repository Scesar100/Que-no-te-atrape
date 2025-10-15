#Version 0.1
#Librerias ocupadas
import pygame
import numpy
import sys


#Iniciamos pygame
pygame.init()

#ponemos el primer tamaño de pantalla del juego
tamaño_ancho = 720
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


#la estructura para hacer un texto centrado
tipo_texto = pygame.font.Font(None, 50) #el tipo de texto que se ocupara como su color
color_texto = (255,255,255)

texto_surface = tipo_texto.render("HOOOOOOLA MUY BUENAS :D", True, color_texto) #la forma de escribir texto 
texto_rect = texto_surface.get_rect()
texto_rect.center = (tamaño_ancho // 2, tamaño_largo // 2)


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
    screen.fill((negro)) #color de fondo //oscuro
    screen.blit(texto_surface, texto_rect)#De esta manera porfin logramos escribir algo en pantalla
    pygame.draw.rect(screen, jugador_color_hitbox, jugador_rect) #le ponemos la hitbox al mouse
    pygame.display.flip() #actualiza la pantalla!



    

    


pygame.quit()
sys.exit()