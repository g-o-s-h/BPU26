#include <stdio.h>
int main() {
    int num1, num2, num3, max;

    printf("请输入三个整数：\n");
    scanf("%d %d %d", &num1, &num2, &num3);

    max = num1;
    if (num2 > max) max = num2;
    if (num3 > max) max = num3;

    printf("三个数中最大的数是: %d\n", max);

    return 0;
}