from lab03 import *

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y*10+x%10
    while x > 0:
        x, y = x//10, f()
    return y == n

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n==1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)


def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        "*** YOUR CODE HERE ***"
        if n==i:
            print(i)
        else:
            print(i)
            return counter(i+1) 
    counter(1)

def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    "*** YOUR CODE HERE ***"
    if b==0:
        return c
    else:
        return a+ab_plus_c(a,b-1,c)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def test(i):
        if n==i:
            return True
        elif n%i==0:
            return False
        else:
            return test(i+1)
    return test(2)

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    def helper(i):
        if n==i:
            if i%2 != 0:
                return odd_term(i)
            else:
                return even_term(i)   
        elif i%2 != 0:
            return odd_term(i)+helper(i+1)
        else:
            return even_term(i)+helper(i+1)
    return helper(1)
# def ten_pairs(n):
#     """Return the number of ten-pairs within positive integer n.

#     >>> ten_pairs(7823952)
#     3
#     >>> ten_pairs(55055)
#     6
#     >>> ten_pairs(9641469)
#     6
#     """
#     "*** YOUR CODE HERE ***"
#     a=[]
#     while n>0:
#         a.append(n%10)
#         n=n//10
#     i,j,result=0,1,0
#     while i<len(a):
#         j=i+1
#         while j<len(a):
#             if a[i]+a[j]==10:
#                 result += 1
#             j=j+1
#         i=i+1
#     return result

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def helper(i,n):
        if n<10:
            return n==i
        else:
            return (n%10==i) + helper(i,n//10)
    if n<10:
        return 0
    else:
        return helper(10-n%10,n//10)+ten_pairs(n//10)

# print(ten_pairs_recur(55055))
# print(ten_pairs_recur(9641469))

