# Дан файл ("data/fruits.txt") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А.txt, fruits_Б.txt, fruits_В.txt ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв,
#        а также есть пустые строки, которые нужно пропустить.
# Напишите универсальный код, который будет работать с любым списком фруктов и
# распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.

# Возможно пригодится:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

fruits_letters = {}
fruits_list = []
last_letter = "0"
with open("data/fruits.txt", "r", encoding="utf_8") as f:
    for line in f:
        if (line.strip() != ""):
            if last_letter != line.strip()[0]:
                if len(fruits_list) > 0:
                    fruits_letters[last_letter] = fruits_list.copy()
                last_letter = line.strip()[0]
                fruits_list.clear()
            fruits_list.append(line)
    if len(fruits_list) > 0:
        fruits_letters[last_letter] = fruits_list.copy()

for key, value in fruits_letters.items():
    with open("data/fruits_" + key + ".txt", "w", encoding="utf_8") as f:
        f.writelines(value)
