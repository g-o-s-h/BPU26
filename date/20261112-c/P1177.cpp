#include <iostream>
#include <cstdlib>
using namespace std;

const int nMax = 100000 + 10;
int n, num[nMax];

void quickSort(int l, int r) {
    if (l >= r) return;

    int ridx = l + rand() % (r - l + 1);
    swap(num[l], num[ridx]);

    // 夹击 Hoare

    int pivot = num[l];
    int i = l, j = r;

    while (i <= j) {
        while (num[i] < pivot) i++;
        while (num[j] > pivot) j--;
        if (i <= j) {
            swap(num[i], num[j]);
            i++;
            j--;
        }
    }

    quickSort(l, j);
    quickSort(i, r);

    // Hoare

    // int pivot = num[l];
    // int i = l - 1, j = r + 1;
    // while (true) {
    //     do i++; while (num[i] < pivot);
    //     do j--; while (num[j] > pivot);
    //     if (i >= j) break;
    //     swap(num[i], num[j]);
    // }

    // quickSort(l, j);
    // quickSort(j + 1, r);

    // Lomuto

    // int pivot = num[l];
    // int i = l, j = r;

    // while (i < j) {
    //     while (i < j && num[j] >= pivot) j--;
    //     while (i < j && num[i] <= pivot) i++;
    //     if (i < j) 
    //         swap(num[i], num[j]);
    // }
    // swap(num[l], num[i]);

    // quickSort(l, i - 1);
    // quickSort(i + 1, r);
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) 
        cin >> num[i];
    
    quickSort(0, n - 1);
    
    for (int i = 0; i < n; i++)
        cout << num[i] << ' ';

    return 0;
}