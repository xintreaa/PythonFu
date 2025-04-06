from route_decorator import route
from models import User

@route("/users/create")
def create_user(data):
    """Створення нового користувача з наданими даними.

    Параметри:
        data (dict): Дані для створення користувача, які передаються як аргументи.

    Повертає:
        dict: Представлення нового користувача у вигляді словника.
    """
    user = User.create(**data)
    return user.to_dict()

@route("/users/get")
def get_user(user_id):
    """Отримання користувача за його ID.

    Параметри:
        user_id (int): ID користувача, якого потрібно отримати.

    Повертає:
        dict: Дані користувача у вигляді словника або повідомлення про помилку, якщо користувача не знайдено.
    """
    user = User.get(user_id)
    if user:
        return user.to_dict()
    return {"error": "User not found"}

@route("/users/update")
def update_user(user_id, data):
    """Оновити дані користувача за його ID з наданими даними.

    Параметри:
        user_id (int): ID користувача, якого потрібно оновити.
        data (dict): Дані для оновлення користувача.

    Повертає:
        dict: Оновлені дані користувача у вигляді словника або повідомлення про помилку, якщо оновлення не вдалося.
    """
    user = User.update(user_id, **data)
    if user:
        return user.to_dict()
    return {"error": "User not found or update failed"}

@route("/users/delete")
def delete_user(user_id):
    """Видалити користувача за його ID.

    Параметри:
        user_id (int): ID користувача, якого потрібно видалити.

    Повертає:
        dict: Повідомлення про успішне видалення користувача або помилку, якщо видалення не вдалося.
    """
    result = User.delete(user_id)
    if result:
        return {"success": True, "message": f"User {user_id} deleted"}
    return {"error": "User not found or delete failed"}
