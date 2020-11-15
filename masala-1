
#Faqat 3 va 7 dan tashkil topgan, raqamlari yig‘indisi ham, o‘zi ham 3 va 7 ga bo‘linadigan eng kichik sonni toping.

import itertools
e = input("Sonni kiriting : ")
f = input("Sonni kiriting : ")
d = int(input("Qatorni kiriting : "))
a = int(e)
b = int(f)
c = 10*a+b
for i in itertools.product(str(c), repeat=d):
    x = (''.join(i)) #sonlar_kombinatsiyasi
    y = (sum(map(int,str(x))))  #raqamlar_yig'indisi
    if ((y%a == 0 and y%b==0) and ((int(x))%a == 0 and (int(x))%b == 0)):
        print(x)
