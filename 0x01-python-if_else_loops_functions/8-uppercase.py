#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            x = ord(str[i]) - 32
        else:
            x = ord(str[i])
        print("{}".format(chr(x)), end="")
    print("")
