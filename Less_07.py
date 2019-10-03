# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа, и фишек(бочонков) с цифрами.
# Количество бочонков — 90 штук(с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток.В каждой строке по 5 случайных цифр, расположенных по
# возрастанию.Все цифры в карточке уникальны.Пример карточки:
import random


# numbers = [i for i in range(1,10)]
# random.shuffle(numbers)
#
# def rand_cards(choise):
#     random_number = random.choice(choise)
#     for i in choise:
#         if i == random_number:
#             choise.remove(i)
#     return random_number
#
# comp_cards = random.sample(range(1, 10), 9)
# player_cards = random.sample(range(1, 10), 9)
#
# comp_cards.sort()
# player_cards.sort()
# print(player_cards,comp_cards)
#
# def quest():
#     a = rand_cards(numbers)
#     print(a)
#     for i in player_cards:
#         if i == a:
#             player_cards.remove(i)
#     print(player_cards)

# В игре 2 игрока: пользователь и компьютер.Каждому в начале выдается случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
class Barrels:
    def __init__(self,numbers):
        self.f(numbers)
        self.rand_cards(numbers)
    def f(self,numbers):
        print(numbers)

    def rand_cards(self,numbers):
        random_number = random.choice(numbers)
        for i in numbers:
            if i == random_number:
                numbers.remove(i)
        return print (random_number)

numbers = [i for i in range(1,10)]
random.shuffle(numbers)
Barrels(numbers)

# Если игрок выбрал "зачеркнуть":
# Если цифра есть на карточке - она зачеркивается и игра продолжается.
# Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# Если цифра есть на карточке - игрок проигрывает и игра завершается.
# Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый  закроет все числа на своей карточке.
# Пример одного хода:
# Новыйбочонок: 70(осталось 76)


# Зачеркнуть
# цифру? (y / n)

# Подсказка: каждый следующий случайный бочонок из мешка удобно получать с помощью функции - генератора.

# Подсказка: для работы с псевдослучайными числами удобно использовать модуль
# random: http: // docs.python.org / 3 / library / random.html