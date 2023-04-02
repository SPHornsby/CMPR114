import pytest
import A3_wordSeparator as A3

def test_separator():
    phrase = 'StopAndSmellTheRoses'
    res = A3.break_into_words(phrase)
    assert 'Stop And Smell The Roses' == res