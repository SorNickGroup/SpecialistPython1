# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def modify_fraction(fraction):
    mod_fraction = {}
    mod_fraction["integer"] = 0
    mod_fraction["numerator"] = 0
    mod_fraction["denominator"] = 0
    array = fraction.split("/")
    if len(array) == 2:
        mod_fraction["denominator"] = int(array[1])

    array = array[0].split()
    if len(array) == 2:
        mod_fraction["integer"] = int(array[0])
        mod_fraction["numerator"] = int(array[1])
    elif mod_fraction["denominator"] != 0:
        mod_fraction["numerator"] = int(array[0])
    else:
        mod_fraction["integer"] = int(array[0])
        mod_fraction["denominator"] = 1

    if mod_fraction["integer"] != 0:
        mod_fraction["numerator"] *= int(mod_fraction["integer"] / abs(mod_fraction["integer"]))
        mod_fraction["numerator"] += int(mod_fraction["integer"] * mod_fraction["denominator"])
        mod_fraction["integer"] = 0

    return mod_fraction


def calculate_expression(expression):
    operands = expression.split(" - ")
    factor = -1
    if len(operands) == 1:
        operands = expression.split(" + ")
        factor = 1
    if len(operands) == 1:
        return "Выражение составлено неверно!"
    operands[0] = modify_fraction(operands[0])
    operands[1] = modify_fraction(operands[1])
    if operands[0]["denominator"] != operands[1]["denominator"]:
        operands[0]["numerator"] *= operands[1]["denominator"]
        operands[1]["numerator"] *= operands[0]["denominator"]
        operands[0]["denominator"] *= operands[1]["denominator"]
        operands[1]["denominator"] = operands[0]["denominator"]
    res = {}
    res["integer"] = 0
    res["numerator"] = operands[0]["numerator"] + operands[1]["numerator"] * factor
    res["denominator"] = operands[0]["denominator"]
    if abs(res["numerator"]) >= res["denominator"]:
        res["integer"] += int(abs(res["numerator"]) // res["denominator"] * abs(res["numerator"]) / res["numerator"])
    if res["integer"] != 0:
        res["numerator"] = int(res["integer"] / abs(res["integer"]) * res["numerator"] % res["denominator"])
        if res["numerator"] != 0:
            return f"{res['integer']} {res['numerator']}/{res['denominator']}"
        else:
            return f"{res['integer']}"
    elif res["numerator"] != 0:
        return f"{res['numerator']}/{res['denominator']}"
    else:
        return "0"


print(calculate_expression("-0 + 0"))
print(calculate_expression("-21 + 18 7/3"))
print(calculate_expression("7/5"))
print(calculate_expression("5/6 + 4/7"))
print(calculate_expression("-2/3 - -2"))
print(calculate_expression("-7 1/2 + -5"))
