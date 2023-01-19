# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint as RN

my_list = [RN(0,10) for _ in range(5)]
result = [my_list[i] * my_list[-i-1] for i in range(int(len(my_list)/2 + 0.5))]
print(f'\nВ списке {my_list} произведение пар чисел {result}\n')