#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except (IndexError, ValueError, ZeroDivisionError) as ex:
        sys.stderr.write(f"Exception: {ex}\n")
        return None
    else:
        return res
