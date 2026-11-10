/*
 * 万年历程序
 * FlashNova
 * 2026-11-05 09:53
 */

#include <stdio.h>

/*
 * 判断是否为闰年
 * @param year 年份
 * @return 1 表示闰年，0 表示平年
 */
int is_leap(int year) {
    return (year % 4 == 0 && year % 100 != 0)
        || (year % 400 == 0);
}

/*
 * 获取指定年份和月份的天数
 * @param year 年份
 * @param month 月份
 * @return 天数
 */
int get_day(int year, int month) {
    static const unsigned short day_table[] = {
        31,  0, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    };
    
    if (month != 2) {
        return day_table[month - 1];
    }

    if (is_leap(year)) {
        return 29; // 闰年
    } else {
        return 28; // 平年
    }
}

/*
 * 获取指定年份和月份的偏移天数
 * @param year 年份
 * @param month 月份
 * @return 偏移天数
 */
int get_offset(int year, int month) {
    static const unsigned short day_accumulate[] = {
          0,  31,  59,  90, 120, 151,
        181, 212, 243, 273, 304, 334
    };
    // 计算从 1900 年到目标年份，跨过了多少年
    int y = year - 1900;
    // 计算经过了多少个闰年
    int leap_count = (year - 1) / 4   // 模 4 的闰年，如 2020
                   - (year - 1) / 100 // 模 100 的平年，如 1900
                   + (year - 1) / 400 // 模 400 的闰年，如 2000 
                   - 460;             // 1900 之前的闰年常量
    // 计算总天数：间隔年数 * 平年天数 + 闰年数 + 当年天数
    int total_days = y * 365
                   + leap_count
                   + day_accumulate[month - 1];
    // 处理边界情况（当年是闰年）
    if (month > 2 && is_leap(year)) {
        total_days += 1;
    }
    // 返回模 7 的结果（从星期一开始的偏移量）
    return ((total_days % 7 + 7) % 7 + 1) % 7;
}


int main() {
    int year, month;
    printf("请输入“年-月”: ");
    scanf("%d-%d", &year, &month);

    printf("\n日 一 二 三 四 五 六\n");
    int offset = get_offset(year, month);

    for (int i = 0; i < offset; i++) {
        printf("   ");
    }
    
    for (int i = 1; i <= get_day(year, month); i++) {
        printf("%2d ", i);
        if ((i + offset) % 7 == 0) {
            printf("\n");
        }
    }

    return 0;
}