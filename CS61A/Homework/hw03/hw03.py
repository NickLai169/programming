HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

from operator import add, mul, sub

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'has_seven',
    ...       ['Assign', 'AugAssign'])
    True
    """
    if k % 10 == 7:
        return True
    elif k % 10 == 0:
        return False
    else:
        return has_seven(k//10)
#DONE

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """

    def bing_bong(num, itr, posneg):
        if (itr+1) == n:
            #print('this', num)
            return num

        elif (not (itr+1)%7) or has_seven((itr+1)):
            if posneg == '+':
                #print(num)
                return bing_bong(num-1, (itr+1), '-')
            else:
                #print(num)
                return bing_bong(num+1, (itr+1), '+')
        else:
            if posneg == '+':
                #print(num)
                return bing_bong(num+1, (itr+1), '+')
            else:
                #print(num)
                return bing_bong(num-1, (itr+1), '-')

    return bing_bong(1, 0, '+')
#DONE

def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument, associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    """
    total, k = base, 1
    while k <= n:
        total, k = combiner(total, term(k)), k + 1
    return total
#idk if i need to do this

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    streets = abs(street(a) - street(b))
    avenues = abs(avenue(a) - avenue(b))
    return streets+avenues
# DONE


def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    L1 = []
    def sqrt(x):
        return x**(1/2)

    for i in s:
        if round(sqrt(i))**2 == i:
            L1.append(round(sqrt(i)))
    return L1
# DONE

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    def pow_of_2(n1):
        'remember, pow_of_2() should always have 1 on the inside'
        if 2*n1 <= amount:
            return pow_of_2(2*n1)
        return n1

    def the_real_count_change(num, change):
        if num == 0:
            #print('perf 0')
            return 1
        elif change == 1:
            #print('got 1')
            return 1
        elif num - change < 0:
            return the_real_count_change(num, change/2)
        else:
            #print('a is ', num-change, change, '| b is ', num, change/2)
            return the_real_count_change(num-change, change) + the_real_count_change(num, change/2)

    #print('amount is ', amount, '| powerchange is ', pow_of_2(1))
    return(the_real_count_change(amount, pow_of_2(1)))
# DONE

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"

    a = start
    c = end
    b = 6-a-c

    if n == 1:
        print_move(a,c)
    elif n == 2:
        print_move(a,b)
        print_move(a,c)
        print_move(b,c)
    else:
        if n%2 == 0:
            move_stack(n-1, a, c)
            print_move(a,b)
            move_stack(n-1, c, a)
            print_move(b,c)
            move_stack(n-1, a, c)
        else:
            move_stack(n-1, a, b)
            print_move(a,c)
            move_stack(n-1, b, c)
# DONE

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # return lambda x: 1 if x == 1 else lambda y: i for i in range(1,y+1)
    '''Note that I didn't actually finish this question, I don't know how to call upon something
    that doesn't have a name XD'''
