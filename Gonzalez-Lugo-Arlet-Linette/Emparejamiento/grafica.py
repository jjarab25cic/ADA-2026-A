import time
import matplotlib.pyplot as plt
import os

def gale_shapley(preferencias_hombres, preferencias_mujeres):
    n = len(preferencias_hombres)
    
    pareja_h = [-1] * n  
    pareja_m = [-1] * n  
    libres = list(range(n))  
    siguiente = [0] * n  
    
    while libres:
        h = libres[0]
        m = preferencias_hombres[h][siguiente[h]]
        siguiente[h] += 1
        
        if pareja_m[m] == -1:
            pareja_m[m] = h
            pareja_h[h] = m
            libres.pop(0)
        else:
            h_actual = pareja_m[m]
            if preferencias_mujeres[m].index(h) < preferencias_mujeres[m].index(h_actual):
                pareja_m[m] = h
                pareja_h[h] = m
                pareja_h[h_actual] = -1
                libres.pop(0)
                libres.append(h_actual)
    
    return pareja_h, pareja_m

def leer_archivo_preferencias(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
    
    n = len(lineas) // 2
    
    preferencias_hombres = []
    hombres = []
    for i in range(n):
        partes = lineas[i].strip().split()
        hombres.append(partes[0])
        pref = [int(m[1:]) - 1 for m in partes[1:]]
        preferencias_hombres.append(pref)
    
    preferencias_mujeres = []
    mujeres = []
    for i in range(n, 2*n):
        partes = lineas[i].strip().split()
        mujeres.append(partes[0])
        pref = [int(h[1:]) - 1 for h in partes[1:]]
        preferencias_mujeres.append(pref)
    
    return preferencias_hombres, preferencias_mujeres, n

def procesar_archivo(nombre_archivo):
    try:
        preferencias_h, preferencias_m, n = leer_archivo_preferencias(nombre_archivo)
        inicio = time.perf_counter()
        pareja_h, pareja_m = gale_shapley(preferencias_h, preferencias_m)
        fin = time.perf_counter()
        
        tiempo_ejecucion = (fin - inicio) * 1000  
        
        return n, tiempo_ejecucion
    
    except Exception as e:
        print(f"Error al procesar {nombre_archivo}: {e}")
        return None, None

def main():
    carpeta = "archivos2"
    archivo_resultados = "resultados_gale_shapley_log_22.txt"
    
    if not os.path.exists(carpeta):
        print(f"Error: La carpeta '{carpeta}' no existe.")
        return
    
    archivos = [f for f in os.listdir(carpeta) if f.endswith('_parejas.txt')]
    archivos.sort(key=lambda x: int(x.split('_')[0]))  # Ordenar por número de parejas
    
    if not archivos:
        print(f"No se encontraron archivos en la carpeta '{carpeta}'")
        return
    
    print(f"Procesando {len(archivos)} archivos...\n")
    
    tamanos = []
    tiempos = []
    
    with open(archivo_resultados, 'w', encoding='utf-8') as f_resultados:
        f_resultados.write("=== RESULTADOS DEL ALGORITMO DE GALE-SHAPLEY ===\n")
        f_resultados.write(f"Fecha de ejecución: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f_resultados.write("=" * 60 + "\n\n")
        f_resultados.write(f"{'Archivo':<40} {'Parejas':<10} {'Tiempo (ms)':<15}\n")
        f_resultados.write("-" * 65 + "\n")
    
    for archivo in archivos:
        ruta_completa = os.path.join(carpeta, archivo)
        print(f"Procesando: {archivo}", end="... ")
        
        n, tiempo = procesar_archivo(ruta_completa)
        
        if n is not None:
            tamanos.append(n)
            tiempos.append(tiempo)
            print(f"Completado (n={n}, tiempo={tiempo:.4f} ms)")
            2
            with open(archivo_resultados, 'a', encoding='utf-8') as f_resultados:
                f_resultados.write(f"{archivo:<40} {n:<10} {tiempo:.4f}\n")
        else:
            print("Error")
            with open(archivo_resultados, 'a', encoding='utf-8') as f_resultados:
                f_resultados.write(f"{archivo:<40} {'ERROR':<10} {'ERROR':<15}\n")
    
    if not tamanos:
        print("No se pudieron procesar archivos.")
        return
    
    with open(archivo_resultados, 'a', encoding='utf-8') as f_resultados:
        f_resultados.write("-" * 65 + "\n")
        f_resultados.write("\n=== ESTADÍSTICAS ===\n")
        f_resultados.write(f"Total de archivos procesados exitosamente: {len(tamanos)}\n")
        f_resultados.write(f"Tamaño mínimo: {min(tamanos)} parejas\n")
        f_resultados.write(f"Tamaño máximo: {max(tamanos)} parejas\n")
        f_resultados.write(f"Tiempo mínimo: {min(tiempos):.4f} ms\n")
        f_resultados.write(f"Tiempo máximo: {max(tiempos):.4f} ms\n")
        f_resultados.write(f"Tiempo promedio: {sum(tiempos)/len(tiempos):.4f} ms\n")
        f_resultados.write(f"Tiempo total: {sum(tiempos):.4f} ms\n")
    
    print(f"\nResultados guardados en: {archivo_resultados}")
    
    plt.figure(figsize=(14, 8))
    plt.plot(tamanos, tiempos, 'b-o', linewidth=2, markersize=6, label='Tiempo de ejecución')
    plt.xscale('log')
    
    for i, (n, t) in enumerate(zip(tamanos, tiempos)):
        if i % 5 == 0: 
            plt.annotate(f'n={n}\n{t:.2f}ms', (n, t), textcoords="offset points", 
                        xytext=(0, 15), ha='center', fontsize=9, 
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))
    
    plt.xlabel('Número de Parejas (n) - Escala Logarítmica', fontsize=12)
    plt.ylabel('Tiempo de Ejecución (ms)', fontsize=12)
    plt.title('Tiempo de Ejecución del Algoritmo de Gale-Shapley (Escala Logarítmica en X)', fontsize=14)
    plt.grid(True, alpha=0.3, which='both')  # 'both' para mostrar grid en escala log
    plt.legend(fontsize=11)
    plt.xticks(tamanos, [str(n) for n in tamanos], rotation=45)
    stats_text = f'Estadísticas:\n'
    stats_text += f'Archivos procesados: {len(tamanos)}\n'
    stats_text += f'Tiempo mínimo: {min(tiempos):.2f} ms\n'
    stats_text += f'Tiempo máximo: {max(tiempos):.2f} ms\n'
    stats_text += f'Tiempo promedio: {sum(tiempos)/len(tiempos):.2f} ms'
    
    plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes, 
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    plt.tight_layout()
    nombre_grafica = 'tiempos_log22'
    plt.savefig(nombre_grafica, dpi=300, bbox_inches='tight')
    print(f"Gráfica guardada como: {nombre_grafica}")

if __name__ == "__main__":
    main()