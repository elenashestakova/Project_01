# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    new_s = s.replace("!", "")
    return new_s

str = input('Введите строку: ')
print(remove_exclamation_marks(str))


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s[-1] == "!":
        new_s = s[:-1]
    else:
        new_s = s
    return new_s


str = input('Введите строку: ')
print(remove_last_em(str))


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"
def remove_word_with_one_em(s):
    return ' '.join(i for i in s.split() if list(i).count('!') != 1)


str = input('Введите строку: ')
print(remove_word_with_one_em(str))