import unittest
from insertion_sort import insertion_sort
class Test_Sorting(unittest.TestCase):
    
    def test_empty(self):
        inp = []
        self.assertEqual(insertion_sort(inp),sorted(inp))
    def test_singel_element(self):
        inp = [1]
        self.assertEqual(insertion_sort(inp),sorted(inp))
    def test_two_elements(self):
        inp = [2, 1]
        self.assertEqual(insertion_sort(inp),sorted(inp))
    def test_three_elements(self):
        inp = [13, 7, 5]
        self.assertEqual(insertion_sort(inp),sorted(inp))
    def test_four(self):
        inp = [23, 7, 13, 5]
        self.assertEqual(insertion_sort(inp),sorted(inp))
    def test_large_nums(self):
        inp = [135604, 1000000, 45, 78435, 456219832, 2, 546]
        self.assertEqual(insertion_sort(inp),sorted(inp))
    def test_more_inps(self):
        inp = [1, 2, 2, 1, 0, 0, 15, 15]
        self.assertEqual(insertion_sort(inp),sorted(inp))
    

if __name__ == "__main__":
    unittest.main()