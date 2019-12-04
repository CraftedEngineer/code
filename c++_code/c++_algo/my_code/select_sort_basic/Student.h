#ifndef SELECTIONSORT_STUDENT_H
#define SELECTIONSORT_STUDENT_H

#include <iostream>
#include <string>

using namespace std;

struct Student{
    string name;
    int score;

    //对小于符号运算符的重载
    bool operator<(const Student &otherStudent){ 
        // 自定义比较  三目运算符
        return score != otherStudent.score? score > otherStudent.score : name < otherStudent.name;
    }
    //输出运算符重载 友元函数
    friend ostream& operator<<(ostream &os,const Student &student){
        os <<"Student:" << student.name << " " <<student.score << endl;
        return os;
    }

};


#endif