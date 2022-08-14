def is_unique_using_dict(s):
    s_chars_dict = {}
    for c in s:
        if c in s_chars_dict:
            return False
        else:
            s_chars_dict[c] = 1
    return True
