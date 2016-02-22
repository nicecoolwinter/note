# GDB


# GDB


- foo.c

```c
#include <stdio.h>

int foo(int a, int b)
{
    int s = a + b;
    printf("%d\n", s);
    return s;

}
```

- main.c


```c
extern int foo(int a, int b);
int main(int argc, char* argv[])
{
    int s = foo(10, 20);
    return s;
}

```


- Makefile

```c
all: so main
so:
	gcc -g foo.c -shared -fPIC -o libfoo.so
main:
	gcc -g main.c -L./ -lfoo -o test
clean:
	rm -f test *.so

```

##實驗 

```sh
make
mkdir src lib
mv *.c src
mv libfoo.so
```

預期使用 directory 指定程式碼路徑 
使用 solib-absolute-prefix ＆ solib-search-path 指定lib 路徑
可使最後失敗必須用set env LD_LIBRARY_PATH 才可以

```
gdb ./test
directory ./src
set env LD_LIBRARY_PATH ./lib/
```


## 問題

1.想知道為什麼 solib-absolute-prefix ＆ solib-search-path 指定lib 不行？ 
2.  下面四個指令有什麼差異？
set solib-absolute-prefix  <br>
set solib-search-path <br>
set env LD_LIBRARY_PATH  <br>
set debug-file-directory<br>


