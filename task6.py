# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform as RN
import math

my_list = [round(RN(0,10),2)  for _ in range(5)]
temp = [my_list[i] - math.floor(my_list[i]) for i in range(len(my_list)) if my_list[i] - math.floor(my_list[i]) !=0]
result = round((max(temp) - min(temp)),2)
print(f'\nРазница между максимальным и минимальным значением дробной части элементов{my_list} = {result}\n')