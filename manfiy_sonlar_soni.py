#Uchta butun son kiritilsin kiritilgan sonlarni nechtasi manfiy ekani aniqlansin. 

def manfiy_sonlar_soni():
  a = int(input())
  b = int(input())
  c = int(input())
  manfiy_sonlar = 0
  sonlar = [a, b, c]
  for i in range(0,3):
      if sonlar[i] < 0:
          manfiy_sonlar += 1

  print(manfiy_sonlar)

manfiy_sonlar_soni()
