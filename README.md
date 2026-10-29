# BPU26

C 语言 & AI 课程笔记仓库。每天一个临时分支，事后合并到 `dev`。

---

## 🌟 核心速查与资源 Resources

为了方便复习和查阅，旧课程的核心资料与代码范例已归档至 `archive/` 目录：

- **Python**
  - [速查清单 (Checklist)](./archive/python/docs/checklist.md)
  - [详细讲义 (Reference)](./archive/python/docs/reference.md)
- **Java**
  - [速查清单 (HTML)](https://g-o-s-h.github.io/BPU26/archive/java/docs/checklist.html)
- **C++**
  - [课程大纲与介绍](./archive/cpp/docs/课程介绍.md)

---

## 一、分支规范 Branch Standard

### 1. 命名逻辑 Naming Logic

分支头是日期，形如 `20260929`。

分支尾是类型：
- C 语言课堂上的分支是 `-c`
- 人工智能课堂上的分支是 `-ai`
- 其他时段的分支暂定为 `-other`
- 自定义任务分支用 `-custom`（见 newb）

例如：`2026 年 9 月 29 日` C 语言课上的分支为 `20260929-c`。

### 2. 分支生命周期 Branch Lifecycle

- **临时分支**：每次上课或写作业时创建，**仅保留在本地**，不推送 GitHub。
- **dev 分支**：主开发线，所有临时分支最终合并到这里，并由 `close` 推送到 GitHub。
- **main 分支**：稳定发布线，仅当项目达到"正式版"标准时从 dev 合并。

---

## 二、脚本说明 Scripts

### newb — 创建今日分支

```
newb                   按日期+课型创建分支
newb -custom <name>    创建自定义名字的分支
newb ?                 显示帮助
```

默认行为：
1. 切到 `dev` 并同步 `origin/dev`
2. 按当前日期和时间决定分支名
   - 周二/周四 08:00-10:00 → `yyyyMMdd-c`
   - 周三 08:00-10:00 → `yyyyMMdd-ai`
   - 其他时段 → `yyyyMMdd-other`
3. 创建同名目录 `date/<分支名>`
4. 若 `dev` 上有未提交改动，会随新分支一起带过去

### execute — 编译 / 运行

```
execute <name>                  全仓库搜索 <name> 的源文件
execute <name> -d <dir>         只在指定目录下搜索
execute <name> -f               强制重新编译（跳过时间戳检查）
execute <name> -repeat <N>      重复运行 N 次
execute <name> -test            自动测试（匹配代码同名的 .in 文件）
execute <name> -test <前缀>     自动测试（匹配指定前缀的 .in 文件）
execute <name> -test -all       自动测试（匹配所有 .in 文件）
execute ?                       显示帮助
```

行为：
- 支持后缀 `.c` `.cpp` `.cc` `.cxx` `.py`
- 找到 1 个 → 直接处理；找到多个 → 列出菜单选择
- **时间戳缓存**：exe 比源文件新时跳过编译，直接运行
- `.c` 用 gcc，`.cpp` 用 g++ (多文件工程如 `archive/cpp/sorting/` 可能需要配合 Makefile 或手动构建)
- `.py` 优先使用根目录 `.venv`，否则用系统 python
- 编译 C/C++ 时加 `-fexec-charset=GBK`，让源文件中的中文在 cmd 正常显示
- 运行 Python 时自动注入 `PYTHONPATH=%REPO_ROOT%`，方便在子目录中直接 `import ai_method`，用法详见 [ai_method 接口说明](ai_method/ai.md)
- 如果使用了 `-repeat <N>`，程序会连续运行 N 次，退出码取最后一次运行的退出码。

**关于 `-test` 自动测试：**
为了免去刷题时手动复制测试数据的痛苦，脚本会自动寻找代码所在目录下的 `.in` 文件，并将其内容作为标准输入（`stdin`）喂给程序，运行完回显输出。
- 没有任何参数（如 `execute calc -test`）：匹配 `calc.in`, `calc_1.in` 等。
- 指定前缀（如 `execute calc -test caseA`）：匹配 `caseA.in`, `caseA_1.in` 等。
- 全部运行（如 `execute calc -test -all`）：无视文件名，运行同目录下所有 `.in` 文件。
*(建议将刷题的数据文件放在同级目录，脚本会自动抓取)*

### close — 关闭当前分支 / 推送 dev

```
close              合并到 dev + 推送 + 删除分支
close -nomerge     直接删除分支，不合并（危险）
close -pushdev     直接推送当前所在的 dev 分支
close ?            显示帮助
```

默认流程：
1. 检查工作区必须干净
2. 读 PAT：本机已配置则自动读取，否则星号回显手动输入（支持 Ctrl+V / 右键粘贴）
3. 切到 `dev`，`git pull --rebase` 同步
4. `git merge --no-ff` 合并临时分支到 `dev`
5. `git push origin dev`
6. 删除本地临时分支
7. 清理 PAT（只存内存环境变量，不落盘）

本机免 PAT 输入（一次性配置）：
1. 仓库根目录创建 `.close_local_pat`，内容为本机 Windows 用户名
2. 首次 `close` 时按提示把 PAT 存入 Windows 凭据管理器
3. 之后自动读取，不再手动输入
4. `.close_local_pat` 必须加进 `.gitignore`，不进版本库

`-nomerge` 说明：
- 直接删除当前分支，**未 commit 的改动会丢失**
- 工作区里**未提交的改动**会继承到 `dev`
- 需要输入 `DELETE` 大写确认词 + PAT 二次锁

### venv — 管理虚拟环境

```
venv init              创建（若不存在）并激活 .venv 环境
venv quit              退出当前 shell 的 venv 激活
venv req save          导出依赖到 requirements.txt
venv req load          从 requirements.txt 安装依赖
venv pip install xxx   在 venv 里跑 pip（无需激活）
venv python xxx.py     在 venv 里跑 python（无需激活）
venv ?                 显示帮助
```

`.venv/` 已在 `.gitignore` 中。

**⚠️ 重要提示：**
日常跑代码或装包，推荐直接使用**命令代理模式**（如 `venv pip`、`venv python`），此模式无需激活环境。如果你需要让终端前缀出现 `(.venv)`，请手动执行 `.venv\Scripts\activate`。

---

## 三、日常使用流程 Workflow

### 一次完整的课程循环

1. `newb` → 创建今日分支（如 `20261008-c`）
2. 在 `date/<分支名>/` 下写代码、记笔记
3. `execute <文件名>` → 编译/运行验证
4. `git add . && git commit -m "..."`
5. `close` → 合并到 dev + 推送 GitHub

### 特殊任务

```
newb -custom test01        → 建 test01 实验分支
（...干活...）
close                      → 正常合并到 dev
```

### 只想删分支，不想合并

```
close -nomerge             → 直接删分支，未提交改动继承到 dev
```

### 测试多组数据（结合 execute 的 -test）

1. 在代码同级目录准备 `calc_1.in`, `calc_2.in`
2. 运行 `execute calc -test` 自动跑完所有数据并回显结果。

---

## 四、注意事项 Notes

### 🐍 首次运行准备 (极为重要)

由于虚拟环境 `.venv/` 和 API 密钥文件不会被 Git 追踪，你在拉取代码后（或者在新的机器上），必须先打开终端执行以下两条命令，才能跑通 Python 相关代码：

```bash
# 1. 初始化并创建虚拟环境（只需执行一次）
venv.bat init

# 2. 一键安装 requirements.txt 中的所有依赖
venv.bat req load
```
*(注：日常运行代码直接使用 `execute <name>` 即可，脚本会自动去 `.venv` 里找 Python，无需手动激活。)*

### ⚠️ 基础构筑工具必须在 dev 分支上修改

**`newb.bat`、`close.bat`、`execute.bat`、`venv.bat`、`.gitignore`、`.vscode/`、`README.md` 等属于"基础构筑"，必须在 `dev` 分支上修改并提交。**

原因：
- 这些是所有分支共用的工具，不属于任何一天的作业。
- 如果在临时分支上修改，`close` 执行 `git checkout dev` 时，**磁盘上的脚本会被 git 换成 dev 版本**。
- Windows cmd 执行 bat 时，如果文件被中途修改，会导致执行混乱甚至中断。

正确做法：
```bash
git checkout dev
#（修改脚本）
git add . && git commit -m "chore: ..."
git push origin dev
```

### ⚠️ 校园网连不上 GitHub

校园网直连 GitHub 会报 `Failed to connect to port 443` 或 `Connection was reset`。挂梯子也救不了。

**推送 GitHub 时请使用手机热点。**

### 其余网络排查

推 GitHub 超时或 SSL 报错时：
1. 关掉梯子（SSL 证书错误大多是梯子中间人导致）
2. 热点也超时的话可以用 `ipconfig /flushdns`

### 💡 VSCode 自动激活 venv 的补充说明

工作区配置中已经默认关闭了 Python 终端自动激活。如果你的终端依然莫名出现了 `(.venv)` 前缀，可以检查你的全局用户配置：

`Ctrl+Shift+P` → `Preferences: Open User Settings (JSON)` → 确保包含：

```json
"python.terminal.activateEnvironment": false
```

保存后**关掉所有终端重新打开**，前缀就会消失。

### PAT 使用

- `close` 需要输入 GitHub Personal Access Token (PAT)
- PAT 仅暂存于内存环境变量，脚本结束时立即清除
- 建议使用 fine-grained token，只授权 `Contents: Read and write`，限定本仓库
- PAT 保存位置：语雀私密文档（已开启二次验证）

---

## 五、目录结构 Directory Layout

```
BPU26/
├── .venv/                    Python 虚拟环境（git 忽略）
├── .vscode/                  VS Code 工作区配置（终端、编码、换行符自动对齐）
├── ai_method/                自研 AI 工具封装库
│   ├── ai.md                 接口说明
│   ├── utils.py              核心工具集（读取配置、获取 Client、文件选择等）
│   └── _secrets_/            存放密钥
│       ├── loader.py         配置读取器
│       └── secret.json       实际 API Key 配置文件（git 忽略）
├── archive/                  ✨ 旧资料归档 / 代码范例库
│   ├── cpp/                  C++ 学习资料与范例
│   │   ├── docs/             课程大纲与随堂笔记（Markdown）
│   │   └── sorting/          多文件排序算法范例（头文件与源文件）
│   ├── java/                 Java 学习资料
│   │   └── docs/             Java 速查表（HTML）
│   └── python/               Python 学习资料与范例
│       ├── docs/             Checklist 与 Reference
│       ├── basic_code/       基础代码范例
│       ├── knn/              KNN 算法范例
│       ├── sorting/          排序算法范例
│       └── turtle/           海龟绘图范例
├── date/                     按日期归档的课堂记录
│   ├── 20261020-c/           2026-10-20 C 语言课
│   │   ├── note.md           课堂笔记
│   │   ├── float_to_int.c    课堂代码
│   │   ├── calc.in           测试用例
│   │   ├── float_to_int.exe  编译产物（git 忽略）
│   │   └── ...
│   ├── 20261021-ai/          2026-10-21 AI 课
│   │   ├── note.md           课堂笔记
│   │   ├── study.py          AI 识别业务代码
│   │   └── ...
│   ├── ...
│   └── <yyyyMMdd>-<type>/    后续按此格式递增
│       ├── note.md           每日笔记
│       ├── *.c / *.cpp       C / C++ 源代码
│       ├── *.py              Python 脚本
│       ├── *.in              测试数据文件
│       └── ...
├── tools/                    自研底层工具源码（如 repo-tool）
├── release/                  正式版产物索引
├── .gitignore
├── .gitattributes            Git 换行符强制配置（保证跨平台一致性）
├── close.bat
├── close.py
├── execute.bat
├── newb.bat
├── venv.bat
└── README.md
```

### 目录与文件说明

**1. `date/` 目录**
- 目录名 = 分支名，形如 `<yyyyMMdd>-<type>`（`c` 代表 C 语言，`ai` 代表人工智能，`other` 代表其他）。
- 每天一个目录，里面存放当天的 `note.md`、源代码（`.c` / `.py`）、以及相关产物。不仅记录笔记，也记录随堂练习代码。

**2. `archive/` 目录**
- 存放以往学习过的其他语言（Python、Java、C++）的旧资料和代码范例。
- 作为个人知识库，将长期沉淀的核心笔记（如 Checklist）与代码片段分类保存。

**3. `ai_method/` 模块**
- 为了提升代码复用性（DRY 原则）而自研封装的 Python 工具库。
- `utils.py` 中封装了系统原生文件选择器（`pick_file`）、百度 AI 客户端实例化（`get_baidu_client`）、文件二进制读取（`get_file_content`）和 JSON 格式化输出（`print_json`）。
- 业务代码（如 `date/20261021-ai/study.py`）只需 `import ai_method.utils as ai` 即可极简调用。
- `_secrets_/` 用于安全隔离密钥，已在 `.gitignore` 中屏蔽，绝不污染版本库。

**4. 脚本**
- 根目录下的 `.bat` 与 `.py` 脚本为自动化基础设施，详细用法见上文“脚本说明”。

### 目录命名规则

- `date/` 下的目录名 = 分支名，形如 `<yyyyMMdd>-<type>`
- `<type>` 取值：`c`（C 语言课）、`ai`（AI 课）、`other`（其他）
- 每个目录下按需放置代码、笔记、作业等
- 目录数量随时间增长，上面仅为格式示例

### 每个目录里可能有什么

| 文件名 | 说明 |
|--------|------|
| `*.c` / `*.cpp` | C / C++ 源代码 |
| `*.py` | Python 脚本 |
| `note.md` | 课堂笔记（Markdown 格式） |
| `note.src.md` | 笔记源文件（含 `@src` / `@exe` 占位符，见 TODO） |
| `*.in` | 测试数据，配合 `execute -test` 使用 |
| `Makefile` | 多文件项目时的构建脚本（可选） |
| `*.exe` | 编译产物（git 忽略） |

---

## 六、发布正式版 Release Process

当某个版本的 repo-tool 达到"完全可用、无 bug"状态时：

1. 在 Win7 32 位虚拟机测试通过
2. 编译最终 exe：
   ```bash
   set GOOS=windows
   set GOARCH=386
   go build -o repo-tool.exe .
   ```
3. 把 dev 合并到 main：
   ```bash
   git checkout main
   git merge dev
   git push origin main
   ```
4. 打 tag：
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
5. 打开 GitHub Releases 页面 → 创建 Release
   - 选择 v1.0.0 tag
   - 上传 `repo-tool.exe`
   - 填写发布说明
6. 在 `release/` 目录下创建对应的 `<版本号>.md`，写清此版本的变更、用法、校验和
7. `README.md` 的"目录结构"或单独一节里超链接引用该文件

---

## 七、待办 TODO

### P1：近期

- [ ] **sync-notes 工具**
  - 目的：提交前（如 close 时）自动把代码和运行结果注入到 `note.md`，替代手动复制。
  - **触发机制**：不生成 `note.src.md`，直接操作 `note.md`。对比 `note.md` 的 LastWriteTime 和 Git 的上次 commit 时间，若修改过才启动扫描解析。
  - **实现语言**：Python 脚本。
  - **语法约定**：
    - `@src <name>`：自动寻找 `<name>.c`（或 .cpp/.py）并嵌入源码。
    - `@exe <name>`：自动编译运行 `<name>`，并在后续行接收**若干行输入样例**，最后捕获运行结果输出。
    - `@end`：作为块结束标识（待定，需找一个不易冲突的结束符）。
  - 调用链：`close → sync-notes (Python) → execute`
  - 失败策略：任何一个 `@exe` 编译失败，整体中止，不写入文件（原子性）。

### P2：下次做

- [ ] **repo-tool 部署工具**
  - 语言：Go 1.20（Win7 最后支持版本）
  - 编译目标：`GOOS=windows GOARCH=386`，32 位静态链接
  - 功能：一键部署环境 + clone 仓库 / 一键清理（删仓库 + 敏感文件，保留通用工具）
  - 代码位置：`tools/repo-tool/`
  - 产物位置：`release/`，exe 本体 gitignore
  - 部署场景：Win7 32 位机房（校园网、可能无管理员权限、无 U 盘）
  - 兼容策略：考虑到无 U 盘，需要实现在线下载，并包含“临时 PAT 与部署仓库本体在关机/下次启动时自动销毁”的逻辑。

- [ ] **execute 支持多文件项目**
  - 判定依据：目标文件所在目录是否存在 Makefile
  - 有 Makefile → 调 `make run`（约定 Makefile 里定义 run 目标）
  - 无 Makefile → 现有 gcc/g++ 单文件逻辑

### P3：远期

- [ ] **close 的二维码传 PAT 方案**
  - 其他机器扫二维码一次性获取 PAT，供一节课使用，全自动
  - 思路：本机起临时服务 → 生成含一次性 token 的二维码 → 扫码下发 → 课后自动失效

- [ ] **脚本输出 ANSI 颜色**
  - 提升交互体验（需兼容 Win7 的 cmd）。

- [ ] 补全历史项目的 README

---

_最后更新：2026-10-27 Deepseek_