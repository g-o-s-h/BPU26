#include <stdio.h>

int main() {
    // 题1验证
    printf("--- 题1 ---\n");
    int n1 = 0;
    while (n1-- >= 0) printf("+++\n");
    printf("^^^\n");

    // 题2验证
    printf("--- 题2 ---\n");
    int num2 = 5;
    if (num2) printf("%d\n", num2); 

    // 题3验证
    printf("--- 题3 ---\n");
    int i3 = 1;
    switch(i3 % 3) {
        case 0: printf("0");
        case 1: printf("1");
        case 2: printf("2");
    }
    printf("\n");

    // 题4验证
    printf("--- 题4 ---\n");
    int x4 = -1;
    int count4 = 0;
    do {
        x4 = x4 * x4;
        count4++;
    } while(!x4);
    printf("循环体执行了 %d 次\n", count4);

    // 题5验证
    printf("--- 题5 ---\n");
    int x5 = 12, y5;
    if(x5 > 12) y5 = x5 + 10;
    else y5 = x5 - 12;
    printf("%d\n", y5);

    // 题6验证
    printf("--- 题6 ---\n");
    int a6 = 2, b6 = 3, c6;
    c6 = a6;
    if (a6 > b6) c6 = 1;
    else if (a6 == b6) c6 = 0;
    else c6 = -1;
    printf("%d\n", c6);

    // 题7验证 (加了3次限制防死循环)
    printf("--- 题7 (演示前3次) ---\n");
    int t7 = 0, count7 = 0;
    while(t7 = 1) {
        t7 = t7 + 1;
        count7++;
        if(count7 == 3) break; 
    }
    printf("由于 while(t=1) 恒成立，执行了 %d 次（理论无限次）\n", count7);

    // 题8验证 (已补全图片中的代码)
    printf("--- 题8 ---\n");
    int count8 = 0;
    for(int i8 = 1; i8 < 5; i8++) {
        printf("程序设计基础\n");
        count8++;
    }
    printf("共输出了 %d 次\n", count8);

    // 题9验证
    printf("--- 题9 ---\n");
    int num9 = 0;
    while(num9 <= 2) {
        num9++; 
        printf("%d\n", num9);
    }

    // 题10验证
    printf("--- 题10 ---\n");
    int a10 = 1, b10 = 7;
    do {
        b10 = b10 / 2;
        a10 = a10 + b10;
    } while(b10 > 1);
    printf("a = %d\n", a10);

    // 题11验证
    printf("--- 题11 ---\n");
    int i11;
    for(i11 = 1; i11 < 4; i11++);
    printf("i = %d\n", i11);

    // 题12验证
    printf("--- 题12 ---\n");
    int x12 = 10, y12 = 20, z12 = 30;
    if(x12 > y12) z12 = x12; 
    x12 = y12; 
    y12 = z12;
    printf("x=%d, y=%d, z=%d\n", x12, y12, z12);

    // 题13验证
    printf("--- 题13 ---\n");
    int a13 = 1, b13 = 2;
    if(a13 == 1) 
        if(b13 == 2) printf("匹配了最近的if\n"); 
        else printf("匹配了外面的if\n");

    // 题14验证 (加了3次限制防死循环)
    printf("--- 题14 (演示前3次) ---\n");
    int count14 = 0;
    for(int i14 = 1; i14 < 5; i14--) {
        printf("我爱中国\n");
        count14++;
        if(count14 == 3) break; 
    }
    printf("由于 i-- 永远小于5，执行了 %d 次（理论无限次）\n", count14);

    return 0;
}