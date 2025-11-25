import pygame
import conway_logica as conway

tam = 5
filas = 100
columnas = 100
tick = 10

def main():
    pygame.init()
    clock = pygame.time.Clock()
    M = conway.generar_aleatoria(filas, columnas)
    ancho = tam * columnas
    alto = tam * filas
    ventana = pygame.display.set_mode((ancho, alto))
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        ventana.fill((0, 0, 0))
        for f in range(filas):
            for c in range(columnas):
                if M[f][c] == 1:
                    x = c * tam
                    y = f * tam
                    pygame.draw.rect(ventana, (0, 255, 128), (x, y, tam, tam))

        pygame.display.update()
        clock.tick(tick)
        M = conway.transicion(M)
    pygame.quit()

if __name__ == "__main__":
    main()