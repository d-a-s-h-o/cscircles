def nestedListContains(NL, target):
    for x in NL:
        if isinstance(x, list):
            if nestedListContains(x, target):
                return True
        else:
            if x == target:
                return True
    return False
