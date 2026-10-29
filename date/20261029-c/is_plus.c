#include <stdio.h>

int main() {

    char temp;
    scanf("%c", &temp);

    if (temp == '+') {
        printf("是加号\n");
    } else {
        printf("不是加号\n");
    }

    return 0;
}