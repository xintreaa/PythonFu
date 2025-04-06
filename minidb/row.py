class Row:
    """Клас для представлення рядка таблиці."""

    def __init__(self, data=None):
        """
        Ініціалізує рядок з даними.

        Args:
            data (dict, optional): Дані рядка у вигляді словника {назва_стовпця: значення}
        """
        self._data = data or {}
        self.id = None  # Ідентифікатор встановлюється таблицею

    def __getitem__(self, key):
        """
        Доступ до значення за назвою стовпця.

        Args:
            key (str): Назва стовпця

        Returns:
            Значення стовпця
        """
        return self._data.get(key, None)

    def __setitem__(self, key, value):
        """
        Встановлення значення за назвою стовпця.

        Args:
            key (str): Назва стовпця
            value: Нове значення
        """
        self._data[key] = value

    def __eq__(self, other):
        """
        Перевіряє рівність рядків.

        Args:
            other (Row): Інший рядок для порівняння

        Returns:
            bool: True, якщо рядки рівні, інакше False
        """
        if not isinstance(other, Row):
            return False
        return self.id == other.id and self._data == other._data

    def keys(self):
        """
        Повертає назви стовпців рядка.

        Returns:
            dict_keys: Ключі словника даних
        """
        return self._data.keys()

    def items(self):
        """
        Повертає пари (назва_стовпця, значення) рядка.

        Returns:
            dict_items: Елементи словника даних
        """
        return self._data.items()

    def __str__(self):
        """Повертає рядкове представлення рядка."""
        return f"Row(id={self.id}, data={self._data})"

    def __repr__(self):
        """Повертає програмне представлення рядка."""
        return f"Row(id={self.id}, data={self._data})"