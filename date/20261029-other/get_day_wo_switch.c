#include <stdio.h>

int main() {
    int year, month, day = 0;
    printf("请输入年份和月份（格式：YYYY-MM）：");
    scanf("%d-%d", &year, &month);

    if (month == 1 
     || month == 3 
     || month == 5 
     || month == 7 
     || month == 8 
     || month == 10 
     || month == 12) {
    
        day = 31;
    
    } else if (month == 4 
            || month == 6 
            || month == 9 
            || month == 11) {
        
        day = 30;
    
    } else if (month == 2) {
        
        if ((year % 4 == 0 && year % 100 != 0)
         || (year % 400 == 0)) {
        
            day = 29;
        
        } else {
        
            day = 28;
       
        }
    
    } else {
        printf("无效的月份（需要在 1-12 之间）\n");
        return 0;
    }

    printf("%d 年 %d 月有 %d 天\n", year, month, day);
    return 0;
}



