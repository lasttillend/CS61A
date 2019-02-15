# 1.
# 不能试图在内函数里修改外函数的参数值，下面的代码会报错

def f(x):
	def g():
		# nonlocal x
		print("before plus 1: ", x)
		x += 1
		print("after plus 1: ", x)
		print(x)
	return g

print(f(2)())

# 2.
# Variable in the current frame cannot be modifed using the nonlocal keyword.
# This means we cannot have both a local and nonlocal variable with the same
# names in a single frame.
def f(lst):
    def g():
    	# nonlocal lst # 必须要用nonlocal statement才能避免报错，修改的是f的frame中的lst
        if len(lst) == 2: # 此时的lst当成f的frame里的lst(nonlocal variable)
            lst[0] = 1
        else:
            lst[0] = 2
        lst = lst[1:] # 但这里左边lst当成g的frame里的lst(local variable)
    g()

a = [4, 5, 6]
f(a)