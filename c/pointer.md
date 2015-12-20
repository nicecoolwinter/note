# pointer


##指標基本6個要點:
```
1.指標也是一塊記憶體 , 跟一般變數區別只是在於它是拿來存放某塊記憶體位址
2.指標要搞懂指標根本型態
3.指向的型態
4.等號兩邊型態必須要一致才可以assign 不然編譯會發出警告, 這規則一般型態也是一樣
5.指標offset(偏移長度）,
6 指標本身佔多大塊記憶體 , 32位元是 4btye, 64位元機器是 8 byte , 這個CPU 定址範圍有關系
ex: 32位元電腦最高支援4G(2^32)記憶體大小, 4byte = 32bit
```

以下面例子來解釋

```c
int a = 100;  // a 變數是個int 型態, assign 100 到這塊記憶體

int *pointer = &a;  // pointer 變數是個指標 , 型態是 int* ;

那第四要點提到等號左右兩邊必須要一樣型態才可以 assign , 既然 pointer變數型態是int*

那代表 &a 也要是 int* , 加上& 之後a 變數要退化一個維度,這概念你可以先背起來 ,

所以&a 型態就變成 int* 符合第四個要素, 編譯就不發出警告

int a;
int *pointer = &a;  // 也可以拆成

int *pointer;
pointer = &a;  // 這時候不能用 *p 跟初始化直接 assign 意義不同了

這時候的 *pointer 是指向a 變數內容可做存取動作 , ex : *pointer = 200;

要點5 & 6 要搞清楚之間差異


以32位元電腦 , 下面指標不管只幾個維度指標都是佔4byte大小
sizeof(char*);
sizeof(char**);
sizeof(int*);
sizeof(long***);
sizeof(float***);
sizeof(void**);
sizeof(double**);

既然佔用記憶體大小都一樣,那不同型態指標之間差異在哪？

在於offset不同, 還有是用二補數或是IEEE764 解析你要存放的記憶體內容

先以offset 長度來說好了

char *a = 1000;
a++;
printf("%d\n",a); // 會是1001


int *a = 1000;
a++;
printf("%d\n",a); // 會是1004


float *a = 1000;
a++;
printf("%d\n",a); // 會是1004


int *long = 1000;
a++;
printf("%d\n",a); // 會是1008


double *a = (double*)1000;
a++;

printf("%ld\n", *(long *)&a);


下面給個完整例子因為上面寫法只是為了測試正常不應該這樣寫所以會出現一些編譯器警告左右兩邊型態不一致問題

#include <stdio.h>

int main(int argc, char *argv[])
{
    double *a = (double*)1000;
    a++;

    printf("%ld\n", *(long *)&a);


    return 0;
}

```

- 列舉5種指標容易搞混的情況
- 1 & 2 是宣告指標變數是等價關係 , 第2 方式是拆成兩步驟
- 3 是 指標指向a變數內容可以做讀寫存取動作
- 4 & 5 要小心之間差異

```c
// 1
int *pointer = &a;  // 宣告指標初始化指向 a 變數


// 2
int *pointer; // 宣告指標
pointer = &a; // 指標指向 a 變數


// 3
*pointer = 200;  // 指標指向a變數內容可以做讀寫存取動作

// 4
printf("%p\n",(void*)pointer);  // 印出指標內容 , 內容即是a 變數位址

// 5
printf("%p\n",(void*)&pointer); // 指標變數本身也是一塊記憶體所有有位址 , 代表指標變數位址 , 初學者常常搞不懂宣告一塊指標變數來存記憶體用但是指標變數本身也是一塊記體所以也是也位址 , 4 & 5 要比較一下差異 , 意義差很大可以對照我畫的示意圖

```


```c
#include <stdio.h>

int main(int argc, char *argv[])
{

    int a = 100;
    int *pointer = &a;

    printf("%d\n",a);
    printf("%p\n",(void*)&a);
    *pointer = 200;
    printf("%p\n",(void*)pointer);
    printf("%p\n",(void*)&pointer);
    printf("%d\n",a);

    return 0;
}
```


![](./images/pointer1.jpg)

![](./images/pointer2.jpg)
