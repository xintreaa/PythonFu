import unittest
from minidb.database import Database

# python -m unittest discover -s tests

class TestDatabase(unittest.TestCase):

    def setUp(self):
        """Ініціалізація тестів: створення екземпляра бази даних."""
        self.db = Database("test_db")

    def test_create_record(self):
        """
        Тестує створення нового запису в базі даних.

        Перевіряється, чи коректно створюється запис і чи додається ID.
        """
        data = {"name": "Alice", "age": 30}
        record = self.db.create("Person", data)
        self.assertEqual(record["name"], "Alice")  # Перевірка на ім'я
        self.assertEqual(record["age"], 30)       # Перевірка на вік
        self.assertIn("id", record)               # Перевірка на наявність id

    def test_read_record(self):
        """
        Тестує читання запису з бази даних.

        Перевіряється, чи коректно зчитується запис по ID.
        """
        data = {"name": "Bob", "age": 25}
        record = self.db.create("Person", data)
        read_record = self.db.read("Person", record["id"])
        self.assertEqual(read_record, record)  # Перевірка чи зчитаний запис співпадає

    def test_update_record(self):
        """
        Тестує оновлення запису в базі даних.

        Перевіряється, чи коректно оновлюється запис.
        """
        data = {"name": "Charlie", "age": 35}
        record = self.db.create("Person", data)
        updated_data = {"age": 36}
        updated_record = self.db.update("Person", record["id"], updated_data)
        self.assertEqual(updated_record["age"], 36)  # Перевірка оновленого віку

    def test_delete_record(self):
        """
        Тестує видалення запису з бази даних.

        Перевіряється, чи коректно видаляється запис і чи відсутній після видалення.
        """
        data = {"name": "David", "age": 40}
        record = self.db.create("Person", data)
        result = self.db.delete("Person", record["id"])
        self.assertTrue(result)  # Перевірка, чи видалено запис
        read_record = self.db.read("Person", record["id"])
        self.assertIsNone(read_record)  # Перевірка, що запис відсутній після видалення

if __name__ == '__main__':
    unittest.main()
