#函数的参数
'''
形参：形式参数  是一种意义上的参数。在定义时并不占用具体的内存地址
实参：实际参数
'''
#这种也叫作关键字参数
def my_func_1(name,age):
    print(name)
    print(age)
my_func_1(name = "Ginger",age = 19)
my_func_1(age = 19, name = "Ginger")

#默认参数
def my_func_2(name = "Jiang", age = 20):
    print(name)
    print(age)

my_func_2("li",30)

def my_func_3(name,age = 5):
    print(name)
    print(age)
my_func_3(2,3)

#递归:自己调用自己(在函数内部)
# def my_func_4(x):   会死循环
#     print(x)
#     my_func_4(x+1)

# my_func_4(1)
#函数的返回值
def f(x):
    return "你传入的参数是" + str(x)
r = f(1)
print(r)

def f(x):
    #明确递归结束条件
    if x == 1:
        return 1
    print("计算" + str(x) + "+" + "f(" + str(x-1)+")")
    return x + f(x-1)
print(f(10))
