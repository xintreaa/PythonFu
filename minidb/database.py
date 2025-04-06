class Database:
    """Simple in-memory database simulation."""

    def __init__(self, name):
        """Initialize the database with a name."""
        self.name = name
        self._storage = {}
        self._id_counters = {}

    def create(self, model_name, data):
        """Create a new record for the specified model."""

        if model_name not in self._storage:
            self._storage[model_name] = {}
            self._id_counters[model_name] = 0

        # Генерація нового ID
        self._id_counters[model_name] += 1
        new_id = self._id_counters[model_name]

        # Створення запису з таким ID
        record = data.copy()
        record['id'] = new_id

        # Зберігаємо запис
        self._storage[model_name][new_id] = record

        return record

    def read(self, model_name, record_id):
        """Read a record by ID for the specified model."""
        if model_name in self._storage and record_id in self._storage[model_name]:
            return self._storage[model_name][record_id]
        return None

    def update(self, model_name, record_id, data):
        """Update a record by ID for the specified model."""
        if model_name in self._storage and record_id in self._storage[model_name]:
            record = self._storage[model_name][record_id]
            record.update(data)
            return record
        return None

    def delete(self, model_name, record_id):
        """Delete a record by ID for the specified model."""
        if model_name in self._storage and record_id in self._storage[model_name]:
            del self._storage[model_name][record_id]
            return True
        return False