"""Main tests."""

from wildcard_matching import is_match


def test_sample1():
    """
    Test if the string s = `"aa"` matches the pattern `p` = `"a"`.
    """
    assert is_match("aa", "a") is False


def test_sample2():
    """
    Test if the string s = `"aa"` matches the pattern `p` = `"*"`.
    """
    assert is_match("aa", "*") is True


def test_sample3():
    """
    Test if the string s = `"cb"` matches the pattern `p` = `"?a"`.
    """
    assert is_match("cb", "?a") is False


def test_sample4():
    """
    Test if the string s = `"abcdefgt"` matches the pattern `p` = `"ab?def*"`.
    """
    assert is_match("abcdefgt", "ab?def*") is True


def test_sample5():
    """
    Test if the string s = `"abcdefgt"` matches the pattern `p` = `"ab?def*t"`.
    """
    assert is_match("abcdefgt", "ab?def*t") is True


def test_sample6():
    """
    Test if the string s = `"abcdefgt"` matches the pattern `p` = `"ab?def*t***"`.
    """
    assert is_match("abcdefgt", "ab?def*t***") is True
