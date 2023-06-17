
# Экспоненциальный поиск
from random import randint

def Binary(arr,x):
  low = 0
  high = len(arr)-1
  index = -1
  while (low <= high) and (index == -1):
    mid = (low+high)//2
    if arr[mid] == x:
      index = mid
    else:
      if x < arr[mid]:
        high = mid - 1
      else:
        low = mid + 1
  return index


def ExponentialSearch (arr, x):
  if arr[0] == x:
    return 0
  index = 1
  while index < len(arr) and arr[index] <= x:
    index = index * 2
  return Binary ( arr[:min(index, len(arr))],x)


#Тестовый массив
testarr = [17, 36, 37, 37, 58, 74, 77, 78, 78, 82]
#for i in range(10):
#  testarr.append(randint(1,100))
#testarr.sort()
print (testarr)

x = int(input("Введи число: "))

# Вызов функции

if ExponentialSearch(testarr, x) != -1:
  print ("Элемент найден в массиве, под индексом: ", ExponentialSearch(testarr, x))
else:
  print ("Элемент НЕ найден в массиве")

# Jump поиск
from random import randint
import math


def Jumpsearch(arr, x):
  jump = int(math.sqrt(len(arr)))
  left = 0
  right = 0
  while left < len(arr) and arr[left] <= x:
    right = min(len(arr)-1, left + jump)
    if arr[left] <= x and arr[right] >= x:
      break
    left += jump
  if left >= len(arr) or arr[left] > x:
    return -1
  right = min(len(arr)-1, right)
  n = left
  while n <= right and arr[n] <= x:
    if arr[n] == x:
      return n
    n +=1
  return -1


#Тестовый массив
testarr = []
for i in range(10):
 testarr.append(randint(1,100))
testarr.sort()
print (testarr)

x = int(input("Введи число: "))

# Вызов функции

if Jumpsearch(testarr, x) != -1:
  print ("Элемент найден в массиве, под индексом: ", Jumpsearch(testarr, x))
else:
  print ("Элемент НЕ найден в массиве")

# Интреполяционный поиск
from random import randint


def InterpolationSearch (arr,x):
  low = 0
  high = (len(arr)-1)
  while low <= high and x >= arr[low] and x <= arr[high]:
   index = low + int((x - arr[low]) * (high - low) / (arr[high] - arr[low]))
    if arr[index] == x:
      return index
    if arr[index] < x:
      low = index + 1
    else:
      high = index - 1
  return -1

#Тестовый массив
testarr = []
for i in range(10):
 testarr.append(randint(1,100))
testarr.sort()
print (testarr)

x = int(input("Введи число: "))

# Вызов функции

if InterpolationSearch(testarr, x) != -1:
  print ("Элемент найден в массиве, под индексом: ", InterpolationSearch(testarr, x))
else:
  print ("Элемент НЕ найден в массиве")

# Задача 3

import os

def get_paths(path = '.'):
  for name in os.listdir(path):
    abs_path = os.path.abspath(os.path.join(path, name))
    yield abs_path
    if os.path.isdir(abs_path) is True:
      yield from get_paths(abs_path)

for i in get_paths(r"C:\Users\Елена\Desktop\project_01"):
  print(i)

# Задача 4

import os
def get_pathss(path = '.'):
  for name in os.listdir(path):
    abs_path = os.path.abspath(os.path.join(path, name))
    if os.path.isfile(abs_path) is True:
       yield abs_path
    elif os.path.isdir(abs_path) is True:
      yield from get_pathss(abs_path)


for i in get_pathss(r"C:\Users\Елена\Desktop\project_01"):
  print(i)