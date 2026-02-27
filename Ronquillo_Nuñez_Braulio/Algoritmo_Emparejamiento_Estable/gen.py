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
    tamanos = [
      32,
    64,
    128,
    256,
    384,
    512,
    640,
    768,
    896,
    1024,
    1200,
    1400,
    1600,
    1800,
    1900,
    2000
]

    data = {
        "format": "stable-matching-indexed-v1",
        "instances": [gen_instancia(N, seed=i) for i, N in enumerate(tamanos)]
    }

    with open("instancias.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    print("OK")

if __name__ == "__main__":
    main()