## 关键字考察

- **输入、输出** <details> <summary></summary>
    - `input`
    - `print`
</details>

- **推导式输入** <details> <summary></summary>
    - `a = [int(each) for each in input().split()]`
</details>

- mapping 输入 <details> <summary></summary>
    - `a = list(map(int, input().split()))`
</details>

- **数据类型**（5 种）<details> <summary></summary>
    - `int`
    - `float`
    - `bool`
    - `str`
    - `list`
</details>

- **四个空值** <details> <summary></summary>
    - None
        值是空，类型也是不存在的
    - 0
        整数 int / 浮点数 float 的空值
    - '\0' 或者 '\000'
        字符串型的空值
    - ""
        字符串类型的 “空串”
</details>

- **选择结构** <details> <summary></summary>
    - `if <条件>`
    - `elif <条件>`
    - `else`
</details>

- 列表的函数（直接展开说功能）<details> <summary></summary>
    - `len`
    - `max`
    - `min`
</details>

- 列表的方法（直接展开说功能）<details> <summary></summary>
    - `append(value)`
        - 只能在末尾添加
    - `insert(position, value)`
        - 在任意位置添加
    - `pop(position)`
        - 删除位置的值
    - `remove(value)`
        - 删除某个数值（第一次出现）
    - `index(value)`
        - 找一个数的下标
    - `count(value)`
        - 找这个数出现的次数
        - `count(<not_exist>) => 0`
    - `reverse()`
        - 倒置
    - `sort()`
        - 排序（默认是 从小到大）
</details>

- **循环** <details> <summary></summary>
    - `for <变量> in range()`
    - `for <变量> in <集合>`
    - `for 里有 if，if 里有 break，for 外有 else`（吃剩饭）
    - `while <条件>`
    - `while 里有 if，if 里有 break，while 外有 else`（吃剩饭）
</details>



## 七则运算

- **分别是什么？**<details> <summary></summary>
    - `+`
    - `-`
    - `*`
    - `/`
    - `**`
    - `//`
    - `%`
</details>


## 函数

- 函数三要素 <details> <summary></summary>
    - 函数名
    - 参数
    - 返回值
</details>


## 布尔运算符

- 有几个？<details> <summary></summary>
    - 9个
</details>

- 分为几类？<details> <summary></summary>
    - 比较符
    - 逻辑符
</details>

- **分别是什么？**<details> <summary></summary>
    - 比较符
        - `>`
        - `>=`
        - `<`
        - `<=`
        - `==`
        - `!=`
    - 逻辑符
        - `and`
        - `or`
        - `not`
</details>


## 打擂台思想

- 解释具体思路 <details> <summary></summary>
    - 第一个人上擂台
    - 后续每个人跟擂台上的单挑，赢的留下
</details>

- **功能** <details> <summary></summary>
    - 在一堆数里面求最大值、最小值、其他最值
</details>


## 区间的三个参数

- `range(a, b, c)` 的三个参数分别表示了 <details> <summary></summary>
    - 起点 start
    - 终点 end
    - 步长 step
</details>

- `range(10)` 代表哪些数？ <details> <summary></summary>
    0 1 2 3 4 5 6 7 8 9
</details>

- `range(4, 9)` 代表哪些数？ <details> <summary></summary>
    4 5 6 7 8
</details>

- `range(3, 15, 4)` 代表哪些数？ <details> <summary></summary>
    3 7 11
</details>

- `range(9, -1, -1)` 代表哪些数？ <details> <summary></summary>
    9 8 7 6 5 4 3 2 1 0
</details>


## 列表的三个参数

`nums` 是一个 `list`

- `nums[2:7]` 代表 <details> <summary></summary>
    从 元素 2 到 元素 6
</details>

- `nums[4:]` 代表 <details> <summary></summary>
    从 元素 4 到末尾元素
</details>

- `nums[:7]` 代表 <details> <summary></summary>
    从 元素 0（开头）到 元素 6
</details>

- `nums[::-1]` 代表 <details> <summary></summary>
    从末尾到开头（倒序）
</details>


## 列表的其他内容

- 列表里可以存储哪些类型？ <details> <summary></summary>
    所有类型（跟变量一样）
</details>

- 有 n 层嵌套的列表是多少维？ <details> <summary></summary>
    n 维
</details>

- 加法运算的功能 <details> <summary></summary>
    连接两个列表
</details>

