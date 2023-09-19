#!/usr/bin/python3
def roman_to_int(roman_string):
    romantoint = {
            'I': 1, 'V': 5,
            'X': 10, 'L': 50,
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
            if i != length - 1:
                if romantoint[roman_string[i]] < romantoint[
                        roman_string[i + 1]]:
                    res -= romantoint[roman_string[i]]
                else:
                    res += romantoint[roman_string[i]]
            else:
                res += romantoint[roman_string[i]]
            i += 1
    return res
