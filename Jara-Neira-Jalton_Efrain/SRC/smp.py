import time
import matplotlib.pyplot as plt

def gsp(archivo):
    with open(archivo, 'r') as f:
        linea_inicial = f.readline().split()
        if not linea_inicial: return None
        
        n = int(linea_inicial[0])
        propone = linea_inicial[1].lower()

        hombres_pref = {}
        mujeres_pref = {}

        for i in range(n):
            datos = f.readline().split()
            hombres_pref[datos[0]] = datos[1:]
        for j in range(n):
            datos = f.readline().split()
            mujeres_pref[datos[0]] = datos[1:]

    start_algo = time.perf_counter()

    if propone == 'm':
        proponentes = hombres_pref
        receptores = mujeres_pref
    else:
        proponentes = mujeres_pref
        receptores = hombres_pref

    rank_receptores = {r: {p: i for i, p in enumerate(lista)} for r, lista in receptores.items()}

    parejas = {r: None for r in receptores}
    libres = list(proponentes.keys())

    while libres:
        p = libres.pop(0)
        lista_p = proponentes[p]
        if not lista_p: continue
        
        candidata = lista_p.pop(0)
        actual = parejas[candidata]

        if actual is None:
            parejas[candidata] = p
        else:
            if rank_receptores[candidata][p] < rank_receptores[candidata][actual]:
                parejas[candidata] = p
                libres.append(actual)
            else:
                libres.append(p)

    end_algo = time.perf_counter()
    return end_algo - start_algo

valores_n = []
tiempos = []

for i in range(1, 15):
    nombre_archivo = f"entrada{i}.txt"
    n = 2**i
    try:
        print(f"Procesando {nombre_archivo} (n={n})...")
        tiempo_ejecucion = gsp(nombre_archivo)
        if tiempo_ejecucion is not None:
            valores_n.append(n)
            tiempos.append(tiempo_ejecucion)
    except FileNotFoundError:
        print(f"Archivo {nombre_archivo} no encontrado.")

#Curva logarítmica
plt.figure(figsize=(10, 6))
plt.plot(valores_n, tiempos, marker='o', linestyle='-', color='b', label='Tiempo de ejecución')

plt.xscale('log', base=2)
plt.yscale('log')

plt.xlabel('Número de parejas (n)')
plt.ylabel('Tiempo (segundos)')
plt.title('Complejidad Gale-Shapley: n vs Tiempo')
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend()
plt.show()