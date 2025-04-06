import sqlite3

class Database:
    """
    Клас для роботи з базою даних SQLite.

    Атрибути:
        name (str): Ім'я бази даних.
        connection (sqlite3.Connection): Підключення до бази даних SQLite.
    """

    def __init__(self, name):
        self.name = name
        self.connection = sqlite3.connect(f"{name}.db")
        self.connection.row_factory = sqlite3.Row
        self._initialize_database()

    def _initialize_database(self):
        # Update the path to schema.sql if it's in the minidb directory
        schema_path = "minidb/schema.sql"
        with open(schema_path, "r", encoding="utf-8") as f:
            self.connection.executescript(f.read())

    def create(self, table, data):
        keys = ', '.join(data.keys())
        values = ', '.join(['?'] * len(data))
        sql = f"INSERT INTO {table} ({keys}) VALUES ({values})"
        cursor = self.connection.cursor()
        cursor.execute(sql, tuple(data.values()))
        self.connection.commit()
        return cursor.lastrowid

    def read(self, table, record_id):
        sql = f"SELECT * FROM {table} WHERE id = ?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (record_id,))
        return cursor.fetchone()

    def update(self, table, record_id, data):
        keys_values = ', '.join([f"{key} = ?" for key in data.keys()])
        sql = f"UPDATE {table} SET {keys_values} WHERE id = ?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (*data.values(), record_id))
        self.connection.commit()
        return cursor.rowcount

    def delete(self, table, record_id):
        sql = f"DELETE FROM {table} WHERE id = ?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (record_id,))
        self.connection.commit()
        return cursor.rowcount

    def execute_query(self, query, params=()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor.fetchall()