class Database:

    def __init__(self, name):
        """Ініціалізація бази даних з вказаним ім'ям.

        Параметри:
            name (str): Ім'я бази даних.
        """
        self.name = name
        self._storage = {}
        self._id_counters = {}

    def create(self, model_name, data):
        """Створити новий запис для вказаної моделі.

        Параметри:
            model_name (str): Назва моделі, для якої створюється запис.
            data (dict): Дані для нового запису.

        Повертає:
            dict: Створений запис з новим ID.
        """
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
        """Прочитати запис за ID для вказаної моделі.

        Параметри:
            model_name (str): Назва моделі, для якої необхідно отримати запис.
            record_id (int): ID запису, який потрібно отримати.

        Повертає:
            dict or None: Запис з вказаним ID або None, якщо запис не знайдено.
        """
        if model_name in self._storage and record_id in self._storage[model_name]:
            return self._storage[model_name][record_id]
        return None

    def update(self, model_name, record_id, data):
        """Оновити запис за ID для вказаної моделі.

        Параметри:
            model_name (str): Назва моделі, для якої потрібно оновити запис.
            record_id (int): ID запису, який потрібно оновити.
            data (dict): Дані для оновлення запису.

        Повертає:
            dict or None: Оновлений запис або None, якщо запис не знайдено.
        """
        if model_name in self._storage and record_id in self._storage[model_name]:
            record = self._storage[model_name][record_id]
            record.update(data)
            return record
        return None

    def delete(self, model_name, record_id):
        """Видалити запис за ID для вказаної моделі.

        Параметри:
            model_name (str): Назва моделі, для якої потрібно видалити запис.
            record_id (int): ID запису, який потрібно видалити.

        Повертає:
            bool: True, якщо запис було успішно видалено, або False, якщо запис не знайдено.
        """
        if model_name in self._storage and record_id in self._storage[model_name]:
            del self._storage[model_name][record_id]
            return True
        return False
