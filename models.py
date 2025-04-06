# models.py
from registry import DatabaseRegistry

class BaseModelMeta(type):
    """Метаклас, який реєструє всі моделі у внутрішньому реєстрі."""
    registry = {}

    def __new__(cls, name, bases, attrs):
        obj = super().__new__(cls, name, bases, attrs)
        if name != "BaseModel":  # Уникаємо реєстрації самого базового класу
            BaseModelMeta.registry[name] = obj
        return obj

class BaseModel(metaclass=BaseModelMeta):
    """Базова модель з підтримкою вибору бази даних."""
    _db_instance = None  # Will be initialized later

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items()}

    @classmethod
    def _ensure_db(cls):
        """Ensure we have a database instance."""
        if cls._db_instance is None:
            cls._db_instance = DatabaseRegistry.get("default")
            if cls._db_instance is None:
                raise ValueError("Default database not initialized. Make sure to register databases before using models.")

    @classmethod
    def use_db(cls, db_name):
        """Динамічно змінює базу даних для моделі."""
        db = DatabaseRegistry.get(db_name)
        if db:
            cls._db_instance = db
        else:
            raise ValueError(f"Database '{db_name}' not found")

    @classmethod
    def create(cls, **data):
        """Створює новий об'єкт у вибраній базі."""
        cls._ensure_db()  # Make sure we have a database
        obj_data = cls._db_instance.create(cls.__name__, data)
        return cls(**obj_data)

    @classmethod
    def get(cls, obj_id):
        """Отримує об'єкт за ID."""
        cls._ensure_db()  # Make sure we have a database
        obj_data = cls._db_instance.read(cls.__name__, obj_id)
        if obj_data:
            return cls(**obj_data)
        return None

    @classmethod
    def update(cls, obj_id, **data):
        """Оновлює об'єкт за ID."""
        cls._ensure_db()  # Make sure we have a database
        updated_data = cls._db_instance.update(cls.__name__, obj_id, data)
        if updated_data:
            return cls(**updated_data)
        return None

    @classmethod
    def delete(cls, obj_id):
        """Видаляє об'єкт за ID."""
        cls._ensure_db()  # Make sure we have a database
        return cls._db_instance.delete(cls.__name__, obj_id)

# Динамічні моделі
class User(BaseModel):
    pass

class Product(BaseModel):
    pass