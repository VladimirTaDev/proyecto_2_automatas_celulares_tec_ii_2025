import pygame
import pickle

import trafico_bml_logica as trafico
import hormiga_de_langton_logica as hormiga

COLORES = [[(255, 0, 0), 1], [(0, 0, 255), 2]]
# parámetros para guardar
PARAM_AUTOMATA = {"TAM": 5,
                  "FILAS": 100,
                  "COLUMNAS": 100,
                  "TICK": 1000,
                  "MATRIZ": []}

def inicializar_automata(automata, aleatorio = False):
    """
    Inicializa el autómata seleccionado.
    Entradas y restricciones:
    - automata (int): tipo de autómata. 1 = tráfico, 2 = hormiga.
    - aleatorio (bool): si se debe generar una matriz aleatoria. Por defecto False.
    Salida:
    - Ninguna. Actualiza PARAM_AUTOMATA y COLORES globales.
    """
    global COLORES
    match automata:
        case 1:  # trafico
            PARAM_AUTOMATA["MATRIZ"] = trafico.generar_aleatoria(PARAM_AUTOMATA["FILAS"],
                                                                 PARAM_AUTOMATA["COLUMNAS"])
            COLORES = trafico.COLORES
            PARAM_AUTOMATA["CONFIG"] = "trafico.pkl"
        case 2:  # hormiga
            if aleatorio:
                PARAM_AUTOMATA["MATRIZ"] = hormiga.generar_aleatoria(PARAM_AUTOMATA["FILAS"],
                                                                PARAM_AUTOMATA["COLUMNAS"])
            else:
                PARAM_AUTOMATA["MATRIZ"] = hormiga.generar_nula(PARAM_AUTOMATA["FILAS"],
                                                            PARAM_AUTOMATA["COLUMNAS"])
            PARAM_AUTOMATA.update({"POS": [PARAM_AUTOMATA["FILAS"] // 2, PARAM_AUTOMATA["COLUMNAS"] // 2],
                                   "DIR": 2})
            COLORES = hormiga.COLORES
            PARAM_AUTOMATA["CONFIG"] = "hormiga.pkl"

def main(automata = 1):
    """
    Función principal que invoca la lógica y renderiza la imagen.
    Entradas y restricciones:
    - automata (int): tipo de autómata a ejecutar. 1 = tráfico, 2 = hormiga...
    Salida:
    - Simulación renderizada en pantalla.
    """

    global PARAM_AUTOMATA
    global COLORES

    pygame.init()
    clock = pygame.time.Clock()
    alto = PARAM_AUTOMATA["TAM"] * PARAM_AUTOMATA["FILAS"]
    ancho = PARAM_AUTOMATA["TAM"] * PARAM_AUTOMATA["COLUMNAS"]
    ventana = pygame.display.set_mode((ancho, alto))

    # inicializar
    inicializar_automata(automata)

    # Bucle del juego
    loop = True
    pausa = False
    mouse_pos = None
    while loop:
        # eventos de teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausa = not pausa
                elif event.key == pygame.K_r:
                    inicializar_automata(automata, True)
                elif event.key == pygame.K_b:
                    inicializar_automata(automata)
                elif event.key == pygame.K_g:
                    # guardar autómata
                    with open(f"config/{PARAM_AUTOMATA['CONFIG']}", "wb") as salida:
                        pickle.dump(PARAM_AUTOMATA, salida)
                elif event.key == pygame.K_c:
                    # cargar autómata
                    try:
                        with open(f"config/{PARAM_AUTOMATA['CONFIG']}", "rb") as entrada:
                            PARAM_AUTOMATA = pickle.load(entrada)
                    except FileNotFoundError:
                        pass  # no hacer nada


            elif event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                f = y // PARAM_AUTOMATA["TAM"]
                c = x // PARAM_AUTOMATA["TAM"]
                mouse_pos = (f, c)


        if pausa:
            continue
        # dibujar tablero
        ventana.fill((0, 0, 0))

        # dibuja las celdas de colores, lista de listas [color, valor_celda]
        for color in COLORES:
            for f in range(PARAM_AUTOMATA["FILAS"]):
                for c in range(PARAM_AUTOMATA["COLUMNAS"]):
                    if PARAM_AUTOMATA["MATRIZ"][f][c] == color[1]:
                        x = c * PARAM_AUTOMATA["TAM"]
                        y = f * PARAM_AUTOMATA["TAM"]
                        pygame.draw.rect(ventana, color[0],
                                         (x, y, PARAM_AUTOMATA["TAM"],
                                          PARAM_AUTOMATA["TAM"]))
                    else:
                        continue

        # ejecutar autómata
        match automata:
            case 1: # trafico
                # ejecutar lógica
                PARAM_AUTOMATA["MATRIZ"] = trafico.main(PARAM_AUTOMATA["MATRIZ"], mouse_pos)
            case 2: # hormiga
                # ejecutar lógica
                PARAM_AUTOMATA["MATRIZ"], PARAM_AUTOMATA["DIR"] = hormiga.main(PARAM_AUTOMATA["MATRIZ"],
                                                                               PARAM_AUTOMATA["POS"],
                                                                               PARAM_AUTOMATA["DIR"],
                                                                               PARAM_AUTOMATA["FILAS"],
                                                                               PARAM_AUTOMATA["COLUMNAS"],
                                                                               mouse_pos)
                # dibujar hormiga
                y = PARAM_AUTOMATA["POS"][0] * PARAM_AUTOMATA["TAM"]  # fila
                x = PARAM_AUTOMATA["POS"][1] * PARAM_AUTOMATA["TAM"]  # columna
                pygame.draw.rect(ventana, (255, 0, 0), (x, y, PARAM_AUTOMATA["TAM"], PARAM_AUTOMATA["TAM"]))

        mouse_pos = None # Reiniciar la posición del mouse.
        pygame.display.update()
        clock.tick(PARAM_AUTOMATA["TICK"])
    pygame.quit()

if __name__ == "__main__":
    main(1)