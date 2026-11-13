#include <stdio.h>

int main() {
    int head, foot;
    scanf("%d %d", &head, &foot);
    if (head < 0 || foot < 0 || foot % 2 != 0 || foot < 2 * head || foot > 4 * head) {
        printf("无解");
        return 1;
    }

    // 二分答案
    int left = 0, right = head;
    while (left <= right) {
        int chicken = (left + right) / 2;
        int rabbit = head - chicken;
        int expected_foot = 2 * chicken + 4 * rabbit;

        if (expected_foot == foot) {
            printf("鸡有 %d 只，兔有 %d 只", chicken, rabbit);
            return 0;
        } else if (expected_foot < foot) {
            right = chicken - 1;
        } else {
            left = chicken + 1;
        }
    }

    printf("无解");
    return 1;
}