#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    idx = len(roman_string) - 1
    while (idx >= 0):
        if idx > 0 and roman[roman_string[idx]] > roman[roman_string[idx - 1]]:
            total += roman[roman_string[idx]] - roman[roman_string[idx - 1]]
            idx -= 2
        else:
            total += roman[roman_string[idx]]
            idx -= 1
    return total
