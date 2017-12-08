#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    x = len(sys.argv) - 1
    result = 0
    for x in range(1, x + 1):
        result += int(sys.argv[x])
    print(result)
