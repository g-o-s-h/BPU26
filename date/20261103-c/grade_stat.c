/*
用键盘输入一批学生的成绩，计算平均成绩，并统计不及格学生的人数。
- 确定循环条件
    - 不知道输入数据的个数，无法事先确定循环次数
*/
#include <stdio.h>
int main() {
    
    float score, sum = 0, average;
    int count = 0, fail_count = 0;

    printf("请输入学生成绩（输入负数结束）：\n");
    while (1) {
        scanf("%f", &score);
        if (score < 0) {
            break; // 输入负数结束循环
        }
        sum += score;
        count++;
        if (score < 60) {
            fail_count++;
        }
    }

    if (count > 0) {
        average = sum / count;
        printf("平均成绩: %.2f\n", average);
        printf("不及格人数: %d\n", fail_count);
    } else {
        printf("没有输入有效的成绩。\n");
    }

    return 0;
}