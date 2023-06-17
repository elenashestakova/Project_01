import sqlite3


# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# sqlquery = """
# CREATE TABLE School (
# School_Id INTEGER NOT null PRIMARY KEY,
# School_Name TEXT NOT NULL,
# Place_Count INTEGER NOT null
# );"""
# cursor.execute(sqlquery)
# connection.commit
# connection.close


#вставка значений в таблицу school
#connection = sqlite3.connect('teachers.db')
#cursor = connection.cursor()
#sqlquery = """INSERT INTO School
#(School_Id, School_Name, Place_Count)
#VALUES ('1', 'Протон', 200),
#('2', 'Преспектива', 300),
#('3', 'Спектр', 400),
#('4', 'Содружество', 500);
#);"""
#cursor.execute(sqlquery)
#connection.commit()
#connection.close()

# def get_connection():
#     connection = sqlite3.connect('teachers.db')
#     return connection
#
# def close_connection():
#     if connection:
#         connection.close()
#
# def experience_update():
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#
#         cursor.execute('UPDATE Teacher SET Experience = 5 WHERE School_Id = 1')
#         connection.commit()
#         close_connection()
#     except(Exception, sqlite3.Error) as error:
#         print('Ошибка в получении данных: ', error)
#
# experience_update()




