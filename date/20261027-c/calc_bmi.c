// BMI = weight (kg) / height^2 (m^2)
#include <stdio.h>

int main() {

    float weight, height;

    printf("请输入体重 (kg)：");
    scanf("%f", &weight);
    printf("请输入身高 (m)：");
    scanf("%f", &height);

    printf("BMI:%.2f\n", weight / (height * height));
    
    return 0;
}