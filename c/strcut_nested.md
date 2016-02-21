# strcut nested

## 巢狀結構(nested structure)  

- 就strcut 裡面包strcut 
- strcut 復合資料型態可以先想成只是一個型態類似 char int long float double , 但是裡面`資料至少一個欄位名稱以上` 下面struct Student 例子就有四個欄位

- 再來是struct Student students[2]; 宣個陣列裡面元素型態是strcut

```c
struct Student {
    char* name;
    int number;

    struct {
        char* color;
        double radius;
    } ball;
};

int main(int argc, char* argv[])
{
    struct Student student1 = {.name = "James",
        .number = 1,
         .ball.color = "red",
               .ball.radius = 10.0
    };

    struct Student student2 = {.name = "Jason",
        .number = 2,
         .ball.color = "black",
               .ball.radius = 6.0
    };

    // 把宣告陣列2 , 裡面元素是結構這樣解釋
    struct Student students[2] = {

        {
            .name = "James",
            .number = 1,
            .ball.color = "red",
            .ball.radius = 10.0
        },

        {
            .name = "Jason",
            .number = 2,
            .ball.color = "black",
            .ball.radius = 6.0
        }
    };

    printf("student1 name=%s, number=%d, color=%s, radius=%f\n", student1.name,
           student1.number, student1.ball.color, student1.ball.radius);

    printf("student2 name=%s, number=%d, color=%s, radius=%f\n", student2.name,
           student2.number, student2.ball.color, student2.ball.radius);


    printf("student1 name=%s, number=%d, color=%s, radius=%f\n", students[0].name,
           students[0].number, students[0].ball.color, students[0].ball.radius);
    printf("student2 name=%s, number=%d, color=%s, radius=%f\n", students[1].name,
           students[1].number, students[1].ball.color, students[1].ball.radius);


    return 0;
}
```


- 因為使用了c99, 下面這指定struct欄位名稱是c語言c99用法所以gcc 要下 -std=c99

```c
            .name = "James",
            .number = 1,
            .ball.color = "red",
            .ball.radius = 10.0
```

```c
gcc test.c -std=c99 -o test
```



