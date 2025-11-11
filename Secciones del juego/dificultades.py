# ...existing code...
import pygame
import sys

def start(screen):
    reloj = pygame.time.Clock()
    FPS = 60
    running = True

    tipo_texto = pygame.font.Font(None, 40)
    # Divide el texto en líneas y cámbialas si quieres
    lines = [
        "Bienvenido a la sección de dificultades :D",
        "Recomiendo que empieces el tutorial con RICK,",
        "él está esperando para darte la tutoría."
    ]
    color = (255, 255, 255)
    line_height = tipo_texto.get_linesize()
    start_y = int(screen.get_height() * 0.10)  # 10% desde arriba

    while running:
        reloj.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((50, 50, 50))

        # Dibujar líneas centradas horizontalmente, empezando en start_y
        for i, text in enumerate(lines):
            surf = tipo_texto.render(text, True, color)
            rect = surf.get_rect(centerx=screen.get_width() // 2)
            rect.top = start_y + i * line_height
            screen.blit(surf, rect)

        pygame.display.flip()
