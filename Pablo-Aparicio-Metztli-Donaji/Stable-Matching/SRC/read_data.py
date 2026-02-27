from pathlib import Path

#Ruta de archivos
SRC_DIR = Path(__file__).resolve().parent
base_dir = SRC_DIR.parent
base = base_dir / "DAT" 

def leer_preferencias(ruta):
    datos = {}

    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()   # quita \n

            if not linea:
                continue           # salta líneas vacías
            nombre, prefs = linea.split(":")
            lista = prefs.strip().split(", ")
            datos[nombre.strip()] = lista
            
    return datos

def main():
    num_file = int(input("numero de archivos: "))
    for i in range(num_file):
        name = f'd{i+1}.txt'
        new_ruta = base / name
        data = leer_preferencias(new_ruta)

if __name__=="__main__":
    main()