def murakkab_son():
  a = int(input())
  b = 2          # 2dan boshlanadi bo'lish chunki tub son 1 va o'ziga bo'linadi
  while a%b != 0:
      b = b + 1   #agar shartni qanoatlantirsa 1taga ortib ketaveradi
  if a == b:      # oxir oqibat hech qaysi songa bo'linmasa demak bu tub son b==a ga teng bo'lganda
      print("Tub son")
  else:
      print("Murakkab son")

murakkab_son()
