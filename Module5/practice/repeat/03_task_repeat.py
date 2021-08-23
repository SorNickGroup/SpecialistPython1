# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    inverted_number = 0
    number_copy = number
    while number_copy > 0:
        last_digit = number_copy % 10
        inverted_number = inverted_number * 10 + last_digit
        number_copy = number_copy // 10
    return inverted_number == number


a = 1001
b = 2002
palindromes = []
for el in range(a, b+1):
    if palindrome(el)==True:
        palindromes.append(el)

print(f"Количество полиндромов в диапазоне от {a} до {b} включительно = {len(palindromes)}")
print(palindromes)
