# Iterators, Iterables, and Generators

# 1 Iterators and Iterables
from math import sqrt
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    assert n >= 1, "n is not a positive integer"
    k = 2
    if n == 1:
        flag = False
    else:
        flag = True
    while k <= sqrt(n):
        if n % k == 0:
            flag = False
            break
        k += 1
    return flag

class PrimeIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __next__(self):
        if self.current < self.end:
            while not is_prime(self.current):
                self.current += 1
            if self.current < self.end:
                self.current += 1
                return self.current - 1
        raise StopIteration

    def __iter__(self):
        return self

class PrimeIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __getitem__(self, i):
        # assume this is already implemented for you
        pass

    def __iter__(self):
        return PrimeIterator(self.start, self.end)

import re
def get_vowels(word):
    # A bit of RegEx magic to isolate all the vowels of a word in order
    return re.sub(r'[^aeiou]', '', word)

class Vowels:
    def __init__(self, word):
        self.vowels = get_vowels(word)
        self.counter = 0

    def __next__(self):
        if self.counter < len(self.vowels):
            self.counter += 1
            return self.vowels[self.counter-1]
        raise StopIteration

    def __iter__(self):
        return self

    def __getitem__(self, i):
        try:
            return self.vowels[i]
        except IndexError:
            raise IndexError("Out of bounds index " + str(i))
        except TypeError as e:
            raise TypeError(e)

# 2 Generators

from random import random

def randoms(low, high, num):
    for _ in range(num):
        yield int((random() * (high - low)) + low)

# equivalent to randoms(1, 10, 5)
(int((random() * (10 - 1)) + 1) for _ in range(5)) # this is a generator expression, which returns a generator
# (int((random() * (high - low)) + low) for _ in range(num))
