'''
字典是一种可变容器模型，它可以存储任意类型的对象
'''
set_param = {"1","2","3"}
#d = {k1:v1,k2:v2}
d = {1:"ZhangSan",2:"LiSi"}
print(d)
print(d[2])
dist_2 = {1:"ZhangSan",1:"LiSi"}
keys = d.keys()
print(keys)
for i in keys:
    print(i)
    print(d[i])
print(d.values())
print(d)
#添加
d.setdefault(4,"aaa")
print(d)
#更新
d[2] = "Ginger"
print(d)
#删除
r = d.pop(2)  #返回删除的那个元素
print(r)
print(d)

#使用del关键字删除
del d[1]
print(d)

d["a"] = 1
print(d)
del d["a"]
print(d)

