from .row import Row


class SimpleQuery:
    """Клас для виконання простих запитів до таблиці."""

    def __init__(self, table):
        """
        Ініціалізує запит до таблиці.

        Параметри:
            table (Table): Таблиця для запиту
        """
        self.table = table
        self.selected_columns = None
        self.filter_conditions = []
        self.sort_column = None
        self.sort_ascending = True

    def select(self, columns):
        """
        Вибирає стовпці для включення в результат.

        Параметри:
            columns (list): Список назв стовпців

        Повертає:
            SimpleQuery: Поточний об'єкт запиту для ланцюжка
        """
        self.selected_columns = columns
        return self  # Повертаємо self для ланцюжка

    def where(self, column, operator, value):
        """
        Додає умову фільтрації.

        Параметри:
            column (str): Назва стовпця
            operator (str): Оператор порівняння ("=", ">", "<", ">=", "<=")
            value: Значення для порівняння

        Повертає:
            SimpleQuery: Поточний об'єкт запиту для ланцюжка
        """
        self.filter_conditions.append((column, operator, value))
        return self

    def order_by(self, column, ascending=True):
        """
        Встановлює сортування результатів.

        Параметри:
            column (str): Назва стовпця для сортування
            ascending (bool, optional): Напрямок сортування

        Повертає:
            SimpleQuery: Поточний об'єкт запиту для ланцюжка
        """
        self.sort_column = column
        self.sort_ascending = ascending
        return self

    def execute(self):
        """
        Виконує запит і повертає результати.

        Повертає:
            list: Список об'єктів Row, що відповідають запиту
        """
        # Фільтруємо рядки за умовами where
        filtered_rows = []
        for row in self.table:
            matches_all_conditions = True
            # Перевіряємо кожну умову фільтрації
            for column, operator, value in self.filter_conditions:
                row_value = row[column]

                # Пропускаємо рядки, які не відповідають умові
                if operator == "=" and row_value != value:
                    matches_all_conditions = False
                    break
                elif operator == ">" and not (row_value > value):
                    matches_all_conditions = False
                    break
                elif operator == "<" and not (row_value < value):
                    matches_all_conditions = False
                    break
                elif operator == ">=" and not (row_value >= value):
                    matches_all_conditions = False
                    break
                elif operator == "<=" and not (row_value <= value):
                    matches_all_conditions = False
                    break

            # Якщо рядок відповідає всім умовам, додаємо його
            if matches_all_conditions:
                filtered_rows.append(row)

        # Сортуємо результати, якщо вказано
        if self.sort_column:
            filtered_rows.sort(
                key=lambda r: r[self.sort_column] if r[self.sort_column] is not None else "",
                reverse=not self.sort_ascending
            )

        # Вибираємо тільки потрібні стовпці
        results = []
        for row in filtered_rows:
            if self.selected_columns:
                # Створюємо новий рядок тільки з вибраними стовпцями
                new_row_data = {col: row[col] for col in self.selected_columns if col in row.keys()}
                new_row = Row(new_row_data)
                new_row.id = row.id  # Зберігаємо ідентифікатор
                results.append(new_row)
            else:
                # Якщо стовпці не вказані, беремо всі
                results.append(row)

        return results


class JoinedTable:
    """Клас для з'єднання двох таблиць."""

    def __init__(self, left_table, right_table, left_column, right_column):
        """
        Ініціалізує з'єднання таблиць.

        Параметри:
            left_table (Table): Ліва таблиця
            right_table (Table): Права таблиця
            left_column (str): Назва стовпця лівої таблиці для з'єднання
            right_column (str): Назва стовпця правої таблиці для з'єднання
        """
        self.left_table = left_table
        self.right_table = right_table
        self.left_column = left_column
        self.right_column = right_column
        self.rows = self._join()

    def _join(self):
        """
        Виконує з'єднання таблиць.

        Повертає:
            list: Список об'єктів Row з об'єднаними даними
        """
        joined_rows = []
        for left_row in self.left_table:
            left_value = left_row[self.left_column]
            for right_row in self.right_table:
                right_value = right_row[self.right_column]
                if left_value == right_value:
                    # Об'єднуємо дані з обох рядків
                    joined_data = {}

                    # Додаємо дані з лівої таблиці
                    for key, value in left_row.items():
                        joined_data[f"{self.left_table.name}.{key}"] = value

                    # Додаємо дані з правої таблиці
                    for key, value in right_row.items():
                        joined_data[f"{self.right_table.name}.{key}"] = value

                    joined_row = Row(joined_data)
                    joined_row.id = left_row.id  # Використовуємо id з лівої таблиці
                    joined_rows.append(joined_row)

        return joined_rows

    def __len__(self):
        """
        Повертає кількість рядків в об'єднаній таблиці.

        Повертає:
            int: Кількість рядків
        """
        return len(self.rows)

    def __iter__(self):
        """
        Повертає ітератор по рядках об'єднаної таблиці.

        Повертає:
            iterator: Ітератор рядків
        """
        return iter(self.rows)
