/*
编写程序，任意输入年龄(整数)，输出对应的人生阶段。
0-6岁，童年
7-17岁，少年
18-40岁，青年
41-65岁，中年
66岁以上，老年

提交代码和运行结果的截图，结果要体现所有分支，可分别截图。

（40.0分）
*/

#include <stdio.h>

int main() {
    
    int age;
    printf("请输入年龄: ");
    scanf("%d", &age);

    if (age >= 0 && age <= 6) {
        printf("童年\n");
    } else if (age >= 7 && age <= 17) {
        printf("少年\n");
    } else if (age >= 18 && age <= 40) {
        printf("青年\n");
    } else if (age >= 41 && age <= 65) {
        printf("中年\n");
    } else if (age >= 66) {
        printf("老年\n");
    } else {
        printf("输入的年龄无效\n");
    }

    return 0;
}