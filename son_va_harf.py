# Gap berilgan shunda faqat son va harf qatnashgan so'zlarni output qilish kerak
soz = "Bugun sana 20yanvar havo 10C iliq "
str1 = soz.split()

for i in str1:
    a = 0
    b = 0
    for x in i:
        if x in "1234567890":
            b += 1
        if x.lower() in "qwertyuiopasdfghjklzxcvbnm" :
            a += 1            
    if  a > 0 and b > 0:
        print(i)
