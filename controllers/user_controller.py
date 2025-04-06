from route_decorator import route
from models import User

@route("/users/create")
def create_user(data):
    """Create a new user with the provided data."""
    user = User.create(**data)
    return user.to_dict()

@route("/users/get")
def get_user(user_id):
    """Get a user by ID."""
    user = User.get(user_id)
    if user:
        return user.to_dict()
    return {"error": "User not found"}

@route("/users/update")
def update_user(user_id, data):
    """Update a user by ID with the provided data."""
    user = User.update(user_id, **data)
    if user:
        return user.to_dict()
    return {"error": "User not found or update failed"}

@route("/users/delete")
def delete_user(user_id):
    """Delete a user by ID."""
    result = User.delete(user_id)
    if result:
        return {"success": True, "message": f"User {user_id} deleted"}
    return {"error": "User not found or delete failed"}