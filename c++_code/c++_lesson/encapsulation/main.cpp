/*
// string 类型
#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

int main(void)
{
	string name;
	cout << "请输入你的姓名:" << endl;
	getline(cin, name);
	if (name.empty())
	{
		cout << "输入为空" << endl;
		system("pause");
		return 0;
	}
	if (name == "imooc")
	{
		cout << "管理员" << endl;
	}
	cout << "hello " + name << endl;
	cout << "名字长度是:" << name.size() << endl;
	cout << "名字的首字母是:" << name[0] << endl;
	system("pause");
	return 0;
}
*/
/*

// 数据的封装
#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

class Student
{
public:
	void setName(string _name)
	{
		m_strName = _name;
	}

	string getName()
	{
		return m_strName;
	}

	void setGender(string _gender)
	{
		m_strGender = _gender;
	}

	string getGender()
	{
		return m_strGender;
	}

	int getScore()
	{
		return m_iScore;
	}

	void initScore()
	{
		m_iScore = 0;
	}

	void study(int _score)
	{
		m_iScore += _score;
	}

private:
	string m_strName;
	string m_strGender;
	int m_iScore;
};

int main(void)
{
	Student stu;
	stu.initScore();
	stu.setName("Ginger");
	stu.setGender("男");
	stu.study(3);
	stu.study(5);

	cout << stu.getName() << " " << stu.getGender() << " " << stu.getScore() << endl;
	system("pause");
	return 0;
}
*/
/*
#include <iostream>
#include <stdlib.h>
#include <string>
#include "Teacher.h"
using namespace std;

class Teacher
{
public:
	void setName(string _name);
	string getName();
	void setGender(string _gender);
	string getGender();
	void setAge(int _age);
	int getAge();
	void teach();
private:
	string m_strName;
	int m_iAge;
	string m_strGender;
};

void Teacher::setName(string _name)
{
	m_strName = _name;
}

string Teacher::getName()
{
	return m_strName;
}

void Teacher::setAge(int _age)
{
	m_iAge = _age;
}

int Teacher::getAge()
{
	return m_iAge;
}

void Teacher::setGender(string _gender)
{
	m_strGender = _gender;
}

string Teacher::getGender()
{
	return m_strGender;
}

void Teacher::teach()
{
	cout << "要上课啦！" << endl;
}

int main(void)
{
	Teacher t;
	t.setName("孔子");
	t.setGender("男");
	t.setAge(30);
	cout << t.getName() << " " << t.getAge() << " ";
	t.teach();
	system("pause");
	return 0;
}
*/
/*
//构造函数代码演示
#include <iostream>
#include <stdlib.h>
#include <string>
#include "Teacher.h"
using namespace std;

int main(void)
{
	Teacher t1;
	Teacher t2("Hao", 19);
	Teacher t3("Jiang");
	cout << t1.getName() << " " << t1.getAge() << endl;
	cout << t2.getName() << " " << t2.getAge() << endl;
	cout << t3.getName() << " " << t3.getAge() << endl;
	system("pause");
	return 0;
}
*/
/*


#include <iostream>
#include <stdlib.h>
#include <string>
#include "Teacher.h"
using namespace std;

void test(Teacher t)
{

}

int main(void)
{
	Teacher t1;
	Teacher *p = new Teacher();
	delete p;
	Teacher t2(t1);
	system("pause");
	return 0;
}
*/

