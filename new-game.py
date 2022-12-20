import random
import math
ochko = 0

# Функция для генерации случайного числа в диапазоне 0-1000
def generate_number():
    return random.randint(0, 1000)

def xrad():
    return (random.randint(0,1000))**(1/2)
# Функция для генерации случайного математического выражения
def generate_math_expression():
    
    math_expressions = [math.sqrt(xrad()),  math.pi , xrad()]
    return random.choice(math_expressions)

# Функция для генерации случайной дроби
def generate_fraction():
    numerator = random.randint(1, 1000)
    denominator = random.randint(1, 1000)
    kasr = numerator/denominator
    return kasr

# Игра длится 10 повторений
for i in range(10):
    # Генерируем случайные числа
    number1 = generate_number()
    number2 = generate_math_expression()
    number3 = generate_fraction()

    # Выводим сгенерированные числа для выбора игроком
    print(f'1. {number1}')
    print(f'2. {number2}')
    print(f'3. {number3}')

    # Получаем выбор игрока
    choice = int(input('Sonni tanlang: '))

    # Проверяем, какое число выбрал игрок
    if choice == 1:
        selected_number = (number1)
    elif choice == 2:
        selected_number = (number2)
    elif choice == 3:
        selected_number = (number3)
    if selected_number == max(max(number1,(number2)),(number3)):
        ochko += 1
print(f'Sizn {ochko} topladingiz!' ) 
