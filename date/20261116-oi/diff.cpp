#include <iostream>
using namespace std;

const int nMax = 100000 + 5;
int n, m;
long long a[nMax], diff[nMax];

void print_diff() {
	// for (int i = 0; i < n; i++) cout << diff[i] << " ";
	// cout << endl;
}

int main() {
	
	cin >> n >> m;
	
	cin >> a[0];
	diff[0] = a[0];
	for (int i = 1; i < n; i++) {
		cin >> a[i];
		diff[i] = a[i] - a[i - 1];
	}

	print_diff();

	for (int i = 0; i < m; i++) {
		int l, r, c;
		cin >> l >> r >> c;

		diff[l - 1] += c;
		diff[r] -= c;

		print_diff();

	}

	long long current = 0;
	for (int i = 0; i < n; i++) {
		current += diff[i];
		cout << current << " ";
	}

	return 0;
}