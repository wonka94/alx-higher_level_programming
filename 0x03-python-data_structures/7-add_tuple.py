#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b
    c1 = 0
    c2 = 0
    if len(a) == 0:
        c1 += 0
        c2 += 0
    elif len(a) == 1:
        c1 += a[0]
        c2 += 0
    else:
        c1 += a[0]
        c2 += a[1]

    if len(b) == 0:
        c1 += 0
        c2 += 0
    elif len(b) == 1:
        c1 += b[0]
        c2 += 0
    else:
        c1 += b[0]
        c2 += b[1]
    return(c1, c2)
