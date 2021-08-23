# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def sum_digit(number):
    summa=0
    for _ in range(3):
        summa+=number%10
        number=number//10
    return summa

def lucky_ticket(ticket_number):
    start_part=ticket_number//1000
    end_part=ticket_number%1000
    return sum_digit(start_part)==sum_digit(end_part)


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
