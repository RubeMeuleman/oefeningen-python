import unittest
import main


class TestFunction(unittest.TestCase):
    # Oefening 1
    def test_full_name(self):
        # Test with valid first name and surname
        result = main.full_name("John", "Doe")
        self.assertEqual("John Doe", result)

    def test_empty_names(self):
        # Test with empty first name and surname
        result = main.full_name("", "")
        self.assertEqual("", result)

    def test_single_name(self):
        # Test with only a first name
        result = main.full_name("Alice", "")
        self.assertEqual("Alice", result)

    def test_whitespace_names(self):
        # Test with whitespace-only first name and a valid surname
        result = main.full_name("   ", "Smith")
        self.assertEqual("    Smith", result)


    # Oefening 2
    def test_normal_sentence(self):
        result = main.word_counter("Hello World!")
        self.assertEqual(2, result)

    def test_sentence_with_extra_white_spaces(self):
        result = main.word_counter("      I love Python     ")
        self.assertEqual(3, result)

    def test_empty_sentence(self):
        result = main.word_counter("")
        self.assertEqual(0, result)

    def test_int_given(self):
        result = main.word_counter(10)
        self.assertEqual(1, result)


    # Oefening 3
    def test_normal_list(self):
        result = main.average_number([1, 3])
        self.assertEqual(2, result)

    def test_long_list(self):
        result = main.average_number([15, 18, 2, 36, 12, 78, 5, 6, 9])
        self.assertEqual(20, result)

    def test_zero_list(self):
        result = main.average_number([0, 0, 0, 0, 0])
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
