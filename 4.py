def find_last_not_of(a, b):
    list_a = list(a)
    list_a.reverse()
    for i in list_a:
        if i in list_a and i not in b:
            return i
        else:
            return None
print(find_last_not_of("hip", ["h", "i"]))
