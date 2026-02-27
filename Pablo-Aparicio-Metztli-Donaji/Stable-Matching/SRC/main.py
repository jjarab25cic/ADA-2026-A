import generate_data
import read_data
import gale_shapley
from pathlib import Path
import time
import matplotlib.pyplot as plt

#Ruta de archivos
SRC_DIR = Path(__file__).resolve().parent
base_dir = SRC_DIR.parent
base = base_dir / "DAT" 

# Variable de los datos leidos
data = {}

def matcher(g,data):
    first_preferences = {}
    second_preferences = {}
    names = list(data.keys())
    n = len(names)//2
    grupo1 = names[:n]
    grupo2 = names[n:]

    for i in grupo1:
        first_preferences[i] = data[i]
    for i in grupo2:
        second_preferences[i] = data[i]

    if g == 'M':
        gale_shapley.matching(first_preferences, second_preferences)
        # print("\n")
    elif g == 'W':
        gale_shapley.matching(second_preferences, first_preferences)
        # print("\n")
    else:
        raise ValueError("Genero debe ser M o W")
    return n

def grafo(n, gen, read, match):

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 5))

    # -------- NORMAL --------
    ax1.plot(n, gen, marker="o", label="Generación")
    ax1.plot(n, read, marker="o", label="Lectura")
    ax1.plot(n, match, marker="o", label="Matching")

    ax1.set_title("Escala normal")
    ax1.set_xlabel("Número de parejas (n)")
    ax1.set_ylabel("Tiempo (s)")
    ax1.legend()
    ax1.grid(True)

    # -------- LOG --------
    ax2.plot(n, gen, marker="o", label="Generación")
    ax2.plot(n, read, marker="o", label="Lectura")
    ax2.plot(n, match, marker="o", label="Matching")

    ax2.set_yscale("log")

    ax2.set_title("Escala logarítmica")
    ax2.set_xlabel("Número de parejas (n)")
    ax2.set_ylabel("Tiempo (s)")
    ax2.legend()
    ax2.grid(True)

    # -------- LOG --------
    ax3.plot(n, gen, marker="o", label="Generación")
    ax3.plot(n, read, marker="o", label="Lectura")
    ax3.plot(n, match, marker="o", label="Matching")

    ax3.set_xscale("log")

    ax3.set_title("Escala logarítmica")
    ax3.set_xlabel("Número de parejas (n)")
    ax3.set_ylabel("Tiempo (s)")
    ax3.legend()
    ax3.grid(True)

    plt.suptitle("Tiempo por fase vs n")
    plt.tight_layout()
    plt.show()

def main():
    # Pedimos con que genero empieza y el numero de archivos a generar
    g = input("genero que empieza? ").upper()
    num_file = int(input("numero de archivos: "))

    rep = 3 # numero de repeticiones para cada n

    n_vals = []
    gen_times = []
    read_times = []
    match_times = []

    # Generamos los archivos de acuerdo al genero por prioridad
    gen_total = 0
    for _ in range(rep):
        t0 = time.perf_counter()
        generate_data.make_file(num_file, g)
        t1 = time.perf_counter()

        gen_total += (t1 - t0)

    gen_avg = gen_total / rep

     # -------- TABLA --------
    print("\n==============================================")
    print("Archivo |   n   | Generación | Lectura | Matching")
    print("==============================================")

    # Leemos los archivos generados
    for i in range(1,num_file+1):
        name = f'd{i}.txt'
        new_ruta = base / name
        read_sum = 0

        for _ in range(rep):

            t2 = time.perf_counter()
            data = read_data.leer_preferencias(new_ruta)
            t3 = time.perf_counter()

            read_sum += (t3 - t2)

        read_avg = read_sum / rep
        match_sum = 0

        for _ in range(rep):

            t4 = time.perf_counter()
            n = matcher(g, data)
            t5 = time.perf_counter()

            match_sum += (t5 - t4)

        match_avg = match_sum / rep
        n_vals.append(n)
        gen_times.append(gen_avg/num_file)
        read_times.append(read_avg)
        match_times.append(match_avg)
        print(f"{i:^7} | {n:^5} | "
              f"{gen_avg/num_file:9.6f} | "
              f"{read_avg:7.6f} | "
              f"{match_avg:8.6f}")

    print("==============================================\n")

    grafo(n_vals, gen_times, read_times, match_times)

    t3 = time.perf_counter()

if __name__=="__main__":
    main()