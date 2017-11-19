HW_SOURCE_FILE = 'hw04.py'

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n<=3:
        return n
    else:
        return g(n-1)+2*g(n-2)+3*g(n-3)
def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    i=3
    if n<=3:
        return n
    else:
        curr,lag1,lag2,lag3=0,3,2,1
        while i<n:
            curr=lag1+2*lag2+3*lag3
            lag1,lag2,lag3=curr,lag1,lag2
            i+=1
        return curr

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
    "*** YOUR CODE HERE ***"
    if n==1:
        return n
    else:
        return pingpong(n-1)+help(n-1)
def help(n):
    if n==1:
        return n
    elif n%7!=0 and has_seven(n) is False:
        return help(n-1)
    else:
        return help(n-1)*(-1)

def pingpong1(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong1(7)
    7
    >>> pingpong1(8)
    6
    >>> pingpong1(15)
    1
    >>> pingpong1(21)
    -1
    >>> pingpong1(22)
    0
    >>> pingpong1(30)
    6
    >>> pingpong1(68)
    2
    >>> pingpong1(69)
    1
    >>> pingpong1(70)
    0
    >>> pingpong1(71)
    1
    >>> pingpong1(72)
    0
    >>> pingpong1(100)
    2
    """
    i,curr,sig=1,1,1
    while i<n:
        if i%7!=0 and has_seven(i) is False:
            sig=sig
            curr=curr+1*sig
            i=i+1
        else:
            sig=-sig
            curr=curr+1*sig
            i=i+1
    return curr

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
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

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
    """
    "*** YOUR CODE HERE ***"
    
    return counting(amount,1)

def counting(amount,m):
    if amount==0:
        return 1
    elif amount<0:
        return 0
    elif amount<m:
        return 0
    else:
        return counting(amount-m,m)+counting(amount,m*2)      
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
    return lambda m:lam
