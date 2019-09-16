# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format() '>'	выравнивание объекта по правому краю.
#Выполнение задачи-1:

fruits = ["яблоко", "банан", "киви", "арбуз"]
i = 0

while i <len(fruits):
    alignment = "{:>7}".format(fruits[i])
    i += 1
    print(i,".",alignment)

# или так

fruits = ["яблоко", "банан", "киви", "арбуз"]

for i in range(0,len(fruits)):
    alignment = fruits[i].rjust(7, ' ')
    print(i+1,".", alignment)

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

import random

list_1, list_2 = [],[]
i = 0

def rand(x,y):
    n = random.randrange(x,y)
    return n

while i<4:
    a = rand(0,10)
    list_1.append(a)
    b = rand(0,10)
    list_2.append(b)
    i += 1

print(list_1,list_2)
a = set(list_1)
b = set(list_2)
print(a-b)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list_v3 = []
i = 0

def rand(x,y):
    n = random.randrange(x,y)
    return n
while i<10:
    a = rand(0,100)
    list_v3.append(a)
    i += 1

print(list_v3)
i = 0
new_list=[]
while i<len(list_v3):
    #new_list = []
    if list_v3[i] % 2:
        b = list_v3[i]*2
        new_list.append(b)
        print(b)
        i += 1
    else:
        c = list_v3[i]/4
        new_list.append(c)
        print(c)
        i += 1

print(new_list)