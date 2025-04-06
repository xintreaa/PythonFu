import unittest
from route_decorator import route, handle_request

class TestRouteDecorator(unittest.TestCase):

    def setUp(self):
        """
        Підготовка для тестування декоратора маршруту.
        Оголошуємо маршрут /test за допомогою декоратора.
        """
        @route("/test")
        def test_route():
            return "Test route executed"

    def test_handle_request(self):
        """
        Тестує обробку запиту до існуючого маршруту.

        Перевіряється, чи правильно обробляється запит до маршруту /test.
        Очікується повернення рядка "Test route executed".
        """
        response = handle_request("/test")
        self.assertEqual(response, "Test route executed")  # Перевірка відповіді на запит до /test

    def test_handle_request_nonexistent_route(self):
        """
        Тестує обробку запиту до неіснуючого маршруту.

        Перевіряється, чи виникає ValueError при запиті до маршруту, якого не існує.
        """
        with self.assertRaises(ValueError):  # Перевірка, що буде викликано ValueError
            handle_request("/nonexistent")

if __name__ == '__main__':
    unittest.main()
