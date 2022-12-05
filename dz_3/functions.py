import random
from typing import List
def create_list(numbs = []):
    for i in range(int(input('Введите количество элементов списка: '))):
        numbs.append(random.randint(1,9))
    return numbs