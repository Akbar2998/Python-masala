def murakkab_son():
  a = int(input()) #sonni kiritamiz
  b = 0          #boshlang'ich
  for i in range(1, a):
      if a%i == 0: #har bir son uchun bo'linishni tekshirib ko'ramiz
          b = b + i
  if (b == a):
      print("Mukammal son ")
  else:
      print("Mukammal son emas")

murakkab_son()
