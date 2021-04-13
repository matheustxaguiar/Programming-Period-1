def f_piramide(i, n):
    for x in range(i, n + 1):
        for j in range(x):
            print(f"{i} ", end="")
            if i == 1:
                i = 0
            else:
                i = 1
        print()
