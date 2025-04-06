class DatabaseRegistry:
    """Глобальний реєстр баз даних, що дозволяє реєструвати, отримувати та списувати бази даних."""

    _databases = {}

    @classmethod
    def register(cls, name, db_instance):
        """
        Реєструє базу даних у реєстрі.

        Args:
            name (str): Назва бази даних.
            db_instance (object): Екземпляр бази даних, що реєструється.
        """
        cls._databases[name] = db_instance

    @classmethod
    def get(cls, name):
        """
        Отримує зареєстровану базу даних за її назвою.

        Args:
            name (str): Назва бази даних.

        Returns:
            object: Екземпляр бази даних або None, якщо база даних не знайдена.
        """
        return cls._databases.get(name)

    @classmethod
    def list(cls):
        """
        Повертає список назв усіх зареєстрованих баз даних.

        Returns:
            list: Список назв баз даних.
        """
        return list(cls._databases.keys())
