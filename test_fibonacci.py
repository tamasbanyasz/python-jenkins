import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    
    def test_zero(self):
        self.assertEqual(fibonacci(0), [])
        
    def test_one(self):
        self.assertEqual(fibonacci(1), [0])
        
    def test_two(self):
        self.assertEqual(fibonacci(2), [0, 1])
    
    def test_four(self):
        self.assertEqual(fibonacci(4), [0, 1, 1, 2])
        
    def test_five(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])

if __name__ == '__main__':
    unittest.main()
