#include <stdio.h>

int n;
int prime[100005];

void print_format(int num) {
    static int allign = 1;
    printf("%5d%c", 
        num, 
        (allign++ % 10 == 0)
            ? '\n' 
            : ' '
    );
}

int main() {
    printf("输入一个整数：");
    scanf("%d", &n);
    if (n < 2) {
        printf("输入必须 >= 2");
        return 1;
    }

    int top = 1;
    print_format(prime[0] = 2);

    for (int i = 3; i <= n; i += 2) {
        _Bool flag = 1;

        for (int j = 0; prime[j] <= i / prime[j]; j++) {
            if (i % prime[j] == 0) {
                flag = 0;
                break;
            }
        }

        if (flag) {
            prime[top++] = i;
            print_format(i);
        }
    }

    return 0;
}