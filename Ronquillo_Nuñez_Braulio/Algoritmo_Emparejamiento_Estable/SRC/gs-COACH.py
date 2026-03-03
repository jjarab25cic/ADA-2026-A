import sys
from collections import deque

def gs(proposers, receivers):
    rank = {}
    for r, prefs in receivers.items():
        rank[r] = {p: i for i, p in enumerate(prefs)}

    free = deque(proposers.keys())
    engaged = {}  # receiver -> proposer
    nxt = {p: 0 for p in proposers}

    while free:
        p = free.popleft()
        i = nxt[p]
        if i >= len(proposers[p]):
            continue

        r = proposers[p][i]
        nxt[p] = i + 1

        if r not in engaged:
            engaged[r] = p
        else:
            p2 = engaged[r]
            if rank[r][p] < rank[r][p2]:
                engaged[r] = p
                free.append(p2)
            else:
                free.append(p)

    return engaged  # receiver -> proposer

def read_cases(lines):
    i = 0
    L = len(lines)
    while i < L:
        while i < L and not lines[i].strip():
            i += 1
        if i >= L:
            break

        first = lines[i].split()
        i += 1
        if len(first) < 2:
            break

        n = int(first[0])
        who = first[1]

        men = []
        for _ in range(n):
            while i < L and not lines[i].strip():
                i += 1
            men.append(lines[i].split())
            i += 1

        women = []
        for _ in range(n):
            while i < L and not lines[i].strip():
                i += 1
            women.append(lines[i].split())
            i += 1

        yield n, who, men, women

def solve_case(n, who, men_rows, women_rows):
    men_prefs = {row[0]: row[1:] for row in men_rows}
    women_prefs = {row[0]: row[1:] for row in women_rows}

    men_names = [row[0] for row in men_rows]

    if who == 'm':
        engaged = gs(men_prefs, women_prefs)  # woman -> man
        man_to_woman = {m: w for w, m in engaged.items()}
    else:
        engaged = gs(women_prefs, men_prefs)  # man -> woman
        man_to_woman = engaged

    # Salida por ORDEN ALFABÉTICO ?
    out = []
    for m in sorted(men_names):
        out.append(m + " " + man_to_woman[m])
    return out

def main():
    lines = sys.stdin.read().splitlines()
    out_all = []
    for n, who, men_rows, women_rows in read_cases(lines):
        out_all.extend(solve_case(n, who, men_rows, women_rows))
    sys.stdout.write("\n".join(out_all))

if __name__ == "__main__":
    main()