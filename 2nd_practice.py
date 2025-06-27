# Импорт для пятого задания, VS Code автоматом ставит наверх. Решил немного оживить игру.
import random

# Задача 1. Сумма чисел


def summa_n(a):
    summ = 0
    for i in range(1, a + 1):
        summ += i
    return summ


n = int(input('Введите число: '))
print(summa_n(n))


# Задача 2. Функция в функции

def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


def neutral():
    print('Ноль не является ни положительным, ни отрицательным')


def test():
    number = int(input('Введите число: '))
    if number > 0:
        positive()
    elif number < 0:
        negative()
    else:
        neutral()


test()


# Задача 3. Апгрейд калькулятора

# Функция для нахождения суммы цифр
def summ_of_digits(a):
    summ = 0
    while a > 0:
        last_digit = a % 10
        summ += last_digit
        a = a // 10
    return summ


# Функция для нахождения максимальной цифры
def max_digit(a):
    mx_digit = 0
    while a > 0:
        if a % 10 > mx_digit:
            mx_digit = a % 10
        a = a // 10
    return mx_digit


# Функция для нахождения минимальной цифры
def min_digit(a):
    mn_digit = 9
    while a > 0:
        if a % 10 < mn_digit:
            mn_digit = a % 10
        a = a // 10
    return mn_digit


# Блок ввода информации
while True:
    num = int(input('Введите число (или 0 для выхода): '))
    if num == 0:
        print('Выход из программы.')
        break

    for i in range(5, 0, -1):
        print('\nВведите номер действия:\n1 - сумма цифр\n2 - максимальная цифра\n3 - минимальная цифра: ', end='')
        choose = int(input())
        if choose == 1:
            print('\nСумма цифр:', summ_of_digits(num))
            break
        elif choose == 2:
            print('\nМаксимальная цифра:', max_digit(num))
            break
        elif choose == 3:
            print('\nМинимальная цифра:', min_digit(num))
            break
        else:
            print('Неверный ввод')
            print(f'У вас осталось {i - 1} попытки.' if i >
                  2 else 'У вас осталась 1 попытка')
    else:
        print('Вы не справились даже с выбором желаемого... Больше мы вас тут не держим. Прощайте!')


# Задача 4. Текстовый редактор

# Тело функции которая считает, сколько раз в тексте встречается любая выбранная буква или цифра.
def count_letters():
    text = input('Введите текст: ').lower()
    digit = input('Какую цифру ищем? ')
    while not digit.isdigit():
        print("Ошибка: введите одну цифру от 0 до 9.")
        digit = input('Какую цифру ищем? ')
    letter = input('Какую букву ищем? ').lower()

    digit_counter = 0
    letter_counter = 0

    for _ in text:
        if digit == _:
            digit_counter += 1
        if letter == _:
            letter_counter += 1

    print(f'Количество цифр {digit}: {digit_counter}')
    print(f'Количество букв {letter}: {letter_counter}')


# Вызов функции
count_letters()


# Задача 5. Недоделка


def rock_paper_scissors(user_name):
    # Здесь будет игра «Камень, ножницы, бумага»

    print(f'{user_name}, вы выбрали игру "КАМЕНЬ, НОЖНИЦЫ, БУМАГА!"')
    print('Правила очень простые: Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.\nВы играете против нашего суперсовременного ИИ способного предугадывать ваши действия.\nА для игры достаточно выбрать камень, ножницы или бумагу.\n')

    while True:
        random_number = random.randint(1, 3)
        print('1 - Камень\n2 - Ножницы\n3 - Бумага\n0 - выход из игры')

        choice = int(
            input('\nСделайте свой выбор: '))
        print()

        if choice == 0:
            print('Вы вышли из игры "КАМЕНЬ, НОЖНИЦЫ, БУМАГА!"\n')
            break
        elif not 0 < choice < 4:
            print('Введённое число должно быть от 0 до 3.')
            choice = int(input('\nСделайте свой выбор: '))
        elif choice == random_number:
            print('Ничья.')
        elif (choice == 1 and random_number == 2) or (choice == 2 and random_number == 3) or (choice == 3 and random_number == 1):
            print('Вы победили!')
        else:
            print('вы проиграли :(')

        if random_number == 1:
            print('У соперника был Камень')
        elif random_number == 2:
            print('У соперника были Ножницы')
        else:
            print('У соперника была Бумага')
        print()


def guess_the_number(user_name):
    # Здесь будет игра «Угадай число»

    print(f'{user_name}, вы выбрали игру "Угадай число!"')
    print('Правила очень простые: Наш ИИ запрашивает у пользователя число от 1 до 10 до тех пор, пока он не угадает загаданное.')
    print(f'0 - для выхода\n')
    # Генерация случайного числа от 1 до 10 (включительно)

    random_number = random.randint(1, 10)
    user_input = int(input('Введите число: '))

    while user_input != random_number:
        if user_input == 0:
            print('Вы вышли из игры "Угадай число!"\n')
            break
        elif not 0 < user_input < 11:
            print('Введённое число должно быть от 1 до 10.\n')
            user_input = int(input('Введите число: '))

        print('Введённое число не совпадает с загаданным, попробуйте ещё раз.\n')
        user_input = int(input('Введите число: '))
    else:
        print(f'Поздравляем вас {user_name}, вы угадали загаданное число!')


def main_menu():
    print('\nРады вас видеть в нашей уютной игровой комнате!')
    user_name = input('Как вас зовут?\n')
    print(f'\nПриветствуем вас {user_name}!')
    while True:
        print('На выбор пока что есть только 2 игры.')
        print('\n1 - Камень, Ножницы, Бумага\n2 - Угадай число\n')
        game = int(
            input('Выберите игру: '))
        if game == 1:
            print()
            rock_paper_scissors(user_name)
        elif game == 2:
            print()
            guess_the_number(user_name)
        elif game == 0:
            exit()
        else:
            print('Введённое число должно быть 1 или 2.\n')


main_menu()
