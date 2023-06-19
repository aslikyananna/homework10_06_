def ends_with(a, b):
    k = len(a)-len(b)
    if k < 0:
        return False
    if a[k:] == b:
        return True
    else:
        return False
print(ends_with("hethere", "there"))



