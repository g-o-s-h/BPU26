/*
编写程序，输出200以内能被3和5同时整除的数，要求每行5个数。

提交代码和运行结果的截图。
*/

#include <stdio.h>

int main() {
    for (int i = 1, count = 0; i <= 200; i++) {
        // if (i % 3 == 0 && i % 5 == 0) {
        if (i % 15 == 0) {
            printf("%3d ", i);
            count++;
            if (count % 5 == 0) {
                printf("\n");
            }
        }
    }
    return 0;
}

/*
 * Line 12 优化解释：根据同余定理
 * “模 3 余 0” 的同时 “模 5 余 0”
 * 等价于 “模 15 余 0”
 */