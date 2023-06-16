def find_last_not_of(a, b):
    for i in b:
        if i in b and i in a:
            index = a.index(i)
        return a[index-1]
    print(find_last_not_of("hithere", "i,o,e,k"))


