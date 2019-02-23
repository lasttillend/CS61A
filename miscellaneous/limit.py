# 计算一个复杂极限（结果算不出来...）
from sympy import *

u = Symbol("u")
v = Symbol("v")
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

eta = abs(v) / sqrt(2 * (sqrt(u ** 2 + v ** 2) + u)) + b
xi = v / sqrt(2 * (sqrt(u ** 2 + v ** 2) - u)) + a + 1 -c
u = (c - a + 1) ** 2 - b ** 2 - 4 * c
v = -2 * b * (c - a + 1)

eta = (abs(v) / sqrt(2 * (sqrt(u ** 2 + v ** 2) + u)) + b).subs({u: (c - a + 1) ** 2 - b ** 2 - 4 * c, v: -2 * b * (c - a + 1)})

xi = (v / sqrt(2 * (sqrt(u ** 2 + v ** 2) - u)) + a + 1 -c).subs({u: (c - a + 1) ** 2 - b ** 2 - 4 * c, v: -2 * b * (c - a + 1)})


T = (2 * eta / (xi ** 2 + eta ** 2)).subs({eta: abs(v) / sqrt(2 * (sqrt(u ** 2 + v ** 2) + u)) + b, xi: v / sqrt(2 * (sqrt(u ** 2 + v ** 2) - u)) + a + 1 -c,
         }).simplify()


print("T化简为：", T)

print("Limit of T as b -> 0", limit(T, b, 0))
