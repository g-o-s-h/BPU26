/*
任意输入一个大于1的整数，判断是否为素数(质数)
*/

#include <stdio.h>
#include <stdbool.h>

bool is_prime(int n) {
    if (n <= 1) return false;
    // 可读性解释：
    // i <= n / i 等价于 i * i < n
    // 但后者更容易导致溢出，因此优先往小值算，而非积出大值
    for (int i = 2; i <= n / i; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int num;
    printf("请输入一个大于1的整数: ");
    scanf("%d", &num);

    if (is_prime(num)) {
        printf("%d 是素数。\n", num);
    } else {
        printf("%d 不是素数。\n", num);
    }

    return 0;
}