import unittest
from binary_search_iter import binary_search

class TestBinarySearch(unittest.TestCase):
   
    def setUp(self):
        self.arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_first(self):
        self.assertEqual(binary_search(self.arr, 1), 0, "Failed to search for first element")
        
    def test_lower_half(self):
        self.assertEqual(binary_search(self.arr, 3), 2, "Failed to search for element in lower half")
        
    def test_middle(self):
        self.assertEqual(binary_search(self.arr, 6), 5, "Failed to search for mid element")
        
    def test_upper_half(self):
        self.assertEqual(binary_search(self.arr, 9), 8, "Failed to search for upper half element")
        
    def test_last(self):
        self.assertEqual(binary_search(self.arr, 10), 9, "Failed to search for last element")
        
    def test_below_first(self):
        self.assertEqual(binary_search(self.arr, -1), None, "Incorrect result for search below first element")
        
    def test_above_last(self):
        self.assertEqual(binary_search(self.arr, 12), None, "Incorrect result 2 for search above last element")
        
if __name__ == "__main__":
    tests = TestBinarySearch()
    
    tests_loaded = unittest.TestLoader().loadTestsFromModule(tests)
    
    unittest.TextTestRunner().run(tests_loaded)

 