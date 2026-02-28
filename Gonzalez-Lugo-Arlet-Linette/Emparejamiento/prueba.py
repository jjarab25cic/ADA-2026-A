def gale_shapley(preferencias_hombres, preferencias_mujeres, hombres, mujeres, propone):
    n = len(hombres)
    h_id = {h: i for i, h in enumerate(hombres)}
    m_id = {m: i for i, m in enumerate(mujeres)}
    pref_h = [[m_id[m] for m in pref] for pref in preferencias_hombres]
    pref_m = [[h_id[h] for h in pref] for pref in preferencias_mujeres]
    pareja_h = [-1] * n
    pareja_m = [-1] * n
    libres = list(range(n))
    siguiente = [0] * n

    if propone == 'm':          
        while libres:
            h = libres[0]
            m = pref_h[h][siguiente[h]]
            siguiente[h] += 1

            if pareja_m[m] == -1:
                pareja_m[m] = h
                pareja_h[h] = m
                libres.pop(0)

            else:
                h_actual = pareja_m[m]
                if pref_m[m].index(h) < pref_m[m].index(h_actual):
                    pareja_m[m] = h
                    pareja_h[h] = m
                    pareja_h[h_actual] = -1
                    libres.pop(0)
                    libres.append(h_actual)

    else:                      
        while libres:
            m = libres[0]
            h = pref_m[m][siguiente[m]]
            siguiente[m] += 1

            if pareja_h[h] == -1:
                pareja_h[h] = m
                pareja_m[m] = h
                libres.pop(0)

            else:
                m_actual = pareja_h[h]
                if pref_h[h].index(m) < pref_h[h].index(m_actual):
                    pareja_h[h] = m
                    pareja_m[m] = h
                    pareja_m[m_actual] = -1
                    libres.pop(0)
                    libres.append(m_actual)

    return pareja_h, pareja_m


def main():
    n, propone = input().split()
    n = int(n)
    propone = propone.lower()

    hombres = []
    mujeres = []
    pref_h = []
    pref_m = []


    for _ in range(n):
        partes = input().split()
        hombres.append(partes[0])
        pref_h.append(partes[1:])

    for _ in range(n):
        partes = input().split()
        mujeres.append(partes[0])
        pref_m.append(partes[1:])

    pareja_h, pareja_m = gale_shapley(pref_h, pref_m, hombres, mujeres, propone)
    
    if propone == 'm':
        for i in range(n):                 
            if pareja_h[i] != -1:
                print(hombres[i], mujeres[pareja_h[i]])
    else:
        for i in range(n):                 
            if pareja_m[i] != -1:
                print(mujeres[i], hombres[pareja_m[i]])


if __name__ == "__main__":
    main()