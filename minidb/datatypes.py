from datetime import datetime


class DataType:
    """Базовий клас для всіх типів даних."""

    def validate(self, value):
        """
        Перевіряє відповідність значення типу даних.

        Args:
            value: Значення для перевірки

        Returns:
            bool: True, якщо значення відповідає типу, інакше False
        """
        raise NotImplementedError("Підкласи повинні реалізувати цей метод")

    def __str__(self):
        """Повертає рядкове представлення типу даних."""
        return self.__class__.__name__

    def __repr__(self):
        """Повертає програмне представлення типу даних."""
        return f"{self.__class__.__name__}()"


class IntegerType(DataType):
    """Тип даних для цілих чисел."""

    def validate(self, value):
        """
        Перевіряє, чи є значення цілим числом.

        Args:
            value: Значення для перевірки

        Returns:
            bool: True, якщо значення є цілим числом, інакше False
        """
        if value is None:
            return True
        return isinstance(value, int)

    def __repr__(self):
        return "IntegerType()"


class StringType(DataType):
    """Тип даних для рядків."""

    def __init__(self, max_length=None):
        """
        Ініціалізує тип даних для рядків.

        Args:
            max_length (int, optional): Максимальна довжина рядка
        """
        self.max_length = max_length

    def validate(self, value):
        """
        Перевіряє, чи є значення рядком і відповідає максимальній довжині.

        Args:
            value: Значення для перевірки

        Returns:
            bool: True, якщо значення є рядком і відповідає обмеженням, інакше False
        """
        if value is None:
            return True
        if not isinstance(value, str):
            return False
        if self.max_length is not None and len(value) > self.max_length:
            return False
        return True

    def __repr__(self):
        """Повертає програмне представлення типу даних."""
        return f"StringType(max_length={self.max_length})"


class BooleanType(DataType):
    """Тип даних для логічних значень."""

    def validate(self, value):
        """
        Перевіряє, чи є значення логічним.

        Args:
            value: Значення для перевірки

        Returns:
            bool: True, якщо значення є логічним, інакше False
        """
        if value is None:
            return True
        return isinstance(value, bool)

    def __repr__(self):
        return "BooleanType()"


class DateType(DataType):
    """Тип даних для дат."""

    def validate(self, value):
        """
        Перевіряє, чи є значення датою.

        Args:
            value: Значення для перевірки

        Returns:
            bool: True, якщо значення є датою, інакше False
        """
        if value is None:
            return True
        return isinstance(value, datetime)

    def __repr__(self):
        return "DateType()"