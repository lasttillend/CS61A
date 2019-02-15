from linked_list import *

### Sets as unsorted sequences ###

# Time order of growth theta(1)
def empty(s):
	return s is Link.empty

# theta(n): time depends on whether & where v appears in s. We need to search the WHOLE linked list
def contains(s, v):
	"""Return true if set s contains value v as an element.

	>>> s = Link(1, Link(3, Link(2)))
	>>> contains(s, 2)
	True
	>>> contains(s, 5)
	False
	"""
	if empty(s):
		return False
	elif s.first == v:
		return True 
	else:
		return contains(s.rest, v)

# theta(n)
def adjoin(s, v):
	if contains(s, v):
		return s 
	else:
		return Link(v, s)

# theta(n^2): we perform 'contains' operation, which is theta(n), on every element of set1
def intersect(set1, set2):
	in_set2 = lambda v: contains(set2, v)
	return filter_link(in_set2, set1)

# theta(n^2)
def union(set1, set2):
	not_in_set2 = lambda v: not contains(set2, v)
	set1_not_set2 = filter_link(not_in_set2, set1) # theta(n^2) for "filter_link" operation
	return extend_link(set1_not_set2, set2) # theta(n) for "extend_link" operation

### Sets as ordered sequences ###

# faster in some cases, but time order of growth is still theta(n)
def contains2(s, v):
	"""Return true if set s contains value v as an element.

	>>> s = Link(1, Link(2, Link(3)))
	>>> contains2(s, 2)
	True
	>>> contains2(s, 5)
	False
	"""
	if empty(s) or s.first > v:
		return False
	elif s.first == v:
		return True 
	else:
		return contains2(s.rest, v)

# theta(n)
def adjoin2(s, v):
	"""Return a set containing all elements of s and element v.

	>>> s = Link(1, Link(2, Link(3)))
	>>> t = adjoin2(s, 4)
	>>> t
	Link(1, Link(2, Link(3, Link(4))))
	"""
	if empty(s) or s.first > v:
		return Link(v, s)
	elif s.first == v:
		return s 
	else:
		return Link(s.first, adjoin2(s.rest, v))

# theta(n)
def add(s, v):
	"""Add v to a set s, returning modified s. If s is not empty, 
	returns same object.

	>>> s = Link(1, Link(3, Link(5)))
	>>> add(s, 0)
	Link(0, Link(1, Link(3, Link(5))))
	>>> add(s, 3)
	Link(0, Link(1, Link(3, Link(5))))
	>>> add(s, 4)
	Link(0, Link(1, Link(3, Link(4, Link(5)))))
	>>> add(s, 6)
	Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
	"""
	if empty(s):
		return Link(v)
	if s.first > v:
		s.first, s.rest = v, Link(s.first, s.rest)
	elif s.first < v and empty(s.rest):
		s.rest = Link(v, s.rest)
	elif s.first < v:
		add(s.rest, v)
	return s

# theta(n)
def intersect2(s, t):
    """Return a set containing all elements common to s and t.

    >>> s = Link(1, Link(2, Link(3))) 
    >>> t = Link(2, Link(3, Link(4)))
    >>> intersect2(s, t)
    Link(2, Link(3))
    """
    if empty(s) or empty(t):
        return Link.empty
    else:
        e1, e2 = s.first, t.first
        if e1 == e2:
            return Link(e1, intersect2(s.rest, t.rest))
        elif e1 < e2:
            return intersect2(s.rest, t)
        elif e2 < e1:
            return intersect2(s, t.rest)

# theta(n)
def union2(s, t):
    """Return a set containing all elements either in s or t.

    >>> s = Link(1, Link(2, Link(3))) 
    >>> t = Link(2, Link(3, Link(4)))
    >>> union2(s, t)
    Link(1, Link(2, Link(3, Link(4))))
    """
    if empty(s):
        return t
    elif empty(t):
        return s
    else:
        e1, e2 = s.first, t.first
        if e1 == e2:
            return Link(e1, union2(s.rest, t.rest))
        elif e1 < e2:
            return Link(e1, union2(s.rest, t))
        elif e2 < e1:
            return Link(e2, union2(s, t.rest))