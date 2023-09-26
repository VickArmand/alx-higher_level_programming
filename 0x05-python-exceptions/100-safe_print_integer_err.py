#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        sys.stderr.write(f"Exception: {ve}\n")
        return False
    return True
