import unittest
from minidb.database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database("test_db")

    def test_create_record(self):
        data = {"name": "Alice", "email": "alice@example.com"}
        record_id = self.db.create("users", data)
        self.assertIsNotNone(record_id)

    def test_read_record(self):
        data = {"name": "Bob", "email": "bob@example.com"}
        record_id = self.db.create("users", data)
        read_record = self.db.read("users", record_id)
        self.assertEqual(read_record["name"], "Bob")
        self.assertEqual(read_record["email"], "bob@example.com")

    def test_update_record(self):
        data = {"name": "Charlie", "email": "charlie@example.com"}
        record_id = self.db.create("users", data)
        updated_data = {"email": "charlie_new@example.com"}
        updated_rows = self.db.update("users", record_id, updated_data)
        self.assertEqual(updated_rows, 1)
        read_record = self.db.read("users", record_id)
        self.assertEqual(read_record["email"], "charlie_new@example.com")

    def test_delete_record(self):
        data = {"name": "David", "email": "david@example.com"}
        record_id = self.db.create("users", data)
        deleted_rows = self.db.delete("users", record_id)
        self.assertEqual(deleted_rows, 1)
        read_record = self.db.read("users", record_id)
        self.assertIsNone(read_record)

if __name__ == '__main__':
    unittest.main()