def starts_with(a, b):
    k = len(a)-len(b)
    if len(a) < len(b):
        return False
    elif a[:(k-1)] == b:
        return True
    else:
        return False
print(starts_with("hi", "hit"))

