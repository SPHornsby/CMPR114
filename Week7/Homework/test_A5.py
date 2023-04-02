import pytest
import A5_CaesarCipher as A5

def test_encode_with_13_UPPERS():
    shift = 13
    phrase = 'BEWARE THE IDES OF MARCH'
    res = A5.encode(phrase, shift)
    assert 'ORJNER GUR VQRF BS ZNEPU' == res

def test_encode_with_13_lowers():
    shift = 13
    phrase = 'beware the ides of march'
    res = A5.encode(phrase, shift)
    assert 'orjner gur vqrf bs znepu' == res