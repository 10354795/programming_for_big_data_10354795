import unittest
from spellcheck import SpellChecker
class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.spellChecker = SpellChecker()
        self.spellChecker.load_words('spell.words')

    def test_spell_checker(self):
        self.assertTrue(self.spellChecker.check_word('zygotic'))  # Checks if (single) word is present in list
        failed_words = self.spellChecker.check_words('zygotic mistasdas tennyy elementary') # two incorrect words
        self.assertEquals(2, len(failed_words))  # Checks that failed_words has two entries, i.e. mistasdas and tennyy
        print ('Contents of failed words array ', failed_words)   # print failed_words array to see what's in it.
        self.assertEquals('mistasdas', failed_words[0]['word'])  # Checks that the zero'th failed word in the array is mistasda
        self.assertEquals('tennyy', failed_words[1]['word'])  # checks that the 2nd failed word (in Position 1) is tennyy
        self.assertEquals({'line':1, 'word':'mistasdas', 'pos': 9}, failed_words[0]) # checks the line number, word (mistasdas) and caret position are correct 
        self.assertEquals({'line':1, 'word':'tennyy', 'pos': 19}, failed_words[1]) # checks the line number, word (tenny) and caret position are correct 
        self.assertEquals(1, failed_words[0]['line'])  # Checks that the zero'th failed (mistasdas) word occurs on line 1
        self.assertEquals(19, failed_words[1]['pos'])    # checks that the 2nd failed word occurs at caret position 19
        self.assertEquals(0, len(self.spellChecker.check_words('our first correct sentence'))) # checks that lebgth of array is 0, i.e. includes no failed words

        # handle case sensitivity
        self.assertEquals(0, len(self.spellChecker.check_words('Our first correct sentence')))
        # handle full stop
        self.assertEquals(0, len(self.spellChecker.check_words('Our first correct sentence.')))

        failed_words = self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary')
        print ('Contents of failed words array ', failed_words)   # print failed_words array to see what's in it.
        self.assertEquals(2, len(failed_words)) # Checks that array length is 2, i.e. has two failed words
        self.assertEquals('mistasdas', failed_words[0]['word'])
        self.assertEquals(1, failed_words[0]['line'])  # Checks that the zero'th failed (mistasdas) word occurs on line 1
        self.assertEquals(9, failed_words[0]['pos'])    # checks that the zero'th failed word occurs at caret position 9
        self.assertEquals('spelllleeeing', failed_words[1]['word']) # checks the 2nd word in the failed words array
        self.assertEquals(1, failed_words[1]['line'])  # Checks that the 2nd failed (spelllleeeing) word occurs on line 1
        self.assertEquals(19, failed_words[1]['pos'])    # checks that the 2nd failed word occurs at caret position 19

        self.assertEquals({'line':1, 'word':'mistasdas', 'pos': 9}, failed_words[0])  # Checks the contents of zero'th position in failed words array
        self.assertEquals({'line':1, 'word':'spelllleeeing', 'pos': 19}, failed_words[1]) # Checks the contents of 2ND position in failed words array

        # more bugs because the spell checker doesn’t spell check itself correctly – 0 entries when .lower is used – dictionary words need to be lower
        self.assertEqual(0, len(self.spellChecker.check_document('spell.words')))

        
if __name__ == '__main__':
    unittest.main()

