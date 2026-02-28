import random
import os
from pathlib import Path

base_dir = Path(__file__).parent
folder = base_dir / "Files"
folder.mkdir(parents=True, exist_ok=True)

print("Ingresa el número base de parejas ")
numBase = int(input())
print("Ingresa el número de archivos a generar: ")
numFiles = int(input())
print("Que tipo de crecimiento deseas\n" \
"1. Lineal\n" \
"2. Logaritmica")
scale = int(input())
factor = 1;


if scale == 1:
    print("Ingresa el intervalo entre cada archivo: ")
    interval= int(input())
else:
    print("Ingresa el factor de crecimiento: ")
    factor = float(input())
    #print(os.getcwd())

def generateFile(fileNumber, scale):
    numPairs=0
    if scale == 1:
        numPairs = numBase+(fileNumber*interval)
    else:
        numPairs = int(numBase * (factor ** fileNumber))
    values1 = list(range(numPairs))
    values2 = list(range(numPairs, numPairs*2))
    fileName = folder / f"File_{fileNumber}.txt"
    
    print(fileName)
    #print(type(fileName))

    with open(fileName, "w") as f:
        f.write(f"{numPairs} m\n")
        group1 = {}
        group2 = {}

        for person in values1:
            pref = values2[:]
            random.shuffle(pref)
            group1[person] = pref
            f.write(str(person) + " " + " ".join(map(str, pref)) + "\n")

        for person in values2:
            pref = values1[:]
            random.shuffle(pref)
            group2[person] = pref
            f.write(str(person) + " " + " ".join(map(str, pref)) + "\n")
        #print(f"range group 1: {group1}")
        #print(f"range group 1: {group2}")

for i in range(numFiles):
    generateFile(i, scale)
print(f"{numFiles} archivos creados")