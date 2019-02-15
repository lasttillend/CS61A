""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def cycle_num(n):
        def cycle_compose(x):
            result = x
            k = 1
            while k <= n:
                if k % 3 == 1:
                    result = f1(result)
                elif k % 3 == 2:
                    result = f2(result)
                else:
                    result = f3(result)
                k += 1
            return result
        return cycle_compose
    return cycle_num

## Lambda expressions

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
    f = lambda: 10 * y + x % 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)
# Method 1(using one parameter)
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
    def calculate(k):
        if k <= n ** 0.5:
            if n % k == 0: 
                return False
            else:
                return calculate(k + 1)
        else:
            return True

    return calculate(2)

# Method 2(using two parameters)
# k is current divisor to check.  
# def isPrime(n, k = 2): 
#     # Base cases 
#     if n <= 2: 
#         return True if n == 2 else False
#     if n % k == 0: 
#         return False
#     if k * k > n:   # tried all divisors to sqrt, must be prime
#         return True 
#     # Check for next divisor 
#     return isPrime(n, k + 1) 

# Method 1
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    def calculate(k, is_odd=False):
        if k <= 0:
            return 0
        elif is_odd:
            return odd_term(k) + calculate(k - 1, False)
        else:
            return even_term(k) + calculate(k - 1, True) 

    return calculate(n, n%2)

# # Method 2(Official solution)
# # 总共有n项要加，从第一项开始加，base case为已经加到第n项的时候
#     def helper(term0, term1, k):
#         if k == n: # 如果加的是第n项
#             return term0(k)
#         return term0(k) + helper(term1, term0, k + 1) # 间隔着去加第k+1项
#     return helper(odd_term, even_term, 1)

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

    if n < 10:
        return 0
    else:   # 数一下和最后一位数匹配的数出现的次数(e.g. 9去找1，8去找2...)
        return count_digit(n // 10, 10 - n % 10) + ten_pairs(n // 10) 

def count_digit(num, digit):
    """Count the number that digit appears in num."""
    if num < digit:
        return 0
    elif num % 10 == digit:
        return 1 + count_digit(num // 10, digit)
    else:
        return count_digit(num // 10, digit)

