#include <stdio.h>

int main() {
    int year, month, day = 0;
    printf("请输入年份和月份（格式：YYYY-MM）：");
    scanf("%d-%d", &year, &month);

    switch (month) {

        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            day = 31;
            break;

        case 4:
        case 6:
        case 9:
        case 11:
            day = 30;
            break;

        case 2:
            if ((year % 4 == 0 && year % 100 != 0)
              || (year % 400 == 0)) {
                day = 29;
            } else {
                day = 28;
            }
            break;

        default:
            // day = -1;
            printf("无效的月份（需要在 1-12 之间）\n");
            return 0;
    }

    // if (day == -1) {
        // printf("无效的月份（需要在 1-12 之间）\n");
    // } else {
        // printf("%d 年 %d 月有 %d 天\n", year, month, day);
    // }

    printf("%d 年 %d 月有 %d 天\n", year, month, day);
    return 0;
}