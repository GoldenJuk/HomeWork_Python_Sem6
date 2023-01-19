#Реализуйте алгоритм перемешивания списка.

from random import randint as RN, shuffle

my_list = sorted([RN(0,20) for _ in range(10)])
print(f'\nСгенерированный и сортированный список случайных чисел: {my_list}\n')
shuffle(my_list)
print(f'Перемешанный список: {my_list}\n')