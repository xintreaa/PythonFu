_routes = {}

def route(path):
    """Декоратор для реєстрації маршрутів."""
    def decorator(func):
        _routes[path] = func
        return func
    return decorator

def handle_request(path, **kwargs):
    """Обробляє запит за шляхом."""
    func = _routes.get(path)
    if func:
        return func(**kwargs)
    raise ValueError(f"No route found for path: {path}")