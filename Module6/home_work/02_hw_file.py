# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

with open("data/info.txt", "r") as f:
    summa=0
    for line in f:
        line=line.rstrip()
        if (line[0]=="-" or line[0]=="+") and line[1:len(line)].isdigit():
            summa+=int(line)
        elif line.isdigit():
            summa+=int(line)
    print(summa)
