#include <stdio.h>

int main() {
    // 1. 挑战将库函数名作为变量名（这在 gcc 下只会产生 Warning，不会报错）
    int printf = 10;
    int scanf = 20;
    
    // 2. 挑战将真·关键字作为变量名（如果取消下面这行的注释，编译会直接失败）
    // int if = 30; 
    // int return = 40;

    // 3. 因为 printf 被我们霸占成变量了，我们改用 puts 来打印字符串
    puts("代码成功编译并运行了！");
    
    // 4. 验证刚才用库函数名命名的变量
    if (printf == 10 && scanf == 20) {
        puts("这证明了 printf 和 scanf 不是关键字，可以被当成变量！");
    }

    return 0;
}