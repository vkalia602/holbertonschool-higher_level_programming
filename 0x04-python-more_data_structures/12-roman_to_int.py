#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    idx = len(roman_string) - 1
    total = 0
    if not roman_string or roman_string is None:
        return 0

    while (idx >= 0):
        if idx > 0 and roman[roman_string[idx]] > roman[roman_string[idx - 1]]:
            total += roman[roman_string[idx]] - roman[roman_string[idx - 1]]
            idx -= 2
        else:
            total += roman[roman_string[idx]]
            idx -= 1
    return total
