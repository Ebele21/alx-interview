#!/usr/bin/python3
"""
Module calculates the fewest num of
operations needed to result in exactly the
characters in the file.
"""

import math


def factors(n):
    """The factors of n number"""
    list_nums = []
    while n % 2 == 0:
        list_nums.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            list_nums.append(i)
            n = n / i
    if n > 2:
        list_nums.append(n)
    return list_nums


def minOperations(n):
    """It calculate minimum operations"""
    if type(n) != int or n < 2:
        return 0
    else:
        operations = sum(factors(n))
        return int(operations)
