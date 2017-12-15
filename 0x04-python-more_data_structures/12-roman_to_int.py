#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    total = 0
    if not roman_string or roman_string == None:
        return 0
    for idx in range(1, len(roman_string)):
        if roman[roman_string[idx - 1]] < roman[roman_string[idx]]:
            i += 1
    if i == 0:
        for idx in range(len(roman_string)):
            total += roman[roman_string[idx]]
    elif i < len(roman_string):
        for idx in range(i, len(roman_string)):
            total += roman[roman_string[idx]]
        for idx in range(0, i):
            total -= roman[roman_string[idx]]
    elif i == len(roman_string):
        for idx in range(i):
            total -= roman[roman_string[idx]]
    return total
