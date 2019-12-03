#include "Array.h"
#include <iostream>
using namespace std;

Array::Array(int len) 
{
	this->len = len;
}

Array::~Array()
{
	
}

Array& Array::setLen(int len)
{
	this->len = len;
	return *this;
}

int Array::getLen()
{
	return this->len;
}

Array& Array::printInfo()
{
	cout << this << endl;
	cout << "len = " << len << endl;
	return *this;
}

