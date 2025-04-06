import unittest
from minidb.database import Database

# python -m unittest discover -s tests

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database("test_db")

    def test_create_record(self):
        data = {"name": "Alice", "age": 30}
        record = self.db.create("Person", data)
        self.assertEqual(record["name"], "Alice")
        self.assertEqual(record["age"], 30)
        self.assertIn("id", record)

    def test_read_record(self):
        data = {"name": "Bob", "age": 25}
        record = self.db.create("Person", data)
        read_record = self.db.read("Person", record["id"])
        self.assertEqual(read_record, record)

    def test_update_record(self):
        data = {"name": "Charlie", "age": 35}
        record = self.db.create("Person", data)
        updated_data = {"age": 36}
        updated_record = self.db.update("Person", record["id"], updated_data)
        self.assertEqual(updated_record["age"], 36)

    def test_delete_record(self):
        data = {"name": "David", "age": 40}
        record = self.db.create("Person", data)
        result = self.db.delete("Person", record["id"])
        self.assertTrue(result)
        read_record = self.db.read("Person", record["id"])
        self.assertIsNone(read_record)

if __name__ == '__main__':
    unittest.main()