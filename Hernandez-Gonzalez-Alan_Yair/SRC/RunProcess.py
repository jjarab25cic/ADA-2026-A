import subprocess
import matplotlib.pyplot as plt
from collections import defaultdict

from pathlib import Path
base_dir = Path(__file__).parent
#Los programas se deben encontrar en la misma ruta que la carpeta Files
folder = base_dir / "Files"

file_program = base_dir / "StableMatchingProblem.py"

files = sorted(
    folder.glob("*.txt"),
    key=lambda x: int(x.stem.split("_")[1])
)

def runFile(fileName):
    file_path = Path(folder) / fileName
    input_data = file_path.read_text()
    result = subprocess.run(
        ["python3", file_program],
        input=input_data,
        text=True,
        capture_output=True
    )
    '''
    print("STDOUT:")
    print(result.stdout)

    print("STDERR:")
    print(result.stderr)
    '''

print("Qué operación deseas realizar?\n" \
"1. Correr algoritmo \n" \
"2. Graficar resultados")
operation = int(input())



if operation == 1:
    print("Ingresa el número de veces que quieres ejecutar cada archivo: ")
    rep = int(input())
    for file_path in files:
        print(file_path.name)
        for _ in range(rep):
            runFile(file_path.name)
if operation == 2:
    print("Ingresa el nombre del archivo a graficar")
    fileToGraph = input()
    executionTimes = Path(base_dir) / fileToGraph
    # Leer archivo
    datos = defaultdict(list)

    with open(executionTimes, "r", encoding="cp1252") as f:
        next(f)  # saltar encabezado
        for linea in f:
            n, tiempo = linea.strip().split(",")
            datos[int(n)].append(float(tiempo))

    tamanos = sorted(datos.keys())
    promedios = [sum(datos[n]) / len(datos[n]) for n in tamanos]

    plt.figure()
    plt.plot(tamanos, promedios)
    plt.xlabel("Número de parejas")
    plt.ylabel("Tiempo promedio (segundos)")
    plt.title("Tiempo promedio vs Número de parejas")
    plt.grid(True)
    plt.show()