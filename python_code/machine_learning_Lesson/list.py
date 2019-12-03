#list

list1 = [1,2,3,4] #储存的数据类型多样
print(list1)
print(type(list1))
list1 = [1,2,3,4,'a','b',[1,2,3,4]] #嵌套列表
#访问
print(list1[1])
print(list1[0:2])
print(list1[0:])
#添加   CRUD 增删改查
list1.append("a")
print(list1)
print(list1 + ['b'])

#更新
list1[1] = "l1"
print(list1)
#删除
del list1[1]
print(list1)

#嵌套列表的访问
list1 = [1,2,3,4,'a','b',[1,2,3,4]] #嵌套列表
print(list1[6][1])

