#!/usr/bin/python3
for i in range(100):
    if (i % 10 <= i / 10):
        continue
    elif (i / 10 >= 8):
        print("{:02d}".format(i))
    else:
        print("{:02d}".format(i), end=", ")
