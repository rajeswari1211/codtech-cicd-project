import unittest
from app import greet


class TestApp(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(
            greet("Rajeswari"),
            "Hello, Rajeswari! Welcome to CODTECH CI/CD Project."
        )


if __name__ == "__main__":
    unittest.main()
