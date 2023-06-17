# Калькулятор
print("Буква q будет закрывать программу")
while True:
  s = input("Знак (+,-,*,/,%): ")
  if s == "q":
    break
  if s in ('+', '-', '*', '/', '%'):
    if s == '%':
      print("x  - число от которог берём %")
      print("y - процент, который берём")
    x = float(input("x= "))
    y = float(input("y= "))
    if s == '+':
      print("%.2f" % (x+y))
    elif s == '-':
      print("%.2f" % (x-y))
    elif s == '*':
      print("%.2f" % (x*y))
    elif s == '%':
      print("%.2f" % (x / 100 * y))
    elif s == '/':
      if y != 0:
        print("%.2f" % (x/y))
      else:
        print("Деление на 0")
    else:
      print("Знак операции не распознан")



# Сортировка выбором
from random import randint
n = 10
arr = []
for i in range(n):
  arr.append(randint(1,99))
print(arr)


i = 0
while i < n - 1:
  m = i
  j = i + 1
  while j < n:
    if arr [j] < arr[m]:
      m = j
    j += 1
  arr[i], arr[m] = arr[m], arr[i]
  i += 1

print(arr)


# Сортировка пузырьком
arr = [7, 13, 5, 3, 9]
n = len(arr)
print(n)
print(arr)

for i in range(n-1):
  for j in range(n-i-1):
    if arr[j] > arr[j+1]:
      arr[j], arr[j+1] = arr[j+1], arr[j]

print (arr)


# Сортировка пузырьком
arr = [7, 13, 5, 3, 9]
n = len(arr)
print(arr)

i = 0
while i < n - 1:
  j = 0
  while j < n - 1 - i:
    if arr[j] > arr[j+1]:
      arr[j], arr[j+1] = arr[j+1], arr[j]
    j += 1
  i += 1

print(arr)


# Сортировка вставкой
arr = [7, 13, 5, 3, 9]
n = len(arr)
print(arr)

for i in range(n):
  print(i)
  j = i - 1
  val = arr[i]
  while arr[j] > val and j >= 0:
    arr[j+1] = arr[j]
    j -= 1
  arr[j+1] = val
  print(arr)

#print(arr)


from datetime import datetime

arr = [[4, 6, 2, 1, 9, 63, -134, 566], [-52, 56, 30, 29, -54, 0, -110], [42, 54, 65, 87, 0], [5]]


def insertion(data):
  for i in range(len(data)):
    j = i - 1
    key = data[i]
    while data[j] > key and j >= 0:
      data[j + 1] = data[j]
      j -= 1
    data[j + 1] = key
  return data


def bubble(data):
  n = len(data)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if data[j] > data[j + 1]:
        data[j], data[j + 1] = data[j + 1], data[j]
  return data


def vibor(data):
  n = len(data)
  i = 0
  while i < n - 1:
    m = i
    j = i + 1
    while j < n:
      if data[j] < data[m]:
        m = j
      j += 1
    data[i], data[m] = data[m], data[i]
    i += 1
  return data


def default(data):
  for data in arr:
    data = sorted(data)
    return data


def minimum(arr):
  print("МИНИМАЛЬНЫЕ ЗНАЧЕНИЯ")
  print("Метод сортировки встроенный")
  start_time = datetime.now()
  for data in arr:
    data = sorted(data)
    print("Минимальное значение из массива:", data, min(data))
  end_time = datetime.now()
  print('Продолжительность: {}'.format(end_time - start_time))
  print("Метод сортировки вставкой")
  start_time = datetime.now()
  for data in arr:
    print("Минимальное значение из массива:", data, insertion(data)[0])
  end_time = datetime.now()
  print('Продолжительность: {}'.format(end_time - start_time))
  print("Метод сортировки пузырьком")
  start_time = datetime.now()
  for data in arr:
    print("Минимальное значение из массива:", data, bubble(data)[0])
  end_time = datetime.now()
  print('Продолжительность: {}'.format(end_time - start_time))
  print("Метод сортировки выбором")
  start_time = datetime.now()
  for data in arr:
    print("Минимальное значение из массива:", data, vibor(data)[0])
  end_time = datetime.now()
  print('Продолжительность: {}'.format(end_time - start_time))


