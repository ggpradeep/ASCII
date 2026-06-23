n = int(input("How big do you want your triangle to be?"))
for i in range(n, 0, -1):
    for j in range(i):
        i = i - 1
        print("*",end="")
    print()