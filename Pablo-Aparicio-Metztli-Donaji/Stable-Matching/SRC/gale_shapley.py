def matching(first_preferences, second_preferences, verbose=True):
    sad = {}
    asker = {}
    rank = {}
    couples = {}
    
    sad = list(first_preferences.keys())
    asker = {m: 0 for m in first_preferences}

    rank = {
        w: {m: i for i , m in enumerate(prefers)}
        for w , prefers in second_preferences.items()
        }

    while sad:
        first = sad.pop(0)

        if asker[first] >= len(first_preferences[first]):
            continue

        second = first_preferences[first][asker[first]]
        asker[first] += 1

        if second not in couples:
            couples[second] = first

        else:
            no_sad = couples[second]

            if rank[second][first] < rank[second][no_sad]:
                couples[second] = first
                sad.append(no_sad)
            else:
                sad.append(first)
    
    match = {v: k for k, v in couples.items()}
    for k in sorted(match):
        # imprimir en orden alfabético
        x = (k, match[k])
    
    if verbose:
        for k in sorted(match):
            x = (k, match[k])

def main():
    n, gender = input().split()
    n = int(n)

    # Leer preferencias del grupo A
    first_preferences = {}
    for _ in range(n):
        line = input().split()
        nombre = line[0]
        preferencias = line[1:]
        first_preferences[nombre] = preferencias

    # Leer preferencias del grupo B
    second_preferences = {}
    for _ in range(n):
        line = input().split()
        nombre = line[0]
        preferencias = line[1:]
        second_preferences[nombre] = preferencias

    if gender.upper() == 'M':
        matching(first_preferences,second_preferences)
    elif gender.upper() == 'W':
        matching(second_preferences,first_preferences)
    else:
        print("Error de entrada")

if __name__=="__main__":
    main()