#include "sorting.h"

namespace Sorting {

    // 比较排序
    void compare_sort(std::vector<int>& v, bool (*cmp)(int, int)) {
        if (display) std::cout << "[Compare Sort]\n";
        print(v);

        for (int i = 0; i < v.size() - 1; i++) {
            for (int j = i + 1; j < v.size(); j++) {
                if (cmp(v[i], v[j])) {
                    std::swap(v[i], v[j]);
                    print(v);
                }
            }
        }
    }
   
    // 选择排序
    void selection_sort(std::vector<int>& v, bool (*cmp)(int, int)) {
        if (display) std::cout << "[Selection Sort]\n";
        print(v);

        for (int i = 0; i < v.size() - 1; i++) {
            int value = v[i], position = i;
            for (int j = i + 1; j < v.size(); j++) {
                if (cmp(value, v[j])) {
                    value = v[j];
                    position = j;
                }
            }
            std::swap(v[i], v[position]);
            print(v);
        }
    }

    // 插入排序
    void insertion_sort(std::vector<int>& v, bool (*cmp)(int, int)) {
        if (display) std::cout << "[Insertion Sort]\n";
        print(v);

        for (int i = 1; i < v.size(); i++) {
            for (int j = 0; j < i; j++) {
                if (cmp(v[j], v[i])) {
                    int temp = v[i];
                    v.erase(v.begin() + i);
                    v.emplace(v.begin() + j, temp);
                    print(v);
                }
            }
        }
    }

    // 冒泡排序
    void bubble_sort(std::vector<int>& v, bool (*cmp)(int, int)) {
        if (display) std::cout << "[Bubble Sort]\n";
        print(v);

        for (int i = v.size() - 1; i >= 0; i--) {
            for (int j = 0; j < i; j++) {
                if (cmp(v[j], v[j + 1])) {
                    std::swap(v[j], v[j + 1]);
                    print(v);
                }
            }
        }
    }

    // 哈希排序
    void hash_sort(std::vector<int>& v, bool (*cmp)(int, int)) {
        if (display) std::cout << "[Hash Sort]\n";
        print(v);

        auto maximum = std::max_element(v.begin(), v.end()), 
             minimum = std::min_element(v.begin(), v.end());
        int length = *maximum - *minimum + 1;
        short int hash_table[length] = {0};

        for (auto each : v)
            hash_table[each - *minimum] ++;

        std::vector<int> copy; // 不要直接更改 v，因为会使 maximum 和 minimum 不稳定
        for (int i = 0; i < length; i++) {
            if (hash_table[i]) {
                for (int times = 0; times < hash_table[i]; times++) {
                    copy.push_back(*minimum + i);
                }
                if (display) {
                    std::cout << (*minimum + i) << ": " 
                              << hash_table[i] << " times\n";
                }
            }
        }
        v = copy;
    }
}