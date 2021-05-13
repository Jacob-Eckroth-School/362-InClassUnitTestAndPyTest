import palindrome
import unittest

class palindromeTestCase(unittest.TestCase):
    def test_empty(self):       #This test should succeed because an empty string is a palindrome.
        self.assertEqual(palindrome.isPalindrome(""),True)
    def test_normal(self):  #This test should succeed because racecar is a palindrome.
        self.assertEqual(palindrome.isPalindrome("racecar"),True)
    def test_notPalindrome(self):   #This test should fail. I am running this test because I want to make sure that my palindrome
                                    #Test works for things that are not palindromes. 
        self.assertEqual(palindrome.isPalindrome("Jacob Eckroth"),False)




if __name__ == "__main__":
    unittest.main()