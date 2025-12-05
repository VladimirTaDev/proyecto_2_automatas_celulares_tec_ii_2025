"""
AUTÓMATA ADICIONAL: SIMULACIÓN DE FLUIDOS Y MATERIALES (FALLING SAND)
-----------------------------------------------------------------------

1. DESCRIPCIÓN Y PROCEDENCIA:
   Este autómata es un tipo "Falling Sand Game" (Juego de arena que cae).
   Está inspirado en sistemas de partículas celulares de juegos de simulación física.
   Simula la física newtoniana básica a través de reglas locales en una cuadrícula.

2. NÚMERO DE ESTADOS (3):
   - 0: Vacío (Negro) - Espacio libre.
   - 1: Agua (Azul) - líquida.
   - 2: Arena (color arena) - granular.

3. REGLAS DE COMPORTAMIENTO:
   A. FÍSICA DE LA ARENA (Sólido Granular):
      - Gravedad: "Cae" si la celda inferior está vacía.
      - Densidad: Si la celda de abajo es Agua, la arena se mueve (intercambian).
        simula que la arena es más pesada y se hunde.
      - Amontonamiento: Si tiene base sólida, se queda quieta (formando montañas).

   B. FÍSICA DEL AGUA (Líquido):
      - Prioridad 1 (Gravedad): Intenta caer de forma vertical si tienes espacio.
      - Prioridad 2 (Dispersión): Si no puede caer, intente resbalar en diagonal.
        hacia abajo (izquierda o derecha al azar).
      - Prioridad 3 (Fluidez lateral): Si está atrapada abajo, intenta moverse
        horizontalmente a los lados, simulando el comportamiento de nivelación de un líquido.

4. CARACTERÍSTICAS DE IMPLEMENTACIÓN:
   - Iteración Inversa: La matriz se recorre de abajo hacia arriba para
     Dejar caer bien las partículas en un solo cuadro de animación.
     sin "teletransportarse" incorrectamente.
   - Se usa aleatoriedad para elegir direcciones para prevenir que el
     flujo se desvíe artificialmente hacia un lado.

5. Inspirado en:
    Demostración en clase.
    https://winter.dev/articles/falling-sand
    https://thecodingtrain.com/challenges/180-falling-sand
    https://www.youtube.com/watch?v=JKv6CwOiIlU
"""

from copy import deepcopy
from random import choices, shuffle

# Colores de celdas: 0 = vacío (negro), 1 = agua (azul), 2 = arena (amarillo)
COLORES = [[(0, 0, 0), 0], [(0, 191, 255), 1], [(194, 178, 128), 2]]

def main(matriz, mouse=None):
    """
    Ejecuta un paso de la lógica del autómata de agua.
    Entradas:
    - matriz (list): matriz del tablero.
    - mouse (tuple): posición del mouse (fila, columna) o None.
    Salida:
    - matriz (list): matriz actualizada.
    """
    if mouse:
        f, c = mouse
        cambiar_estado(matriz, f, c)
    return transicion(matriz)

def generar_aleatoria(filas, columnas):
    """
    Genera matriz con gotas de agua arriba y arena abajo.
    Entradas:
    - filas (int): número de filas.
    - columnas (int): número de columnas.
    Salida:
    - matriz (list): matriz aleatoria.
    """
    matriz = generar_nula(filas, columnas)
    # Agua en el 20% superior
    for f in range(filas // 5):
        for c in range(columnas):
            matriz[f][c] = choices([0, 1], weights=[0.7, 0.3])[0]
    # Arena en el 20% inferior (con huecos)
    for f in range(filas - filas // 5, filas):
        for c in range(columnas):
            matriz[f][c] = choices([0, 2], weights=[0.3, 0.7])[0]
    return matriz

def generar_nula(filas, columnas):
    """
    Genera matriz con todas las celdas en estado 0 (vacío).
    Entradas:
    - filas (int): número de filas.
    - columnas (int): número de columnas.
    Salida:
    - matriz (list): matriz vacía.
    """
    return [[0 for c in range(columnas)] for f in range(filas)]

def obtener_vecinos(M, f, c):
    """
    Obtiene las coordenadas de los vecinos relevantes para el movimiento del agua.
    Entradas:
    - M (list): matriz actual del autómata.
    - f (int): fila de la celda.
    - c (int): columna de la celda.
    Salida:
    - dict: diccionario con las coordenadas de abajo, izquierda y derecha.
    """
    filas = len(M)
    columnas = len(M[0])
    return {
        'abajo': (f + 1) if f + 1 < filas else None,
        'izq': (c - 1) if c - 1 >= 0 else None,
        'der': (c + 1) if c + 1 < columnas else None
    }

def cambiar_estado(M, f, c):
    """
    Cambia el estado de la celda (f, c) entre vacío, arena y agua.
    Entradas:
    - M (list): matriz del autómata.
    - f (int): fila de la celda.
    - c (int): columna de la celda.
    """
    # cambiar estado: 0 -> 2 (arena), 2 -> 1 (agua), 1 -> 0 (vacío)
    ciclo = {0: 2, 2: 1, 1: 0}
    M[f][c] = ciclo.get(M[f][c], 0)

def transicion(M):
    """
    Aplica la física del agua a toda la matriz.
    Reglas: Gravedad -> Diagonal -> Flujo lateral.
    Entradas:
    - M (list): matriz actual del autómata.
    Salida:
    - M2 (list): nueva matriz con los estados actualizados.
    """
    filas = len(M)
    columnas = len(M[0])
    M2 = deepcopy(M)

    # Recorrer de abajo hacia arriba
    for f in range(filas - 2, -1, -1):
        for c in range(columnas):
            # Física de la arena
            if M2[f][c] == 2:
                abajo = f + 1 if f + 1 < filas else None
                if abajo is not None:
                    if M2[abajo][c] == 0:
                        M2[abajo][c] = 2
                        M2[f][c] = 0
                    elif M2[abajo][c] == 1:
                        # Intercambiar: arena baja, agua sube
                        M2[abajo][c] = 2
                        M2[f][c] = 1

            # Física del agua
            elif M2[f][c] == 1:
                vecinos = obtener_vecinos(M2, f, c)
                abajo = vecinos['abajo']
                izq = vecinos['izq']
                der = vecinos['der']

                movido = False

                # 1. Intentar mover abajo
                if abajo is not None and M2[abajo][c] == 0:
                    M2[abajo][c] = 1
                    M2[f][c] = 0
                    movido = True

                # 2. Si no, intentar diagonales (aleatorio)
                if not movido and abajo is not None:
                    opciones = []
                    if izq is not None:
                        opciones.append(izq)
                    if der is not None:
                        opciones.append(der)
                    shuffle(opciones)

                    for lado in opciones:
                        if M2[abajo][lado] == 0:
                            M2[abajo][lado] = 1
                            M2[f][c] = 0
                            movido = True
                            break

                # 3. Si no, intentar flujo lateral
                if not movido:
                    opciones = []
                    if izq is not None:
                        opciones.append(izq)
                    if der is not None:
                        opciones.append(der)
                    shuffle(opciones)

                    for lado in opciones:
                        if M2[f][lado] == 0:
                            M2[f][lado] = 1
                            M2[f][c] = 0
                            break

    return M2
