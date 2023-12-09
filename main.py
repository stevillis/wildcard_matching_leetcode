"""Wildcard Matching - LeetCode problem solution."""


def is_char_equal(s: str, p: str) -> bool:
    """
    Check if `s` char is equal to `p` or `p` is the wildcard `?`.
    """
    if p == "?":
        return True

    return s == p


def is_match(s: str, p: str) -> bool:
    """
    Check if `s` string matches the `p` pattern.
    """
    s_index = 0
    p_index = 0
    p_star_index = -1
    s_star_index = -1

    while s_index < len(s):
        if p_index < len(p) and is_char_equal(s[s_index], p[p_index]):
            s_index += 1
            p_index += 1
        elif p_index < len(p) and p[p_index] == "*":
            p_star_index = p_index
            s_star_index = s_index

            p_index += 1
        elif s_star_index != -1:
            s_index = s_star_index + 1
            p_index = p_star_index + 1
            s_star_index += 1
        else:
            return False

    while p_index < len(p) and p[p_index] == "*":
        p_index += 1

    return p_index == len(p)
