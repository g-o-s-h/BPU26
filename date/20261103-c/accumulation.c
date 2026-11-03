#include <stdio.h>
int main() {

    int sum = 0, 
        i = 1;

    while (i <= 10) {
        sum += i;
        i++;
    }

    // for (int i = 1; i <= 10; i++) {
    //     sum += i;
    // }
    
    printf("累加和: %d\n", sum);
    return 0;
}