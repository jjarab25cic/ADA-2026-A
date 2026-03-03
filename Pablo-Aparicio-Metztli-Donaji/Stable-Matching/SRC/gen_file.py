from pathlib import Path
import random

# Ruta base
SRC_DIR = Path(__file__).resolve().parent
base_dir = SRC_DIR.parent
base = base_dir / "DAT"
base.mkdir(exist_ok=True)

def generar_nombres_unicos(n, genero):
    nombres = []

    for i in range(n):
        if genero == "M":
            nombre = f"Hombre{i}"
        else:
            nombre = f"Mujer{i}"

        nombres.append(nombre)

    return nombres

def generate(n):
    # Generar nombres
    hombres = generar_nombres_unicos(n, "M")
    mujeres = generar_nombres_unicos(n, "W")

    # Crear preferencias
    def generar_preferencias(personas, opciones):
        prefs = {}

        for p in personas:
            lista = opciones.copy()
            random.shuffle(lista)
            prefs[p] = lista

        return prefs

    pref_hombres = generar_preferencias(hombres, mujeres)
    pref_mujeres = generar_preferencias(mujeres, hombres)
    return(pref_hombres,pref_mujeres)

# Guardar archivos
def guardar(nombre, data):
    with open(f"{base}/{nombre}", "w", encoding="utf-8") as f:
        for k, v in data.items():
            linea = k + ": " + ", ".join(v)
            f.write(linea + "\n")

def merch_file(g,h,m):
    merch = {}
    if g == 'M':
        merch.update(h)
        merch.update(m)
        return(merch)
    elif g == 'W':
        merch.update(m)
        merch.update(h)
        return(merch)
    else:
        return(0)

def main():
    n = int(input("cuantas personas? "))
    g = input("genero que empieza? ")
    num_file = int(input("archivol actual"))
    h , m = generate(n)
    data = merch_file(g.upper(),h,m)
    guardar(f'd{num_file}.txt', data)

if __name__ == "__main__":
    main()