# Iterators and Generators

# 1 Iterators and Generators
# 1.1 flat_map
class FlatMapper:
    """
    A FlatMapper takes a function fn that returns an iterable
    value. The flat_map method takes an iterable s and returns
    a generator over all values in the iterables returned by calling fn on each element of s.

    >>> stutter = lambda x: [x, x]
    >>> m = FlatMapper(stutter)
    >>> g = m.flat_map((2, 3, 4, 5))
    >>> type(g)
    <class 'generator'>
    >>> list(g)
    [2, 2, 3, 3, 4, 4, 5, 5]
    """

    def __init__(self, fn):
        self.fn = fn

    def flat_map(self, s):
        flat_lst = sum([self.fn(el) for el in s], [])
        for el in flat_lst:
            yield el

# 1.2
class Adele:
    times = '1000'
    def __init__(self, you):
        self.call = you

    def __str__(self):
        return self.times

class Hello(Adele):
    def __next__(self):
        return next(self.call)

never = iter('scheme2Bhome')

def any(more):
    next(never)
    print(outside)
    yield next(never)
    print(next(never))
    yield more(more)

outside = Hello(any(any))  # self.call --> any(any), which is a generator object. Remember when you call a generator function, it doesn't go through the body of the function, but only returns a generator object. The only way to go through the body of a generator function is by calling its next method, like next(any(any)).
# next(never)
# next(outside)
# next(next(outside))
# list(never)[:3]
# next(next(outside))

# 1.3 Amplify
def amplify(f, x):
    """Yield the longest sequence x, f(x), f(f(x)), ... that are all true values.

    >>> list(amplify(lambda s: s[1:], 'boxes'))
    ['boxes', 'oxes', 'xes', 'es', 's']
    >>> list(amplify(lambda x: x//2-1, 14))
    [14, 6, 2]
    """
    while x:
        yield x
        x = f(x)
