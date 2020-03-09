"""Lab 1: Expressions and Control Structures"""

# Q3
def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0 # You can replace this line!

# Q4
def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    L1 = [int(i) for i in str(n)]
    n1 = 0
    for i in L1:
        n1 += i
    return n1

print(sum_digits(12345))

def product_digits(n):
    'should be the same thing right? Just product instead'
    L1 = [int(i) for i in str(n)]
    n1 = 1
    for i in L1:
        n1 *= i
    return n1

def general_digists(n, func):
    """let's try making a general code, cuz why the hell not. Note that since the func is acting
    as a combine here, it will need to take in two arguments and return a single number. This
    func is assumed to be what-do-you-call-it-when-the-order-of-operating-doesn't-matter"""
    L1 = [int(i) for i in str(n)]
    n1 = L1[0]
    for i in L1[1:]:
        n1 = func(n1, i)
        print(n1)
    return n1

List1 = [1,2,3,4,5,6]

print(general_digists(12345, lambda x,y: x+y))
