# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
# list_01 = []
# i = 0
#
def rand(x, y):
    n = random.randrange(x, y)
    return n
#
# for i in range(5):
#     a = rand(1, 20)
#     list_01.append(a)
#
# print(list_01)
#
# new_list = [i**2 for i in list_01]
# print(new_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_01, fruits_02 = ["apple","pear","banana"], ["orange","banana","peach"]
sum_fruits = fruits_01+fruits_02

a = list((x, sum_fruits.count(x)) for x in set(sum_fruits) if sum_fruits.count(x) > 1)
print(a)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
numbers = []
for i in range(10):
    a = rand(-10, 20)
    numbers.append(a)
print(numbers)

list_by_3 = [i for i in numbers if i%3 == 0]
list_by_plus = [i for i in numbers if i > 0]
list_not_4 = [i for i in numbers if i%4 != 0]

print(list_by_3,list_by_plus, list_not_4)