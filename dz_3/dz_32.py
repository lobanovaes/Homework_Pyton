#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# def mult_lst(lst):
#     l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#     new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
#     print(new_lst)

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# mult_lst(lst)

# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: 
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


#Решение на семинаре
import random
import math
from functions import create_list, List

def get_list_product_pairs_elements(numbers: list) -> list:
    """
    Возвращает список, стоящий из произведения пар принятого списка
    
    Args:
        list - список чисел
    Returns:
        list - список произведения пар
    """  
    product_list = []
    for i in range(math.ceil(len(numbers)/2)):
        product_list.append(numbers[i]*numbers[-(i+1)])
    return product_list   

numbers = create_list()
print(f'исходный список {numbers}')  
print(f'произведение пар элементов = {get_list_product_pairs_elements(numbers)}')