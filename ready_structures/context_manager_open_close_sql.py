import sqlite3


class DatabaseManager:
    def init(self, db_name):
        self.db_name = db_name

    def enter(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print("Error connecting to database:", e)
            return None
        else:
            return self.conn

    def exit(self, exc_type, exc_value, traceback):
        try:
            self.conn.close()
        except AttributeError:
            print("Database connection not established")
        except sqlite3.Error as e:
            print("An error occurred while closing the database connection: ", e)


'''В enter() мы пытаемся подключиться к базе данных. Если произойдет ошибка, 
мы выводим сообщение об ошибке и возвращаем None. Если подключение установлено успешно, 
мы возвращаем объект соединения.

exit() закрывает соединение с базой данных в блоке try-except. 
Если соединение не было установлено, возникает исключение AttributeError. 
Если при закрытии соединения возникли другие ошибки, 
они отлавливаются и выводится сообщение об ошибке с их описанием.'''