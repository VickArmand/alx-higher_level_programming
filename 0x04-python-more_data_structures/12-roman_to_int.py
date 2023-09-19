#!/usr/bin/python3
def roman_to_int(roman_string):
    romantoint = {
            'I': 1, 'IV': 4, 'V': 5,
            'IX': 9, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}
    res = 0
    if roman_string in romantoint.keys():
        return romantoint[roman_string]
    elif not isinstance(roman_string, str) or not roman_string:
        return res
    else:
        i = 0
        length = len(roman_string)
        while i < length:
            print(res)
            if roman_string[(i - length):] == 'IV' or roman_string[
                    (i - length):] == 'IX':
                res += romantoint[roman_string[(i - length):]]
                i += 2
            elif roman_string[i] in romantoint.keys():
                res += romantoint[roman_string[i]]
                i += 1
    return res
