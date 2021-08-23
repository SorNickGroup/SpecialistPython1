# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    inverted_number = 0
    number_copy = number
    while number_copy > 0:
        last_digit = number_copy % 10
        inverted_number = inverted_number * 10 + last_digit
        number_copy = number_copy // 10
    return inverted_number == number
