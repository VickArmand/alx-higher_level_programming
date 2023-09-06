#!/usr/bin/python3
def islower(c):
    islow = False
    for i in range(97, 123):
        if (ord(c) == i):
            islow = True
            break
    return islow
