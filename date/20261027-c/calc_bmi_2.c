// BMI = weight (kg) / height^2 (m^2)
#include <stdio.h>

int main() {

    float weight, height;

    printf("请输入体重 (kg)：");
    scanf("%f", &weight);
    printf("请输入身高 (m)：");
    scanf("%f", &height);

    float bmi = weight / (height * height);

    if (bmi < 18.5) {
        printf("BMI:%.2f, 偏瘦\n", bmi);
    } else if (bmi < 24) {
        printf("BMI:%.2f, 正常\n", bmi);
    } else if (bmi < 28) {
        printf("BMI:%.2f, 偏重\n", bmi);
    } else {
        printf("BMI:%.2f, 肥胖\n", bmi);
    }

    return 0;
}