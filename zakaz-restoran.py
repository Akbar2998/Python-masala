tables = [
    {'number': 1, 'status': 'free'},
    {'number': 2, 'status': 'occupied'},
    {'number': 3, 'status': 'free'},
    {'number': 4, 'status': 'occupied'},
]

menu = {
    'burger': 10,
    'shawarma': 8,
    'pizza': 12,
    'salad': 5,
}

order_number = 1
total_sum = 0

while True:
    # Принимаем ввод от пользователя
    dish = input("Выберите фаст-фуд, который хотите заказать: ")
    if dish not in menu:
        print("Извините, такого блюда нет в меню.")
        continue
    
    # Выводим информацию о выбранном блюде
    print(f"Вы выбрали: {dish}")
    print(f"Стоимость: {menu[dish]}")
    
    # Добавляем стоимость блюда к общей сумме
    total_sum += menu[dish]
    
    # Ищем свободный столик
    table_found = False
    for table in tables:
        if table['status'] == 'free':
            table['status'] = 'occupied'
            table_found = True
            break
    
    # Если свободный столик найден, выводим информацию о заказе
    if table_found:
        print(f"Ваш заказ номер {order_number} был принят")
