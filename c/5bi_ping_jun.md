# 5筆平均

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int 5RamAvg(int *sum)
{
    i = i % 5;
    sum -= array[i];
    array[i] = (rand() % 5) + 10;
    sum += array[i];
    printf("i=%d, new=%d, sum=%f\n",i, array[i], sum / 5.0);
    i++;
    getchar();

    return *sum / 5.0; // return avg of 5 items. 
}

int main()
{
    int array[5] = {0};
    int i;
    int sum = 0;

    srand(time(NULL));

    for (i = 0; i < 5; i++) {
        array[i] = (rand() % 5) + 10;
        sum = sum + array[i];
        printf("a[%d] = %d\n", i, array[i]);
    }

    printf("sum=%f\n", sum / 5.0);
    
    // printf("%d\n",i);

    while(1) {
        5RamAvg();
    }

    return 0;
}
```