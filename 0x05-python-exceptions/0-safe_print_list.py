#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    f = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            f += 1
    except:
        pass
    finally:
        print("")
        return f
