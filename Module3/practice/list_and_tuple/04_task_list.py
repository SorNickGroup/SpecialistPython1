# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

numbers=[-10,0,2,-5,7,-3,10]

summa=0
for num in numbers:
    if(num>0):
        summa+=num
print (summa)
