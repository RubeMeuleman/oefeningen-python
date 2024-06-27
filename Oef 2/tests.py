import unittest
import main


class TestFunction(unittest.TestCase):
    # Oefening 1
    def test_small_list(self):
        result = main.word_breaker("leetcode", ["leet", "code"])
        self.assertEqual(True, result)

    def test_word_with_space(self):
        result = main.word_breaker("hello       world", ["hello", "world"])
        self.assertEqual(True, result)

    def test_scrambled_list(self):
        result = main.word_breaker("Rube Meuleman", ["John", "Meuleman", "Doe", "Rube"])
        self.assertEqual(True, result)

    def test_reversed_list(self):
        result = main.word_breaker("I love python!", ["python!", "I love"])
        self.assertEqual(True, result)

    def test_fase_list(self):
        result = main.word_breaker("I love python!", ["Ilove", "python!"])
        self.assertEqual(False, result)


    # Oefening 2
    def test_basic_sorting(self):
        result = main.bertje_zijn_boodschappenlijst(["appels", "bananen", "peren"])
        self.assertEqual(["peren", "appels", "bananen"], result)

    def test_empty_list(self):
        result = main.bertje_zijn_boodschappenlijst([])
        self.assertEqual([], result)

    def test_same_list(self):
        result = main.bertje_zijn_boodschappenlijst(["Peren", "appels", "Bananen"])
        self.assertEqual(["Peren", "appels", "Bananen"], result)

    def test_duplicates(self):
        result = main.bertje_zijn_boodschappenlijst(["aap", "noot", "mies", "aap", "noot", "mies"])
        self.assertEqual(["aap", "aap", "noot", "mies", "noot", "mies"], result)



if __name__ == '__main__':
    unittest.main()