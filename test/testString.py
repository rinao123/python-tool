import unittest
import string


class TestString(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testIsStringLike(self):
        self.assertEqual(string.isStringLike("aaa"), True, "False")
        self.assertEqual(string.isStringLike(u"aaa"), True, "False")
        self.assertEqual(string.isStringLike(111), False, "False")


if __name__ == "__main__":
    unittest.main()