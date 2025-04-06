from registry import DatabaseRegistry

class BaseModelMeta(type):
    """Метаклас, який реєструє всі моделі у внутрішньому реєстрі."""
    registry = {}

    def __new__(cls, name, bases, attrs):
        """
        Створює новий клас і реєструє його у внутрішньому реєстрі моделей.

        Args:
            name (str): Назва класу.
            bases (tuple): Батьківські класи класу.
            attrs (dict): Атрибути класу.

        Returns:
            obj: Створений клас.
        """
        obj = super().__new__(cls, name, bases, attrs)
        if name != "BaseModel":  # Уникаємо реєстрації самого базового класу
            BaseModelMeta.registry[name] = obj
        return obj

class BaseModel(metaclass=BaseModelMeta):
    """Базова модель з підтримкою вибору бази даних."""
    _db_instance = None  # База даних буде ініціалізована пізніше

    def __init__(self, **kwargs):
        """
        Ініціалізує екземпляр моделі з переданими даними.

        Args:
            kwargs (dict): Дані для ініціалізації атрибутів моделі.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        """
        Перетворює екземпляр моделі в словник.

        Returns:
            dict: Словник, що містить атрибути екземпляра.
        """
        return {k: v for k, v in self.__dict__.items()}

    @classmethod
    def _ensure_db(cls):
        """
        Перевіряє, чи ініціалізована база даних для моделі.

        Підключає базу даних за замовчуванням, якщо вона ще не ініціалізована.

        Raises:
            ValueError: Якщо база даних не ініціалізована.
        """
        if cls._db_instance is None:
            cls._db_instance = DatabaseRegistry.get("default")
            if cls._db_instance is None:
                raise ValueError("Default database not initialized. Make sure to register databases before using models.")

    @classmethod
    def use_db(cls, db_name):
        """
        Змінює базу даних, яка використовується моделлю.

        Args:
            db_name (str): Назва бази даних для підключення.

        Raises:
            ValueError: Якщо база даних не знайдена.
        """
        db = DatabaseRegistry.get(db_name)
        if db:
            cls._db_instance = db
        else:
            raise ValueError(f"Database '{db_name}' not found")

    @classmethod
    def create(cls, **data):
        """
        Створює новий об'єкт у вибраній базі даних.

        Args:
            data (dict): Дані для створення нового об'єкта.

        Returns:
            BaseModel: Екземпляр створеного об'єкта.

        Raises:
            ValueError: Якщо база даних не ініціалізована.
        """
        cls._ensure_db()  # Перевірка на наявність бази даних
        obj_data = cls._db_instance.create(cls.__name__, data)
        return cls(**obj_data)

    @classmethod
    def get(cls, obj_id):
        """
        Отримує об'єкт з бази даних за його ID.

        Args:
            obj_id (int): Ідентифікатор об'єкта.

        Returns:
            BaseModel: Екземпляр об'єкта, або None, якщо об'єкт не знайдений.
        """
        cls._ensure_db()  # Перевірка на наявність бази даних
        obj_data = cls._db_instance.read(cls.__name__, obj_id)
        if obj_data:
            return cls(**obj_data)
        return None

    @classmethod
    def update(cls, obj_id, **data):
        """
        Оновлює об'єкт у базі даних за його ID.

        Args:
            obj_id (int): Ідентифікатор об'єкта.
            data (dict): Дані для оновлення.

        Returns:
            BaseModel: Екземпляр оновленого об'єкта, або None, якщо об'єкт не знайдений.
        """
        cls._ensure_db()  # Перевірка на наявність бази даних
        updated_data = cls._db_instance.update(cls.__name__, obj_id, data)
        if updated_data:
            return cls(**updated_data)
        return None

    @classmethod
    def delete(cls, obj_id):
        """
        Видаляє об'єкт з бази даних за його ID.

        Args:
            obj_id (int): Ідентифікатор об'єкта.

        Returns:
            bool: True, якщо об'єкт був успішно видалений, False в іншому випадку.
        """
        cls._ensure_db()
        return cls._db_instance.delete(cls.__name__, obj_id)

# Динамічні моделі
class User(BaseModel):
    """Модель для користувачів."""
    pass

class Product(BaseModel):
    """Модель для продуктів."""
    pass
