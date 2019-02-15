# e.g.1
def trace(fn):
	def wrapped(x):
		print('-> ', fn, '(', x, ')')
		return fn(x)
	return wrapped

@trace
def triple(x):
	return 3 * x

# As usual, the function triple is created. However, the name triple 
# is not bound to this function. Instead, the name triple is bound to 
# the returned function value of calling trace on the newly defined 
# triple function. In code, this decorator is equivalent to:
# triple = trace(triple)

# e.g.2
def count(f):
    """Return a counted version of f with a call_count attribute.

    >>> def fib(n):
    ...     if n == 0 or n == 1:
    ...         return n
    ...     else:
    ...         return fib(n-2) + fib(n-1)
    >>> fib = count(fib)
    >>> fib(20)
    6765
    >>> fib.call_count
    21891
    """
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

def fib(n):
    """The nth Fibonacci number.

    >>> fib(20)
    6765
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

# e.g.3
def memo(f):
    """Memoize f.

    >>> def fib(n):
    ...     if n == 0 or n == 1:
    ...         return n
    ...     else:
    ...         return fib(n-2) + fib(n-1)
    >>> fib = count(fib)
    >>> fib(20)
    6765
    >>> fib.call_count
    21891
    >>> counted_fib = count(fib)
    >>> fib  = memo(counted_fib)
    >>> fib(20)
    6765
    >>> counted_fib.call_count
    21
    >>> fib(35)
    9227465
    >>> counted_fib.call_count
    36
    """
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memoized

# fib = count(fib)
# counted_fib = fib 
# fib = memo(fib)
# fib = count(fib)
# fib(30)
# fib.call_count
# counted_fib.call_count

# e.g.4
def count_frames(f):
	def counted(n):
		counted.open_count += 1
		counted.max_count = max(counted.max_count, counted.open_count)
		result = f(n)
		counted.open_count -= 1
		return result
	counted.open_count = 0
	counted.max_count = 0
	return counted
	
# fib = count_frames(fib)
# fib(19)
# fib.open_count
# fib.max_count




