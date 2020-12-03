X massiv berilgan Z massivga maniy elementlarni ko'chirib yozing!

a = [-1, 5, -6, 9, 11, -10]
b = []
for i in range(len(a)):
    if int(a[i]) < 0:
        b += [int(a[i])]
c = sorted(b, reverse=True)
print(c)
