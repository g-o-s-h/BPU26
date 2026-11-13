#include <stdio.h>

int main() {
    int head, foot;
    scanf("%d %d", &head, &foot);
    if (head < 0 || foot < 0 || foot % 2 != 0 || foot < 2 * head || foot > 4 * head) {
        printf("无解");
        return 1;
    }

    // 一般不这么实现，如果面试这么写，有被打死的风险
    for (int chicken = 0; chicken <= head; chicken++) {
        int rabbit = head - chicken;
        if (2 * chicken + 4 * rabbit == foot) {
            printf("鸡有 %d 只，兔有 %d 只", chicken, rabbit);
            return 0;
        }
    }

    printf("无解");
    return 1;
}