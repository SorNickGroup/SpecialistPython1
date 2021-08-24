# В файлк salaries.txt даны зарплаты сотрудников

# Задача: выведите всех сотрудников в файл highly_paid.txt, зарплаты которых превышают 60000
# Сотружников вывести в формате: Фамилия И.О. ,например: Иванов И.П. (зарплаты в файл не записывать)
f = open("data/salaries.txt", "r", encoding="utf_8")
new_file = open("data/highly_paid.txt", "w", encoding="utf_8")
new_file.write("Фамилия И.О.\n")
f.readline()
for line in f:
    solary = line.split()
    if int(solary[3]) > 60000:
        new_file.write(f"{solary[0]} {solary[1][0]}. {solary[2][0]}.\n")
new_file.close()
