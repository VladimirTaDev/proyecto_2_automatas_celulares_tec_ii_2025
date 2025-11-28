import pygame
import hormiga_de_langton_logica as hormiga

TAM = 5
FILAS = 100
COLUMNAS = 100
TICK = 1000

# variables para guardar
HORMIGA = {"pos" : [FILAS//2, COLUMNAS//2],
           "dir" : 2}
MATRIZ = hormiga.generar_nula(FILAS, COLUMNAS)

def main():
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
                if MATRIZ[f][c] == 1:
                    x = c * TAM
                    y = f * TAM
                    pygame.draw.rect(ventana, (0, 255, 128), (x, y, TAM, TAM))

        # dibujar hormiga
        y = HORMIGA["pos"][0] * TAM # fila
        x = HORMIGA["pos"][1] * TAM # columna
        pygame.draw.rect(ventana, (255, 0, 0), (x, y, TAM, TAM))

        # gira la hormiga
        HORMIGA["dir"] = hormiga.girar_hormiga(MATRIZ[HORMIGA["pos"][0]][HORMIGA["pos"][1]], HORMIGA["dir"])

        # actualizar celda
        MATRIZ[HORMIGA["pos"][0]][HORMIGA["pos"][1]] = hormiga.siguiente(MATRIZ[HORMIGA["pos"][0]][HORMIGA["pos"][1]])

        # avanzar la hormiga
        HORMIGA["pos"][0], HORMIGA["pos"][1] = hormiga.avanzar_hormiga(HORMIGA["pos"][0], HORMIGA["pos"][1], HORMIGA["dir"])

        pygame.display.update()
        clock.tick(TICK)
    pygame.quit()

if __name__ == "__main__":
    main()