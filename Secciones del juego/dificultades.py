#dificultades.py
import pygame
import os
import sys
import tutorial

#ruta de las imagenes
carpeta_imagenes = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Imagenes'))

#verificamos la ruta de las imagenes
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




#letras de bienvenida
lines = [
    "Bienvenido a 'No te atrape!'",
    "Te recomiendo empezar donde el tutorial!!!",
    "donde RICK esta esperandote bastante ansioso...",
    "Para darte la seccion de tutorial",
    "Para ir a un boton, solo mueve el mouse sobre la dificultad que quieras y debes darle click",
    "Mucha suerte y diviertete en 'No te atrape'!"
]


#botones de dificultades

#tamaño de los botones
boton_ancho = 200
boton_largo = 60



def start(screen):
    # 1. SETUP LOCAL (Antes del while)
    FPS = 60
    reloj = pygame.time.Clock()
    correr = True
    
    #Tipo de letra
    tipo_texto = pygame.font.SysFont('Arial', 30)
    color_texto = (255, 255, 255)
    line_height = tipo_texto.get_linesize()

    # Obtener dimensiones dinámicas de la pantalla que main.py nos pasó
    ancho_pantalla = screen.get_width()
    alto_pantalla = screen.get_height()

    # Cálculo de la posición inicial de elementos y mouse
    letra_ubicacion = alto_pantalla * 0.1
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # 2. CALCULAR POSICIÓN DE BOTONES (Antes del while)
    # Usa las variables dinámicas ancho_pantalla y alto_pantalla

    #boton tutorial
    ruta_boton_tutorial = os.path.join(carpeta_imagenes, 'tutorial_boton.png')
    boton_tutorial = cargar_imagen(ruta_boton_tutorial, alpha=True)
    boton_tutorial_escalada = pygame.transform.scale(boton_tutorial, (boton_ancho, boton_largo))


    #boton tutorial hover
    ruta_boton_tutorial_hover = os.path.join(carpeta_imagenes, 'tutorial_boton_hover.png')
    boton_tutorial_hover = cargar_imagen(ruta_boton_tutorial_hover, alpha=True)
    boton_tutorial_hover_escalada = pygame.transform.scale(boton_tutorial_hover, (boton_ancho, boton_largo))
    
    # Botón tutorial centrado
    rect_boton = boton_tutorial_escalada.get_rect()
    rect_boton.center = (ancho_pantalla // 2, alto_pantalla // 2 + 100) 
    
    # Botón tutorial hover centrado
    rect_boton_hover = boton_tutorial_hover_escalada.get_rect(center=rect_boton.center)

    # 3. BUCLE DE EJECUCIÓN (Todo lo que sigue debe ir indentado)
    while correr:
        reloj.tick(FPS)

        # MANEJO DE EVENTOS (AHORA DENTRO DEL WHILE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    correr = False # Sale del bucle start()
            
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
            # comprobar que sea click izquierdo (1)
                if event.button == 1 and rect_boton.collidepoint(event.pos):
                # llamamos a la seccion de dificultades.
                    pygame.mouse.set_visible(True)  # mostrar cursor en la nueva sección
                    tutorial.start(screen)     # llama a la función de la otra parte
                    correr = False  # salir del bucle actual

        # DIBUJO DE PANTALLA (AHORA DENTRO DEL WHILE)
        screen.fill((50, 50, 50)) # limpiador de pantalla
    
        # Dibujar líneas centradas
        for i, text in enumerate(lines):
            surf = tipo_texto.render(text, True, color_texto)
            # screen.get_width() está bien aquí
            rect = surf.get_rect(centerx=screen.get_width() // 2) 
            rect.top = letra_ubicacion + i * line_height
            screen.blit(surf, rect)
            
        # Dibujar el botón de tutorial
        if rect_boton.collidepoint(mouse_x, mouse_y):
            screen.blit(boton_tutorial_hover_escalada, rect_boton_hover)
        else:
            screen.blit(boton_tutorial_escalada, rect_boton)

        # ACTUALIZAR (AHORA DENTRO DEL WHILE)
        pygame.display.flip()
        
    return # La función termina, el control vuelve a main.py