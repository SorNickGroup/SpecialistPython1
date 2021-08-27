# Напишите функцию принимающую на вход целое числом n. И возвращающую список из n элементов.
# заполненный случайными целыми числами в диапазоне от a до b.
# Примечание: все элементы списка должны быть гарантировано уникальными(неповторяющимися)
# Если создать список с заданными параметрами невозможно - функция должна выбросить исключение(любое)

import random

def generate_uniq_random_list(size,min_val=-10,max_val=10):    
    list_numbers = []
    try:
        if size>(max_val-min_val):
            raise
    except Exception:
        print("Создать список с заданными параметрами невозможно!")
    while(len(list_numbers)<size):
        new_value=random.randint(min_val, max_val)
        if list_numbers.count(new_value)==0:
            list_numbers.append(new_value)
    return list_numbers


print(generate_uniq_random_list(10))
print(generate_uniq_random_list(10,2,10))
