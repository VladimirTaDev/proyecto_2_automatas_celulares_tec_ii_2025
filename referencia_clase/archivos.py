def main():
    archivo = open("mensaje.txt", "r", encoding="utf-8")
    for linea in archivo:
        print(linea)
    archivo.close()

def imprimir_contenidos2():
    try:
        with open("data/mensaje1.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                print(linea, end="")
    except Exception as e:
        print(f"ERROR: {e}")

def escribir_contenidos():
    archivo = open("data/datos.txt", "w", encoding="utf-8")
    paises = ["Costa Rica", "Nicaragua", "Corea del Norte", "Rusia", "Luxemburgo"]
    for pais in paises:
        archivo.write(pais + "\n")
    archivo.close()

def copiar_archivo():
    try:
        nombre_original = input("Escriba el nombre del archivo original: ")
        nombre_copia = input("Escriba el nombre del archivo copia: ")
        with open(nombre_original, "r") as archivo_original, \
            open(nombre_copia, "w") as archivo_copia:
            for linea in archivo_original:
                archivo_copia.write(linea)
        print(f"Se creó el archivo {nombre_copia}.")
    except Exception as e:
        print(f"ERROR: {e}")

import pickle

dic = {(1, 2, 3): ["|*|2|_384", 233443, 54354.3234324, False],
       (3, 4, 5): ["80|\\170", 324234, 327457.84536208, True],
       (5, 6, 7): ["<454 \\/3|2|)3", 5749, 234.33333333, False]}

#escritura
archivo = open("datos.pkl", "wb")
pickle.dump(dic, archivo)
archivo.close()

#lectura
archivo = open("datos.pkl", "rb")
dic2 = pickle.load(archivo)
print(dic2)

import json
M = [[4, 7, 6, 9],
     [5, 1, 7, 8],
     [1, 4, 8, 7],
     [3, 9, 0, 1]]

archivo = open("matriz.txt", "w")
json.dump(M, archivo)
archivo.close()

archivo = open("matriz.txt", "r")
M2 = json.load(archivo)
archivo.close()
for f in M2:
    for n in f:
        print(n, end="\t")
    print()

def guardar_hosoya():
    M = hosoya(10, 10)
    with open("hosoya.pickle", "wb") as salida:
        pickle.dump(M, salida)

def cargar_hosoya():
    with open("hosoya.pickle", "rb") as entrada:
        M = pickle.load(entrada)
    print(tabulate.tabulate(M))

def guardar_hosoya_json():
    M = hosoya(10, 10)
    with open("hosoya.json", "w") as salida:
        json.dump(M, salida)

def cargar_hosoya_json():
    with open("hosoya.json", "r") as entrada:
        M = json.load(entrada)
    print(tabulate.tabulate(M))

