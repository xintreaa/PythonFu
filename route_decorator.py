_routes = {}

def route(path):
    """Декоратор для реєстрації маршрутів.

    Цей декоратор дозволяє реєструвати функцію як обробник маршруту
    для конкретного шляху запиту.

    Args:
        path (str): Шлях маршруту, на який буде реагувати функція.

    Returns:
        function: Декорована функція, яка реєструється для зазначеного шляху.
    """
    def decorator(func):
        _routes[path] = func
        return func
    return decorator

def handle_request(path, **kwargs):
    """Обробляє запит за шляхом.

    Ця функція шукає обробник маршруту для зазначеного шляху
    та виконує його з переданими параметрами.

    Args:
        path (str): Шлях запиту, для якого потрібно знайти обробник.
        kwargs (dict): Додаткові параметри, які передаються обробнику.

    Returns:
        any: Результат виконання обробника маршруту.

    Raises:
        ValueError: Якщо для зазначеного шляху не знайдений обробник.
    """
    func = _routes.get(path)
    if func:
        return func(**kwargs)
    raise ValueError(f"No route found for path: {path}")
