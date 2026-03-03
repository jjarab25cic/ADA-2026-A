import random
import os

def generar_preferencias(n):
    preferencias_hombres = []
    for i in range(1, n + 1):
        mujeres = [f"M{j}" for j in range(1, n + 1)]
        random.shuffle(mujeres)
        preferencias_hombres.append(f"H{i} " + " ".join(mujeres))
    
    preferencias_mujeres = []
    for i in range(1, n + 1):
        hombres = [f"H{j}" for j in range(1, n + 1)]
        random.shuffle(hombres)
        preferencias_mujeres.append(f"M{i} " + " ".join(hombres))
    
    return preferencias_hombres, preferencias_mujeres

def crear_archivo(num_parejas, nombre_archivo):
    preferencias_h, preferencias_m = generar_preferencias(num_parejas)
    
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        for linea in preferencias_h:
            f.write(linea + '\n')
        for linea in preferencias_m:
            f.write(linea + '\n')

def main():
    carpeta = "archivos2"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        print(f"Carpeta '{carpeta}' creada exitosamente.")
    for i in range(1, 101):
        num_parejas = i * 80
        nombre_archivo = os.path.join(carpeta, f"{num_parejas}_parejas.txt")
        crear_archivo(num_parejas, nombre_archivo)     
        print(f"Archivo {i}/80 generado: {nombre_archivo} con {num_parejas} parejas")

if __name__ == "__main__":
    
    main()
    print("\n Proceso completado Se generaron 100 archivos en la carpeta 'archivos'.")