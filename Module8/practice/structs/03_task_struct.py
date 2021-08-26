# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random

numbers = [random.randint(-10, 10) for _ in range(10)]
print(numbers)

nums_less10 = [el for el in numbers if el < 10]
print(len(nums_less10))

nums_positive = [el for el in numbers if el > 0]
print(sum(nums_positive))

even_elements = [el for el in numbers if el % 2 == 0]
print(sum(even_elements) / len(even_elements))
