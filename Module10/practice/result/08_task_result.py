# Прочитав число из файла задачи 7, определите:
# Какие цифры встречаются в числе чаще всего?
# Если несколько цифр встречаются одинаковое максимальное кол-во раз - найдите любые.
# Является ли данное число(20000-значное) четным?

def get_digits(number):
    digits=[]
    while number%10!=0:
        digits.append(number%10)
        number=int(number/10)
    return digits

def get_more_repeatable_digits(digits):
    uniq_digits=set([el for el in digits])
    digits_count={}
    max_count=0
    for el in uniq_digits:
        digits_count[el]=digits.count(el)
        if(max_count<digits_count[el]):
            max_count=digits_count[el]
    more_repeatable_digits=[]
    for key,value in digits_count.items():
        if(value==max_count):
            more_repeatable_digits.append(key)
    return more_repeatable_digits
    


with open("numbers.txt", "r",encoding="utf-8") as f:
    number = int(f.readline().strip())
    digits=get_digits(number)
    more_repeatable_digits=get_more_repeatable_digits(digits)
    print(f"В числе чаще всего встречаются цифры : {more_repeatable_digits}")
    if number%2==0:
        print(f"Число {number} - является четным")
    else:
        print(f"Число {number} - не четное")
