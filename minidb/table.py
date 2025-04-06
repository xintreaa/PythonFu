from copy import deepcopy
from .row import Row

class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.rows = []
        self._id_counter = 1

    def insert(self, data):
        # Перевірка даних на відповідність стовпцям
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
        # Створюємо глибоку копію таблиці
        new_table = Table(self.name, deepcopy(self.columns))
        new_table.rows = deepcopy(self.rows)
        new_table._id_counter = self._id_counter
        return new_table

    def __iter__(self):
        return iter(self.rows)

    def __str__(self):
        return f"Table({self.name}, {len(self.rows)} rows)"

    def __repr__(self):
        return f"Table('{self.name}')"