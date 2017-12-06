#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = (abs(number) % 10) * -1
else:
    n = number % 10
print("Last digit of {:d} is".format(number), end=" ")
if n > 5:
    print("{:d} and is greater than 5".format(n))
elif n == 0:
    print("{:d} and is 0".format(n))
else:
    print("{:d} and is less than 6 and not 0".format(n))
