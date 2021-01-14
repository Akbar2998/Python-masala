# 2ta variant avvalgi kodimni optimizatsiya qilib ko'rdim
# Masalan, 30 dan kam sonlarni ko'rib chiqamiz. Dastlab 2 oddiy deb belgilanadi, so'ngra 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28 va 30 chiziladi ya'ni bu sonlar 
# Keyingi 3 oddiy deb ko'rsatiladi, so'ngra 6, 9, 12, 15, 18, 21, 24, 27 va 30 chiziladi.
# Keyingi zarba 5 ga teng, shuning uchun 10, 15, 20, 25 va 30 chiziladi. Va boshqalar. Raqamlar o'zgarishsiz qoladi: 2, 3, 5, 7, 11, 13, 17, 19, 23 va 29
# 1 - variant
a = int(input())
S = [2]
for i in range(3,a+1,2):
    b = 2
    while i%b > 0:
        b += 1
        if b == i:
            S += [i]
print(S)
# 2 - variant
def tub_sonlar(n):
    rezultat = list()
    qator = [True] * (n+1)
    for i in range(2, n+1):
        if (qator[i]):
            out.append(i)
            for x in range(i, n+1, i):
                qator[x] = False
    return rezultat  
tub_sonlar(1000000)
