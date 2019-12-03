def func_1():
    print("函数被调用")
    return "a"
f = func_1()
print(f)
print(type(f))

def func3(x,y):
    z = x + y
    return z

f = func3(3,4)
print(f)

def func4():
    return 1,2  #返回值可以是多个
x,y = func4()
print(x)
print(y)

#函数的返回值是一个函数
def func5(x):
    if x == 2:
        def inner_func(y):
            print("inner 1被调用")
            return y*y
    if x == 3:
        def inner_func(y):
            print("inner 2被调用")
            return y*y*y
    return inner_func
calc = func5(3)
z = calc(2)
print(z)