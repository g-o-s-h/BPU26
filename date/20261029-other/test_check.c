#include <stdio.h>

int main() {
    // --- 题3 ---
    printf("--- 题3 ---\n");
    int i = 6;
    if (i <= 6)
        printf("hello\n");
    else
        printf("bye-bye\n");

    // --- 题5 ---
    printf("--- 题5 ---\n");
    int x5 = 2, y5 = -1, z5 = 2;
    if (x5 < y5)
        if (y5 < 0) z5 = 0;
        else z5 += 1;
    printf("%d\n", z5);

    // --- 题6 (模拟输入 '5') ---
    printf("--- 题6 ---\n");
    char ch = '5'; // 假设输入 '5'
    int flag = ch >= '0' && ch <= '9';
    if (flag)
        printf("%c\n", ch);

    // --- 题10 ---
    printf("--- 题10 ---\n");
    int x10 = 12, y10;
    if (x10 > 12)
        y10 = x10 + 10;
    else
        y10 = x10 - 12;
    printf("%d\n", y10);

    // --- 题11 ---
    printf("--- 题11 ---\n");
    int a11 = 2, b11 = 3, c11;
    c11 = a11;
    if (a11 > b11) c11 = 1;
    else if (a11 == b11) c11 = 0;
    else c11 = -1;
    printf("%d\n", c11);

    // --- 题13 ---
    printf("--- 题13 ---\n");
    int k = 5;
    int j = k--;
    printf("j=%d, k=%d\n", j, k);

    // --- 题15 ---
    printf("--- 题15 ---\n");
    int x15 = 10, y15 = 20, z15 = 30;
    if (x15 > y15) z15 = x15; // 注意：这里没有大括号
    x15 = y15; 
    y15 = z15;
    printf("x=%d, y=%d, z=%d\n", x15, y15, z15);

    // --- 判断题 1 ---
    printf("--- 判断题 1 ---\n");
    int a = 3, b = 4, c = 5;
    int result = (a + b > c) && (b == c);
    printf("%d\n", result);

    return 0;
}