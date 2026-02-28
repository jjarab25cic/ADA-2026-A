import sys
# Author: Alejandro Neftali Vazquez de la Rosa	
# Date: 23/02/2026 
def generador_emparejamiento(pref_hombres, pref_mujeres):
    # --- 1. PRE-PROCESAMIENTO (Ranking Inverso) ---    
    # Se crea un ranking inverso para que las mujeres comparen pretendientes al instante
    # Se le llama ranking "inverso" (o a veces "mapa de prioridades") porque se invierte la forma en que se accede
    # a la información de la lista de preferencias.
    #En lugar de que la relación sea Posición → Nombre hace que sea Nombre → Posición de modo que en lugar de recorrer la lista
    #solo compare los valores que tiene asignados
    ranking_mujeres = {}
    for mujer, preferencias in pref_mujeres.items():
        # ranking_mujeres['M1'] = {'H2': 0, 'H1': 1, ...}
        ranking_mujeres[mujer] = {hombre: posicion for posicion, hombre in enumerate(preferencias)}

    # --- 2. INICIALIZACIÓN ---
    # Todos los hombres comienzan solteros
    hombres_libres = list(pref_hombres.keys())
    
    # Almacena quién es el novio actual de cada mujer
    pareja_de_mujer = {} 
    
    # Almacena a qué mujer le toca proponerle cada hombre (índice de su lista)
    sig_propuesta_hombre = {h: 0 for h in pref_hombres}

    # --- 3. CICLO DE PROPUESTAS (Aceptación Diferida) ---
    while hombres_libres:
        # Extraemos al primer hombre de la lista de solteros hasta que no haya ninguno
        h = hombres_libres.pop(0)
        
        # El hombre elige a la siguiente mujer más preferida en su lista
        lista_opciones = pref_hombres[h]
        m = lista_opciones[sig_propuesta_hombre[h]]
        sig_propuesta_hombre[h] += 1
        
        # CASO A: La mujer está soltera
        if m not in pareja_de_mujer:
            pareja_de_mujer[m] = h
        
        # CASO B: La mujer ya tiene pareja, debe comparar y elegir
        else:
            hombre_actual = pareja_de_mujer[m]
            
            # Consultamos los rankings (un número menor es una preferencia más alta)
            if ranking_mujeres[m][h] < ranking_mujeres[m][hombre_actual]:
                # La mujer prefiere al nuevo pretendiente: cambia de pareja
                pareja_de_mujer[m] = h
                # El novio anterior vuelve a estar soltero
                hombres_libres.append(hombre_actual)
            else:
                # La mujer prefiere a su novio actual: rechaza al nuevo
                hombres_libres.append(h)

    # --- 4. RESULTADO FINAL ---
    # Convertimos de {mujer: hombre} a {hombre: mujer} para la entrega
    return {h: m for m, h in pareja_de_mujer.items()}

def solucionar_tarea():
    # Leer primera línea: N y quién propone
    entrada = sys.stdin.read().splitlines()
    if not entrada: return
    
    primera_linea = entrada[0].split()
    n = int(primera_linea[0])
    quien_propone = primera_linea[1] # 'm' o 'w'

    pref_hombres = {}
    pref_mujeres = {}
    orden_hombres = [] # Para respetar el orden de salida solicitado
    orden_mujeres = []  # Para respetar el orden de salida solicitado

    # Leer bloque de hombres (N líneas)
    for i in range(1, n + 1):
        datos = entrada[i].split()
        nombre_h = datos[0]
        preferencias = datos[1:]
        pref_hombres[nombre_h] = preferencias
        orden_hombres.append(nombre_h)

    # Leer bloque de mujeres (N líneas)
    for i in range(n + 1, 2 * n + 1):
        datos = entrada[i].split()
        nombre_m = datos[0]
        preferencias = datos[1:]
        pref_mujeres[nombre_m] = preferencias
        orden_mujeres.append(nombre_m)

    # DETERMINAR QUIÉN PROPONE
    if quien_propone == 'm':
        # Los hombres proponen, las mujeres reciben
        parejas = generador_emparejamiento(pref_hombres, pref_mujeres)
        # SALIDA: Imprimir pares en el orden de los hombres
        for h in orden_hombres:
            print(f"{h} {parejas[h]}")
    else:
        # Las mujeres proponen, los hombres reciben
        # El resultado será {mujer: hombre}
        parejas = generador_emparejamiento(pref_mujeres, pref_hombres)
        # SALIDA: Imprimir pares en el orden de los hombres
        for m in orden_mujeres:
            print(f"{m} {parejas[m]}")



if __name__ == "__main__":
    solucionar_tarea()
 