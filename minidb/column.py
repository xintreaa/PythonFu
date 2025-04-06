class Column:
    """Клас для представлення стовпця таблиці."""

    def __init__(self, name, data_type, nullable=True):
        """
        Ініціалізує стовпець з іменем, типом даних та можливістю містити NULL.

        Args:
            name (str): Назва стовпця
            data_type (DataType): Тип даних стовпця
            nullable (bool, optional): Чи може стовпець містити значення NULL
        """
        self.name = name
        self.data_type = data_type
        self.nullable = nullable

    def validate(self, value):
        """
        Перевіряє, чи відповідає значення типу даних стовпця.

        Args:
            value: Значення для перевірки

        Returns:
            bool: True, якщо значення відповідає типу, інакше False
        """
        if value is None and not self.nullable:
            return False
        if value is None:
            return True
        return self.data_type.validate(value)

    def __str__(self):
        """Повертає рядкове представлення стовпця."""
        nullable_str = "NULL" if self.nullable else "NOT NULL"
        return f"Column({self.name}, {self.data_type}, {nullable_str})"

    def __repr__(self):
        """Повертає програмне представлення стовпця."""
        return f"Column('{self.name}', {repr(self.data_type)}, nullable={self.nullable})"