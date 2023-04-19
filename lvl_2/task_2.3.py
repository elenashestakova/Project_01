# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
    match number:
        case 0:
            return 'Zero'
        case 1:
            return 'One'
        case 2:
            return'Two'
        case 3:
            return'Three'
        case 4:
            return 'Four'
        case 5:
            return 'Five'
        case 6:
            return 'Six'
        case 7:
            return 'Seven'
        case 8:
            return 'Eight'
        case 9:
            return 'Nine'
        case _:
            return 'None'


    #  digits_words = ["Zero", "One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    #  return digits_words[number] if 0 <= number <= 9 else None


num = int(input('Введите цифру от 0 до 9: '))
print(switch_it_up(num))





