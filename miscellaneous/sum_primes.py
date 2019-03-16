def is_prime(x):
    if x <= 1:
        return False
    return all(map(lambda i: x % i, range(2, x)))
    # return all([x % i for i in range(2, x)])


def sum_primes(a, b):
    return sum(filter(is_prime, range(a, b)))

print(sum_primes(2, 10000))
