#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
//   Дан массив целых чисел длиной n и число m. Найдите все пары чисел, таких что
// a = b mod m
//   Здесь a и b числа из исходной последовательности.
//   Другими словами нужно найти все числа, остатки от деления на m которых равны
//   Если таких чисел нет, вывести на экран соответствующее сообщение.

void output(int* mas,int size){
    for (int i =0; i < size; ++i)
    {
        printf("%d\t", mas[i]);
    }
}

void procedure(int* mas, int size){
    int num = 0;
    scanf("%d", &num);
    int count = 0;

    for (int i = 0; i < size; ++i)
    {
        for (int j = 0; j < size; ++j)
        {
            if((mas[i] % mas[j] == num) && (i != j)){

                printf("\n%d mod %d = %d", mas[i], mas[j], num);

                count += 1;
            }
        }
    }

    if (count == 0){
        printf("No find\n");
    }
    else
        printf("\nFind %d\n", count);
}

int main() {

    int flag = 0;
    int* mas;
    int mas_size;

    while (flag != 4) {
        printf("Chose your step\n"
               "1: Enter array\n"
               "2: procedure array\n"
               "3: Output array\n"
               "4: Exit\n");
        scanf("%d", &flag);

        if (flag == 1)
        {
            printf("Enter array size: ");
            scanf("%d", &mas_size);

            int* mas = (int *) calloc(mas_size,sizeof(int));

            for (int i = 0; i < mas_size; ++i) {
                printf("Enter %d array: ", i + 1);
                scanf("%d", &mas[i]);
            }
            int mas_1[mas_size];
            for(int i = 0; i < mas_size; ++i){
                mas_1[i] = mas[i];
            }
        }
        else if (flag == 2)
        {
                procedure(mas, mas_size);
        }
        else if (flag == 3)
        {
                output(mas, mas_size);
        }
        else if (flag == 4){
            return 1;
        }
        else
        {
            printf("Fail");
            continue;
        }
    }
    free(mas);
    return 0;
}
