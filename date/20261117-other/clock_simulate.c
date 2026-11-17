#include <stdio.h>
#include <windows.h> // 调用 Sleep

void clock_2_loops(int h, int m) {
    for (; h < 24; h = (h == 23) ? 0 : h + 1, m = 0) {
        for (; m < 60; m++) {
            printf("%2d:%02d %s\n", 
                (h + 11) % 12 + 1, // 显示范围从 0-11 挪到 1-12
                // 12 小时制不存在形如 0:00 am，改成 12:00 am 
                m, 
                (h < 12) ? "am" : "pm" // 判定 am/pm
            );            
            Sleep(1000); // 这里正常应该填 60000 毫秒
            // 但我不想等一整天去截张图，故填一秒模拟一分钟
            // 以及懒得实现 esc 退出了，用 winapi 可以写
        }
    }
}

// 多拎出来一层 for 处理上下午和 h 越界归零（其实更繁琐了）
void clock_3_loops(int h, int m) {
    static const char ampm[][3] = {"am\0", "pm\0"};
    // 这里需要预处理，把 ampm 从 hour 拆出来
    _Bool is_pm = (h >= 12);
    h %= 12;
    // 大层迭代的时候，把小层的变量归零
    for (;; is_pm = !is_pm, h = 0) {
        for (; h < 12; h++, m = 0) {
            for (; m < 60; m++) {
                printf("%2d:%02d %s\n", 
                    (h + 11) % 12 + 1, 
                    m, 
                    ampm[is_pm]
                );
                Sleep(1000); // 一秒模拟一分钟，原因同上
            }
        }
    }
}

int main() {
    int h, m;
    printf("请输入当前时间（形如 23:45）：");
    scanf("%d:%d", &h, &m);
    if (h < 0 || h > 23 || m < 0 || m > 59) {
        printf("输入不合法");
        return 1;
    }

    // clock_2_loops(h, m);
    clock_3_loops(h, m);

    return 0;
}