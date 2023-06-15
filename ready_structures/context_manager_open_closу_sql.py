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