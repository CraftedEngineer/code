'''
循环的中断
1.break
2.continue
'''

i =1
while True:
    i = i+1
    print(i)
    # if i == 100:
    #     break
    if i == 10:
        print("此时i的值是10")
        continue   #中断一次循环
    print("continue的下一行")
    if i == 15:
        break      #中断循环
