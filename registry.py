class DatabaseRegistry:
    """Глобальний реєстр баз даних."""
    _databases = {}

    @classmethod
    def register(cls, name, db_instance):
        cls._databases[name] = db_instance

    @classmethod
    def get(cls, name):
        return cls._databases.get(name)

    @classmethod
    def list(cls):
        return list(cls._databases.keys())