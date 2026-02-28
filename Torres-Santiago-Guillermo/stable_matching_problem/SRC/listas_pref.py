"""
    Generador de archivos de listas de preferencia para pruebas del algoritmo
    Implementacion del algoritmo de Gale-Shapley 
    Emparejamiento Estable   

    Centro de Investigacion en Computacion
    Analisis y Diseño de Algoritmos
    
    Torres Santiago Guillermo A260486
    Maestria en Ciencias en Ingenieria de Computo

    23/Febrero/2026 
"""

from __future__ import annotations

import argparse
import random
from pathlib import Path


def validar_entero_positivo(valor: str) -> int:
    numero = int(valor)
    if numero <= 0:
        raise argparse.ArgumentTypeError("El valor debe ser un entero positivo.")
    return numero


def crear_contenido_archivo(cantidad_parejas: int, rng: random.Random) -> list[str]:
    grupo_1 = list(range(1, cantidad_parejas + 1))
    grupo_2 = list(range(cantidad_parejas + 1, (2 * cantidad_parejas) + 1))

    lineas: list[str] = []

    for persona_1 in grupo_1:
        preferencias = rng.sample(grupo_2, k=cantidad_parejas)
        linea = " ".join([str(persona_1), *map(str, preferencias)])
        lineas.append(linea)

    for persona_2 in grupo_2:
        preferencias = rng.sample(grupo_1, k=cantidad_parejas)
        linea = " ".join([str(persona_2), *map(str, preferencias)])
        lineas.append(linea)

    return lineas


def generar_archivos(num_archivos: int, carpeta_destino: Path, semilla: int | None = None) -> None:
    rng = random.Random(semilla)
    carpeta_destino.mkdir(parents=True, exist_ok=True)

    for n_archivo in range(1, num_archivos + 1):
        cantidad_parejas = n_archivo**2
        lineas = crear_contenido_archivo(cantidad_parejas, rng)

        ruta_archivo = carpeta_destino / f"parejas{n_archivo}.txt"
        ruta_archivo.write_text("\n".join(lineas), encoding="utf-8")

        print(f"Creado: {ruta_archivo} | parejas={cantidad_parejas} | lineas={len(lineas)}")


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Genera archivos de listas de preferencia para el algoritmo de Gale-Shapley."
        )
    )
    parser.add_argument(
        "-n",
        "--num-archivos",
        type=validar_entero_positivo,
        required=True,
        help="Cantidad de archivos a generar.",
    )
    parser.add_argument(
        "-c",
        "--carpeta",
        default=r"D:\CIC\Programas\Algoritmos\gs_match\_gen_test",
        help=r"Carpeta donde se guardaran los archivos (por defecto: D:\CIC\Programas\Algoritmos\gs_match\_gen_test).",
    )
    parser.add_argument(
        "-s",
        "--semilla",
        type=int,
        default=None,
        help="Semilla opcional para reproducibilidad.",
    )
    return parser


def main() -> None:
    parser = construir_parser()
    args = parser.parse_args()

    generar_archivos(
        num_archivos=args.num_archivos,
        carpeta_destino=Path(args.carpeta),
        semilla=args.semilla,
    )


if __name__ == "__main__":
    main()
