#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
//   Дан массив целых чисел длиной n и число m. Найдите все пары чисел, таких что
// a = b mod m
//   Здесь a и b числа из исходной последовательности.
//   Другими словами нужно найти все числа, остатки от деления на m которых равны
//   Если таких чисел нет, вывести на экран соответствующее сообщение.
struct h;
struct h {
    int ser;
    int dar;
    struct h bas;
};

int main(){
    int* c;
    struct h* a[3];
    a[0]->ser = 1;
    a[0]->dar = 2;
    c =  (int*)a;
    for (int i = 0; i < 3; ++i) {
        printf("%d", c);
        c++;
    }
    return 0;
}



