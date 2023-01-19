# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as RN
my_list = [RN(0,10) for _ in range(5)]
sum_odd_index = sum([value for key,value in enumerate(my_list) if not key%2])
print(f'\nВ списке {my_list} сумма элементов, стоящих на позиции с нечетным индексом = {sum_odd_index}\n') 