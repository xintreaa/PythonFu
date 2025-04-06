import unittest
from models import User, Product
from registry import DatabaseRegistry
from minidb.database import Database

class TestModels(unittest.TestCase):

    def setUp(self):
        """
        Підготовка середовища для тестів.
        Створюються бази даних для використання в тестах та реєстрація їх в реєстрі.
        """
        self.default_db = Database("default")
        self.test_db = Database("test")
        DatabaseRegistry.register("default", self.default_db)
        DatabaseRegistry.register("test", self.test_db)

    def test_create_user(self):
        """
        Тестує створення користувача.

        Перевіряється, чи коректно створюється користувач з переданими даними.
        """
        user = User.create(name="Alice", email="alice@example.com")
        self.assertEqual(user.name, "Alice")  # Перевірка на ім'я користувача
        self.assertEqual(user.email, "alice@example.com")  # Перевірка на email користувача
        self.assertIsNotNone(user.id)  # Перевірка, що ID не є None

    def test_get_user(self):
        """
        Тестує отримання користувача.

        Перевіряється, чи коректно повертається користувач за його ID.
        """
        user = User.create(name="Bob", email="bob@example.com")
        fetched_user = User.get(user.id)
        self.assertEqual(fetched_user.name, "Bob")  # Перевірка на ім'я користувача
        self.assertEqual(fetched_user.email, "bob@example.com")  # Перевірка на email користувача

    def test_update_user(self):
        """
        Тестує оновлення користувача.

        Перевіряється, чи коректно оновлюється ім'я користувача.
        """
        user = User.create(name="Charlie", email="charlie@example.com")
        updated_user = User.update(user.id, name="Charlie Updated")
        self.assertEqual(updated_user.name, "Charlie Updated")  # Перевірка оновленого ім'я

    def test_delete_user(self):
        """
        Тестує видалення користувача.

        Перевіряється, чи коректно видаляється користувач та чи не існує після видалення.
        """
        user = User.create(name="David", email="david@example.com")
        result = User.delete(user.id)
        self.assertTrue(result)  # Перевірка, чи був успішно видалений користувач
        fetched_user = User.get(user.id)
        self.assertIsNone(fetched_user)  # Перевірка, що користувач відсутній після видалення

if __name__ == '__main__':
    unittest.main()
