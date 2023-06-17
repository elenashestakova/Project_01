# Дано:
# * number          – число, 
# * index1, index2  – два индекса 
# * digit           – цифра, которую нужно искать в заднном числе.
 
# Задача состоит в том, чтобы проверить, существует ли цифра в числе в пределах заданных индексов.

# Будьте внимательны! index2 не обязательно больше index1.

# Например:
#     Есть ли цифра 1 в числе 1234567 между индексами 1 и 0? True
#     Есть ли цифра 1 в числе 1234567 между индексами 0 и 1? True
#     Есть ли цифра 4 в числе 67845123654 между индексами 0 и 0? True
#     Есть ли цифра 1 в числе 9999999999 между индексами 2 и 5? False


def check_digit_in_num(num, ind1, ind2, digit):
    num = str(num)
    for i in range():
        if ind1 < ind2:
            if str(digit) in s[ind1:ind2]:
                return True
        else:
            if str(digit) in s[ind2:ind1]:
                return True





number = int(input("Введите число: "))
index1, index2 = int(input("Введите первый индекс: ")), int(input("Введите второй индекс: "))
digit = int(input("Введите цифру: "))

check_digit_in_num(number, index1, index2, digit)