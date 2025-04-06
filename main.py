
from minidb.database import Database
from registry import DatabaseRegistry

default_db = Database("default")
test_db = Database("test")
DatabaseRegistry.register("default", default_db)
DatabaseRegistry.register("test", test_db)


from route_decorator import handle_request
from controllers.user_controller import *

if __name__ == "__main__":
    print("=== Default Database ===")
    print(handle_request("/users/create", data={"name": "Alice", "email": "alice@example.com"}))
    print(handle_request("/users/create", data={"name": "Bob", "email": "bob@example.com"}))
    print(handle_request("/users/get", user_id=1))

    print("\n=== Switching to test database ===")
    print(handle_request("/database/switch", model_name="User", db_name="test"))

    print("\n=== Creating user in test database ===")
    print(handle_request("/users/create", data={"name": "Charlie", "email": "charlie@example.com"}))

    print("\n=== Getting users from different databases ===")
    User.use_db("default")
    print("Default DB:", handle_request("/users/get", user_id=1))  # Alice
    User.use_db("test")
    print("Test DB:", handle_request("/users/get", user_id=1))  # Charlie

    print("\n=== Updating user ===")
    print(handle_request("/users/update", user_id=1, data={"name": "Charlie Updated"}))

    print("\n=== Deleting user ===")
    User.use_db("default")
    print(handle_request("/users/delete", user_id=2))