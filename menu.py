import easygui
import sys

PARAM_AUTOMATA = {"TAM": 5,
                  "FILAS": 100,
                  "COLUMNAS": 100,
                  "TICK": 1000,
                  "AUTOMATA": 1,  # tipo de autómata a ejecutar. 1 = tráfico, 2 = hormiga, 3 = brian, 4 = cíclico
                  "MATRIZ": []}

def pedir_entradas():
    # pedir entradas con EasyGUI
    # filas
    filas = easygui.integerbox(msg="Ingrese el número de filas (hasta 200):", title="Configuración",
                               default=100, lowerbound=50, upperbound=200)
    if filas is None:
        sys.exit()
    PARAM_AUTOMATA["FILAS"] = filas

    # columnas
    columnas = easygui.integerbox(msg="Ingrese el número de columnas (hasta 200):", title="Configuración",
                                  default=100, lowerbound=50, upperbound=200)
    if columnas is None:
        sys.exit()
    PARAM_AUTOMATA["COLUMNAS"] = columnas

    # tamaño de celda
    tam = easygui.integerbox(msg="Ingrese el tamaño de la celda en píxeles:", title="Configuración",
                             default=5, lowerbound=1, upperbound=20)
    if tam is None:
        sys.exit()
    PARAM_AUTOMATA["TAM"] = tam

    # velocidad de simulación
    tick = easygui.integerbox(msg="Ingrese la velocidad de simulación (FPS):", title="Configuración",
                              default=500, lowerbound=1, upperbound=9000)
    if tick is None:
        sys.exit()
    PARAM_AUTOMATA["TICK"] = tick

    return PARAM_AUTOMATA

def seleccionar_automata():
    # seleccionar autómata con EasyGUI
    opciones = ["Tráfico", "Hormiga de Langton", "Cerebro de Brian", "Autómata celular cíclico", "Salir"]
    opcion = easygui.buttonbox(msg="Seleccione un autómata:", title="Menú Principal", choices=opciones)

    if opcion in (None, "Salir"):
        return None

    if opcion == "Tráfico":
        PARAM_AUTOMATA["AUTOMATA"] = 1
    elif opcion == "Hormiga de Langton":
        PARAM_AUTOMATA["AUTOMATA"] = 2
    elif opcion == "Cerebro de Brian":
        PARAM_AUTOMATA["AUTOMATA"] = 3
    elif opcion == "Autómata celular cíclico":
        PARAM_AUTOMATA["AUTOMATA"] = 4

    return PARAM_AUTOMATA
