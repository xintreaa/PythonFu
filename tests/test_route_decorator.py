import unittest
from route_decorator import route, handle_request

class TestRouteDecorator(unittest.TestCase):

    def setUp(self):
        @route("/test")
        def test_route():
            return "Test route executed"

    def test_handle_request(self):
        response = handle_request("/test")
        self.assertEqual(response, "Test route executed")

    def test_handle_request_nonexistent_route(self):
        with self.assertRaises(ValueError):
            handle_request("/nonexistent")

if __name__ == '__main__':
    unittest.main()