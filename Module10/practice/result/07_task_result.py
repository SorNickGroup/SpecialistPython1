# Напишите программу генерирующую и записывающую в файле произвольное 20000-значное целое число.
import random

with open("numbers.txt", "w",encoding="utf-8") as f:
    f.write(str(random.randint(10000000000000000000,20000000000000000000)))
