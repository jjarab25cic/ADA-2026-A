# gs_run.py
# Gale–Shapley (emparejamiento estable) optimizado para preferencias por índices (0..N-1).
# Mide tiempos por instancia dentro de un archivo JSON que contiene varias instancias.
#Ejecucion --> python gs.py instancias.json --warmup 1
from collections import deque
import json
import time
import argparse


def gale_shapley_idx(proposers_prefs: list[list[int]],
                     receivers_prefs: list[list[int]]) -> list[int]:
    """
    Devuelve match_p (tamaño N):
      match_p[p] = r  -> el proponente p queda emparejado con el receptor r.

    - proposers_prefs[p] es una permutación de 0..N-1 (orden de preferencia de p)
    - receivers_prefs[r] es una permutación de 0..N-1 (orden de preferencia de r)

    Complejidad: O(N^2).
    """
    N = len(proposers_prefs)

    # ranking[r][p] = qué tan bien prefiere r al proponente p (menor = mejor).
    # Esto vuelve la comparación O(1) cuando un receptor decide entre dos proponentes.
    ranking = [[0] * N for _ in range(N)]
    for r in range(N):
        for rank, p in enumerate(receivers_prefs[r]):
            ranking[r][p] = rank

    # next_idx[p] = índice de la siguiente persona a la que p le va a proponer
    # Así evita reintentar propuestas ya hechas
    next_idx = [0] * N

    # engaged_to[r] = proponente actualmente aceptado por el receptor r (-1 si está libre)
    engaged_to = [-1] * N

    # match_p[p] = receptor asignado a p (-1 si p está libre)
    match_p = [-1] * N

    # Cola de proponentes libres: solo procesa a los que están libres.
    free = deque(range(N))

    while free:
        p = free.popleft()
        i = next_idx[p]
        if i >= N:
            continue

        # p propone a su siguiente receptor preferido
        r = proposers_prefs[p][i]
        next_idx[p] = i + 1  # avanza para la próxima vez

        p2 = engaged_to[r]  # pareja actual de r (si existe)

        if p2 == -1:
            # r estaba libre: acepta a p
            engaged_to[r] = p
            match_p[p] = r
        else:
            # r ya tiene pareja: decide si prefiere al nuevo p sobre p2
            if ranking[r][p] < ranking[r][p2]:
                # r prefiere a p: cambia de pareja
                engaged_to[r] = p
                match_p[p] = r

                # p2 queda libre y regresa a la cola
                match_p[p2] = -1
                free.append(p2)
            else:
                # r rechaza a p: p sigue libre y volverá a intentar con su siguiente opción
                free.append(p)

    return match_p


def bench_file(path: str, warmup: int = 0) -> None:
    """
    Lee un JSON con varias instancias y reporta tiempo de ejecución por instancia.

    Formato esperado:
      {
        "instances": [
          {"N": ..., "proposers": [[...], ...], "receivers": [[...], ...]},
          ...
        ]
      }
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    instances = data["instances"]

    # este calentamiento se ejecuta para estabilizar el entorno 
    for _ in range(max(0, warmup)):
        for inst in instances:
            gale_shapley_idx(inst["proposers"], inst["receivers"])

    # Encabezado de tabla
    print(f"{'Instancia':>9} {'N':>6} {'Tiempo (s)':>12} {'Tiempo (ms)':>12}")
    print("-" * 55)

    # tiempo = final - inicial
    for idx, inst in enumerate(instances):
        N = inst["N"]
        proposers = inst["proposers"]
        receivers = inst["receivers"]

        t0 = time.perf_counter()
        _ = gale_shapley_idx(proposers, receivers)
        t1 = time.perf_counter()

        secs = t1 - t0
        print(f"{idx:>9} {N:>6} {secs:>12.6f} {secs * 1000:>12.3f}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "file",
        nargs="?",
        default="instancias.json",
        help="Archivo JSON con instancias (default: instancias.json)"
    )
    ap.add_argument(
        "--warmup",
        type=int,
        default=0,
        help="Repeticiones de warmup (default: 0)"
    )
    args = ap.parse_args()

    bench_file(args.file, warmup=args.warmup)


if __name__ == "__main__":
    main()