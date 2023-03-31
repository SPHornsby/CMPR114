import pytest
import A2_most_frequent as A2

def test_most_frequent_t():
    word = 'totalmente'
    res = A2.get_most_frequent(word)
    assert ['t'] == res

def test_most_frequent_s():
    word = 'dressers'
    res = A2.get_most_frequent(word)
    assert ['s'] == res