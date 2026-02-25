# gen_instancias.py
import json
import random
from typing import Any

def gen_instancia(N: int, seed: int | None = None) -> dict[str, Any]:
    rng = random.Random(seed)
    proposers = [rng.sample(list(range(N)), N) for _ in range(N)]
    receivers = [rng.sample(list(range(N)), N) for _ in range(N)]
    return {"N": N, "proposers": proposers, "receivers": receivers}

def main():
    tamanos = [2, 4, 8, 16, 25, 50, 100, 200, 500, 1000]

    data = {
        "format": "stable-matching-indexed-v1",
        "instances": [gen_instancia(N, seed=i) for i, N in enumerate(tamanos)]
    }

    with open("instancias.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    print("OK: instancias.json generado.")

if __name__ == "__main__":
    main()