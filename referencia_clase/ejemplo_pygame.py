# Un programa de pygame va a tener varias partes
# 1. Inicialización. Inicia la biblioteca, se crea una ventana.
# 2. Ciclo de animación
#    a. Chequeo de eventos
#       - se cierra aplicación
#       - clic del mouse
#       - se presiona una tecla
#    b. Cambiar el estado de nuestros elementos
#       de acuerdo a los eventos que ocurrieron
#    c. Actualizar la imagen en pantalla
# 3. Finalización de la biblioteca.

import pygame

def main():
    pygame.init()
    window = pygame.display.set_mode((600, 400))  # tupla con ancho, alto
    clock = pygame.time.Clock()
    loop = True
    x, y = 300, 200
    while loop:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_SPACE]:
                    x, y = 300, 200

        if keys[pygame.K_w]:
            y -= 1
        if keys[pygame.K_a]:
            x -= 1
        if keys[pygame.K_s]:
            y += 1
        if keys[pygame.K_d]:
            x += 1

        window.fill((244, 162, 36))  # tupla con colo r, g, b
        color = (128, 0, 225)
        rect = (x, y, 20, 20)  # posición x, posicion y, ancho, alto
        pygame.draw.rect(window, color, rect)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()