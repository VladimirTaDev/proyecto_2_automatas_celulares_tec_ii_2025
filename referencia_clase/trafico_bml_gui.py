import pygame
import trafico_bml_logica as trafico

TAM = 5
FILAS = 100
COLUMNAS = 100
TICK = 1000

# variables para guardar
MATRIZ = trafico.generar_aleatoria(FILAS, COLUMNAS)

def main():
    """
    Función principal que invoca la lógica y renderiza la imagen
    Entradas y restricciones:
    - Ninguna.
    Salidas.
    - Simulación renderizada en pantalla. 
    """""

    global MATRIZ

    pygame.init()
    clock = pygame.time.Clock()
    alto = TAM * FILAS
    ancho = TAM * COLUMNAS
    ventana = pygame.display.set_mode((ancho, alto))

    # Bucle del juego
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        # dibujar tablero
        ventana.fill((0, 0, 0))
        for f in range(FILAS):
            for c in range(COLUMNAS):
                # dibujar carros rojos (1)
                if MATRIZ[f][c] == 1:
                    x = c * TAM
                    y = f * TAM
                    pygame.draw.rect(ventana, (255, 0, 0), (x, y, TAM, TAM))
                # dibujar carros azules (2)
                elif MATRIZ[f][c] == 2:
                    x = c * TAM
                    y = f * TAM
                    pygame.draw.rect(ventana, (0, 0, 255), (x, y, TAM, TAM))

        # mover carros
        MATRIZ = trafico.avanzar_rojos(MATRIZ)
        MATRIZ = trafico.avanzar_azules(MATRIZ)

        pygame.display.update()
        clock.tick(TICK)
    pygame.quit()

if __name__ == "__main__":
    main()