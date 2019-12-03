'''
set数据类型的特点：无序的不重复元素的序列
1.可以使用大括号{}
2.set_param1 = set()
'''
# set_param = {"1","2","3"}
# print(set_param)
# set_param1 = set()
# print("1" in set_param)

a = set("abcd")
print(a)
b = set("aqwe")
print(a | b)  #求并集
print(a & b)  #求交集

#集合的CRUD
my_set = set(("Tony","Jack","Robbin"))  #set只能给它一个参数
print(my_set)
my_set.add("you")
print(my_set)
my_set.remove("Tony")
print(my_set)
print(len(my_set))
# my_set.clear()
# print(len(my_set))
#print(my_set[0]) 不支持随机访问