def maximum(arr):
  print("МАКСИМАЛЬНЫЕ ЗНАЧЕНИЯ")
  print("Метод сортировки встроенный")
  start_time = datetime.now()
  for data in arr:
    data = sorted(data)
    print("Максимальное значение из массива:", data, max(data))
  end_time = datetime.now()
  print('Продолжительность: {}'.format(end_time - start_time))
  print("Метод сортировки вставкой")
  start_time = datetime.now()
  for data in arr:
    print("Максимальное значение из массива:", data, insertion(data)[len(data) - 1])
  end_time = datetime.now()
  print('Продолжительность: {}'.format(end_time - start_time))
  print("Метод сортировки пузырьком")
  start_time = datetime.now()
  for data in arr:
    print("Максимальное значение из массива:", data, bubble(data)[len(data) - 1])
  end_time = datetime.now()
  print('Продолжительность: {}'.format(end_time - start_time))
  print("Метод сортировки выбором")
  start_time = datetime.now()
  for data in arr:
    print("Максимальное значение из массива:", data, vibor(data)[len(data) - 1])
  end_time = datetime.now()
  print('Продолжительность: {}'.format(end_time - start_time))


def main():
  print(minimum(arr))
  print(maximum(arr))


print(main())

# Задача №1
salary = float(input("Введи сумму зарплаты в месяц: "))
expenses = float(input("Введи расходы на проживание: "))
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
exptemp = expenses
if salary >= expenses:
  print("Входные данные не корректны")
else:
  for i in month:
    print("Сейчас месяц", i)
    if i != 1:
      all_salary = salary * i
      print("Зарплата: ", all_salary)
      expenses = expenses * 1.1
      exptemp = exptemp + expenses
      print("Расходы: ", exptemp)
    else:
      print("1 месяц у нас без %")
      print("Зарплата: ", salary)
      print("Расходы: ", expenses)
  live = abs(all_salary - exptemp)
  print("Сотрудник будет должен: ", round(live, 2), " рублей")


# Бинарный поиск /// ошибка

def binary_search(arr, low, high, x):
  # Проверяем середину
  if high >= low:
    mid = (high + low) // 2
    # Если элемент в середине:
    if arr[mid] == x:
      return mid
    # Если элемент не в середине, то проверяем левую часть
    elif arr[mid] > x:
      return binary_search(arr, low, mid - 1, x)
    # Или элемент в правой части массива
    else:
      return binary_search(arr, mid + 1, high, x)
  # В случае, если элемент не в массиве
  else:
    return -1


# Тестовый массив
arr = [3, 6, 10, 15, 19, 21, 22, 25, 27]
x = input("Введи число искомое: ")
x = int(x)

# Вызов функции
resultat = binary_search(arr, 0, len(arr) - 1, x)

# Интрерпритация результата
if resultat != -1:
  print("Элемент присутствует в массиве под индексом ", str(resultat))
else:
  print("Элемент НЕ присутствует в массиве")


# Версия №2
def binar(arr, x):
  low = 0
  high = len(arr) - 1
  index = -1
  while (low <= high) and (index == -1):
    mid = (low + high) // 2
    if arr[mid] == x:
      index = mid
    else:
      if x < arr[mid]:
        high = mid - 1
      else:
        low = mid + 1
  return index


# Тестовый массив
arr = [3, 6, 10, 15, 16, 17, 19]
x = input("Введи число искомое: ")
x = int(x)

# Вызов функции
resultat = binar(arr, x)

# Интрерпритация результата
if resultat != -1:
  print("Элемент присутствует в массиве под индексом ", str(resultat))
else:
  print("Элемент НЕ присутствует в массиве")