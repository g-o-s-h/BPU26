#ifndef _SORTING_H_
#define _SORTING_H_

#include <iostream>
#include <vector>
#include <algorithm>

namespace Sorting {

    // display factor
    static bool display = true;

    // default compare
    inline bool dcmp(int x, int y) {
        return x > y;
    }

    // reverse compare
    inline bool rcmp(int x, int y) {
        return !dcmp(x, y);
    }

    // print all elements in a line
    inline void print(std::vector<int> v) {
        if (!display) return;
        for (auto each : v)
            std::cout << each << " ";
        std::cout << std::endl;
    }

    // basic sorts
    void compare_sort   (std::vector<int>& v, bool (*cmp)(int, int) = dcmp);
    void selection_sort (std::vector<int>& v, bool (*cmp)(int, int) = dcmp);
    void insertion_sort (std::vector<int>& v, bool (*cmp)(int, int) = dcmp);
    void bubble_sort    (std::vector<int>& v, bool (*cmp)(int, int) = dcmp);
    void hash_sort      (std::vector<int>& v, bool (*cmp)(int, int) = dcmp);

    // advanced sorts
    // void merge_sort     (std::vector<int>& v, bool (*cmp)(int, int) = dcmp);
    // void quick_sort     (std::vector<int>& v, bool (*cmp)(int, int) = dcmp);
    // void heap_sort      (std::vector<int>& v, bool (*cmp)(int, int) = dcmp);
}

#endif // _SORTING_H_