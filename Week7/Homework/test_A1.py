import pytest
import A1_vowelsAndConsonants as A1

def test_get_one_vowel():
    word = 'word'
    vowels = A1.countVowels(word)
    assert 1 == vowels

def test_get_four_vowels():
    word = 'Mississippi'
    vowels = A1.countVowels(word)
    assert 4 == vowels

def test_get_three_consonants():
    word = 'TiTle'
    consonants = A1.countConsonants(word)
    assert 3 == consonants