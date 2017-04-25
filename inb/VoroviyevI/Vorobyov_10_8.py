# Задачи №10 вариант 8
# Воробьев Илья Андреевич ИНБ-2016-1
# Напишите программу "Генератор персонажей" для игры.
# Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками:
# Сила, Здоровье, Мудрость и Ловкость.
# Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула",
# но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

print(
    """
                     Игра 'Генератор первонажей'
                Пользователю представлено 30 пукнктов
        которые он может распрделить между четырьмя характеристиками
                Сила, Здоровье, Мудрость и Ловкость
    """
)

input("Нажмите Enter чтобы начать")

print("Добро пожаловать в игру\n")
print("Для начало вам надо дать название вашему персонажу")
new = input("Персонаж: ")
print("\nПоздравлем, теперь у вас есть персонаж под именем -", new)

print("\nТеперь ваша задача сделать так, чтобы ваш персонаж был готов к бою")
print("У вас есть 4 характеристики к которым вы можете добавить 30 очков")

x1 = 0
x2 = 0
x3 = 0
x4 = 0

choice = None



while choice != "0":
    punkt = (30 - x1 - x2 - x3 - x4)
    print(
    """

    Меню:
    0 - Выйти из игры
    1 - Добавить очки
    2 - Посмотреть уже присвоенные очки
    3 - удалить очки

    """
    )
    choice = input("Ваш выбор: ")
    print()

# выход
    if choice == "0":
        print("До свидания")


# добаивть очки
    elif choice == "1":
        print("У вас есть", punkt, "очков которые вы можете добавить в характеристики")
        print("1 - Сила")
        print("2 - Здоровье")
        print("3 - Мудрость")
        print("4 - Ловкость")
        s = (input("Введите номер характеристики в которую хотите добавить очки - "))
        if s == "1":
            o = int(input("Сколько очков вы хотите добавить в Силу?"))
            if o >= 0 and o <= punkt:
                x1 += o
            else:
                print("Вы ввели недопустимое кол-во очков")
        elif s == "2":
            o = int(input("Сколько очков вы хотите добавить в Здоровье?"))
            if o >= 0 and o <= punkt:
                x2 += o
            else:
                print("Вы ввели недопустимое кол-во очков")
        elif s == "3":
            o = int(input("Сколько очков вы хотите добавить в Мудрость?"))
            if o >= 0 and o <= punkt:
                x3 += o
            else:
                print("Вы ввели недопустимое кол-во очков")
        elif s == "4":
            o = int(input("Сколько очков вы хотите добавить в Ловкость?"))
            if o >= 0 and o <= punkt:
                x4 += o
            else:
                print("Вы ввели недопустимое кол-во очков")


# Просматриваем хар-ки
    elif choice == "2":
        print("Ваши характеристики:")
        print("Сила - ", x1)
        print("Здоровье - ", x2)
        print("Мудрость - ", x3)
        print("Ловкость - ", x4)
        print("\nУ вас еще есть - ", punkt, "очков")

# Удаление очков
    elif choice == "3":
        print("Удаление результатов")
        print("1 - Сила")
        print("2 - Здоровье")
        print("3 - Мудрость")
        print("4 - Ловкость")
        u = (input("Введите номер характеристики которую в которой хотите удалить очки - "))
        if u == "1":
            d = int(input("Сколько очков вы хотите удалить в Силе - "))
            if d <= x1 and d > 0:
                x1 -= d
            else:
                print("Вы ввели недопустимое кол-во очков")
        elif u == "2":
            d = int(input("Сколько очков вы хотите удвлить в Здоровье - "))
            if d <= x2 and d > 0:
                x2 -= d
            else:
                print("Вы ввели недопустимое кол-во очков")
        elif u == "3":
            d = int(input("Сколько очков вы хотите удалить в Мудрости - "))
            if d <= x4 and d > 0:
                x3 -= d
            else:
                print("Вы ввели недопустимое кол-во очков")
        elif u == "4":
            d = int(input("Сколько очков вы хотите удалить в Ловкости - "))
            if d <= x4 and d > 0:
                x4 -= d
            else:
                print("Вы ввели недопустимое кол-во очков")
        else:
            print("В меню нет пункта", u)
    else:
        print("Извините, в меню нет пункта", choice)