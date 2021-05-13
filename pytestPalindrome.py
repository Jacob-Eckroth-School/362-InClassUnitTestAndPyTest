#testing with palindrome
import palindrome

def test_successful_palindrome():
    assert palindrome.isPalindrome("RaCeCar")

def test_successful_empty_palindrome():
    assert palindrome.isPalindrome("")
def test_unsuccessful_palindrome():
    assert palindrome.isPalindrome("   thisisn'tapalindrome")
    