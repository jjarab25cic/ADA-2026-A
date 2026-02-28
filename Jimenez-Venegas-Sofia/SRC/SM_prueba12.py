import time
import matplotlib.pyplot as plt

valores_n = [2**i for i in range(1, 12)]

def ejecutar_archivo(nombre_archivo):

    inicio_lectura = time.time()

    with open(nombre_archivo, "r") as f:
        var = f.read()

    listas = [line.strip().split() for line in var.splitlines()]

    datos = listas[0]
    n = int(datos[0])
    quien_propone = datos[1]

    m = {}
    w = {}

    for i in range(1, n+1):
        m[listas[i][0]] = listas[i][1:]

    for i in range(n+1, 2*n+1):
        w[listas[i][0]] = listas[i][1:]

    fin_lectura = time.time()
    tiempo_lectura = fin_lectura - inicio_lectura

    if quien_propone == 'm':
        proponedores = m
        receptores = w
    else:
        proponedores = w
        receptores = m

    ranking = {}
    for r in receptores:
        ranking[r] = {}
        posicion = 0
        for p in receptores[r]:
            ranking[r][p] = posicion
            posicion += 1

    #Algoritmo
    inicio_algoritmo = time.time()

    proponedor_receptor = {}
    receptor_proponedor = {}

    pretendientes = list(proponedores.keys())

    propuestas = {}
    for p in proponedores:
        propuestas[p] = 0

    while pretendientes:
        pretendiente = pretendientes[0]

        pareja = proponedores[pretendiente][propuestas[pretendiente]]
        propuestas[pretendiente] += 1

        if pareja not in receptor_proponedor:
            proponedor_receptor[pretendiente] = pareja
            receptor_proponedor[pareja] = pretendiente
            pretendientes.remove(pretendiente)

        else:
            pareja_actual = receptor_proponedor[pareja]

            if ranking[pareja][pretendiente] < ranking[pareja][pareja_actual]:
                proponedor_receptor.pop(pareja_actual)
                pretendientes.append(pareja_actual)

                proponedor_receptor[pretendiente] = pareja
                receptor_proponedor[pareja] = pretendiente
                pretendientes.remove(pretendiente)

    fin_algoritmo = time.time()
    tiempo_algoritmo = fin_algoritmo - inicio_algoritmo

    inicio_impresion = time.time()

    for k in proponedor_receptor:
        _ = proponedor_receptor[k]

    fin_impresion = time.time()
    tiempo_impresion = fin_impresion - inicio_impresion

    return tiempo_lectura, tiempo_algoritmo, tiempo_impresion

# Ejecución

tiempos_totales = []
tabla_resultados = []

inicio_total = time.time()

for n in valores_n:
    nombre = f"entrada_{n}.txt"
    print(f"Ejecutando n = {n}")

    inicio = time.time()

    t_lectura, t_algoritmo, t_impresion = ejecutar_archivo(nombre)

    fin = time.time()
    t_total = fin - inicio

    tiempos_totales.append(t_total)
    tabla_resultados.append((n, t_lectura, t_algoritmo, t_impresion, t_total))

    print(f"Total: {t_total:.6f} segundos\n")

fin_total = time.time()
tiempo_total_experimento = fin_total - inicio_total


#Resultados txt

with open("resultados_tiempos.txt", "w") as f:
    f.write("n\tLectura\tEmparejamiento\tImpresion\tTotal\n")

    for fila in tabla_resultados:
        f.write(f"{fila[0]}\t{fila[1]:.6f}\t{fila[2]:.6f}\t{fila[3]:.6f}\t{fila[4]:.6f}\n")

    f.write(f"\nTiempo total experimento:\t{tiempo_total_experimento:.6f}\n")

#Gráfica logaritmica 

plt.figure()
plt.loglog(valores_n, tiempos_totales, marker='o')
plt.xlabel("n (escala log)")
plt.ylabel("Tiempo total (segundos, escala log)")
plt.title("Comportamiento temporal Stable Matching (Log-Log)")
plt.grid(True, which="both")

plt.savefig("grafica_complejidad_log.png", dpi=300)
plt.close()

#Gráfica lineal

plt.figure()
plt.plot(valores_n, tiempos_totales, marker='o')
plt.xlabel("n")
plt.ylabel("Tiempo total (segundos)")
plt.title("Comportamiento temporal Stable Matching (Lineal)")
plt.grid(True)

plt.savefig("grafica_complejidad_lineal.png", dpi=300)
plt.close()


print("Archivos generados correctamente:")
print(" - resultados_tiempos.txt")
print(" - grafica_complejidad_log.png")
print(" - grafica_complejidad_lineal.png")