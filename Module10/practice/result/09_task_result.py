# Напишите функцию принимающую на вход целое числом n. И возвращающую список из n элементов.
# заполненный случайными целыми числами в диапазоне от a до b.
# Примечание: для генерации случайного числа используйте import random
import random

def generate_random_list(size,min_val=-10,max_val=10):    
    list_numbers = []
    for _ in range(size):
        list_numbers.append(random.randint(min_val, max_val))
    return list_numbers


print(generate_random_list(10))
