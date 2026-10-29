### 标准 C 语言的 switch 语句

_多分支选择结构：语法、执行流程与实战要点_

针对整形表达式的值，在多个固定的整型常量中做“等值匹配分发”

#### 一句话定义

- switch 是 c 语言的关键字，用于多分支选择结构
- 根据 switch 后表达式的值，跳转到第一个与之相等的 case 标签处开始执行

#### 典型使用场景

- 菜单、命令选择：按用户输入的编号执行对应操作
- 运算符分发：按 四则运算 走不同计算流程
- 状态机与有限枚举：星期、月份、状态码的映射

- （诺娃补充）enum / enum class 枚举

#### 解决的痛点

- 多个离散取值需要分别处理时，if-else 嵌套可读性差
- switch 让“按取值分类”的逻辑一目了然、结构清晰

#### 与 if 的分工

- switch：对有限个整形常量做精确等值匹配
- if-else：任一布尔条件、区间与复杂逻辑判断

#### 标准语法结构

表达式结果必须微整形；
每个 case 后面跟整形常数表达式，
break 结束分支，
default 可要可不要


```c
switch (整形表达式) {

    case 常量1:
        语句1;
        语句2;
        ...
        break; // 结束分支，跳出 switch

    case 常量2:
        语句;
        // 这里不 break，就会继续执行 case 常量3 里的语句
    
    case 常量3:
        语句;
        break;

    default: // 所有 case 都不执行时执行 default
        语句;

}
```

#### break 与 case 穿透

```c
switch (month) {
    
    case 12: case 1: case 2:
        printf("冬");
        break;

    case 3: case 4: case 5:
        printf("春");
        break;

    case 6: case 7: case 8:
        printf("夏");
        break;
    
    case 9: case 10: case 11:
        printf("秋");
        break;

    default:
        printf("输入的月份不合法")
}
```

```c
switch (month) {
    
    case 12:
    case 1:
    case 2:
        printf("冬");
        break;

    case 3:
    case 4:
    case 5:
        printf("春");
        break;

    case 6:
    case 7:
    case 8:
        printf("夏");
        break;
    
    case 9:
    case 10:
    case 11:
        printf("秋");
        break;

    default:
        printf("输入的月份不合法")
}
```