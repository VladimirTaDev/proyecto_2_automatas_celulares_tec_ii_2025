from copy import deepcopy
from random import choices

# colores de celdas
# 1 = azules, 2 = rojos
COLORES = [[(255, 0, 0), 1], [(0, 0, 255), 2]]

def main(matriz, mouse = None):
    # cambiar el estado de la celda
    if mouse:
        f, c = mouse
        matriz[f][c] = (matriz[f][c] + 1) % 3
    # ejecutar lógica
    matriz = avanzar_rojos(matriz)
    matriz = avanzar_azules(matriz)
    return matriz

def generar_aleatoria(filas, columnas):
    """Genera matriz con valores aleatorios entre 0, 1 y 2 dejando 60% del espacio libre"""
    return [[choices([0, 1, 2], weights=[0.6, 0.2, 0.2])[0] for c in range(columnas)] for f in range(filas)]

def avanzar_rojos(M):
    """
    Avanza los 'carros' rojos (1).
    Entradas y restricciones:
    - M: (matrix). Matríz actual.
    Salida:
    - M: (matrix). Matríz actualizada.
    """

    M2 = deepcopy(M)
    for f in range(len(M)):
        for c in range(len(M[0])):
            if M[f][c] == 1:
                siguiente_c = (c + 1) % len(M[0])
                if M[f][siguiente_c] == 0:
                    M2[f][siguiente_c] = 1
                    M2[f][c] = 0

    return M2

def avanzar_azules(M):
    """
    Avanza los 'carros' azules (2).
    Entradas y restricciones:
    - M: (matrix). Matríz actual.
    Salida:
    - M: (matrix). Matríz actualizada.
    """
    M2 = deepcopy(M)
    for f in range(len(M)):
        for c in range(len(M[0])):
            if M[f][c] == 2:
                siguiente_f = (f + 1) % len(M)
                if M[siguiente_f][c] == 0:
                    M2[siguiente_f][c] = 2
                    M2[f][c] = 0

    return M2