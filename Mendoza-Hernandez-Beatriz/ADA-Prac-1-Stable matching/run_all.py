import subprocess
import os
import csv
import sys
import matplotlib.pyplot as plt
import pandas as pd

# ======================================
# CONFIGURACIÓN
# ======================================
INPUT_FOLDER = "inputs"
OUTPUT_CSV = "results.csv"

IMG_LINEAR = "growth_linear.png"
IMG_LOG = "growth_loglog.png"

PYTHON_EXEC = sys.executable
SCRIPT = "stable-matching.py"


# ======================================
# EXTRAER LINEA TIMES
# ======================================
def extraer_times(output):

    for line in output.splitlines():
        if line.startswith("TIMES"):
            parts = line.strip().split(",")

            return (
                int(parts[1]),
                float(parts[2]),
                float(parts[3]),
                float(parts[4]),
                float(parts[5]),
            )

    raise ValueError("TIMES lines not found")


# ======================================
# Execute algorithm 

print("\nRunning experiments...\n")

resultados = []

archivos = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".txt")]

# ordenar por N automáticamente
archivos.sort(key=lambda x: int(x.split("_N")[1].replace(".txt", "")))

for archivo in archivos:

    ruta = os.path.join(INPUT_FOLDER, archivo)
    print("Running:", archivo)

    with open(ruta, "r") as entrada:

        proceso = subprocess.run(
            [PYTHON_EXEC, SCRIPT],
            stdin=entrada,
            capture_output=True,
            text=True
        )

    if proceso.returncode != 0:
        print("Error:", proceso.stderr)
        continue

    try:
        datos = extraer_times(proceso.stdout)
        resultados.append(datos)
    except Exception as e:
        print("Times could not be read:", archivo)
        print(proceso.stdout)


# ======================================
# GUARDAR CSV
# ======================================
resultados.sort()

with open(OUTPUT_CSV, "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "N",
        "Reading_Time",
        "Algorithm_Time",
        "Printing_Time",
        "Total_Time"
    ])

    writer.writerows(resultados)

print("\nCSV generado:", OUTPUT_CSV)


# ======================================
# LEER CSV
# ======================================
df = pd.read_csv(OUTPUT_CSV)

N = df["N"]
read_t = df["Reading_Time"]
algo_t = df["Algorithm_Time"]
print_t = df["Printing_Time"]
total_t = df["Total_Time"]


# ======================================
# GRÁFICA LINEAL
# ======================================
plt.figure()

plt.plot(N, read_t, marker='o', label="Reading")
plt.plot(N, algo_t, marker='o', label="Algorithm")
plt.plot(N, print_t, marker='o', label="Printing")
plt.plot(N, total_t, marker='o', label="Total")

plt.xlabel("Input Size (N)")
plt.ylabel("Time (seconds)")
plt.title("Stable Matching Execution Time (Linear Scale)")

plt.legend()
plt.grid(True)

plt.savefig(IMG_LINEAR, dpi=300)
plt.close()

print("Graph Linear created:", IMG_LINEAR)


# ======================================
# GRÁFICA LOG
# ======================================
plt.figure()

plt.loglog(N, algo_t, marker='o')

plt.xlabel("log(N)")
plt.ylabel("log(Time)")
plt.title("Log-Log Growth of Gale-Shapley Algorithm")

plt.grid(True, which="both", linestyle="--")

plt.savefig(IMG_LOG, dpi=300)
plt.close()

print("Graph Log created:", IMG_LOG)

print("\n✅ EXPERIMENT FINISHED")