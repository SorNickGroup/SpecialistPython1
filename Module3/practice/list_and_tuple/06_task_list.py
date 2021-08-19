# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Первое число: "))     # Первое число
second_number = int(input("Второе число: "))    # Второе число

my_3list=[]
while first_number<second_number:
    first_number+=1
    if first_number%3==0:
        my_3list.append(first_number)
print(my_3list)
