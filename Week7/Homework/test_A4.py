import pytest
import A4_piglatin as A4

def test_translate_word():
    word = 'SLEPT'
    res = A4.translate_word(word)
    assert 'LEPTSAY' == res

def test_translate_phrase():
    phrase = 'I SLEPT MOST OF THE NIGHT'
    res = A4.translate_phrase(phrase)
    assert 'IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY' == res
