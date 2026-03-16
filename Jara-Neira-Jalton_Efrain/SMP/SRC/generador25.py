import random

def generar_entrada(n, proponente='m', archivo='entrada1.txt'):
    hombres = [f"H{i}" for i in range(n)]
    mujeres = [f"M{i}" for i in range(n)]
    
    with open(archivo, 'w') as f:
        f.write(f"{n} {proponente}\n")
        
        for h in hombres:
            prefs = random.sample(mujeres, len(mujeres))
            f.write(f"{h} {' '.join(prefs)}\n")
            
        for m in mujeres:
            prefs = random.sample(hombres, len(hombres))
            f.write(f"{m} {' '.join(prefs)}\n")
            
    print(f"Archivo '{archivo}' generado con {n} parejas.")

for i in range(1, 26):
    n = 600*i
    nombre_archivo = f"entrada{i}.txt"
    generar_entrada(n, 'm', nombre_archivo)