HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

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
    "*** YOUR CODE HERE ***"
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b)) 

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
    "*** YOUR CODE HERE ***"
    return [round(x ** 0.5) for x in s if x ** 0.5 == round(x ** 0.5)]

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
    if n <= 3:
        return n 
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

# 对比recursive和iterative
"""
Your recursive function can be read as

To find the value of g(30), find the value of g(29), g(28), and g(27)
  To find the value of g(29), find the value of g(28), g(27), and g(26)
    To find the value of g(28), find the value of g(27), g(26), and g(25)
      ...
        (repeat until all sub-finds have completed)
An iterative function would start at the other end,

I know the values of g(1), g(2), and g(3) -> calculate g(4)
I know the values of g(2), g(3), and g(4) -> calculate g(5)
I know the values of g(3), g(4), and g(5) -> calculate g(6)
...
(repeat until the desired g(n) is reached)
"""

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
    if n <= 3:
        return n
    prev3, prev2, prev1 = 1, 2, 3   # 需要3个变量来计算下一次的取值
    for _ in range(3, n):
        curr = prev1 + 2 * prev2 + 3 * prev3
        prev3, prev2, prev1 = prev2, prev1, curr

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
    def helper(x, cnt=1, up=1):
        if cnt == n:
            return x
        if has_seven(cnt) or cnt % 7 == 0:
            return helper(x-up, cnt+1, -up)
        return helper(x+up, cnt+1, up)

    return helper(1)

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
    def max_coin(amount, x=1):
        if 2 ** x > amount:
            return 2 ** (x - 1)
        else:
            return max_coin(amount, x+1)

    # print("largest value coin = ", largest_value_coin(amount))
    def count_bipartitions(total, max_coin):
        if total == 0:
            return 1
        elif total < 0:
            return 0
        elif max_coin == 0:
            return 0
        else:
            with_max = count_bipartitions(total-max_coin, max_coin)
            without_max = count_bipartitions(total, max_coin // 2)
            return with_max + without_max

    # 和count_partitions做比较，只是partition的方式变了
    # def count_partitions(n, m):
    #     """Count the ways to partition n using parts up to m."""
    #     if n == 0:
    #         return 1
    #     elif n < 0:
    #         return 0
    #     elif m == 0:
    #         return 0
    #     else:
    #         return count_partitions(n-m, m) + count_partitions(n, m-1)

    return count_bipartitions(amount, max_coin(amount))


###################
# Extra Questions #
###################

from operator import sub, mul
"""
这道题要点，把函数当做参数传入，构造call, 在call里用lambda构造这个函数的behavior，这样就解决了迭代时需要函数名的问题。主要分为两部分。
1，第一个括号： (lambda f: lambda k: f(f, k))
构造一个需要f函数作为参数的函数，返回值是需要k为参数的函数，返回f函数的值，并且规定了f是一个需要2个参数的函数，f自身和k
2，第二个括号：(lambda f , k: k if k == 1 else k * f(f, k-1) )
这部分作为第一个括号的第一个call，构造f函数的行为，需要2个参数：f, k. 返回值为k或else后的值，if给出最简式，else给出，k和k-1的关系
3，注意环境变量的变化，写成相同的名字便于理解，实际并不相同。
"""
def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # return 'YOUR_EXPRESSION_HERE'
    return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))  # 太难了！



