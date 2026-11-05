#include <stdio.h>

int main() {
    int sum = 0;

    for (int i = 1; i <= 10; i++) {
        sum += i;
    }

    // int i = 1;
    // while (i <= 10) {
    //     sum += i;
    //     i++;
    // }

    printf("一到十的和是 %d\n", sum);
    return 0;
}