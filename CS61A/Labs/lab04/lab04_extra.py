""" Lab 04 Optional Questions """

from lab04 import *


this_file = __file__

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> check(this_file, 'hailstone',
    ...       ['While', 'For'])
    True
    """
    def the_real_hailstone(num, itr):
        num = int(num)
        print(num)
        if num == 1:
            return itr
        else:
            if num % 2:
                return the_real_hailstone((num*3)+1, itr + 1)
            else:
                return the_real_hailstone(num/2, itr + 1)
    return the_real_hailstone(n, 1)

print(hailstone(5))
