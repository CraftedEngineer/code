# for 变量 in 可迭代的对象
list1 = [1,2,3]
for l in list1:
    print(l)
# while一定要控制条件

a = [13,24,1,54,2,65,36]
#冒泡排序
#a.sort(reverse = True)
#print(a)
for i in range(len(a) - 1):
    for j in range(len(a) - 1 - i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1] ,a[j]
print(a)
