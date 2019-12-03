# -*- coding: utf-8 -*-
'''
list 列表: []
set 集合:{}
tuple 元祖:()
'''
#t = ("1")
#t = () #声明一个空的元组
t = (1,"2")
t = (1,)  #元组只有一个对象时，后面也要有逗号！
t = (1, 2, 3, 4, 5)
print(t)
print(type(t))
print(t[0])
# t[1] = 6 这一行代码会报错，不让修改
l = ["a",'b']
t = (1,2,3,4,l)
print(t)
l.append("c") #指针不变
print(t)

