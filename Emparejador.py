"""
Este script realiza el algoritmo de Stable matching
"""
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

if __name__ == "__main__":
    # Prueba rápida con un ejemplo pequeño
    ejemplo_h = {'H1': ['M1', 'M2'], 'H2': ['M1', 'M2']}
    ejemplo_m = {'M1': ['H2', 'H1'], 'M2': ['H1', 'H2']}
    
    resultado = generador_emparejamiento(ejemplo_h, ejemplo_m)
    print("Parejas formadas:", resultado)