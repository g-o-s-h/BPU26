#include <stdio.h>

int main() {
    int head, foot;
    scanf("%d %d", &head, &foot);
    if (head < 0 || foot < 0 || foot % 2 != 0 || foot < 2 * head || foot > 4 * head) {
        printf("无解");
        return 1;
    }

    // 最简单的实现方式
    int rabbit = (foot - 2 * head) / 2;
    int chicken = head - rabbit;

    if (rabbit < 0 || chicken < 0
     || 2 * chicken + 4 * rabbit != foot) {
        printf("无解");
        return 1;
    }

    printf("鸡有 %d 只，兔有 %d 只", chicken, rabbit);
    return 0;
}