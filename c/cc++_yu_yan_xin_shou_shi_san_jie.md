# C/C++ 語言新手十三誡


目錄：                                                       (頁碼/行號) 2/24

01. 不可以使用尚未給予適當初值的變數                                     3/46
02. 不能存取超過陣列既定範圍的空間                                       5/90
03. 不可以提取不知指向何方的指標                                         7/134
04. 不要試圖用 char* 去更改一個"字串常數"                               12/244
05. 不能在函式中回傳一個指向區域性自動變數的指標                        16/332
06. 不可以只做 malloc(), 而不做相應的 free()                            19/398
07. 在數值運算、賦值或比較中不可以隨意混用不同型別的數值                21/442
08. ++i/i++/--i/i--/f(&i)哪個先執行跟順序有關                           24/508
09. 慎用Macro                                                           27/574
10. 不要在 stack 設置過大的變數以避免堆疊溢位(stack overflow)           32/684
11. 使用浮點數精確度造成的誤差問題                                      35/750
12. 不要猜想二維陣列可以用 pointer to pointer 來傳遞                    36/772
13. 函式內 new 出來的空間記得要讓主程式的指標接住                       40/860




---

##01. 你不可以使用尚未給予適當初值的變數

錯誤例子：
```c
int accumulate(int max)    /* 從 1 累加到 max，傳回結果 */
{
    int sum;    /* 未給予初值的區域變數，其內容值是垃圾 */
    for (int num = 1; num <= max; num++) {  sum += num;  }
    return sum;
}```

正確例子：
```c
int accumulate(int max)
{
    int sum = 0;    /* 正確的賦予適當的初值 */
    for (int num = 1; num <= max; num++) {  sum += num;  }
    return sum;
}
```

備註：

```
根據 C Standard，具有靜態儲存期(static storage duration)的變數，
例如 全域變數(global variable)或帶有 static 修飾符者等，
　如果沒有顯式初始化的話，根據不同的資料型態予以進行以下初始化：

　若變數為算術型別 (int , double , ...) 時，初始化為零或正零。
　若變數為指標型別 (int*, double*, ...) 時，初始化為 null 指標。
　若變數為複合型別 (struct, double _Complex, ...) 時，遞迴初始化所有成員。
　若變數為聯合型別 (union) 時，只有其中的第一個成員會被遞迴初始化。

                                       (以上感謝Hazukashiine板友指正)

(但是有些MCU 編譯器可能不理會這個規定，所以還是請養成設定初值的好習慣)
```






##02. 你不可以存取超過陣列既定範圍的空間

錯誤例子：
```c
int str[5];
for (int i = 0 ; i <= 5 ; i++) str[i] = i;
```

正確例子：

```c
int str[5];
for (int i = 0; i < 5; i++) str[i] = i;
```



說明：宣告陣列時，所給的陣列元素個數值如果是 N, 那麼我們在後面
透過 [索引值] 存取其元素時，所能使用的索引值範圍是從 0 到 N-1

C/C++ 為了執行效率，並不會自動檢查陣列索引值是否超過陣列邊界，
我們要自己來確保不會越界。一旦越界，操作的不再是合法的空間，
將導致無法預期的後果。

備註：

C++11之後可以用Range-based for loop提取array、
vector(或是其他有提供正確.begin()和.end()的class)內的元素


可以確保提取的元素一定落在正確範圍內。

例：

```c
// vector
std::vector<int> v = {0, 1, 2, 3, 4, 5};

for(const int &i : v) // access by const reference
    std::cout << i << ' ';
std::cout << '\n';

// array
int a[] = {0, 1, 2, 3, 4, 5};
for(int n: a)  // the initializer may be an array
    std::cout << n << ' ';
std::cout << '\n';
```

補充資料：

http://en.cppreference.com/w/cpp/language/range-for

## 你不可以提取(dereference)不知指向何方的指標（包含 null 指標）。

錯誤例子：

    char *pc1;      /* 未給予初值，不知指向何方 */
    char *pc2 = NULL;  /* pc2 起始化為 null pointer */
    *pc1 = 'a';     /* 將 'a' 寫到不知何方，錯誤 */
    *pc2 = 'b';     /* 將 'b' 寫到「位址0」，錯誤 */

    正確例子：
    char c;          /* c 的內容尚未起始化 */
    char *pc1 = &c;  /* pc1 指向字元變數 c */
    *pc1 = 'a';      /* c 的內容變為 'a' */

    /* 動態分配 10 個 char(其值未定),並將第一個char的位址賦值給 pc2 */
    char *pc2 = (char *) malloc(10);
    pc2[0] = 'b';    /* 動態配置來的第 0 個字元，內容變為 'b'
    free(pc2);

    說明：指標變數必需先指向某個可以合法操作的空間，才能進行操作。

    ( 使用者記得要檢查 malloc 回傳是否為 NULL，
      礙於篇幅本文假定使用上皆合法，也有正確歸還記憶體 )

    錯誤例子：

    char *name;   /* name 尚未指向有效的空間 */
    printf("Your name, please: ");
    fgets(name,20,stdin);   /* 您確定要寫入的那塊空間合法嗎??? */
    printf("Hello, %s\n", name);

    正確例子：

    /* 如果編譯期就能決定字串的最大空間，那就不要宣告成 char* 改用 char[] */

    char name[21];   /* 可讀入字串最長 20 個字元，保留一格空間放 '\0' */
    printf("Your name, please: ");
    fgets(name,20,stdin);
    printf("Hello, %s\n", name);


    正確例子(2)：

    若是在執行時期才能決定字串的最大空間，C提供兩種作法：

    a. 利用 malloc() 函式來動態分配空間，用malloc宣告的陣列會被存在heap
    須注意：若是宣告較大陣列，要確認malloc的回傳值是否為NULL

    size_t length;
    printf("請輸入字串的最大長度(含null字元): ");
    scanf("%u", &length);

    name = (char *)malloc(length);
    if (name) {         // name != NULL
        printf("您輸入的是 %u\n", length);
    } else {            // name == NULL
        puts("輸入值太大或系統已無足夠空間");
    }
    /* 最後記得 free() 掉 malloc() 所分配的空間 */
    free(name);
    name = NULL;  //(註1)


    b. C99開始可使用variable-length array (VLA)
    須注意：
          - 因為VLA是被存放在stack裡，使用前要確認array size不能太大
          - 不是每個compiler都支援VLA(註2)
          - C++ Standard不支援(雖然有些compiler支援)

    float read_and_process(int n)
    {
        float vals[n];
        for (int i = 0; i < n; i++)
            vals[i] = read_val();
        return process(vals, n);
    }


   正確例子(3)：

   C++的使用者也有兩種作法：

   a. std::vector (不管你的陣列大小會不會變都可用)

    std::vector<int> v1;
    v1.resize(10);               // 重新設定vector size


   b. C++11以後，若是確定陣列大小不會變，可以用std::array
   須注意：一般使用下(存在stack)一樣要確認array size不能太大

    std::array<int, 5> a = { 1, 2, 3 }; // a[0]~a[2] = 1,2,3; a[3]之後為0;
    a[a.size() - 1] = 5;                // a[4] = 0;

備註：

   註1. C++的使用者，C++03或之前請用0代替NULL，C++11開始請改用nullptr
   註2. gcc和clang支援VLA，Visual C++不支援

補充資料：

   http://www.cplusplus.com/reference/vector/vector/resize/






   
   
