def starts_with(a, b):
    k = len(a)-len(b)
    if len(a) < len(b):
        return False
    elif a[:len(b)] == b:
        return True
    else:
        return False

print(starts_with("hitt", "hit"))
