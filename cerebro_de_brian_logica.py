from copy import deepcopy
from random import choices


COLORES = [
    ((0, 0, 0), 0),      
    ((0, 200, 255), 1),  
    ((255, 150, 0), 2)   
]

def main(matriz, mouse=None):
    """
    Ejecuta un paso del autómata 'El cerebro de Brian'.
    Entradas:
    - matriz (list): matriz del tablero
    - mouse (tuple): posición del mouse (fila, columna) o None
    Salida:
    - matriz (list): matriz actualizada
    """
 
    if mouse:
        f, c = mouse
        cambiar_estado(matriz,f,c)

    return transicion(matriz)


def generar_aleatoria(filas, columnas):
    """
    Genera una matriz inicial aleatoria para el autómata 'El cerebro de Brian'.
    Entradas:
    - filas (int): número de filas de la matriz
    - columnas (int): número de columnas de la matriz
    Salida:
    - matriz (list): matriz generada con celdas mayormente muertas (0),
      algunas vivas (1) y pocas muriendo (2)
    """
    return [[choices([0, 1, 2], weights=[0.8, 0.15, 0.05])[0]
             for i in range(columnas)] for i in range(filas)]

def generar_nula(filas, columnas):
    """
    Genera una matriz inicial con todas las celdas en estado 0 (muertas).
    Entradas:
    - filas (int): número de filas de la matriz
    - columnas (int): número de columnas de la matriz
    Salida:
    - matriz (list): matriz generada con todas las celdas en estado 0
    """
    return [[0 for _ in range(columnas)] for _ in range(filas)]


def obtener_vecinos(M, f, c):
    """
    Obtiene los estados de los 8 vecinos de la celda en posición (f, c).
    La matriz se interpreta como un toroide (bordes conectados).
    Entradas:
    - M (list): matriz actual del autómata
    - f (int): fila de la celda
    - c (int): columna de la celda
    Salida:
    - vecinos (list): lista con los 8 estados vecinos de la celda
    """
    vecinos = []
    filas = len(M)
    columnas = len(M[0])

    for df in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if df == 0 and dc == 0:
                continue
            nf = (f + df) % filas
            nc = (c + dc) % columnas
            vecinos.append(M[nf][nc])

    return vecinos

def transicion_celula(estado, vecinos):
    """
    Calcula el siguiente estado de una célula según las reglas de 'Cerebro de Brian'.
    Entradas:
    - estado (int): estado actual de la célula (0: muerta, 1: viva, 2: refractaria)
    - vecinos (list): lista de estados de los vecinos de la célula
    Salida:
    - nuevo estado (int): estado actualizado de la célula
    """
    vivos = vecinos.count(1)
    if estado == 0 and vivos == 2:
        return 1
    elif estado == 1:
        return 2
    elif estado == 2:
        return 0
    return estado

def transicion(M):
    """
    Aplica las reglas de actualización del autómata 'El cerebro de Brian' a
    toda la matriz.
    Entradas:
    - M (list): matriz actual del autómata
    Salida:
    - M2 (list): nueva matriz tras aplicar las reglas:
    """
    M2 = deepcopy(M)
    filas = len(M)
    columnas = len(M[0])
    for f in range(filas):
        for c in range(columnas):
            vecinos = obtener_vecinos(M,f,c)
            M2[f][c] = transicion_celula(M[f][c],vecinos)

    return M2

def cambiar_estado(M, f, c):
    """
    Cambia el estado de la célula (f,c) al siguiente estado permitido.
    Entradas:
    - M (list): matriz actual del autómata
    - f (int): fila de la célula
    - c (int): columna de la célula
    Salida:
    - M (list): matriz modificada con la célula actualizada
    """
    M[f][c] = (M[f][c] + 1) % 3

           
           
