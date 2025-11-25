import pygame
import conway_logica as conway

TAM_CELDA = 10
FILAS = 60
COLUMNAS = 80
FPS = 10

def main():
    pygame.init()
    clock = pygame.time.Clock()
    M = conway.generar_nula(FILAS, COLUMNAS)
    ancho = TAM_CELDA * COLUMNAS
    alto = TAM_CELDA * FILAS
    ventana = pygame.display.set_mode((ancho, alto))
    pausa = True
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausa = not pausa
                if event.key == pygame.K_c:
                    M = conway.generar_nula(FILAS, COLUMNAS)
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                f = y // TAM_CELDA
                c = x // TAM_CELDA
                conway.cambiar_estado(M, f, c)

        ventana.fill((0, 0, 0))
        for f in range(FILAS):
            for c in range(COLUMNAS):
                if M[f][c] == 1:
                    color = (0, 255, 128)
                else:
                    color = (50, 50, 50)
                x = c * TAM_CELDA
                y = f * TAM_CELDA
                pygame.draw.rect(ventana, color, (x, y, TAM_CELDA, TAM_CELDA))
                pygame.draw.rect(ventana, (0,0,0), (x, y, TAM_CELDA, TAM_CELDA), 1)

        pygame.display.update()
        clock.tick(FPS)
        if not pausa:
            M = conway.transicion(M)
    pygame.quit()

if __name__ == "__main__":
    main()