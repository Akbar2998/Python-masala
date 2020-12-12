def mmf():
    print("A intervalning oraliqlarini kiriting: ")
    a = int(input("a = "))
    b = int(input("b = "))
    A = [a, b]
    print("A",A)
    print("B intervalning oraliqlarini kiriting: ")
    c = int(input("c = "))
    d = int(input("d = "))
    B = [c, d]
    print("B",B)
    print("\n")
    print("A + B = ", [(a+c),(b+d) ])
    print("A - B = ", [(a - d), (b - c)])
    print("A * B = ", [(a * c), (b * d)])
    print("A / B = ", [(a / d), (b / c)])

mmf()
