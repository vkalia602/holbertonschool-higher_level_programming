#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    tup1 = (('+', calculator_1.add), ('-', calculator_1.sub),
            ('*', calculator_1.mul), ('/', calculator_1.div))
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    for mem in tup1:
        if sys.argv[2] is mem[0]:
            result = mem[1](a, b)
            print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, result))
            exit(0)
    else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
