import unittest
import file

class TestFile(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testGetPathsReturnType(self):
        self.assertEqual(isinstance(file.getPaths(r"e:\todolist"), list), True, "False")
        
if __name__ == "__main__":
    unittest.main()