# На числовой прямой расположены точки A, B, C и D.
# Напишите программу, которая выведет, во сколько раз отрезок AB больше или меньше, чем отрезок CD.
# Формат входных данных:
# На вход программе подается четыре целых числа A, B, C и D.
# Расположение точек относительно друг друга на координатной прямой произвольное.
# Формат выходных данных:
# Выведите, во сколько раз отрезок AB больше, чем отрезок CD. Ответ введите с точностью до 6-ти знаков после запятой.

while True:
    input_str = input("Введите четыре целых числа в формате: A, B, C и D: ")
    snumbers = input_str.split(",")
    numbers = []
    try:
        if len(snumbers) != 4:
            raise ValueError
        numbers = list(map(lambda str: int(str.strip()), snumbers))
        break
    except ValueError:
        print("Данные введены в неверно!")

len_ab=abs(numbers[1]-numbers[0])
len_cd=abs(numbers[3]-numbers[2])

if(len_ab>len_cd):
    diff =len_ab/len_cd
    print(f"Отрезок АВ={len_ab} больше СD={len_cd} в {diff:.6f} раз(-а)")
else:
    diff =len_cd/len_ab
    print(f"Отрезок АВ={len_ab} меньше СD={len_cd} в {diff:.6f} раз(-а)")
