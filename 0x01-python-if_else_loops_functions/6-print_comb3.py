#!/usr/bin/python3
for i in range(100):
    if (i % 10 == i / 10):
        continue
    else:
        print("{:02d}".format(i), end=", ")
