"""Tree recursion occurs when a function calls itself more than once. 
This results in a ”tree” of function calls, where each function call 
branches into a few more. We can benefit from this type recursion most 
when finding permutations or combinations.
"""

# Example 1: count stairs(one or two steps)
def stairs(n):
    """Give the number of ways to take n steps, given that at each step, 
    you can choose to take 1, 2
    >>> stairs(2)
    2
    >>> stairs(4)
    5
    >>> stairs(1)
    1
    >>> stairs(3)
    3
    """
    ### YOUR CODE HERE ###
    if n <= 0:
    	return 0
    elif n == 1 or n == 2:
    	return n
    else:
    	with_step_one = stairs(n - 1)
    	with_step_two = stairs(n - 2)
    	return with_step_one + with_step_two

# Example 2: count stairs(k steps)
def kstairs(n, k):
    """Give the number of ways to take n steps, given that at each step, 
    you can choose to take 1, 2, ... k-2, k-1 or k steps.

    >>> kstairs(5, 2)
    8
    >>> kstairs(5, 5)
    16
    >>> kstairs(10, 5)
    464
    """
    ### YOUR CODE HERE ###
    if n == 0:
        return 1
    if n <= k:			# 有可能一次就登顶
        return 2**(n-1) # 有n个台阶，最后一个台阶一定要踩到，剩下的n-1个台阶
        				# 可以踩也可以不踩，所以总共(n-1, 0) + (n-1, 1) + ... + (n-1, n-1) = 2^(n - 1)
    return sum([kstairs(n - i, k) for i in range(1, k + 1)]) # 不能一次就登顶的情况								
    

