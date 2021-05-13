import re
def wordCount(userEntry):
    if not isinstance(userEntry,str):
        return -1
    separatedWords = re.split('\s',userEntry)
    while("" in separatedWords) :
        separatedWords.remove("")
    return len(separatedWords)





def main():
    userEntry = input("Enter a string to count the number of words:")
    userEntry = userEntry[:-1]  #Everything except newline
    result = wordCount(userEntry)
    print(result)


if __name__ == "__main__":
    main()