#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;
/**
 * 定义类：Student
 * 数据成员：m_strName
 * 无参构造函数：Student()
 * 有参构造函数：Student(string _name)
 * 拷贝构造函数：Student(const Student& stu)
 * 析构函数：~Student()
 * 数据成员函数：setName(string _name)、getName()
 */
 /*
 class Student {
 public:
	 Student() {
		 cout << "无参构造函数" << endl;
	 }
	 Student(string _name) {
		 cout << "有参构造函数" << endl;
	 }
	 Student(const Student& stu) {
		 cout << "拷贝构造函数" << endl;
	 }
	 ~Student() {
		 cout << "析构函数" << endl;
	 }
	 void setName(string _name) {
		 cout << "设置名字" << endl;
	 }
	 string getName() {
		 cout << "获取名字" << endl;
		 return m_strName;
	 }

 private:
	 string m_strName;

 };

 int main(void)
 {
	 // 通过new方式实例化对象*stu
	 Student *stu = new Student;
	 // 更改对象的数据成员为“慕课网”
	 stu->setName("慕课网");
	 // 打印对象的数据成员
	 Student stu3;
	 Student stu1("Ginger");
	 Student stu2(stu1);
	 stu1.setName("JiangHao");
	 stu1.getName();
	 delete stu;
	 stu = NULL;
	 system("pause");
	 return 0;
 }
 */
 /*
 #include <iostream>
 #include <stdlib.h>
 #include "Coordinate.h"
 using namespace std;

 int main(void)
 {
	 Coordinate coor[3];
	 coor[0].m_iX = 3;
	 coor[0].m_iY = 5;

	 Coordinate *p = new Coordinate[3];
	 p->m_iX = 7;
	 p[0].m_iY = 9;

	 p++;   // p = p+1  P+=1;
	 p->m_iX = 11;
	 p[0].m_iY = 13;

	 p[1].m_iX = 15;
	 p++;

	 p->m_iY = 17;

	 for (int i = 0; i < 3; i++)
	 {
		 cout << "coor_x" << coor[i].m_iX << endl;
		 cout << "coor_y" << coor[i].m_iY << endl;
	 }

	 for (int j = 0; j < 3; j++)
	 {
		 cout << "p_x" << p->m_iX << endl;
		 cout << "p_y" << p->m_iY << endl;
		 p--;
	 }
	 p++;
	 delete []p;
	 p = NULL;

	 system("pause");
	 return 0;
 }
 */
 /*
 #include <iostream>
 #include <stdlib.h>
 #include "Line.h"
 using namespace std;

 int main(void)
 {
	 Line *p = new Line(1,2,3,4);
	 p->printInfo();
	 delete p;
	 p = NULL;

	 system("pause");
	 return 0;
 }

 */

 // 浅拷贝练习2
 /*
 #include <iostream>
 #include <stdlib.h>
 #include "Array.h"
 using namespace std;


 int main(void)
 {
	 Array arr1(5);
	 Array arr2(arr1);
	 arr1.printAddr();
	 arr2.printAddr();
	 arr1.printArr();
	 arr2.printArr();
	 system("pause");
	 return 0;
 }
 */
/*
#include <iostream>
#include <stdlib.h>
#include "Coordinate.h"
using namespace std;

int main(void)
{
	Coordinate *p1 = NULL;
	p1 = new Coordinate;
	Coordinate *p2 = new Coordinate();
	p1->m_iX = 10;
	p1->m_iY = 20;
	(*p2).m_iX = 30;
	(*p2).m_iY = 40;
	cout << p1->m_iX + (*p2).m_iX << endl;
	cout << p1->m_iY + (*p2).m_iY << endl;
	delete p1;
	p1 = NULL;
	delete p2;
	p2 = NULL;

	Coordinate p3;
	Coordinate *p4 = &p3;
	p4->m_iX = 50;
	p4->m_iY = 60;
	cout << "p3.m_iX = " << p3.m_iX << endl;
	cout << "p3.m_iY = " << p3.m_iY << endl;
	system("pause");
	return 0;
}
*/
/*
#include <iostream>
#include <stdlib.h>
#include "Line.h"
using namespace std;


int main(void)
{
	Line *p = new Line(1, 2, 3, 4);
	p->printInfo();
	delete p;
	cout << sizeof(p) << endl;
	cout << sizeof(Line) << endl;
	p = NULL;
	system("pause");
	return 0;
}
*/
/*
#include <iostream>
#include <stdlib.h>
#include "Array.h"
using namespace std;

int main(void)
{
	Array arr1(10);
	arr1.printInfo().setLen(5).printInfo();
	cout << &arr1 << endl;
	system("pause");
	return 0;
}
*/

//常对象成员和常成员函数实践
#include <iostream>
#include <stdlib.h>
#include "Line.h"
using namespace std;

int main(void)
{
	const Line line(1, 2, 3, 4);
	line.printInfo();
	system("pause");
	return 0;
}