- 乘法运算的功能 <details> <summary></summary>
    连着复制很多份
</details>


## 计数循环

- **解释一下迭代** <details> <summary></summary>
    更新换代，每一轮循环换一个新的值
</details>

- for 循环的功能 <details> <summary></summary>
    让迭代变量依次经过范围内的每个值
</details>

- for each 的功能 <details> <summary></summary>
    让迭代变量依次变成集合内的每个元素
</details>

- for 循环的“迭代变量”一般用哪几个<details> <summary></summary>
    - `i`
    - `j`
    - `k`
</details>

- for each 一般用哪个迭代变量 <details> <summary></summary>
    - `each`
    - 如果嵌套，变量命名应当形如 `each_student`, `each_score`
</details>

- for else 的触发条件 <details> <summary></summary>
    循环结束，没 break 过
</details>

- for else 的具体逻辑 <details> <summary></summary>
    - for 里有 if，if 里有 break，触发 break 会结束循环
    - for 外有 else，如果循环结束没 break 过就执行 else
</details>


## 当型循环

- **while 循环的功能** <details> <summary></summary>
    当条件成立时循环
    （可以无视次数循环）
</details>

- while 跟什么条件是死循环？<details> <summary></summary>
    `while True`
</details>

- while else 的触发条件 <details> <summary></summary>
    循环结束，没 break 过
</details>


## 递推
- 斐波那契数列 <details> <summary></summary>
    1 1 2 3 5 8 13 21 34 55 89
</details>

- **通项公式** <details> <summary></summary>
    表示数列的某几项的关系，在任何时候都成立
</details>

- **斐波那契数列的通项公式** <details> <summary></summary>
    `fib[i] = fib[i - 1] + fib[i - 2]`
</details>


## 字符串
- 转义字符（的功能是什么？）<details> <summary></summary>
    用来区分 “代码里的关键字” 和 “字符串里直接输出的字符”
</details>

- **转义字符 Escape Characters** <details> <summary></summary>
    - `\` 的位置在哪里？
        退格键 Backspace 和回车键 Enter 之间

    - `\`（行末）
        ```py
        print(
        """\
        1: hamburger
        2: pizza
        3: ...\
        """)
        ```
    
    - `\\`
        ```py
        print("\\")
        ```
        result: 
        ```
        \
        ```

    - `\'`
        输出的时候 转换为 普通的 单引号

    - `\"`
        输出的时候 转换为 普通的 双引号
        
    - `\0`
        None
        空（什么都没有）
        0 (整数)

    - `\n`
        输出的时候按换行处理
        ```py
        print("123\n123456")
        ```
        result
        ```
        123
        123456
        ```
    - `\r`
        输出的时候按回车执行，将位置挪到开头，覆盖先前输出的内容
        ```py
        print("Hello\r World!")
        print("1234567890\rabc")
        ```
        result
        ```
        World!
        abc4567890
        ```
</details>

- 字符串运算 String Operations（跟 list 的运算规则相同）<details> <summary></summary>
    - `+`
        连接 concat
        ```py
        print("abc" + "123")
        ```
        result
        ```
        abc123
        ```
    - `*`
        复制 clone
        ```py
        print("abc" * 2)
        ```
        result
        ```
        abcabc
        ```
    - `[]`
        索引，查找某个单字符
        ```py
        print("chicken"[3])
        name = "kun"
        print(name[1])
        ```
        result
        ```
        c
        u
        ```
    - `[a:b]` 和 `[a:b:c]`
        从 a 到 b（不等于b），每一次间隔 c

    - char in string
        字符串 string 包含 单字符 char
    - not in
        不包含，跟上方相反
    - r串
        相当于每个字符都是字面意思，取消转义，也取消特殊字符的功能（意义）
        所见即所得
</details>

- 字符串函数 String Functions <details> <summary></summary>
    ```py
    len(string)
    max(string)
    min(string)
    ```
</details>

