import matplotlib.pyplot as plt

# словарь с данными о жильцах
residents = {
    "John Smith": {"nationality": "USA", "room": 1},
    "Mary Jones": {"nationality": "UK", "room": 2},
    "Ali Ahmed": {"nationality": "Egypt", "room": 3}
}

# функция для добавления новых жильцов в словарь
def add_resident(name, nationality, room):
    residents[name] = {"nationality": nationality, "room": room}

# функция для удаления жильца из словаря
def remove_resident(name):
    del residents[name]

# функция для вывода списка жильцов в виде таблицы с флагами национальностей
def visualize_residents_table():
    names = []
    nationalities = []
    rooms = []

    # извлечение данных из словаря
    for name, data in residents.items():
        names.append(name)
        nationalities.append(data["nationality"])
        rooms.append(data["room"])
    
    # создание таблицы с помощью matplotlib
    fig, ax = plt.subplots()
    ax.table(cellText=[names, nationalities, rooms], colLabels=["Name", "Nationality", "Room"], loc="center")
