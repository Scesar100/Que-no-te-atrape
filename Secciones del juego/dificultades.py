# ...existing code...
import pygame
import os
import sys

boton_ancho = 200
boton_largo = 60

# ajustamos el tamaño con una función que lee la carpeta, empareja normal/hover,
# escala manteniendo aspecto y devuelve una lista de botones listos para usar
def scale_image(carpeta, screen, ancho_max=boton_ancho, largo_max=boton_largo, start_y=None, spacing=12, orden=None):
    # Lista sólo png que contienen 'boton' en el nombre
    files = [f for f in os.listdir(carpeta) if f.lower().endswith('.png') and 'boton' in f.lower()]

    # Emparejar normal/hover bajo una clave base (ej: 'tutorial')
    pairs = {}
    for f in files:
        name = os.path.splitext(f)[0].lower()  # ejemplo: 'tutorial_boton' o 'tutorial_boton_hover'
        is_hover = name.endswith('_hover')
        base = name[:-6] if is_hover else name
        if base.endswith('_boton'):
            base = base[:-6]

        pairs.setdefault(base, {})['hover' if is_hover else 'normal'] = os.path.join(carpeta, f)

    # Orden de las claves
    keys = orden if orden is not None else sorted(pairs.keys())

    if start_y is None:
        start_y = int(screen.get_height() * 0.65)

    botones = []
    for i, key in enumerate(keys):
        p = pairs.get(key, {})
        normal_path = p.get('normal')
        hover_path = p.get('hover')

        # Cargar imágenes con fallback
        try:
            if normal_path:
                img = pygame.image.load(normal_path).convert_alpha()
            else:
                raise FileNotFoundError('normal image missing')
        except Exception as e:
            print(f"Error cargando {normal_path}: {e}")
            img = pygame.Surface((ancho_max, largo_max), pygame.SRCALPHA)
            img.fill((150, 150, 150))

        try:
            hover_img = pygame.image.load(hover_path).convert_alpha() if hover_path else None
        except Exception:
            hover_img = None

        # Si falta hover, crear una versión oscurecida
        if hover_img is None:
            hover_img = img.copy()
            overlay = pygame.Surface(hover_img.get_size(), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 60))
            hover_img.blit(overlay, (0, 0))

        # Escalar manteniendo aspecto (por defecto no agrandar)
        orig_w, orig_h = img.get_width(), img.get_height()
        scale = min(ancho_max / orig_w, largo_max / orig_h, 1.0)
        new_w, new_h = int(orig_w * scale), int(orig_h * scale)
        if (new_w, new_h) != (orig_w, orig_h):
            img = pygame.transform.smoothscale(img, (new_w, new_h))
            hover_img = pygame.transform.smoothscale(hover_img, (new_w, new_h))

        # Posición vertical en lista, centrado horizontalmente
        y = start_y + i * (new_h + spacing)
        rect = img.get_rect(center=(screen.get_width() // 2, y))

        botones.append({
            'name': key,
            'img': img,
            'hover_img': hover_img,
            'rect': rect,
            'action': None,
        })

    return botones


def start(screen):
    reloj = pygame.time.Clock()
    FPS = 60
    running = True

    tipo_texto = pygame.font.Font(None, int(screen.get_height() * 0.03))  # Tamaño de fuente relativo a la altura de la pantalla
    # Divide el texto en líneas y cámbialas si quieres
    lines = [
        "Bienvenido a la sección de dificultades :D",
        "Recomiendo que empieces el tutorial con RICK,",
        "él está esperando para darte la tutoría."
    ]
    color = (255, 255, 255)
    line_height = tipo_texto.get_linesize()
    start_y = int(screen.get_height() * 0.10)  # 10% desde arriba

    # Cargar automáticamente todos los botones desde la carpeta Imagenes
    base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Imagenes")
    buttons = scale_image(base_path, screen, ancho_max=boton_ancho, largo_max=boton_largo,
                          start_y=int(screen.get_height() * 0.65), spacing=12, orden=None)

    # Asignar acciones (callbacks) por nombre; ajusta aquí según tus funciones reales
    for b in buttons:
        if b['name'] == 'tutorial':
            b['action'] = lambda n=b['name']: print("Botón tutorial clickeado")
        else:
            b['action'] = lambda n=b['name']: print("clic en", n)

    while running:
        reloj.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for b in buttons:
                    if b['rect'].collidepoint(event.pos):
                        if b['action']:
                            b['action']()

        screen.fill((50, 50, 50))

        # Dibujar líneas centradas horizontalmente, empezando en start_y
        for i, text in enumerate(lines):
            surf = tipo_texto.render(text, True, color)
            rect = surf.get_rect(centerx=screen.get_width() // 2)
            rect.top = start_y + i * line_height
            screen.blit(surf, rect)

        # Dibujar los botones (normal / hover)
        mouse_pos = pygame.mouse.get_pos()
        for b in buttons:
            is_hover = b['rect'].collidepoint(mouse_pos)
            if is_hover:
                screen.blit(b['hover_img'], b['rect'])
            else:
                screen.blit(b['img'], b['rect'])

        pygame.display.flip()
