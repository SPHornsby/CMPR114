import pytest

import login

def test_short_password():
    password = '12Dd'
    is_valid = login.valid_password(password)
    assert is_valid == False

def test_no_uppers():
    password = 'aaa123aaaaaa'
    is_valid = login.valid_password(password)
    assert is_valid == False

def test_no_lowers():
    password = 'AAAA123AAAA'
    is_valid = login.valid_password(password)
    assert is_valid == False

def test_no_digits():
    password = 'abcdABCD'
    is_valid = login.valid_password(password)
    assert is_valid == False

def test_good_pw():
    password = 'abcdABCD1234'
    is_valid = login.valid_password(password)
    assert is_valid == True