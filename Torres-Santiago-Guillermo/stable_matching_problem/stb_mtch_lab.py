"""
    Implementacion del algoritmo de Gale-Shapley 
    Emparejamiento Estable   
    Pruebas de complejidad 
    Mediciones de tiempo y guardar en excel

    Centro de Investigacion en Computacion
    Analisis y Diseño de Algoritmos
    
    Torres Santiago Guillermo A260486
    Maestria en Ciencias en Ingenieria de Computo

    23/Febrero/2026 
"""
import argparse
import time
import pandas as pd
from pathlib import Path
import re

# --------------------------------- Algoritmo Gale - Shapley ------------------------------
def stable_match(pref_1, pref_2):

    personas_libres = list(pref_1.keys()) # Guardar en lista 
    propuesta = {p1: 0 for p1 in pref_1}  # Guardar propuesta actual
    parejas_hechas = {}

    p2_rank = {}
    for p2, prefs in pref_2.items():
        p2_rank[p2] = {p1: rank for rank, p1 in enumerate(prefs)}   # Asignar un valor a cada preferencia

    while personas_libres:
        p1 = personas_libres[0]             # Primera persona de la lista
        p2 = pref_1[p1][propuesta[p1]]      # Persona a proponer, para persona 1
        propuesta[p1] += 1                  # Actualizar propuesta actual

        if p2 not in parejas_hechas:        
            parejas_hechas[p2] = p1         # Crear pareja
            personas_libres.pop(0)          # Quitar de lista a la persona
        else: 
            
            pareja_actual = parejas_hechas[p2]  

            if p2_rank[p2][p1] < p2_rank[p2][pareja_actual]:    # Revisar si prefiere la nueva pareja
                parejas_hechas[p2] = p1                         # Cambiar por la nueva pareja
                personas_libres.pop(0)                          
                personas_libres.append(pareja_actual)           

    matches = {p1: p2 for p2, p1 in parejas_hechas.items()}     # Reordenar las parejas, P1 - P2
    return matches

# ------------------------------ Leer el numero de archivo --------------------------
def obtener_indice_archivo(path_archivo: Path, total_hombres: int) -> int:
    match = re.search(r"(\d+)$", path_archivo.stem)
    if match:
        return int(match.group(1))
    return total_hombres

# ----------------------------------- MAIN ------------------------------------------
pref_hombres = {}
pref_mujeres = {}
parejas = {}

#nf = input("Numero de Archivo: ")

t1 = time.time()    # Tiempo Inicial

parser = argparse.ArgumentParser()
parser.add_argument("--archivo", required=True)
args = parser.parse_args()
path_archivo = Path(args.archivo)


with open(path_archivo, "r") as t:
    datos_list = t.read().splitlines()
t.close()

#with open(f"D:/parejas/parejas{nf}.txt", "r") as t:
    #datos_list = t.read().splitlines()
#t.close()

np = len(datos_list)

t2 = time.time()

for jk in range(np):
        
        nombre_pref = datos_list[jk].split(" ")    # Separar nombres y guardar en arreglo
        nombre = nombre_pref[0]
        preferencias = nombre_pref[1:]
        if jk <= (np/2)-1:
            pref_hombres.update({nombre:preferencias})
        else:
            pref_mujeres.update({nombre:preferencias})

t3 = time.time()

parejas = stable_match(pref_hombres,pref_mujeres)

t4 = time.time()




for h in pref_hombres:  # Imprimir resultado en el orden de los hombres
        print(f"{h} {parejas[h]}")

t5 = time.time()    # Timepo Final

t_total = t5 - t1
t_leer = t2 - t1
t_lista = t3 - t2
t_stbl = t4 - t3
t_impr = t5 - t4



df = pd.read_excel(r"D:\CIC\Programas\Algoritmos\time_stb_mtch.xlsx",sheet_name="tiempos")

nf = obtener_indice_archivo(path_archivo, total_hombres=len(pref_hombres))
# Ejemplo: Crear y escribir en un archivo
with open(f"D:/CIC/Programas/Algoritmos/gs_match/stable_matching_problem/Resultados/resultados{nf}.txt", "w") as archivo:
    for h in pref_hombres:  # Imprimir resultado en el orden de los hombres 
        archivo.write(f"{h} {parejas[h]}\n")
        
    

df.loc[len(df)] = [int(nf),t_total,t_leer,t_lista,t_stbl,t_impr]
df.to_excel(r"D:\CIC\Programas\Algoritmos\time_stb_mtch.xlsx", index=False, sheet_name='tiempos')
print("----------- FIN -----------")