# Algoritmo Gale-Shapley (GS) 
import json
import random

tamanos = [2,4,8,16,25,50,100,200,500,1000]

for idx, N in enumerate(tamanos):
    hombres = {f"Hombre_{i+1}": random.sample([f"M{j+1}" for j in range (N)],N) for i in range(N)}
    mujeres = {f"Mujer_{i+1}": random.sample([f"H{j+1}" for j in range (N)],N) for i in range(N)}

    datos = {
        "hombres": hombres,"mujeres": mujeres}

    with open(f"archivo_{idx}.json", "w") as f:
        json.dump(datos, f, indent=4)

print("Archivos JSON generados exitosamente.")


