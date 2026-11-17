/*
编写程序，任意输入两个整数，计算其最大公约数、最小公倍数，提示：分开计算，即在不同的循环中。
*/

#include <stdio.h>

int get_gcd(int a, int b) {
    // 辗转相除（其实也可以写成 while）
    for (int r = a % b; r > 0; 
        a = b, 
        b = r, 
        r = a % b
    );
    return b;
}

long long get_lcm(int a, int b) {
    // 加步长判断
    long long step = a > b ? a : b;
    long long m = step;
    while (m % a != 0 || m % b != 0)
        m += step;
    return m;
}

int main() {
    int a, b;
    printf("输入两个正整数：");
    scanf("%d %d", &a, &b);    

    int gcd = get_gcd(a, b);
    long long lcm = (long long)a * (b / gcd);
    // long long lcm = get_lcm(a, b);
    // 这个实现逻辑非常磨蹭，过测试点的时候我干脆用公式了
    printf("最大公约数：%d\n最小公倍数：%lld", gcd, lcm);

    return 0;
}