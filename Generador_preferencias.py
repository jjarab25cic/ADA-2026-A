"""
Este script genera una lista aleatoria de preferencias para la practica del algoritmo de Stable matching
"""
import random
import os

def generador_datos(n, id_archivo):
    #Aseguramos que la carpeta para los datos existe
    if not os.path.exists("DAT"):
        os.makedirs("DAT")
    #Se define la ruta y el nombre del archivo (hasta ahora solo es una cadena de texto)
    nombre_archivo = f"DAT/entrada{id_archivo}_n{n}"
    #Se crea el archivo y se agrega inicialmente el tamaño "n"
    with open(nombre_archivo,"w") as f:
        f.write(f"{n}\n")

        #Genera las preferencias de los hombres (H1, H2, ...)
        for i in range(1, n + 1):
            h_nombre = f"H{i}"
            #Genera la lista de preferencias de mujeras para el hombre de la iteración
            preferencias = [f"M{j}" for j in range(1 , n+1)]
            random.shuffle(preferencias)
            f.write(f"{h_nombre} " + " ".join(preferencias) + "\n")

        #Genera las preferencia de las mujeres (M1, M2, ...)
        for i in range(1, n+1):
            m_nombre= f"M{i}"
            #Genera la lista de preferencias de hombres para la mujer en la iteración
            preferencias = [f"H{j}" for j in range(1 , n+1)]
            random.shuffle(preferencias)
            f.write(f"{m_nombre} " + " ".join(preferencias) + "\n")
    print(f"Archivo {nombre_archivo} creado exitosamente.")


if __name__ == "__main__":
    print("Iniciando generación de archivos de prueba...")
    
    # Definimos 25 tamaños de N. 
    # Como la complejidad es O(N^2), haremos que N crezca 
    # para que la curva se vea clara en la gráfica.
    tamanos_n = [
        10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 
        150, 200, 250, 300, 350, 400, 450, 500, 
        600, 700, 800, 900, 1000, 1200, 1500
    ]
    
    # Usamos un bucle para llamar a la función 25 veces
    for i, n in enumerate(tamanos_n):
        id_archivo = i + 1
        generador_datos(n, id_archivo)
        
    print(f"\n¡Listo! Se han generado {len(tamanos_n)} archivos en la carpeta /DAT")

