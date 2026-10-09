import unittest
from main import to_upper


class TestMain(unittest.TestCase):
    def test_to_upper(self):
        self.assertEqual(to_upper("hello"), "HELLO")
        self.assertEqual(to_upper("world"), "WORLD")


if __name__ == '__main__':
    unittest.main()
