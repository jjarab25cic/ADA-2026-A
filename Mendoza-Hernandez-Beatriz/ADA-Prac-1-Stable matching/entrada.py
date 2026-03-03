import random
import os

# -----------------------------
# Crear nombres
# -----------------------------
def generar_nombres(prefijo, n):
    return [f"{prefijo}{i+1}" for i in range(n)]

# -----------------------------
# Generar preferencias aleatorias
# -----------------------------
def generar_preferencias(personas, opciones):
    preferencias = {}
    for p in personas:
        lista = opciones[:]
        random.shuffle(lista)
        preferencias[p] = lista
    return preferencias

# -----------------------------
# Crear archivo de entrada
# -----------------------------
def generar_archivo(N, first, filename):

    hombres = generar_nombres("H", N)
    mujeres = generar_nombres("M", N)

    pref_hombres = generar_preferencias(hombres, mujeres)
    pref_mujeres = generar_preferencias(mujeres, hombres)

    with open(filename, "w") as f:

        # primera línea
        f.write(f"{N} {first}\n")

        # preferencias hombres
        for h in hombres:
            f.write(h + " " + " ".join(pref_hombres[h]) + "\n")

        # preferencias mujeres
        for m in mujeres:
            f.write(m + " " + " ".join(pref_mujeres[m]) + "\n")

# -----------------------------
# Generar M archivos
# -----------------------------
def generar_conjunto_archivos():
    os.makedirs("inputs", exist_ok=True)

    MAX_N = 1000   # cambia si quieres permitir tamaños enormes

    for M in range(1, 26):  # 1 a 25
        N = 2 ** M

        # evitar tamaños absurdos
        if N > MAX_N:
            print(f"Saltando M={M}, N={N} demasiado grande")
            continue

        filename = f"inputs/input_M{M}_N{N}.txt"

        generar_archivo(N, 'm', filename)

        print(f"Archivo creado: {filename}")

# -----------------------------
# Ejecutar
# -----------------------------
generar_conjunto_archivos()