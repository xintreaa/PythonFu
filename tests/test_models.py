import unittest
from models import User, Product
from registry import DatabaseRegistry
from minidb.database import Database

class TestModels(unittest.TestCase):

    def setUp(self):
        self.default_db = Database("default")
        self.test_db = Database("test")
        DatabaseRegistry.register("default", self.default_db)
        DatabaseRegistry.register("test", self.test_db)

    def test_create_user(self):
        user = User.create(name="Alice", email="alice@example.com")
        self.assertEqual(user.name, "Alice")
        self.assertEqual(user.email, "alice@example.com")
        self.assertIsNotNone(user.id)

    def test_get_user(self):
        user = User.create(name="Bob", email="bob@example.com")
        fetched_user = User.get(user.id)
        self.assertEqual(fetched_user.name, "Bob")
        self.assertEqual(fetched_user.email, "bob@example.com")

    def test_update_user(self):
        user = User.create(name="Charlie", email="charlie@example.com")
        updated_user = User.update(user.id, name="Charlie Updated")
        self.assertEqual(updated_user.name, "Charlie Updated")

    def test_delete_user(self):
        user = User.create(name="David", email="david@example.com")
        result = User.delete(user.id)
        self.assertTrue(result)
        fetched_user = User.get(user.id)
        self.assertIsNone(fetched_user)

if __name__ == '__main__':
    unittest.main()