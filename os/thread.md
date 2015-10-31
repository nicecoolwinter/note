# thread

## HW pi.c
```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

long incircle = 0;
long points_per_thread;

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void *runner() {
    long incircle_thread = 0;

    unsigned int rand_state = rand();
    long i;
    for (i = 0; i < points_per_thread; i++) {
        /* Was initially using random(), but didn't appear to get performance
         * improvement with threading. random() apparently uses some global state
         * that is shared between threads, and isn't guaranteed to be threadsafe. */
        double x = rand_r(&rand_state) / ((double)RAND_MAX + 1) * 2.0 - 1.0;
        double y = rand_r(&rand_state) / ((double)RAND_MAX + 1) * 2.0 - 1.0;

        if (x * x + y * y < 1) {
            incircle_thread++;
        }
    }

    pthread_mutex_lock(&mutex);
    incircle += incircle_thread;
    pthread_mutex_unlock(&mutex);
}

/* Calculate Pi by the Monte Carlo method. Program arguments are the total number of random
 * points to use in the calculation and the number of threads to use. */
int main(int argc, const char *argv[])
{
    if (argc != 3) {
        fprintf(stderr, "usage: ./pi <total points> <threads>\n");
        exit(1);
    }

    long totalpoints = atol(argv[1]);
    int thread_count = atoi(argv[2]);
    points_per_thread = totalpoints / thread_count;

    /* Tried using clock, but it measures CPU time, not wall clock time,
     * so doesn't demonstrate improvement gained by threading */
    time_t start = time(NULL);

    srand((unsigned)time(NULL));

    pthread_t *threads = malloc(thread_count * sizeof(pthread_t));

    pthread_attr_t attr;
    pthread_attr_init(&attr);

    int i;
    for (i = 0; i < thread_count; i++) {
        pthread_create(&threads[i], &attr, runner, (void *) NULL);
    }

    for (i = 0; i < thread_count; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&mutex);
    free(threads);

    printf("Pi: %f\n", (4. * (double)incircle) / ((double)points_per_thread * thread_count));
    printf("Time: %d sec\n", (unsigned int)(time(NULL) - start));

    return 0;
}
```
```
gcc pi.c -o pi -lpthread

./pi 10 2
```


http://shihyu.github.io/books/ch35s01.html

创建线程的时候提到一个函数`pthread_self`，这个函数使POSIX线程库中的一个函数，通过这个函数可以获得线程的ID，可是我们打印出来这个ID会发现这个ID是一个很大的数字。没有得到我们想象的一个数字，其实这个ID是POSIX线程库提供的一个数字，而linux内核中也为这个线程提供了一个ID，这个ID可以通过gettid获得，`gettid`是linux内核提供的一个系统调用，Glibc没有封装函数，只能通过系统调用实现。

```c
數據類型
pthread_t：線程句柄
pthread_attr_t：線程屬性
線程操縱函數（簡介起見，省略參數）
pthread_create()：創建一個線程
pthread_exit()：終止當前線程
pthread_cancel()：中斷另外一個線程的運行
pthread_join()：阻塞當前的線程，直到另外一個線程運行結束
pthread_attr_init()：初始化線程的屬性
pthread_attr_setdetachstate()：設置脫離狀態的屬性（決定這個線程在終止時是否可以被結合）
pthread_attr_getdetachstate()：獲取脫離狀態的屬性
pthread_attr_destroy()：刪除線程的屬性
pthread_kill()：向線程發送一個信號

同步函數
用於 mutex 和條件變量
pthread_mutex_init() 初始化互斥鎖
pthread_mutex_destroy() 刪除互斥鎖
pthread_mutex_lock()：佔有互斥鎖（阻塞操作）
pthread_mutex_trylock()：試圖佔有互斥鎖（不阻塞操作）。當互斥鎖空閒時將佔有該鎖；否則立即返回
pthread_mutex_unlock(): 釋放互斥鎖
pthread_cond_init()：初始化條件變量
pthread_cond_destroy()：銷毀條件變量
pthread_cond_wait(): 等待條件變量的特殊條件發生
pthread_cond_signal(): 喚醒第一個調用pthread_cond_wait()而進入睡眠的線程
Thread-local storage（或者以Pthreads術語，稱作 線程特有數據）:
pthread_key_create(): 分配用於標識進程中線程特定數據的鍵
pthread_setspecific(): 為指定線程特定數據鍵設置線程特定綁定
pthread_getspecific(): 獲取調用線程的鍵綁定，並將該綁定存儲在 value 指向的位置中
pthread_key_delete(): 銷毀現有線程特定數據鍵

與一起工作的工具函數
pthread_equal(): 對兩個線程的線程標識號進行比較
pthread_detach(): 分離線程
pthread_self(): 查詢線程自身線程標識號
```


## pthread_create & pthread_join  還沒create thread PID 會跟 TID 相同


getppid // 取得父行程ID
getpid  // 取得目前ID
gettid  // 取得目前 Thread ID (TID)


```c
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/syscall.h>

#define gettid() syscall(__NR_gettid)

void *show_message( void *ptr )
{
    char *message;
    message = (char *) ptr;
    int x = 5;
    for(x = 5 ; x > 0 ; --x) {
        printf("the %s thread ppid = %d,pid = %d,tid = %ld.\n",message, getppid(),getpid(),gettid());
        sleep(2);
    }
}

int main() {
    pthread_t thread1;
    pthread_t thread2;

    printf("the main thread ppid = %d,pid = %d,tid = %ld.\n",getppid(),getpid(),gettid());  // 還沒create thread PID 會跟 TID 相同

    pthread_create(&thread1, NULL , show_message , (void*) "Thread 1");
    pthread_create(&thread2, NULL , show_message , (void*) "Thread 2");
    pthread_join( thread1, NULL);
    pthread_join( thread2, NULL);

    return 0;
}

```
```
gcc thread_test.c -o thread_test -lpthread
```

## 27603 是 shell 的 pid

```
the main thread ppid = 27603,pid = 31008,tid = 31008.
the Thread 1 thread ppid = 27603,pid = 31008,tid = 31009.
the Thread 2 thread ppid = 27603,pid = 31008,tid = 31010.
the Thread 1 thread ppid = 27603,pid = 31008,tid = 31009.
the Thread 2 thread ppid = 27603,pid = 31008,tid = 31010.
the Thread 1 thread ppid = 27603,pid = 31008,tid = 31009.
the Thread 2 thread ppid = 27603,pid = 31008,tid = 31010.
the Thread 1 thread ppid = 27603,pid = 31008,tid = 31009.
the Thread 2 thread ppid = 27603,pid = 31008,tid = 31010.
the Thread 1 thread ppid = 27603,pid = 31008,tid = 31009.
the Thread 2 thread ppid = 27603,pid = 31008,tid = 31010.
[shihyu-MS-7758 ~]$ echo $$
27603
```

