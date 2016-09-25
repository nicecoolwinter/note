# strlen  vs sizeof


```c
#include <stdio.h>
#include <stdlib.h>
int main()
{
    char strAry[] = "This is string";

    printf("%ld\n", sizeof(strAry));
    printf("%ld\n", strlen(strAry));

    return 0;
}
```

