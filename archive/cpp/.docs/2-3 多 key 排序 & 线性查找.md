## 刷题（排序）

- P1177
- P1059
- P1093
- P2676

## std::pair

```c++
    pair<int, int> a = {1, 2};
    pair<int, double> b = {1, 2.3};
    cout << a.first << " " << a.second << endl;
```

## struct 结构体 (structure)

```c++
struct Student {
    int id;
    int total_score;
    int chinese;
} student[305];


int main() {
    student[i] = {i + 1, chinese + math + english, chinese};
    cout << student[i].id << " " << student[i].total_score << endl;
}
```

## 查找 search

### 线性查找 linear search

有 `n` 个数，请问他们中间是否存在一个数 `k`。  

第一行输入 `n` 和 `k`  
第二行输入 `n` 个数  

输出 `true` 或者 `false`  

```
8 24
1 5 24 72 100 6 73 8
```

```
yes
```


### 二分查找 binary search

下节课讲