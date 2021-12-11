import unittest
from translator import english_to_french, french_to_english

class TestENFR(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
        self.assertNotEqual(french_to_english('Love'), 'Au revoir')



class TestFREN(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
        self.assertNotEqual(french_to_english('Au revoir'), 'Love')


 
unittest.main()
