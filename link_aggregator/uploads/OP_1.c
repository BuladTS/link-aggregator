#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
//   Дан массив целых чисел длиной n и число m. Найдите все пары чисел, таких что
// a = b mod m
//   Здесь a и b числа из исходной последовательности.
//   Другими словами нужно найти все числа, остатки от деления на m которых равны
//   Если таких чисел нет, вывести на экран соответствующее сообщение.

void output(int* mas,int size){
    for (int i = 0; i < size; ++i){
        printf("%d\t", mas[i]);
    }
    printf("\n");
}


void procedure(int* mas, int size, int num){
    int count = 0;

    for (int i = 0; i < size; ++i){
        for (int j = 0; j < size; ++j){
            if((mas[i] % mas[j] == num) && (i != j)){

                printf("%d mod %d = %d\n", mas[i], mas[j], num);

                count += 1;
            }
        }
    }

    printf("---------------------");

    if (count == 0){
        printf("No find\n");
    }
    else
        printf("\nFind %d\n", count);
}


int main(){

    char b = 100;
    int a;
    a = (int)b;
    printf("%d", a);
    int fl;
    int size;
    int* mas;
    int fl2;

    while (1){
        fl = 0;
        printf("Chose your step\n"
               "1: Enter array\n"
               "2: procedure array\n"
               "3: Output array\n"
               "4: Exit\n");
        if (scanf("%d", &fl) != 1){
            while(fgetc(stdin) != '\n')
                continue;
        }

            if (fl == 1){
                fl = 2;
                printf("Enter size array:");
                if (scanf("%d", &size) != 1){
                    while (fgetc(stdin) != '\n')
                        continue;
                }

                mas = (int *) calloc(size, sizeof(int));

                int mode;
                printf("User num - 1\n"
                       "Random num - 2\n");
                if (scanf("%d", &mode) != 1){
                    while(fgetc(stdin) != '\n');
                    continue;
                }

                if (mode == 1){
                    for (int i = 0; i < size; ++i){
                        printf("Enter %d member array:", i + 1);
                        if (!scanf("%d", &mas[i]) != 1){
                            while (fgetc(stdin) != '\n')
                                continue;
                        }
                    }
                }
                else if (mode == 2){
                    for (int i = 0; i < size; ++i)
                    {
                        mas[i] = rand() % 100 + 1;
                    }
                }
                else{
                    printf("Error\n");
                    continue;
                }

            }
            else if (fl == 2 && fl2 != 0){
                int num;
                printf("Enter num\n");
                if (scanf("%d", &num) != 1){
                    while (fgetc(stdin) != '\n')
                        continue;
                }
                procedure(mas, size, num);
            }
            else if (fl == 3 && fl2 != 0){
                output(mas, size);
            }
            else if (fl == 4){
                free(mas);
                return 0;
            }
            else{
                printf("Error\n");
                continue;
            }
        }
}
