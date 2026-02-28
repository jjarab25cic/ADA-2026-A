import random

valores_n = [2**i for i in range(1, 12)]

def generar_archivo(n, nombre_archivo):
    hombres = [f"m{i}" for i in range(1, n+1)]
    mujeres = [f"w{i}" for i in range(1, n+1)]

    quien_propone = random.choice(['m', 'w'])

    with open(nombre_archivo, "w") as f:
        f.write(f"{n} {quien_propone}\n")

        if quien_propone == 'm':

            for h in hombres:
                prefs = mujeres[:]
                random.shuffle(prefs)
                f.write(h + " " + " ".join(prefs) + "\n")

            for m in mujeres:
                prefs = hombres[:]
                random.shuffle(prefs)
                f.write(m + " " + " ".join(prefs) + "\n")
        else:

            for m in mujeres:
                prefs = hombres[:]
                random.shuffle(prefs)
                f.write(m + " " + " ".join(prefs) + "\n")

            for h in hombres:
                prefs = mujeres[:]
                random.shuffle(prefs)
                f.write(h + " " + " ".join(prefs) + "\n")

for n in valores_n:
    nombre = f"entrada_{n}.txt"
    print(f"Generando n = {n}")
    generar_archivo(n, nombre)