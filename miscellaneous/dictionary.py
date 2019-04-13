# stem_and_leaf(茎叶图)
def stem_and_leaf(lst, leaf_max):
    """Returns a dictionary representing a stem-and-leaf plot.

    >>> stem_and_leaf([7, 31, 365, 365, 3650], 100)
    {0: [7, 31], 3: [65, 65], 36: [50]}
    """
    plot = {}
    for num in lst:
        stem, leaf = num // leaf_max, num % leaf_max
        if stem not in plot:
            plot[stem] = []
        plot[stem].append(leaf)
    return plot

# one_to_one
def one_to_one(d):
    """Returns True if D represents a one-to-one mapping of keys to values.

    >>> d = {'a': 4, 'b': 5, 'c': 3}
    >>> one_to_one(d)
    True
    >>> fail = {'a': 2, 'b': 4, 'c': 2}
    >>> one_to_one(fail)
    False
    """
    seen = set()
    for value in d.values():
        if value in seen:
            return False
        seen.add(value)
    return True

# degree of separation
users = {
    'Robert': ['Brian', 'Mark'],
    'Mark': ['Eric', 'Brian', 'Robert'],
    'Brian': ['Eric', 'Mark', 'Robert'],
    'Eric': ['Mark', 'Brian'],
    'Albert': []
}

def degrees(users, start, end, visited):
    """Finds the degree of separation between START and END. If START and END are not connected, return infinity: float('inf').

    PARAMETERS:
    users   -- dictionary; keys are users, values are friends lists
    start   -- starting user
    end     -- ending user
    visited -- a Python set of users we've already checked
    """
    if start == end:
        return 0
    smallest = float('inf')  # infinity
    visited.add(start)
    for friend in users[start]:
        if friend not in visited:
            friend_degree = degrees(users, friend, end, visited)
            smallest = min(smallest, friend_degree + 1)
    return smallest
print(degrees(users, 'Robert', 'Eric', set()))



