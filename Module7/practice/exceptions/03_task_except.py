# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.
while True:
    input_str = input("Введите пять целых чисел, разделенных пробелом: ")
    try:
        numbers=input_str.split()
        if len(numbers) != 5:
            raise ValueError
        min_number=int(numbers[0])
        for number in numbers:
            if min_number>int(number):
                min_number=int(number)
        print(min_number)
        break
    except ValueError:
        print("Данные введены в неверно!")
    except Exception as e:
        print(e)
