# minidb/database.py
class Database:
    """Simple in-memory database simulation."""

    def __init__(self, name):
        """Initialize the database with a name."""
        self.name = name
        self._storage = {}  # Format: {model_name: {id: data}}
        self._id_counters = {}  # Format: {model_name: last_id}

    def create(self, model_name, data):
        """Create a new record for the specified model."""
        # Initialize storage for the model if it doesn't exist
        if model_name not in self._storage:
            self._storage[model_name] = {}
            self._id_counters[model_name] = 0

        # Generate new ID
        self._id_counters[model_name] += 1
        new_id = self._id_counters[model_name]

        # Create record with ID
        record = data.copy()
        record['id'] = new_id

        # Store record
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