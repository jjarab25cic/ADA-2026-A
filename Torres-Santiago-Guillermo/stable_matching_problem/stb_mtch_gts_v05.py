"""
    Implementacion del algoritmo de Gale-Shapley 
    Emparejamiento Estable    

    Centro de Investigacion en Computacion
    Analisis y Diseño de Algoritmos
    
    Torres Santiago Guillermo A260486
    Maestria en Ciencias en Ingenieria de Computo

    24/Febrero/2026 
"""

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
    

# -------------------------- Crear listas de preferencias ----------------------------
def listas_preferencia(parejas):
    pref_list = {}
    
    for jk in range(parejas): 
        persona=input()
        
        nombre_pref = persona.split(" ")    # Separar nombres y guardar en arreglo
        nombre = nombre_pref[0]             
        preferencias = nombre_pref[1:]

        pref_list.update({nombre:preferencias})
    return pref_list

# ----------------------------------- MAIN ------------------------------------------
pref_hombres = {}
pref_mujeres = {}
parejas = {}

cadena1 = input() #Numero de parejas y quien elige primero
cadena2 = cadena1.split(" ")
np = int(cadena2[0])    # Guardar numero de parejas
proponer = cadena2[1].upper()   # Guarda quien se propone primero, Hombres(M) o mujeres(W)

pref_hombres = listas_preferencia(np)   # Leer nombres y preferencias
pref_mujeres = listas_preferencia(np)

if proponer == "M":
    parejas = stable_match(pref_hombres,pref_mujeres)   # Ejecutar algoritmo
elif proponer == "W":
    parejas = stable_match(pref_mujeres,pref_hombres)


if proponer == "M":
    for h in pref_hombres:  # Imprimir resultado en el orden de los hombres
        print(f"{h} {parejas[h]}")
elif proponer == "W":
    for m in pref_mujeres:  # Imprimir resultado en el orden de las mujeres
        print(f"{m} {parejas[m]}")
