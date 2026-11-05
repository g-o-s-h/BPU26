#include <stdio.h>

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
            if ((year % 4 == 0 && year % 100 != 0)
             || (year % 400 == 0)) {
                return 29; // 闰年
            } else {
                return 28; // 平年
            }
    
        default:
            return -1; // 非法
    }
}

int main() {

    int year, month;
    printf("请输入年份: ");
    scanf("%d", &year);
    printf("请输入月份: ");
    scanf("%d", &month);

    printf("\n日 一 二 三 四 五 六\n");
    for (int i = 1; i <= get_day(year, month); i++) {
        printf("%2d ", i);
        if (i % 7 == 0) {
            printf("\n");
        }
    }

    // char *day_tags[] = {
    //     "日", "一", "二", "三", "四", "五", "六"
    // };
    // for (int i = 0; i < 7; i++) {
    //     printf("%3s", day_tags[i]);
    // }

    // for (int i = 1; i <= 30; i++) {
    //     if (i % 7 == 1) {
    //         printf("\n");
    //     }
    //     printf("%3d", i);
    // }

    // printf("日\t一\t二\t三\t四\t五\t六\n");
    // for (int i = 1; i <= 30; i++) {
    //     printf("%d\t", i);
    //     if (i % 7 == 0) {
    //         printf("\n");
    //     }
    // }

}