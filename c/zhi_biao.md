# 指標

- strAry , &strAry , &strAry[0] 差異

```c
#include <stdio.h>
#include <stdlib.h>
int main()
{
    char strAry[] = "This is string";

    printf("%p\n", strAry);
    printf("%p\n", &strAry[0]);
    printf("%p\n", &strAry);

    printf("%ld\n", sizeof(strAry));
    printf("%ld\n", sizeof(&strAry[0]));
    printf("%ld\n", sizeof(&strAry));

    printf("%c\n",strAry[0]);
    printf("%c\n",strAry[1]);


    printf("%c\n", *strAry);
    printf("%c\n", *(strAry + 1));


    return 0;
}
```

