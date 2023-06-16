def starts_with(a, b):
    k = len(a)-len(b)
    if a[k:] == b:
        return True
    else:
        return False
print(starts_with("hithere", "thekre"))