"""
Gestiona la lectura de archivos, medición de tiempos y exportación de resultados.
"""
# Importamos nuestras herramientas locales
from Emparejador import generador_emparejamiento
from Generador_preferencias import generador_datos
import time
import csv
import os

def leer_instancia(ruta_archivo):
    """
    Lee el archivo generado y separa el nombre de la lista de preferencias.
    """
    pref_h = {}
    pref_m = {}
    
    with open(ruta_archivo, 'r') as f:
        lineas = f.readlines()
        if not lineas: return None, None
        
        n = int(lineas[0].strip())
        
        # Lectura de Hombres (líneas 1 a n)
        for i in range(1, n + 1):
            partes = lineas[i].split()
            nombre = partes[0]
            preferencias = partes[1:]
            pref_h[nombre] = preferencias
            
        # Lectura de Mujeres (líneas n+1 a 2n)
        for i in range(n + 1, 2 * n + 1):
            partes = lineas[i].split()
            nombre = partes[0]
            preferencias = partes[1:]
            pref_m[nombre] = preferencias
            
    return pref_h, pref_m

def ejecutar_experimento():
    # Definimos los tamaños de N para observar la complejidad cuadrática
    tamanos_n = [10, 50, 100, 200, 400, 600, 800, 1000, 1200, 1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600, 3900, 4200, 4500, 4800, 5100, 5400, 5700, 6000, 6300, 6600, 6900, 7200, 7500, 7800, 8100, 8400, 8700, 9000, 9300, 9600, 9900, 10200, 10500, 10800, 11100, 11400, 11700, 12000]
    resultados = []

    print(f"{'N':<10} | {'Tiempo (seg)':<15}")
    print("-" * 30)

    for i, n in enumerate(tamanos_n):
        id_archivo = i + 1
        # 1. Genera los datos usando Generador_preferencias
        generador_datos(n, id_archivo)
        
        # 2. Ruta del archivo
        ruta = f"DAT/entrada{id_archivo}_n{n}"
        
        # 3. Cargar a diccionarios la información en los archivos
        h_prefs, m_prefs = leer_instancia(ruta)
        
        # 4. Mide tiempo del algoritmo
        inicio = time.perf_counter()
        generador_emparejamiento(h_prefs, m_prefs)
        fin = time.perf_counter()
        
        tiempo_ejecucion = fin - inicio
        resultados.append([n, tiempo_ejecucion])
        print(f"{n:<10} | {tiempo_ejecucion:<15.6f}")

    # 5. Guarda en CSV para el Visualizador
    with open("resultados_tiempos.csv", "w", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(["N", "Tiempo_Segundos"])
        escritor.writerows(resultados)

if __name__ == "__main__":
    if not os.path.exists("DAT"): os.makedirs("DAT")
    ejecutar_experimento()