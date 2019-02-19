# Mutable Data

# 2 Linked Lists


class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        assert rest is Link.empty or isinstance(rest, Link)
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


# (a)
cycle = Link(1, Link(2, Link(3)))
cycle.rest.rest.rest = cycle

# (b)


def has_loop(s):
    slow = s
    fast = s.rest
    loop = False
    while not loop and fast is not Link.empty and fast.rest is not Link.empty:
        if fast == slow or fast.rest == slow:
            loop = True
        fast = fast.rest.rest
        slow = slow.rest

    return loop

# 3 List and Dictionary Comprehensions
# (a)


def is_prime(n, k=2):
    # Base cases
    if n <= 2:
        return True if n == 2 else False
    if n % k == 0:
        return False
    if k * k > n:   # tried all divisors to sqrt, must be prime
        return True
    # Check for next divisor
    return is_prime(n, k + 1)


prime_list = [[j for j in range(i * 10, (i + 1) * 10) if is_prime(j)] for i in range(10)]

# (b)


def more_than_2_times(lst):
    return {e: lst.count(e) for e in lst if lst.count(e) > 2}


lst = ['A', 'A', 'A', 'B', 'C', 'C', 'C', 'C', 'D', 'D']
print(more_than_2_times(lst))

# (c)
triangles = [(a, b, c) for a in range(1, 31) for b in range(a, 31) for c in range(b, 31)
             if a ** 2 + b ** 2 == c ** 2]  # a 3D list comprehension COOL!
print(triangles)

x = ('This will build a very long long long long '
     'long long long long long long long long string')
print(x)
