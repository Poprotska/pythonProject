# print('Hello')
#
# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4  вивело в консолі.

# st = 'as 23 fdfdg544'
# print(', '.join(i for i in st if i.isdigit()))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
#
# st = 'as 23 fdfdg544 34'
# print(', ' .join('' .join(i if i.isdigit() else ' ' for i in st).split()))

# #################################################################################
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#

# greeting = 'Hello, world'
# print(', '.join(a for a in greeting).upper())
# print([a.upper() for a in greeting])

# 2) з диапозону від 0-50 записати тільки непарні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#

# num = [i**2 for i in range(50) if i % 2]
# print(num)

# function
#
# - створити функцію яка виводить ліст
#
# def show_list(l):
#     print(l)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

#
# a = 2
# b = 3
# c = 8
#
# def get_max(a, b, c):
#     result = max(a, b, c)
#     print(result)
#     return result

# print(get_max(a,b,c))

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def get_num(*args):
#     print(max(args))
#     return min(args)
#
# print(get_num(4,6,9,13))

# - створити функцію яка повертає найбільше число з ліста
# - створити функцію яка повертає найменьше число з ліста
#
# l=[3, 5 , 7 , 8]
#
# def max_num(l):
#     return max(l)
#
# def min_num(l):
#     return min(l)
#
# print(min_num(l))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
#
# def sum_of_list(l):
#     return sum(l)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
#
# def average(l):
#     return sum(l)/len(l)

# print(average(l))

# ################################################################################################
# 1)Дан list:
# list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
# print(min(list))
#   - видалити усі дублікати

arr = [22, 3,5,2,8,2,-23, 8,23,5]
def duplicate():
    l = arr.copy()
    print(list(set(l)))

#   - замінити кожне 4-те значення на 'X'

def subst():
    l = arr.copy()
    print(['X' if not (i + 1) % 4 else item for i, item in enumerate(l)])
#
# subst()

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')
#
#
# square(5)

# 3) вывести табличку множення за допомогою цикла while

def multi_table():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            res = i*j
            # print(' ' if res//10 else '  ', end='')
            # print(res, end='')
            print(f'{res:4}', end='')
            j+=1
        i+=1
        print()
#
# multi_table()

# 4) переробити це завдання під меню

while True:
    print('1) знайти мін число')
    print('2) видалити усі дублікати')
    print('3) замінити кожне 4-те значення на \'X\'')
    print('4) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
    print('5) вывести табличку множення за допомогою цикла while')
    print('9) вихід')

    choice = input('виберіть завдання:')
    if choice == '1':
        print(min(arr.copy()))
    elif choice == '2':(
        duplicate())
    elif choice == '3':(
        subst())
    elif choice == '4':(
        square(5))
    elif choice == '5':(
        multi_table())
    elif choice == '9':
        break