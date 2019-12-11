import  pymysql
import random

frequence = random.randint(1, 10)
print("本次考勤的人数为" + str(frequence))
rs = random.sample(range(0, 10), frequence)
print("本次考勤的具体职工为：")
print(rs)
for i in range (frequence):
    print("目前选中的职工是0" + str(rs[i]) + " 请选择其是否到场，0为缺席，1为到场")