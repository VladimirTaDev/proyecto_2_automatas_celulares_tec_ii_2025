def generar_nula(filas, columnas):
    """Genera matriz de ceros"""
    return [[0 for c in range(columnas)] for f in range(filas)]

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