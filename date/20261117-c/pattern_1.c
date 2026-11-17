#include <stdio.h>

int main() {
    int m, n;
    printf("输入行数和列数：");
    scanf("%d %d", &m, &n);

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}