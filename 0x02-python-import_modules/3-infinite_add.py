#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    argc = len(sys.argv)
    for i in range(1, argc):
        val = int(sys.argv[i])
        sum += val
    print(sum)

