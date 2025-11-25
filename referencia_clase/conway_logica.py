from copy import deepcopy
from random import randint

def generar_aleatoria(filas, columnas):
    """Genera matriz con valores aleatorios entre 0 y 1"""
    return [[randint(0, 1) for c in range(columnas)] for f in range(filas)]

def generar_nula(filas, columnas):
    """Genera matriz de ceros"""
    return [[0 for c in range(columnas)] for f in range(filas)]

def obtener_vecinos(M, fila, columna):
    """Retorna una lista con los vecinos de la célulaM[f][c]"""
    vecinos = []
    for f in range(fila - 1, fila + 2):
        for c in range(columna - 1, columna + 2):
            if f != fila or c != columna:
                vecinos.append(M[f % len(M)][c % len(M[0])])
    return vecinos

def transicion_celula(estado, vecinos):
    """Retorna el nuevo estado de la célula de acuerdo a sus vecinos.
    estado == 0 y 3 vivos --> viva
    estado == 1 y menos de 2 vivos --> muerta
    estado == 1 y más de 3 vivos --> muerta
    en cualquier otro caso, queda igual."""
    vivos = vecinos.count(1)
    if estado == 0 and vivos == 3: #nacimiento
        return 1
    if estado == 1 and vivos < 2: #despoblación
        return 0
    if estado == 1 and vivos > 3: #sobrepoblación
        return 0
    return estado

def transicion(M):
    """Genera una nueva matriz con el siguiente estado del autómata"""
    M2 = deepcopy(M)
    for f in range(len(M)):
        for c in range(len(M[0])):
            vecinos = obtener_vecinos(M, f, c)
            M2[f][c] = transicion_celula(M[f][c], vecinos)
    return M2

def cambiar_estado(M, f, c):
    """Le cambia el estado a la célula M[f][c]"""
    M[f][c] = (M[f][c] + 1) % 2