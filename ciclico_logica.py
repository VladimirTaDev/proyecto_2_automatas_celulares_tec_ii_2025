from copy import deepcopy
from random import randint

COLORES = [
    ((255, 64, 0), 0),
    ((255, 128, 0), 1),
    ((255, 191, 0), 2),
    ((255, 255, 0), 3),
    ((191, 255, 0), 4),
    ((128, 255, 0), 5),
    ((64, 255, 0), 6),
    ((0, 255, 0), 7),
    ((0, 255, 64), 8),
    ((0, 255, 128), 9),
    ((0, 255, 191), 10),
    ((0, 255, 255), 11),
    ((0, 191, 255), 12),
    ((0, 128, 255), 13),
    ((0, 64, 255), 14),
    ((255, 0, 255), 15)
]

def generar_aleatoria(filas, columnas):
    """
    Genera una matriz inicial aleatoria para el autómata celular cíclico.
    Entradas:
    - filas (int): número de filas de la matriz
    - columnas (int): número de columnas de la matriz
    Salida:
    - matriz (list): matriz generada con valores enteros de 0 a 15,
      representando los 16 estados cíclicos posibles de cada celda
    """
    return [[randint(0, 15) for i in range(columnas)] for i in range(filas)]

def generar_nula(filas, columnas):
    """
    Genera una matriz inicial con todas las celdas en estado 0.
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
    filas = len(M)
    columnas = len(M[0])
    vecinos = []
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
    Calcula el siguiente estado de una célula según la regla del autómata
    cíclico.
    Entradas:
    - estado (int): estado actual de la célula (0-15)
    - vecinos (list): lista de estados de los vecinos de la célula
    Salida:
    - nuevo_estado (int): estado actualizado de la célula
    """
    siguiente = (estado + 1) % 16
    if siguiente in vecinos:
        return siguiente
    return estado

def transicion(M):
    """
    Aplica la regla de transición a toda la matriz del autómata.
    Entradas:
    - M (list): matriz actual del autómata
    Salida:
    - M2 (list): nueva matriz con los estados actualizados
    """
    M2 = deepcopy(M)
    for f in range(len(M)):
        for c in range(len(M[0])):
            vecinos = obtener_vecinos(M, f, c)
            M2[f][c] = transicion_celula(M[f][c], vecinos)
    return M2

def cambiar_estado(M, f, c):
    """
    Cambia el estado de la célula (f,c) al siguiente estado del ciclo.
    Entradas:
    - M (list): matriz actual del autómata
    - f (int): fila de la célula
    - c (int): columna de la célula
    Salida:
    - M (list): matriz modificada con la célula actualizada
    """
    M[f][c] = (M[f][c] + 1) % 16

def main(matriz, mouse=None):
    """
    Ejecuta un paso del autómata celular cíclico.
    Entradas:
    - matriz (list): matriz actual del autómata
    - mouse (tuple o None): posición de la célula clickeada (fila, columna). 
      Si se pasa, se actualiza el estado de la célula usando 'cambiar_estado'
    Salida:
    - matriz (list): matriz actualizada después de aplicar 'transicion' a todas las células
    """
    if mouse:
        f, c = mouse
        cambiar_estado(matriz, f, c)
    return transicion(matriz)

