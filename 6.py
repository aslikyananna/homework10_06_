
def rotate_by(a=[1, 2, 3, 4], b=3):
    count_ = 0
    var = a[-1]
    while count_ < b:
        count_ += 1
        a.insert(0, var)
    del a[-1]
    return a

print(rotate_by())
