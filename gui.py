import pygame

import trafico_bml_logica as trafico
import hormiga_de_langton_logica as hormiga

# parámetros para guardar
PARAM_AUTOMATA = {"TAM": 5,
                  "FILAS": 100,
                  "COLUMNAS": 100,
                  "TICK": 1000,
                  "MATRIZ": []}

def main(automata = 1):
    """
    Función principal que invoca la lógica y renderiza la imagen
    Entradas y restricciones:
    - Ninguna.
    Salidas.
    - Simulación renderizada en pantalla. 
    """""

    global PARAM_AUTOMATA
    colores = [[(255, 0, 0), 1], [(0, 0, 255), 2]]


    pygame.init()
    clock = pygame.time.Clock()
    alto = PARAM_AUTOMATA["TAM"] * PARAM_AUTOMATA["FILAS"]
    ancho = PARAM_AUTOMATA["TAM"] * PARAM_AUTOMATA["COLUMNAS"]
    ventana = pygame.display.set_mode((ancho, alto))

    # inicialización de variables
    match automata:
        case 1:  # trafico
            PARAM_AUTOMATA["MATRIZ"] = trafico.generar_aleatoria(PARAM_AUTOMATA["FILAS"],
                                                                 PARAM_AUTOMATA["COLUMNAS"])
            colores = trafico.COLORES
        case 2:  # hormiga
            PARAM_AUTOMATA["MATRIZ"] = hormiga.generar_nula(PARAM_AUTOMATA["FILAS"],
                                                            PARAM_AUTOMATA["COLUMNAS"])
            PARAM_AUTOMATA.update({"POS" : [PARAM_AUTOMATA["FILAS"]//2, PARAM_AUTOMATA["COLUMNAS"]//2],
                                   "DIR" : 2})
            colores = hormiga.COLORES

    # Bucle del juego
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        # dibujar tablero
        ventana.fill((0, 0, 0))

        # dibuja las celdas de colores, lista de listas [color, valor_celda]
        for color in colores:
            for f in range(PARAM_AUTOMATA["FILAS"]):
                for c in range(PARAM_AUTOMATA["COLUMNAS"]):
                    if PARAM_AUTOMATA["MATRIZ"][f][c] == color[1]:
                        x = c * PARAM_AUTOMATA["TAM"]
                        y = f * PARAM_AUTOMATA["TAM"]
                        pygame.draw.rect(ventana, color[0], (x, y, PARAM_AUTOMATA["TAM"], PARAM_AUTOMATA["TAM"]))
                    else:
                        continue

        # ejecutar autómata
        match automata:
            case 1: #trafico
                PARAM_AUTOMATA["MATRIZ"] = trafico.main(PARAM_AUTOMATA["MATRIZ"])
            case 2: #hormiga
                PARAM_AUTOMATA["MATRIZ"] = hormiga.main(PARAM_AUTOMATA["MATRIZ"], PARAM_AUTOMATA["POS"], PARAM_AUTOMATA["DIR"], PARAM_AUTOMATA["FILAS"], PARAM_AUTOMATA["COLUMNAS"])
                y = PARAM_AUTOMATA["POS"][0] * PARAM_AUTOMATA["TAM"]  # fila
                x = PARAM_AUTOMATA["POS"][1] * PARAM_AUTOMATA["TAM"]  # columna
                pygame.draw.rect(ventana, (255, 0, 0), (x, y, PARAM_AUTOMATA["TAM"], PARAM_AUTOMATA["TAM"]))

        pygame.display.update()
        clock.tick(PARAM_AUTOMATA["TICK"])
    pygame.quit()

if __name__ == "__main__":
    main(1)