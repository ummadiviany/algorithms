import unittest
from naive_poly_mult import naive_poly_mult
from fft_poly_mult import inbuilt_fft_poly_mult
from fft_poly_mult import fft_poly_mult

class TestNaiveMult(unittest.TestCase):
    def test_two_elements(self):
        inp = [[1,2,3],[2,1,4]]
        self.assertEqual(fft_poly_mult(inp[0],inp[1]), 
        inbuilt_fft_poly_mult(inp[0],inp[1]))
    def test_different_lengths(self):
        inp = [[1,2,3,4,5],[2,1,4]]
        self.assertEqual(fft_poly_mult(inp[0],inp[1]), 
        inbuilt_fft_poly_mult(inp[0],inp[1]))
    def test_single_element(self):
        inp = [[1],[2]]
        self.assertEqual(fft_poly_mult(inp[0],inp[1]), 
        inbuilt_fft_poly_mult(inp[0],inp[1]))

if __name__ == "__main__":
    unittest.main()