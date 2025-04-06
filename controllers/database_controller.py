from route_decorator import route
from models import BaseModelMeta

@route("/database/switch")
def switch_database(model_name, db_name):
    """Switch the database used by a specific model."""
    model_class = BaseModelMeta.registry.get(model_name)
    if model_class:
        model_class.use_db(db_name)
        return {"success": True, "message": f"Switched {model_name} to {db_name} database"}
    return {"error": f"Model {model_name} not found"}