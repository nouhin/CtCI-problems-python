def is_permutation(s1, s2):
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    for i, c in enumerate(s1):
        if c != s2[i]:
            return False
    return True
