#include <stdio.h>
int main() {
    int odd_sum = 0, even_sum = 0;

    for (int i = 1; i <= 100; i++) {
        if (i % 2 == 0) {
            even_sum += i;
        } else {
            odd_sum += i;
        }
    }

    printf("奇数和: %d\n", odd_sum);
    printf("偶数和: %d\n", even_sum);

    return 0;
}