import unittest

class DummyTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_dummy(self):
        assert 1 == 1

if __name__ == "__main__":
    unittest.main()
