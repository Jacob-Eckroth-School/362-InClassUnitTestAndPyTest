

def isPalindrome(userEntry):
    #First put it into lowercase.
    lowerString = userEntry.lower()
    reversedEntry = lowerString[::-1]
    if(reversedEntry == lowerString):
        return True
    else:
        return False





def main():
    userEntry = input("Enter a string to determine if it is a palindrome:")
    result = isPalindrome(userEntry)
    if(result == True):
        print("It's a palindrome!")
    else:
        print("It's not a palindrome")

if __name__ == "__main__":
    main()