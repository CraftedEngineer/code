import  pymysql
import  random

#连接mysql数据库
db = pymysql.connect("localhost","root","69a12c07e","staff_attendence")
cursor = db.cursor()

#测试考勤次数为10
times = 10

for k in range (times):
    print("第"+ str(k+1) +"次考勤")
    #考勤开始时，所有人的考勤成绩加1，被抽到的人如果没有到，考勤成绩减1，否则成绩不变
    for j in range (0,10):
        rs = '0' + str(j)
        #读出该工作人员的flag信息，若flag = 1,说明其已经缺勤超过5次，不改动其考勤成绩
        sql8 = "SELECT * from staff_information WHERE 职工号 = '%s'" % rs
        cursor.execute(sql8)
        results = cursor.fetchall()
        for row in results:
            flag = row[7]
        if flag == 0:
            sql9 = "UPDATE staff_information SET 考勤成绩 = 考勤成绩 + 1 WHERE 职工号 = '%s'" % rs
            cursor.execute(sql9)
            db.commit()
    #随机生成本次考勤的人数和对应的工作人员
    frequence = random.randint(1, 10)
    print("本次考勤的人数为" + str(frequence))
    # 选择考勤的具体职工
    rss = random.sample(range(0, 10), frequence)
    print("本次考勤的具体职工为：")
    print(rss)
    for i in range (frequence):
        print("请您考勤")
        print("目前选中的职工是0" + str(rss[i]) + " 请选择其是否到场，0为缺席，1为到场")
        rs = '0' + str(rss[i])
        # 定义需要用到的sql语句
        sql1 = "UPDATE staff_information SET 考勤成绩 = 0 WHERE 职工号 = '%s'" % rs
        sql2 = "UPDATE staff_information SET 连续缺勤数 = 连续缺勤数 + 1 WHERE 职工号 = '%s'" % rs
        sql3 = "UPDATE staff_information SET 缺勤总数 = 缺勤总数 + 1 WHERE 职工号 = '%s'" % rs
        sql4 = "SELECT * from staff_information WHERE 职工号 = '%s'" % rs
        sql5 = "UPDATE staff_information SET 连续缺勤数 = 0 WHERE 职工号 = '%s'" % rs
        sql6 = "UPDATE staff_information SET flag = 1 WHERE 职工号 = '%s'" % rs
        sql7 = "UPDATE staff_information SET 考勤成绩 = 考勤成绩 - 1 WHERE 职工号 = '%s'" % rs

        #该考勤成员未到
        m = int(input())
        if (m == 0):
                #读取被考勤人员的信息
                cursor.execute(sql4)
                results = cursor.fetchall()
                for row in results:
                    flag = row[7]
                if flag == 0:
                    # 因为缺席，所以考勤成绩-1
                    cursor.execute(sql7)
                    db.commit()
                    #连续缺勤数和缺勤总数+1
                    cursor.execute(sql2)
                    db.commit()
                    cursor.execute(sql3)
                    db.commit()

                #读出本轮修改后的连续缺勤数和总缺勤数
                cursor.execute(sql4)
                results = cursor.fetchall()
                for row in results:
                    con_amount = row[5]
                    amount = row[6]

                #如果该员工连续3次缺勤，则将其考勤成绩暂时置0
                if con_amount == 3:
                    cursor.execute(sql1)
                    db.commit()

                #如果该员工共计5次缺勤，则将其考勤成绩永久置0
                if amount == 5:
                    cursor.execute(sql1)
                    db.commit()
                    cursor.execute(sql6)
                    db.commit()
                    print("缺勤总数已到达5")
                else:
                    print("缺勤总数未超过5")

        # 该考勤成员已到
        elif (m == 1):
            #因为一开始所有人的考勤成绩已经+1，此处只需将其连续缺勤数清0即可
            cursor.execute(sql5)
            db.commit()
        else:
            print("输入错误，请您重新输入")
    print("下面是本次考勤的结果情况")
    for j in range (0,10):
        rs = '0' + str(j)
        sql8 = "SELECT * from staff_information WHERE 职工号 = '%s'" % rs
        cursor.execute(sql8)
        results = cursor.fetchall()
        for row in results:
            grade = row[4]
            con_amount = row[5]
            amount = row[6]
            flag = row[7]
        print("员工编号：" + rs + " 考勤成绩：" + str(grade) + " 连续缺勤数：" + str(con_amount) +" 缺勤总数：" + str(amount)
              + " flag: " + str(flag))

print("考勤结束，辛苦啦")
db.close()