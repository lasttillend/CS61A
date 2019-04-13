# 1. 用higher order function将变量保存在frame里，这样就可以在更新变量的同时仍然可以访问旧版变量(e.g. disc11 6.2)

# 2. Fibonacci sequence(recursive, iterative, tree, tail-recursive fibo, stream-fibo etc.)

# 3. Tail recursion
# (define (factorial n)
#     (define (helper n total)
#         (if (= n 0)
#             total
#             (helper (- n 1) (* n total))))
#     (helper n 1)
# )

# Thunk object用来延时计算，它的expr用来保存表达式，env则用来保存环境
"""
因为当我们要eval的一个expr是在tail context底下的时候（e.g. (helper n 1），我们直接return一个Thunk object而不是eval它，所以不会增加新的frame。但是这样一来我们就仍处于isinstance(result, Thunk)的循环当中，所以会继续eval这个新的Thunk object。如此循环下去，直到最后我们用Thunk object保存的expr和env计算出想要的结果并退出循环。
"""

# 4. 笑话
# If a promise contains an empty list, is it an empty promise?
