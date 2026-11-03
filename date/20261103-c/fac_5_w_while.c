// 计算 5 的阶乘，用 while 循环实现

#include <stdio.h>
int main() {
    int factorial = 1, 
        n = 5, i = 1;

    while (i <= n) {
        factorial *= i;
        i++;
    }

    printf("5的阶乘是: %d\n", factorial);
    return 0;
}