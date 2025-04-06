from copy import deepcopy
from .row import Row

class Table:
    """Клас для представлення таблиці з даними."""

    def __init__(self, name, columns):
        """
        Ініціалізує таблицю з ім'ям і стовпцями.

        Параметри:
            name (str): Назва таблиці
            columns (list): Список об'єктів стовпців, які визначають структуру таблиці
        """
        self.name = name
        self.columns = columns
        self.rows = []
        self._id_counter = 1

    def insert(self, data):
        """
        Вставляє новий рядок в таблицю після перевірки відповідності даних стовпцям.

        Параметри:
            data (dict): Дані для вставки у вигляді словника {назва_стовпця: значення}

        Повертає:
            Row: Створений рядок, що містить вставлені дані

        Викидає:
            ValueError: Якщо значення не відповідає вимогам стовпця (наприклад, поле не може бути null)
        """
        for col in self.columns:
            if col.name not in data and not col.nullable:
                raise ValueError(f"Column '{col.name}' cannot be null")
            if col.name in data:
                col.validate(data[col.name])
        row = Row(data)
        row.id = self._id_counter
        self._id_counter += 1
        self.rows.append(row)
        return row

    def copy(self):
        """
        Створює глибоку копію таблиці, включаючи її стовпці та рядки.

        Повертає:
            Table: Копія таблиці
        """
        new_table = Table(self.name, deepcopy(self.columns))
        new_table.rows = deepcopy(self.rows)
        new_table._id_counter = self._id_counter
        return new_table

    def __iter__(self):
        """
        Повертає ітератор для перебору рядків таблиці.

        Повертає:
            iterator: Ітератор рядків таблиці
        """
        return iter(self.rows)

    def __str__(self):
        """Повертає рядкове представлення таблиці."""
        return f"Table({self.name}, {len(self.rows)} rows)"

    def __repr__(self):
        """Повертає програмне представлення таблиці."""
        return f"Table('{self.name}')"
