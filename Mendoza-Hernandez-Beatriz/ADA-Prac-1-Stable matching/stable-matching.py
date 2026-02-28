import time
import sys


# -------------------------------------------------
# Gale-Shapley
# -------------------------------------------------
def gale_shapley(proposers_preferences, receivers_preferences):

    free = list(proposers_preferences.keys())
    engaged = {}  # receiver -> proposer
    proposals_count = {p: 0 for p in proposers_preferences}

    ranking = {
        r: {person: i for i, person in enumerate(prefs)}
        for r, prefs in receivers_preferences.items()
    }

    while free:
        p = free[0]

        # protección importante
        if proposals_count[p] >= len(proposers_preferences[p]):
            free.remove(p)
            continue

        r = proposers_preferences[p][proposals_count[p]]
        proposals_count[p] += 1

        if r not in engaged:
            engaged[r] = p
            free.remove(p)

        else:
            current = engaged[r]

            if ranking[r][p] < ranking[r][current]:
                engaged[r] = p
                free.remove(p)
                free.append(current)

    return engaged
# -------------------------------------------------
# 1️⃣ MEDIR LECTURA
# -------------------------------------------------
read_start = time.perf_counter()

first_line = sys.stdin.readline().split()
N = int(first_line[0])
first = first_line[1]

men_preferences = {}
women_preferences = {}

# IMPORTANTE: usar readline (NO input)
for _ in range(N):
    data = sys.stdin.readline().split()
    men_preferences[data[0]] = data[1:]

for _ in range(N):
    data = sys.stdin.readline().split()
    women_preferences[data[0]] = data[1:]

read_end = time.perf_counter()
read_time = read_end - read_start


# -------------------------------------------------
# 2️⃣ MEDIR ALGORITMO
# -------------------------------------------------
algo_start = time.perf_counter()

if first == 'm':
    # hombres proponen
    engaged = gale_shapley(men_preferences, women_preferences)

    # convertir a proposer -> pareja
    matches = {man: woman for woman, man in engaged.items()}
    output_order = men_preferences.keys()

else:
    # mujeres proponen
    engaged = gale_shapley(women_preferences, men_preferences)

    # engaged = {hombre : mujer}
    matches = {woman: man for man, woman in engaged.items()}
    output_order = women_preferences.keys()

algo_end = time.perf_counter()
algo_time = algo_end - algo_start


# -------------------------------------------------
# 3️⃣ MEDIR IMPRESIÓN
# -------------------------------------------------
print_start = time.perf_counter()

for proposer in output_order:
    print(proposer, matches[proposer])

print_end = time.perf_counter()
print_time = print_end - print_start


# -------------------------------------------------
# 4️⃣ OUTPUT DE TIEMPOS (PARSEABLE)
# -------------------------------------------------
total_time = read_time + algo_time + print_time

print("TIMES,"
      f"{N},"
      f"{read_time:.8f},"
      f"{algo_time:.8f},"
      f"{print_time:.8f},"
      f"{total_time:.8f}")