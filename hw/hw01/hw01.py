from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a ** 2 + b ** 2 + c ** 2 - min(a, b, c) ** 2

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """

    # Method 1
    k = n - 1
    largest_factor = 1
    while k > 0:
        if n % k == 0:
            largest_factor = k
            break
        k -= 1
    return largest_factor

    # Method 2
    # k = 1
    # largest_factor = 1
    # while k < n:
    #     if n % k == 0:
    #         largest_factor = k
    #     k = k + 1
    # return largest_factor

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return False 
    

def t():
    return 1 / 0


def f():
    return 1

# Some explanation of the difference between if_function and if statement.
"""
The function with_if_function uses a call expression, which guarantees that 
all of its operand subexpressions will be evaluated before if_function is 
applied to the resulting arguments. Therefore, even if c returns False, 
the function t will be called. By contrast, with_if_statement will never 
call t if c returns False.
"""

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

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
    """
    k = 0
    while n > 0:
        k = k + 1
        print(n)
        if n == 1:
            break
        elif n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

    return k


