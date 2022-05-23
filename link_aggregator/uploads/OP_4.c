#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int NSW_prime_recursion(num) {
    if (num == 0 || num == 1) {
        return 1;
    } else {
        return 2 * NSW_prime_recursion(num - 1) + NSW_prime_recursion(num - 2);
    }
}

double NSW_prime_formula(num) {
    return ((pow(1 + pow(2, 0.5), num) + pow(1 - pow(2, 0.5), num)) / 2);
}


int main(){
    int user_step;
    int number;

    while (1) {
        printf("Chose your step\n"
               "1: Enter number NSW\n"
               "2: Exit\n");
        if (scanf("%d", &user_step) != 1)
            while(fgetc(stdin) != '\n')
                continue;
        if (user_step == 1) {
            printf("Enter number \n");
            if (scanf("%d", &number) != 1)
                while(fgetc(stdin) != '\n')
                    continue;
            else if (number >= 0) {
                printf("Number by recursion --- %d\n", NSW_prime_recursion(number));
                printf("The number according to the formula --- %f\n", NSW_prime_formula(number));
            }
            else {
                printf("invalid number");
            }
        }
        else if (user_step == 2)
            return 0;
        else {
            printf("invalid enter\n");
            continue;
        }
    }
}