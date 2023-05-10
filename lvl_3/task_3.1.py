# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)

class Matrix:
    """Класс матрица, которая представляет собой вложенные списки"""
    def __init__(self, row, col=1, value=None):
        """метод для инициализации матрицы"""
        self.__x = row
        self.__y = col
        self.__matrix = [[value] * col for _ in range(row)]

    def add_value(self, value):
        """метод для добавления новых (одинаковых) значений в матрицу"""
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[i])):
                self.__matrix[i][j] = value

    def set_value(self, row, col, value):
        """метод для добавления/замены значения в определенной ячейке матрицы"""
        if row >= self.__x or col >= self.__y:
            return f'Номер строки/колонки выходит за пределы матрицы'
        self.__matrix[row][col] = value

    def set_snake(self):
        """метод для заполнения матрицы змейкой"""
        count = 1

        for i in range(self.__x):
            for j in range(self.__y):
                self.__matrix[i][j] = count
                count += 1

        for i in range(1, self.__x, 2):
            self.__matrix[i].reverse()

    def show_num_rows(self):
        """метод для отображения количества строк в матрице"""
        return self.__x

    def show_num_col(self):
        """метод для отображения количества колонок в матрице"""
        return self.__y

    def print_matrix(self):
        """метод для отображения матрицы"""
        for row in self.__matrix:
            print(' '.join((str(i) if i is not None else "N") for i in row))

    def print_matrix_snake(self):
        """метод для отображения матрицы"""
        for row in self.__matrix:
            print(' '.join((str(i).ljust(3) if i is not None else "N") for i in row))


m1 = Matrix(4, 6)
m1.print_matrix()

m1.set_value(1, 1, 3)
m1.print_matrix()

m1.set_snake()
m1.print_matrix_snake()







