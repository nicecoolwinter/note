# ex1







- 指標三個位置代表含意務必搞懂 , &p , p , *p

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{

    int a = 100;
    int *p = &a;

    printf("%p\n", &a);
    printf("%d\n\n", a);

    // &p 是指標的位址 , 指標本身也是一塊記憶體拿來紀錄某塊記憶體位址
    printf("%p\n", &p);
    printf("%p\n", p);
    printf("%d\n", *p);

    return 0;
}

```


- 下面差異程式碼 , 前面兩區塊是等價 , 那 *p 是等價於 a 內容

```c
int a = 100; 
int *p = &a;
```
```c
int a = 100; 
int *p;
p = &a;
```

```c
*p
```

---

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char aa[4][20];  // aa 陣列名稱是指標常數 , 無法變動
    char (*cpa)[20] =  aa;  // cpa 是指標可以變動

    printf("%d\n", &aa[3][19] - &aa[0][0]);
    return 0;
}

```


```c
#include <stdio.h>
#include <stdlib.h>

void test(char (*aa)[20]) {
     // aa 是 char (*)[20] 指標
    printf("aa=%ld\n", sizeof(aa)); 
}

int main()
{
    char *cp;
    char (*cpa)[20];
    char aa[4][20] = {100,127};

    cp = &aa[0][0];  // cp 型態是 char*   &a[0][0] 型態是 char  ,  a[0][0] 型態是 char 
    cpa = aa;   // cp & aa 型態都是 char (*)[20]

    printf("cp=%ld\n", sizeof(cp));
    printf("cpa%ld\n", sizeof(cpa));
    printf("aa=%ld\n", sizeof(aa));

    test(aa);
    
    return 0;
}




```