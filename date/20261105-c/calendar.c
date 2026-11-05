/*
 * 万年历程序
 * FlashNova
 * 2026-11-05 09:53
 */

#include <stdio.h>

/*
 * 获取指定年份和月份的天数
 * @param year 年份
 * @param month 月份
 * @return 天数
 */
int get_day(int year, int month) {

    switch(month) {

        case 1: 
        case 3: 
        case 5: 
        case 7: 
        case 8: 
        case 10: 
        case 12:
            return 31;
        
        case 4: 
        case 6: 
        case 9: 
        case 11:
            return 30;
       
        case 2:
            if ((year % 4 == 0 
              && year % 100 != 0)
             || (year % 400 == 0)) {
                return 29; // 闰年
            } else {
                return 28; // 平年
            }
    
        default:
            return -1; // 非法
    }
}

/*
 * 获取指定年份和月份的偏移天数
 * @param year 年份
 * @param month 月份
 * @return 偏移天数
 */
int get_skip(int year, int month) {
    int skip = 0;
    
    for (int i = 1900; i < year; i++) {
        if ((i % 4 == 0 
          && i % 100 != 0)
         || (i % 400 == 0)) {
            skip ++;
        }
        skip += 365;
        skip %= 7;
    }

    for (int i = 1; i < month; i++) {
        skip += get_day(year, i);
        skip %= 7;
    }

    return skip;
}


int main() {
    int year, month;
    printf("请输入“年-月”: ");
    scanf("%d-%d", &year, &month);

    printf("\n日 一 二 三 四 五 六\n");
    int skip = get_skip(year, month);

    for (int i = 0; i < skip; i++) {
        printf("   ");
    }
    
    for (int i = 1; i <= get_day(year, month); i++) {
        printf("%2d ", i);
        if ((i + skip) % 7 == 0) {
            printf("\n");
        }
    }

    return 0;
}