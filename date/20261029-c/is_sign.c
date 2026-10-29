#include <stdio.h>

int main() {

    char temp;
    scanf("%c", &temp);

    switch (temp) {
        
        case '+':
            printf("是加号\n");
            break;

        case '-':
            printf("是减号\n");
            break;

        case '*':
            printf("是乘号\n");
            break;
            
        case '/':
            printf("是除号\n");
            break;
            
        default:
            printf("不是运算符\n");
    }

    // if (temp == '+') {
    //     printf("是加号\n");
    // } else if (temp == '-') {
    //     printf("是减号\n");
    // } else if (temp == '*') {
    //     printf("是乘号\n");
    // } else if (temp == '/') {
    //     printf("是除号\n");
    // } else {
    //     printf("不是运算符\n");
    // }

    return 0;
}