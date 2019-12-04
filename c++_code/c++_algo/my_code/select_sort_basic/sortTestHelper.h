#include <iostream>
#include <ctime>

using namespace std;

namespace SortTestHelper{
    //生成有n个元素的随机数组，每个元素的随机范围是[rangeL,rangeR]
    int* generateRandomArray(int n, int rangeL, int rangeR){

        int *arr = new int[n];
        srand(time(NULL));
        for (int i = 0; i < n; i++)
            arr[i] = rand() % (rangeR - rangeL + 1) + rangeL; //做一个偏移
        return arr;
    }
}