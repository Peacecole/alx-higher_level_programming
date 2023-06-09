#!/usr/bin/python3
if __name__ == "__main__":
    """ imports the function def add(a, b): from the file add_0.p"""
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
