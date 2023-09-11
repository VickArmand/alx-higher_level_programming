#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if (argc < 1):
        print(f"{argc} arguments.")
    elif (argc == 1):
        print(f"{argc} argument:")
    else:
        print(f"{argc} arguments:")
    if (argc > 0):
        for i in range(1, argc + 1):
            print(f"{i}: {sys.argv[i]}")
