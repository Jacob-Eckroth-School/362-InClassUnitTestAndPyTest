import wordcount
import unittest

class wordcountTestCase(unittest.TestCase):
    def test_empty(self):   #Empty string should have 0 words
        self.assertEqual(wordcount.wordCount(""),0)
    def test_regular(self): #Testing with a normal string
        self.assertEqual(wordcount.wordCount("word1 word2,word2still word3 word4 word5"),5)
    def test_invalidInput(self):    #invalid data type should return a -1
        self.assertEqual(wordcount.wordCount(1),-1)



if __name__ == "__main__":
    unittest.main()