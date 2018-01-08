#!/usr/bin/python3
""" Prints first name and last name


"""


def say_my_name(first_name, last_name=""):

    """function to print first and last name

    """
    errormsg_fn = "first_name must be a string"
    errormsg_ln = "last_name must be a string"

# check for first name type
    if type(first_name) is not str:
        raise TypeError(errormsg_fn)

# check for last name type
    if type(last_name) is not str:
        raise TypeError(errormsg_ln)

#print first name and last name
    print("My name is {} ".format(first_name), end="")
    print("{}".format(last_name))
