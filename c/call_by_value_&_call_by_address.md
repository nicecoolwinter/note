# call by value & call by address

## call by value 

- 只是copy value main函數a b 變數跟 swap函數 a b 都是再不同記憶體空間

```c
#include <stdio.h>

void swap(int a, int b) {
    int tmp;

    printf("swap before a=%d, b=%d\n", a, b);
    tmp = a;
    a = b;
    b = tmp;
    printf("swap after a=%d, b=%d\n", a, b);
}



int main(int argc, char* argv[])
{
    int a = 100, b = 50;

    printf("main before a=%d, b=%d\n", a, b);
    swap(a, b);
    printf("main after a=%d, b=%d\n", a, b);
    return 0;
}
```


## call by address

- swap 函數指標a & b 指向 main a & b 變數同塊記憶體
- 你可以在複習一下 * & 用法

```c
#include <stdio.h>

void swap(int *a, int *b) {
    int tmp;

    printf("swap before a=%d, b=%d\n", *a, *b);
    tmp = *a;
    *a = *b;
    *b = tmp;
    printf("swap after a=%d, b=%d\n", *a, *b);
}



int main(int argc, char* argv[])
{
    int a = 100, b = 50;

    printf("main before a=%d, b=%d\n", a, b);
    swap(&a, &b);
    printf("main after a=%d, b=%d\n", a, b);
    return 0;
}

```