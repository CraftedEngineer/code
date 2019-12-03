
#include <iostream>
#include "Line.h"
using namespace std;

Line::Line(int x1, int y1, int x2, int y2):m_CoorA(x1,y1),m_CoorB(x2,y2)
{
	// m_CoorA.setX(x1);

}
Line::~Line()
{
	
}

void Line::setA(int x, int y)
{
	 // m_CoorA.setX(x);
	 // m_CoorA.setY(y);
}

void Line::setB(int x, int y)
{
	m_CoorB.setX(x);
	m_CoorB.setX(y);
}

void Line::printInfo()
{
	cout << "printInfo()" << endl;
	cout << "(" << m_CoorA.getX() << "," << m_CoorA.getY() << ")"<< endl;
	cout << "(" << m_CoorB.getX() << "," << m_CoorB.getY() << ")" << endl;
}

void Line::printInfo() const
{
	cout << "const printInfo()" << endl;
	cout << "(" << m_CoorA.getX() << "," << m_CoorA.getY() <<  ")" << endl;
	cout << "(" << m_CoorB.getX() << "," << m_CoorB.getY() <<  ")" << endl;
}




