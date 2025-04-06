from route_decorator import route
from models import BaseModelMeta

@route("/database/switch")
def switch_database(model_name, db_name):
    """Зміна бази даних для конкретної моделі.

    Параметри:
        model_name (str): Назва моделі, для якої потрібно змінити базу даних.
        db_name (str): Назва нової бази даних, яку потрібно використовувати.

    Повертає:
        dict: Відповідь у вигляді словника з результатом операції.
            Якщо зміна була успішною:
                {"success": True, "message": f"Switched {model_name} to {db_name} database"}
            Якщо модель не знайдена:
                {"error": f"Model {model_name} not found"}
    """
    model_class = BaseModelMeta.registry.get(model_name)
    if model_class:
        model_class.use_db(db_name)
        return {"success": True, "message": f"Switched {model_name} to {db_name} database"}
    return {"error": f"Model {model_name} not found"}
