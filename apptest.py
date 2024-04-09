import unittest
from app import calculate_square_area


class TestAreaCalculation(unittest.TestCase):

    def test_calculate_square_area_positive(self):
        # Test cases for positive side lengths
        self.assertEqual(calculate_square_area(4), 16)
        self.assertEqual(calculate_square_area(0), 0)
        self.assertEqual(calculate_square_area(10), 100)

    # def test_calculate_square_area_negative(self):
    #     # Test cases for negative side lengths
    #     self.assertEqual(calculate_square_area(-4), 0)  # negative side length
    #     self.assertEqual(calculate_square_area(-10), 0)  # negative side length

    # def test_calculate_square_area_invalid_input(self):
    #     # Test case for invalid input (string)
    #     with self.assertRaises(TypeError):
    #         calculate_square_area("4")  # string input

    def test_calculate_square_area_student_id(self):
        # Test case for student ID (last two digits)
        student_id_last_two_digits = 00  # Replace this with your actual last two digits of your student ID
        self.assertEqual(calculate_square_area(student_id_last_two_digits), 00)  

if __name__ == '__main__':
    unittest.main()

