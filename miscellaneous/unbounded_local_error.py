# 1.
# 不能试图在内函数里修改外函数里immutable的变量，不加nonlocal statement的话下面的代码会报错

def f(x):
	def g():
		nonlocal x
		print("before plus 1: ", x)
		x += 1
		print("after plus 1: ", x)
		print(x)
	return g

print(f(2)())

# 2.
# Variable in the current frame cannot be modified using the nonlocal keyword.
# This means we cannot have both a local and nonlocal variable with the same
# names in a single frame.
def f(lst):
    def g():
        nonlocal lst  # 必须要用nonlocal statement才能避免报错，修改的是f的frame中的lst
        if len(lst) == 2:  # 此时的lst当成f的frame里的lst(nonlocal variable)
            lst[0] = 1
        else:
            lst[0] = 2
        lst = lst[1:]  # 但这里赋值语句产生g的frame里的lst(local variable)
    g()

a = [4, 5, 6]
f(a)

# 3
def campa(nile):
    def ding(ding):
        nonlocal nile
        def nile(ring):
            return ding
    return nile(ding(1914)) + nile(1917)  # 第一个nile不变，仍指向lambda函数；第二个nile被修改了


ring = campa(lambda nile: 103) # 返回103 + 1914 = 2017
print(ring)

# 4 一旦在local frame中赋值了一个同名变量，就失去了在该赋值语句前引用/修改它的任何机会，但之后应用它却不受影响
def butter(fly):
    cater = 20
    pillar = 10
    def chrysalis(mystery):
        nonlocal cater
        cater = mystery(cater)
        # print(pillar)  # 报错
        pillar = mystery(fly)  # pillar: local variable
        print(pillar)  # OK
        return [cater, pillar]
    return chrysalis

pupa = butter(4)
a = pupa(lambda x: x / 2)
b = pupa(lambda x: x / 2)
bugs = list([a, b]) + list(a)
print(bugs)
