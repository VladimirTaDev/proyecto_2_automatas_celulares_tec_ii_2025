from random import choices
# colores de celdas
# 1 = azules, 2 = rojos
COLORES = [[(0, 0, 255), 1], [(255, 0, 0), 2]]

def main(matriz, pos, dir, filas, columnas, mouse = None):
    """
    Ejecuta un paso de la lógica del autómata de Langton.
    Entradas y restricciones:
    - matriz (list): matriz del tablero.
    - pos (list): posición actual de la hormiga [fila, columna].
    - dir (int): dirección de la hormiga: 1↑, 2→, 3↓, 4←.
    - filas (int): número de filas del tablero.
    - columnas (int): número de columnas del tablero.
    - mouse (tuple): posición del mouse (fila, columna) o None.
    Salida:
    - matriz (list): matriz actualizada.
    - dir (int): dirección actualizada de la hormiga.
    """
    # cambiar el estado de la celda
    if mouse:
        f, c = mouse
        matriz[f][c] = (matriz[f][c] + 1) % 2

    # ejecutar lógica
    # gira la hormiga
    dir = girar_hormiga(matriz[pos[0]][pos[1]], dir)

    # actualizar celda
    matriz[pos[0]][pos[1]] = siguiente(matriz[pos[0]][pos[1]])

    # avanzar la hormiga
    nueva_f, nueva_c = avanzar_hormiga(pos[0], pos[1], dir)
    pos[0] = nueva_f % filas
    pos[1] = nueva_c % columnas

    return matriz, dir

def generar_nula(filas, columnas):
    """
    Genera matriz de ceros.
    Entradas y restricciones:
    - filas (int): número de filas.
    - columnas (int): número de columnas.
    Salida:
    - matriz (list): matriz de ceros.
    """
    return [[0 for c in range(columnas)] for f in range(filas)]

def generar_aleatoria(filas, columnas):
    """
    Genera matriz con valores aleatorios entre 0 y 1, dejando 90% del espacio en 0.
    Entradas y restricciones:
    - filas (int): número de filas.
    - columnas (int): número de columnas.
    Salida:
    - matriz (list): matriz aleatoria.
    """
    return [[choices([0, 1], weights=[0.9, 0.1])[0] for c in range(columnas)] for f in range(filas)]

def girar_hormiga(giro, dir):
    """
    Gira la hormiga.
    Entradas y restricciones:
    - giro (int): en qué dirección girar la hormiga. 0 = derecha, 1 = izquierda.
    - dir (int): dirección de la hormiga: 1↑, 2→, 3↓, 4←.
    Salida:
    - nueva_dir (int): dirección siguiente de la hormiga: 1↑, 2→, 3↓, 4←.
    """

    nueva_dir = 0

    # gira derecha o izquierda
    if giro == 0:
        nueva_dir = (dir % 4) + 1
    else:
        nueva_dir = ((dir - 2) % 4) + 1

    return int(nueva_dir)

def avanzar_hormiga(y, x, dir):
    """
    Avanza a la hormiga en la dirección.
    Entradas y restricciones:
    - x, y (int): posición actual de la hormiga.
    - dir (int): dirección de la hormiga: 1↑, 2→, 3↓, 4←.
    Salida:
    - x, y (int): posición siguiente de la hormiga.
    """
    nueva_y = 0
    nueva_x = 0

    # avanza la hormiga
    match dir:
        case 1: # ↑
            nueva_x = x
            nueva_y = y - 1
        case 2:  # →
            nueva_x = x + 1
            nueva_y = y
        case 3:  # ↓
            nueva_x = x
            nueva_y = y + 1
        case 4:  # ←
            nueva_x = x - 1
            nueva_y = y

    return nueva_y, nueva_x

def siguiente(celda):
    """
    Actualiza la celda en la que se encuentra.
    Entradas y restricciones:
    - celda (int): estado actual de la celda.
    Salida:
    - celda (int): nuevo estado de la celda.
    """
    return 1 - celda