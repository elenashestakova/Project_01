# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

def get_connection():
    connection = sqlite3.connect('teachers.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()


# Содание таблицы Students в базе данных teachers

#connection = get_connection()
#cursor = connection.cursor()
#sqlquery = '''CREATE TABLE Students (
#  Student_Id INTEGER NOT NULL PRIMARY KEY,
#  Student_Name VARCHAR(20) NOT NULL,
#  School_Id INTEGER NOT NULL
#); '''
#cursor.execute(sqlquery)
#connection.commit()
#close_connection(connection)

# Вставка значений в таблицу Students

#connection = get_connection()
#cursor = connection.cursor()
#sqlquery = '''INSERT INTO Students (Student_Id, Student_Name, School_Id)
#VALUES
#('201', 'Иван', '1'),
#('202', 'Петр', '2'),
#('203', 'Анастасия', '3'),
#('204', 'Игорь', '4'); '''
#cursor.execute(sqlquery)
#connection.commit()
#close_connection(connection)

# Объявляем функцию, с помощью которой по ID студента можно получать информацию о школе и студенте
def get_info_about_stud_school(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = '''SELECT Students.student_id, Students.student_name, Students.school_id, School.school_name
        FROM Students
        JOIN School ON School.school_id = Students.school_id        
        WHERE Student_id = ?'''
        cursor.execute(select_query, (student_id,))
        record = cursor.fetchall()
        close_connection(connection)
        print('Информацию о школе и студенте:', end='\n\n')
        for row in record:
            print('ID Студента: ', row[0])
            print('Имя студента: ', row[1])
            print('ID школы: ', row[2])
            print('Название школы: ', row[3])
    except (Exception, sqlite3.Error) as error:
        print("Ошибка в подключении данных: ", error)

# Запускаем функцию с указанием ID студента
get_info_about_stud_school(201)