#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_score = 0
    key = None
    for k in a_dictionary.keys():
        if best_score < a_dictionary[k]:
            best_score = a_dictionary[k]
            key = k
    return key
