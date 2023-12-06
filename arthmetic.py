def sum(a, b):
    while b != 0:
        c = a & b
        a ^= b
        b = c << 1
    return a


def mult(a, b):
    if b == 0:
        return 0
    if b == 1:
        return a
    if b & 1:
        return sum(a, mult(a << 1, b >> 1))
    else:
        return mult(a << 1, b >> 1)


c = mult(100, 20)
print(c)
