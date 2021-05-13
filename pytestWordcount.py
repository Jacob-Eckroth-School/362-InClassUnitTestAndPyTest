#testing with pytest
import wordcount

def test_successful_wordcount():
    assert wordcount.wordCount("oneword twoword,stilltwo,stilltwo-two threeword") == 3

def test_successful_empty_word():
    assert wordcount.wordCount("") == 0

def test_unsuccessful_wordcount():
    assert wordcount.wordCount("oneWord") != 1
    