- 字符串方法 String Methods <details> <summary></summary>
    常用 功能
    ```py
    string.count(str, beg = 0, end = len(string)) # 在 begin 和 end 之间统计 str 出现的次数
        "aaaabbccc".count("a") # 结果是 4，因为 a 出现了四次
        "abcabcabc".count("abc") # 结果是 3，因为 abc 出现了三次
    string.find(str, beg = 0, end = len(string)) # 在这个范围内，从左往右，找 str 第一次出现的位置。找不到返回 -1
        "aaaabbccc".find("a") # 结果 0，因为从左往右，第一个 a 在 0 的位置出现
        "aaaabbccc".find("x") # 结果 -1，因为 x 没出现过
    string.rfind(str, beg = 0, end = len(string)) # 在这个范围内，从右往左，找 str 第一次出现的位置。找不到返回 -1
        "aaaabbccc".rfind("a") # 结果 3，因为从右往左，第一个 a 在 3 的位置出现
        "aaaabbccc".find("x") # 结果 -1，因为 x 没出现过
    string.index(str, beg = 0, end = len(string)) # 跟 find 功能类似，但没找到会报错（不会返回 -1，代码直接崩溃）
        "aaaabbccc".index("a") # 结果 0，因为从左往右，第一个 a 在 0 的位置出现
        "aaaabbccc".index("x") # 代码崩溃，因为 x 没出现过
    string.rindex(str, beg = 0, end = len(string)) # 跟 index 类似，从右往左（类似 rfind）
        "aaaabbccc".index("a") # 结果 3，因为从右往左，第一个 a 在 0 的位置出现
        "aaaabbccc".index("x") # 代码崩溃，因为 x 没出现过

    string.capitalize() # 首字母变成大写，后面变成小写
        "abcdEFG".capitalize() # 结果 "Abcdefg"
    string.upper() # 全部大写
        "abcdEFG".upper()      # 结果 "ABCDEFG"
    string.lower() # 全部小写
        "abcdEFG".lower()      # 结果 "abcdefg"
    string.swapcase() # 大小写交换
        "abcdEFG".swapcase()   # 结果 "ABCDefg"
    string.replace(old, new, <max>) # 把 old 字符串替换为 new 字符串，最高 max 次（可以不指定 - 全部替换）
        "abcdEFG".replace("bc", "1234") # 结果 "a1234dEFG"

    string.split(sep = None, maxsplit = -1) # 在 string 里面逢 sep 就分割，最多 maxsplit 次，存到一个 list 里（默认切割空格 " "）
        "Hello World How Are You".split() # 结果是 ["Hello", "World", "How", "Are", "You"]
    string.splitlines([keepends]) # 逢 "\r" "\n"（换行符）分割
    string.join(seq) # 让 seq 的每一项连接起来，中间加上 string
        "-".join([1, 2, 3]) # 结果是 "1-2-3"
    string.lstrip(<chars>) # 删掉左侧的空格 / 指定字符
        "     abcd     ".lstrip() # 结果是 "abcd     "
    string.rstrip(<chars>) # 删掉右侧的空格 / 指定字符
        "     abcd     ".rstrip() # 结果是 "     abcd"
    ```

    不常用 功能
    ```py
    string.center(width, fillchar)
    string.encode(encoding = "utf-8", errors = "strict")
    string.expandtabs(tabsize = 8)
    string.ljust(width, <fillchar>)
    string.maketrans()
    string.rjust(width, <fillchar>)
    string.strip(<chars>)
    string.title()
    string.translate(table, deletechars = "")
    string.zfill(width)
    ```

    常用 判断
    ```py
    # 判断是否以 substr 开头（可以指定范围）
    string.startswith(substr, beg = 0, end = len(string))
    # 判断是否以 suffix 结尾（可以指定范围）
    string.endswith(suffix, beg = 0, end = len(string))

    string.isalpha() # 非空，全是字母
        "abc".isalpha()    # 返回 True
        "abc123".isalpha() # 返回 False，因为包含数字
        "abc!".isalpha()   # 返回 False，因为包含非字母字符
        "".isalpha()       # 返回 False，因为空字符串不包含任何字符

    string.isnumeric() # 非空，全是数字字符（包括阿拉伯数字 0 - 9，汉语数字一二三，全角数字等）
        "123".isnumeric()       # 返回 True
        "一二三".isnumeric()     # 返回 True（因为“一二三”是汉字数字）
        "Ⅳ".isnumeric()         # 返回 True（因为“Ⅳ”是罗马字符）
        "IV".isnumeric()        # 返回 False（用英文字母表示的罗马数字在这个方法中不被认为是数字）

    string.isalnum() # alpha + numeric = alnum
        "abc12三".isalnum()  # 返回 True
        "abc!".isalnum()    # 返回 False

    string.isdigit()   # 非空，全是数字 0 - 9
        "123".isdigit()  # 返回 True
        "12a".isdigit()  # 返回 False

    string.isdecimal() # 全是十进制（可以用于判断 bytes 串）

    string.isupper() # 全是大写
    string.islower() # 全是小写
    ```

    [isdigit 和 isdecimal 的区别](https://blog.csdn.net/zhangchen124/article/details/81630631)
    [特殊字符（包含罗马字符）](https://zhuanlan.zhihu.com/p/481922245)

    不常用 判断
    ```py
    string.isspace() # 只有空格
    string.istitle() # 是标题格式（目前没啥用）
    ```
</details>


<!-- 待补全 -->

- 输出格式化 <details> <summary></summary>

    - 手动调整
        ```py
        a = int(input())
        b = int(input())
        print(a, "+", b, "=", a + b)
        ```

    - 格式串 + %
        ```py
        print("%d + %d = %d" % (a, b, a + b))

        # 四舍五入
        print("%.2f" % number)
        print(round(number, 2))
        ```
        - %d integer 整数
        - %f float 浮点数
        - %s string 字符串

    - str.format() 方法
        ```py
        print("{a} + {b} = {result}".format(a = a, b = b, result = a + b))
        ```

    - f string（f 串）
        ```py
        print(f"{a} + {b} = {a + b}")
        ```
</details>

- ASCII 码和字符如何转换 <details> <summary></summary>
    - `chr(code)` 把 ASCII Code 转换成对应的字符 (char, Character, chr)
    - `ord(char)` 把字符 (char) 转换成对应的 ASCII Code (order, Order, ord)
</details>

- **常用 ASCII 码** <details> <summary></summary>
    - `' '`: 32
    - `'0' - '9'`: 48 - 57
    - `'A' - 'Z'`: 65 - 90
    - `'a' - 'z'`: 97 - 122
</details>


## 函数

- 函数三要素 <details> <summary></summary>
    - 函数名
    - 参数
    - 返回值
</details>

- **函数的格式** <details> <summary></summary>
    ```py
    def 函数名(参数名1: 参数类型, 参数名2: 参数类型) -> 返回值类型:
        代码行
        return 返回值
    ```

    ```py
    def 函数名(参数名1, 参数名2):
        代码行
        return 返回值
    ```
</details>

- 全局变量声明<details> <summary></summary>
    全局变量：跟随整体代码的变量，从代码中的第一个赋值开始，到运行完消失
    局部变量：某一个代码块内使用的变量，从代码块内被定义（第一次赋值）开始，到这个代码块结束消失
    ```py
    a = 1

    def first():
        global a
        print(a)
    ```
</details>


## 递归

- 如果说“递推”是积少成多，那么“递归”是 <details> <summary></summary>
    - 大事化小，小事化了
</details>

- **以求阶乘为例，阐述递归三要素** <details> <summary></summary>
    - 终止条件 / 基础情况：1! = 1（这时候退出）
    - 状态转移方程：n! = n * (n-1)!
    - 递归调用：（调用 (n-1)! 就是一种递归调用，在 fac(n) 的函数里面调用了 fac(n-1)）
</details>

- 递归 & 递推 —— 优劣分析 <details> <summary></summary>

    递归：
    - 容易爆栈（stack overflow），待处理的问题堆的太多
    - 运行时间长

    - 代码可读性强
    - 逻辑清晰，方便编写

    递推：
    - 效率高，速度快
    - 占的内存少（变量反复使用）

    - 有时候可读性很差（譬如
    ```py
    while a % b != 0:
        a, b = b, a % b
    ```
    - 逻辑很容易把自己绕进去，需要特意设计迭代
</details>


## 模块化

- import 和 pip install <details> <summary></summary>
    ```bat
    @REM 检查更新（如果是最新版只会有一行提示）
    py -m pip install --upgrade pip
    @REM 安装某个包（这里以 tqdm 为例）
    py -m pip install tqdm
    ```

    ```py
    # 几种 import 方法
    import math
    import random as rd
    from os import system
    from my_lib import * 
    # 不建议 import *，因为很容易产生冲突，
    # 因此干脆不讲这个内容（大部分教程都会
    # 批判这个坏习惯）
    ```
</details>

<!-- 
- <details> <summary></summary>
    
</details>
 -->


## 补充：match case

（类似一般代码的 switch case  
https://zhuanlan.zhihu.com/p/585154318  