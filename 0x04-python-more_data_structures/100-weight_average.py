#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    den = 0
    for tple in my_list:
        num += tple[0] * tple[1]
        den += tple[1]
    return (num / den)
