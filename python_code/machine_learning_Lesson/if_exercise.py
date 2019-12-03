dollar = 0.1491
print(dollar)
yen = 16.6955
pound = 0.1139
hongkong_dollar = 1.1691
euro = 0.1318
print(yen - pound)
print(111.25 * dollar)
print(type(123))
print(type(True))
print(type("123"))
s1 = "I want to study in PKU"
print(s1[3])
print(s1[2:5]) # 左闭右开原则
s = "PKU"
str = '123'
print(s in s1)
print("ab\"cd") #转义字符
print('ab"cd')
print("ab\\ncd")
print(r"ab\ncd") #输出原始字符串
print(R"ab\ncd")
print("Hello World".find("llo")) #返回起始位置
print("Hello World".upper()) #
print("Hello World".lower())
print("%s最帅"%("浩哥"))
a = "你好吗?"
print(a.replace("吗","").replace("?","!"))


# if的用法
if False:
    print("True")
elif True:
    print("elif")
else:
    print("else")

"""
比较运算符
== 判断两个值是否相等
=== 地址和值都相等
"""

if 1 == 2:
    print("相等")
a = [1,2,3]
b = a
c = [1,2,3]
if a is b:
    print("True")
else:
    print("False")
if b is c:
    print("True")
else:
    print("False")

if "a" >= "b":
    print("a大于b")
else:
    print("a小于b")

if "ab" >= "bc":  #按照字母顺序比较大小
    print("a大于b")
else:
    print("a小于b")

"""
in
not in
"""

print("a" in "ab")
print("a" not in "ab")

"""
and
or
not
"""

if 1 and 2 and 3:  #也可以是一个表达式
    print("and")

print(1 and 0)
print(1 or 0)
print(not 0)

"""
身份运算
is #判断地址是否相等
is not
"""

a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)


