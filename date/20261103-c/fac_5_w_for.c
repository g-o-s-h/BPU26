// 计算 5 的阶乘，用 for 循环实现

#include <stdio.h>
int main() {
    int factorial = 1, 
        n = 5;

    for (int i = 1; i <= n; i++) {
        factorial *= i;
    }

    printf("5的阶乘是: %d\n", factorial);
    return 0;
}