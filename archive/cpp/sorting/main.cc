#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

#include "sorting.h"

// g++ -I ./ basic.cc advanced.cc main.cc -o sorting.exe

// 封装调用函数，简化每次调用
void call(std::vector<int> sample, 
          void (*sort)(std::vector<int>&, bool (*)(int, int))) {
    sort(sample, Sorting::dcmp);
    std::cout << std::endl;
}

int main() {
    // 初始化
    std::vector<int> sample = {1, 2, 3, 4, 5, 6, 7, 8, 9};

    // 使用 随机数引擎 mt19937 对 vector 进行 shuffle
    std::random_device rd;
    std::mt19937 g(rd());
    std::shuffle(sample.begin(), sample.end(), g);

    // 预先打印一次洗过的 sample
    std::cout << "sample: ";
    Sorting::print(sample);

    // 使用封装的函数，调用更方便
    call(sample, Sorting::compare_sort);
    call(sample, Sorting::selection_sort);
    call(sample, Sorting::insertion_sort);
    call(sample, Sorting::bubble_sort);
    call(sample, Sorting::hash_sort);
}