import gen_file   # importa tu archivo

def make_file(num_file,g):
    for i in range(num_file):
        # Llamar a la función gen_file.generate
        n = i*300
        h, m = gen_file.generate(n)
        data = gen_file.merch_file(g,h,m)
        gen_file.guardar(f'd{i+1}.txt', data)

def make_one_file(i, g):
    n = 2 ** i

    h, m = gen_file.generate(n)
    data = gen_file.merch_file(g, h, m)
    gen_file.guardar(f'd{i+1}.txt', data)

    return n

def main():
    g = input("genero que empieza? ").upper()
    num_file = int(input("numero de archivos: "))
    data = make_file(num_file, g)

if __name__=="__main__":
    main()