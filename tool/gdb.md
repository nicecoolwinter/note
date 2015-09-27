# gdb

## .gdbinit 設定

用戶根目錄下設置 .gdbinit 文件，文件內容如下：
```sh
set history save on
set history size 10000
set history filename ~/.gdb_history
set print pretty on
set print static-members off
set charset ASCII
```


## GDB控制程序運行過程

- 設置環境變量與配置變量

```
(gdb) set env USER_NAME=smith
(gdb) show env
```

- 設置信號與中斷

```
(gdb) handle SIGINT ignore
```
- 設置寄存器

```
(gdb) set $PC = main
```
- 時候調試（內存轉儲）

```
$ gdb xxxx core
$(gdb) where
```

- 監視點

```
(gdb) watch a[0]
(gdb) watch *0x80049874
```

- 函數斷點

```
(gdb) b method_name
(gdb) b *method_name     ; 函數調用前加斷點，可以觀察參數/返回地址/幀地址等的壓棧過程
```

- 條件斷點

```
(gdb) break 38 if a[0] == 0
```
- 線程斷點

```
(gdb) break **lines** thread **thread_no**
```

- 顯示信息

<table class="muse-table" border="0" cellpadding="5">
  <thead>
    <tr>
      <th>命令</th>
      <th>說明</th>
    </tr>
  </thead>
  <tfoot>
    <tr>
      <td>info line xxx</td>
      <td>xxx在內存中的地址(行號，函數名)</td>
    </tr>
  </tfoot>
  <tbody>
    <tr>
      <td>info f</td>
      <td>當前棧信息</td>
    </tr>
    <tr>
      <td>info args</td>
      <td>當前函數名及參數</td>
    </tr>
    <tr>
      <td>info locals</td>
      <td>當前函數的局部變量</td>
    </tr>
    <tr>
      <td>info catch</td>
      <td>當前函數異常處理信息</td>
    </tr>
    <tr>
      <td>info thread</td>
      <td>當前線程信息</td>
    </tr>
    <tr>
      <td>info proc mapping</td>
      <td>當前程序的內存映像信息</td>
    </tr>
  </tbody>
</table>


- 源碼搜索

```
(gdb) search <regexp>         ; 向前找
(gdb) reverse_search <regexp> ; 全部搜索
```
- 指定源文件路徑
gdb啟動時通過 -d 來制定路徑

```
(gdb) dir <dirname:--:-->
(gdb) show directories  ; 顯示源文件路徑
```

- 彙編顯示

```
(gdb) disas **func**
(gdb) x/5i  0xaddress   ; 如果沒有符號情報，使用該方法
```
- 彙編及調試

```
(gdb) display /i $PC
(gdb) si    ; 執行一條彙編指令
```
- 顯示內存值

```
(gdb) x/nuh (b,w,g,i,s)
(gdb) x/4i $PC
(gdb) x/16xb $SP
(gdb) x/s *(argv+1)
```

<table class="muse-table" border="0" cellpadding="5">
  <thead>
    <tr>
      <th>符號</th>
      <th>說明</th>
    </tr>
  </thead>
  <tfoot>
    <tr>
      <td>s</td>
      <td>字符串</td>
    </tr>
  </tfoot>
  <tbody>
    <tr>
      <td>n</td>
      <td>顯示單位字節個數</td>
    </tr>
    <tr>
      <td>b</td>
      <td>1個字節單位</td>
    </tr>
    <tr>
      <td>h</td>
      <td>2個字節單位</td>
    </tr>
    <tr>
      <td>w</td>
      <td>4個字節單位</td>
    </tr>
    <tr>
      <td>g</td>
      <td>8個字節單位</td>
    </tr>
    <tr>
      <td>i</td>
      <td>指令</td>
    </tr>
  </tbody>
</table>


- 顯示線程執行狀態

```
(gdb) thread apply **n** where  ; n是線程編號
```

- 顯示動態數組

```
(gdb) p *array@len
```

- 運行時設置參數

```
% gdb --args program --foo --bar
(gdb) run

# or
(gdb) set args ....
(gdb) show args
```

- 調試已運行程序

```
;; 方法1
(gdb) <program> PID
;; 方法2
(gdb) attach <program>
```
- 設置觀察點

```
(gdb) watch <expr>  ; 變化時
(gdb) rwatch <expr> ; 被讀時
(gdb) awatch <expr> ; 讀寫時
```
- 設置捕捉點

```
(gdb) catch <event>  ; event可以是C++關鍵字(throw, catch),  系統調用(exec,fork,vfork)等
(gdb) tcatch <event> ; 只設置一次捕捉點，用完就刪除
```
- 輸出格式

<table class="muse-table" border="0" cellpadding="5">
  <thead>
    <tr>
      <th>符號</th>
      <th>說明</th>
    </tr>
  </thead>
  <tfoot>
    <tr>
      <td>p/u</td>
      <td>16進制，無符號</td>
    </tr>
  </tfoot>
  <tbody>
    <tr>
      <td>p/a</td>
      <td>16進制</td>
    </tr>
    <tr>
      <td>p/f</td>
      <td>浮點數</td>
    </tr>
    <tr>
      <td>p/x</td>
      <td>16進制</td>
    </tr>
    <tr>
      <td>p/t</td>
      <td>2進制</td>
    </tr>
    <tr>
      <td>p/o</td>
      <td>8進制</td>
    </tr>
    <tr>
      <td>p/c</td>
      <td>字符</td>
    </tr>
  </tbody>
</table>


- 程序跳轉

```
(gdb) jump <line>
(gdb) jump <address>
(gdb) set $PC=xxxx
```
- 其他顯示選項

<table class="muse-table" border="0" cellpadding="5">
  <thead>
    <tr>
      <th>命令</th>
      <th>說明</th>
    </tr>
  </thead>
  <tfoot>
    <tr>
      <td>set print vtbl</td>
      <td>是否用規格的格式顯示虛函數表</td>
    </tr>
  </tfoot>
  <tbody>
    <tr>
      <td>set print address on/off</td>
      <td>是否顯示函數的參數地址</td>
    </tr>
    <tr>
      <td>set print elements &lt;numbers of elements&gt;</td>
      <td>指定顯示數組的最大元素個數</td>
    </tr>
    <tr>
      <td>set print null-stop on/off</td>
      <td>是否當遇到字符串結束符後停止</td>
    </tr>
    <tr>
      <td>set print pretty on/off</td>
      <td>比較漂亮的顯示結構體</td>
    </tr>
    <tr>
      <td>set print union on/off</td>
      <td>是否顯示結構體內的聯合數據</td>
    </tr>
  </tbody>
</table>


- Frame相關

```
(gdb) bt        ; 顯示上下文
(gdb) frame     ; 顯示當前幀
(gdb) frame n   ; 顯示第n號幀
(gdb) up / down ; 向上或下移動幀
(gdb) i frame 1 ; 詳細顯示1號幀情報
```


### 用GDB調試嵌入式系統

```
#cd /opt
#tar xzvf /tmp/gdb-6.6.tar.gz
#cd /opt
#mkdir -p arm-gdb/build
#cd arm-gdb/build
#/opt/gdb-6.6/configure --target=arm-linux --prefix=/opt/arm-gdb
#make
#make install
#cd /opt/arm-gdb/bin/
#cp arm-linux-gdb /usr/bin/
#cd /opt/gdb-6.6/gdb/gdbserver
#./configure --host=arm-linux --target=arm-linux --prefix=/opt/arm-gdb/gdbserver
#make
#make install
```

### 目標板上

```
#cd \usr\lib
#ln –s libthread_db-x.x.so libthread_db.so
#ln –s libthread_db-x.x.so libthread_db.so.1
#./gdbserver 192.168.0.2:2345 hello
```

其中192.168.0.2為目標板的IP。2345為gdbserver打開的端口

```
#./arm-linux-gdb hello
(gdb)target remote 192.168.0.2:2345
 ...
```

## 死鎖時的對應

`首先查看進程屬性`

```
$ ps ax -L | grep xxxx
7259  7259 pts/2    Sl+    0:00 -bash
7288  7288 pts/2    S      0:00 su
7289  7289 pts/2    S      0:00 bash
7374  7374 pts/2    R+     0:00 ps ax -L
```
```
R ⇒ 執行狀態
S ⇒ 睡眠狀態（可中斷，有死鎖的可能性）
D ⇒ 睡眠狀態（不可中斷）
T ⇒ 停止狀態
```

`檢測死鎖進程狀態`

```
$ gdb -p 'pidof xxxx'
...
(gdb) bt
```

`死鎖用測試腳本`

```
debug.cmd
#####################################

set pagination off
set logging file debug.log
set logging overwrite
set logging on
start
set $addr1 = pthread_mutex_lock
set $addr2 = pthread_mutex_unlock
b *$addr1
b *$addr2
while 1
    c
    if $pc != $addr1 && $pc != $addr2
        quit
    end
    bt
end

#####################################

# 使用
$ gdb xxxx -x debug.cmd
...

# 解析
$ cat debug.log | grep -A1 "^#0.*pthread_mutex_" | sed s/from\ .*$// | sed s/.*\ in\ //
```

## 測量程序的耗時

### 精密測量（時鐘週期）

#### Inter x86
在Intel x86CPU（也包括AMD的Athlon）內部，有一個按照CPU時鐘計算的64位的時間戳計數器（IA32_TIME_STAMP_COUNTER_MSR）。 通過RDTSC（Read Time Stamp Counter）命令，我們可以將這個值讀出來。通過它，我們可以高精度地測量某一程序的耗時。 因為這個計數器是64位的，所以基本上可以不必在意它有溢出的問題。
其實Windows的QueryPerformanceCounter內部函數就是利用了RDTSC指令。 通過RDTSC指令，計數器的值被保存到EAX（低階32bit）、EDX（高階32bit）。

在執行RDTSC指令之前，需要一條CPUID指令，該指令是為了確保測試之前的指令離開流水線，不要混入待測程序中。 但是，CPUID指令本身就比較耗時（幾百個時鐘週期） ，所以被測的程序需要減掉這一部分的損耗。 （Interl的RDTSC指令的介紹中，提到在前兩次調用CPUID的時候比較花時間，這之後就不會有很大的消耗了）

```c
#ifndef RDTSC_H_
#define RDTSC_H_

inline unsigned long long rdtsc() {
    unsigned long long ret;
    __asm__ volatile ("rdtsc" : "=A" (ret));
    return ret;
}

#endif /* RDTSC_H_ */


/* 使用例 */
#include "rdtsc.h"
#include <stdio.h>

int measure_func()
{
    unsigned long long start = rdtsc();
    to_be_measured();
    unsigned long long stop = rdtsc();
    printf("measured time : %I64d [clock]\n", stop - start);

    return 0;
}
```
## 一般測量（毫秒級）

```c
struct timespec ts;
long    basesec;
long    baseusec;
long    pastusec;

clock_gettime(CLOCK_MONOTONIC, &ts);
basesec  = ts.tv_sec;
baseusec = ts.tv_nsec/1000;

to_be_measured();

clock_gettime(CLOCK_MONOTONIC, &ts);
pastusec = (ts.tv_sec - basesec) * 1000000;
pastusec += (ts.tv_nsec/1000) - baseusec;

printf("Process Time :%d nano second.\n", pastusec);
```

## Core Dump

```
# 有效化core dump
$ ulimit -c unlimited

# 設置dump size
$ ulimit -c 1073741824

# 設置 dump 路徑（kernel.core_pattern）
$ cat /etc/sysctl.conf
kernel.core_pattern = /var/core/%t-%e-%p-%c.core
kernel.core_uses_pid = 0
$ sysctl -p

# 自動壓縮保存的 core dump
$ cat /etc/sysctl.conf
kernel.core_pattern = = |/usr/local/sbin/core_helper %t %e %p %c
kernel.core_uses_pid = 0
$ sysctl -p

$ cat /usr/local/sbin/core_helper
#!/bin/sh

exec gzip -> /var/core/$1-$2-$3-$4.core.gz

# 系統全體的 core dump 有效，編輯 /etc/profile
ulimit -S -c unlimited > /dev/null 2>&1
# /etc/sysconfig/init 中添加
DAEMON_COREFILE_LIMIT = `unlimited`
# /etc/sysctl.conf 中添加
fs.suid_dumpable = 1

# 用gdb解析core dump
$ gdb -c dump.core ./a.out


# 系統默認棧的大小
$ ulimit -s
# 更改系統默認棧大小
$ ulimit -Ss 123456
```

## 應用程序調試技巧

### SIGSEGV例外問題

#### 發生SIGSEGV的時候，基本是以下幾種情況：

- 訪問空指針
- 訪問非法指針地址
- 棧溢出，訪問非法地址

### Linux下實現程序異常時輸出backtrace

#### 方法1 : 註冊信號處理

```c
#include <stdlib.h>
#include <execinfo.h>
#include <signal.h>

void stacktrace(int signal) {
    void *trace[128];
    int n = backtrace(trace, sizeof(trace) / sizeof(trace[0]));
    backtrace_symbols_fd(trace, n, 1);
}

int foo() {
    return 1 /0;
}

void bar() {
    foo();
}

int main() {
    struct sigaction sa;
    memset(&sa, 0, sizeof(sa));
    sa.sa_handler = stacktrace;
    sa.sa_flags = SA_ONESHOT;
    sigaction(SIGFPE, &sa, NULL);
    bar();
    return 0;
}
```

```
% ./a.out
./a.out(stacktrace+0x1f)[0x8048743]
/lib/libc.so.6[0x400466f8]
./a.out(bar+0xb)[0x8048796]
./a.out(main+0x65)[0x80487fd]
/lib/libc.so.6(__libc_start_main+0xc6)[0x40032e36]
./a.out[0x8048681]
zsh: 7442 floating point exception (core dumped)  ./a.out

# 下面定位出錯代碼
% addr2line -e ./a.out 0x8048743
```

#### 方法2 : 使用/lib/libSegFault.so

設置程序的 LD_PRELOAD=/lib/libSegFault.so SEGFAULT_SIGNALS=all 。

```c
% export LD_PRELOAD=/lib/libSegFault.so
% export SEGFAULT_SIGNALS=all
% ./a.out

--- Floating point exception
Register dump:

 EAX: 00000001   EBX: 40150880   ECX: 00000001   EDX: 00000000
 ESI: 40016540   EDI: bfffe894   EBP: bfffe828   ESP: bfffe824

 EIP: 080485f9   EFLAGS: 00010286

 CS: 0023   DS: 002b   ES: 002b   FS: 0000   GS: 0000   SS: 002b

 Trap: 00000000   Error: 00000000   OldMask: 00000000
 ESP/signal: bfffe824   CR2: 00000000

Backtrace:
./a.out(foo+0x15)[0x80485f9]
./a.out(main+0x15)[0x8048619]
/lib/libc.so.6(__libc_start_main+0xc6)[0x40036e36]
./a.out[0x8048541]

Memory map:

08048000-08049000 r-xp 00000000 09:00 5538441    /home/satoru/tmp/a.out
08049000-0804a000 rw-p 00000000 09:00 5538441    /home/satoru/tmp/a.out
40000000-40016000 r-xp 00000000 08:01 700392     /lib/ld-2.3.2.so
40016000-40017000 rw-p 00015000 08:01 700392     /lib/ld-2.3.2.so
40017000-40018000 rw-p 00000000 00:00 0
40018000-4001b000 r-xp 00000000 08:01 700650     /lib/libSegFault.so
4001b000-4001c000 rw-p 00002000 08:01 700650     /lib/libSegFault.so
40021000-40149000 r-xp 00000000 08:01 700628     /lib/libc-2.3.2.so
40149000-40151000 rw-p 00127000 08:01 700628     /lib/libc-2.3.2.so
40151000-40154000 rw-p 00000000 00:00 0
bfffd000-c0000000 rwxp ffffe000 00:00 0
zsh: 11875 floating point exception (core dumped)  ./a.out
```
其實 libSegFault.so 使用了gcc的擴展屬性 __attribute__((constructor)) 在main函數執行之前設置了信號處理。

#### 方法3 : 使用catchsegv命令
catchsegv其實就是使用/lib/libSegFault.so的一個腳本。

```
$ catchsegv  ./a.out
--- Floating point exception
Register dump:

 EAX: 00000001   EBX: 40150880   ECX: 00000001   EDX: 00000000
 ESI: 40016540   EDI: bffff674   EBP: bffff608   ESP: bffff604

 EIP: 08048369   EFLAGS: 00010282

 CS: 0023   DS: 002b   ES: 002b   FS: 0000   GS: 0000   SS: 002b

 Trap: 00000000   Error: 00000000   OldMask: 80000000
 ESP/signal: bffff604   CR2: 00000000

Backtrace:
/home/name/undernomal/test1.c:2(foo)[0x8048369]
/home/name/undernomal/test1.c:7(main)[0x8048389]
/lib/libc.so.6(__libc_start_main+0xc6)[0x40036e36]
../sysdeps/i386/elf/start.S:105(_start)[0x80482b1]

Memory map:

08048000-08049000 r-xp 00000000 03:01 328342 /home/name/undernomal/a.out
08049000-0804a000 rw-p 00000000 03:01 328342 /home/name/undernomal/a.out
0804a000-0806b000 rwxp 00000000 00:00 0
40000000-40016000 r-xp 00000000 03:01 2859 /lib/ld-2.3.2.so
40016000-40017000 rw-p 00015000 03:01 2859 /lib/ld-2.3.2.so
40017000-40018000 rw-p 00000000 00:00 0
40018000-4001b000 r-xp 00000000 03:01 95875 /lib/libSegFault.so
4001b000-4001c000 rw-p 00002000 03:01 95875 /lib/libSegFault.so
40021000-40149000 r-xp 00000000 03:01 3581 /lib/libc-2.3.2.so
40149000-40151000 rw-p 00127000 03:01 3581 /lib/libc-2.3.2.so
40151000-40154000 rw-p 00000000 00:00 0
bfffe000-c0000000 rwxp fffff000 00:00 0
$ env | grep LD_ ; env | grep SEG
LD_PRELOAD=/lib/libSegFault.so
SEGFAULT_SIGNALS=all

$ ./a.out
--- Floating point exception
Register dump:000 r-xp 00000000 03:01 328346 /home/name/undernomal/a2.out
08049000-0804a000 rw-p 00000000 03:01 328346 /home/name/undernomal/a2.out
 EAX: 00000001   EBX: 40150880   ECX: 00000001   EDX: 00000000
 ESI: 40016540   EDI: bffff684   EBP: bffff618   ESP: bffff614
40016000-40017000 rw-p 00015000 03:01 2859 /lib/ld-2.3.2.so
 EIP: 08048369   EFLAGS: 000102860:00 0
40018000-4001b000 r-xp 00000000 03:01 95875 /lib/libSegFault.so
 CS: 0023   DS: 002b   ES: 002b   FS: 0000   GS: 0000   SS: 002b
40021000-40149000 r-xp 00000000 03:01 3581 /lib/libc-2.3.2.so
 Trap: 00000000   Error: 00000000   OldMask: 800000002.3.2.so
 ESP/signal: bffff614   CR2: 00000000 0
bfffe000-c0000000 rwxp fffff000 00:00 0
Backtrace:name:~/undernomal$
./a.out[0x8048369]
./a.out[0x8048389]
/lib/libc.so.6(__libc_start_main+0xc6)[0x40036e36]
./a.out[0x80482b1]

Memory map:

08048000-08049000 r-xp 00000000 03:01 328342     /home/name/undernomal/a.out
08049000-0804a000 rw-p 00000000 03:01 328342     /home/name/undernomal/a.out
0804a000-0806b000 rwxp 00000000 00:00 0
40000000-40016000 r-xp 00000000 03:01 2859       /lib/ld-2.3.2.so
40016000-40017000 rw-p 00015000 03:01 2859       /lib/ld-2.3.2.so
40017000-40018000 rw-p 00000000 00:00 0
40018000-4001b000 r-xp 00000000 03:01 95875      /lib/libSegFault.so
4001b000-4001c000 rw-p 00002000 03:01 95875      /lib/libSegFault.so
40021000-40149000 r-xp 00000000 03:01 3581       /lib/libc-2.3.2.so
40149000-40151000 rw-p 00127000 03:01 3581       /lib/libc-2.3.2.so
40151000-40154000 rw-p 00000000 00:00 0
bfffe000-c0000000 rwxp fffff000 00:00 0
浮動小數點演算例外です (core dumped)
$ addr2line -f -e ./a.out 0x8048369
foo
/home/user/undernomal/test1.c:2
$ addr2line -f -e ./a.out 0x8048389
main
/home/user/undernomal/test1.c:7
$ addr2line -f -e ./a.out 0x80482b1
_start
../sysdeps/i386/elf/start.S:105
```

### 檢測日誌文件的更新
```
tail -f -n 10 mylog.log
```

### 利用 ltrace 檢測共享庫函數的調用

ltrace可以用來檢測共享庫的函數調用，同樣可以利用strace來跟蹤系統調用。


```
% ltrace -o log.txt wget https://www.codeblog.org/

% grep SSL log.txt | head
SSL_library_init(0, 0, 0, 0, 0)                  = 1
SSL_load_error_strings(0, 0, 0, 0, 0)            = 0
OPENSSL_add_all_algorithms_noconf(0, 0, 0, 0, 0) = 1
SSL_library_init(0, 0, 0, 0, 0)                  = 1
SSLv23_client_method(0, 0, 0, 0, 0)              = 0x40038880
SSL_CTX_new(0x40038880, 0, 0, 0, 0)              = 0x808b228
SSL_CTX_set_verify(0x808b228, 0, 0x8068585, 0, 0) = 0x8068585
SSL_new(0x808b228, 0x7a060ed3, 1, 0, 0)          = 0x808cd20
SSL_set_fd(0x808cd20, 3, 1, 0, 0)                = 1
SSL_set_connect_state(0x808cd20, 3, 1, 0, 0)     = 0
SSL_connect(0x808cd20, 3, 1, 0, 0```


### strace

檢測系統調用時的問題

```
strace -i xxxx                      ; 顯示系統調用時的地址，可以在gdb中加斷點用
strace -p 'pidof xxxx'
strace -o output.log xxxx           ; 輸出到指定文件
strace xxxx 2>&1 | grep xxx
strace -f xxxx                      ; fock()的進程也執行trace
strace -t xxxx                      ; 表示系統調用時的時刻(秒單位)
strace -tt xxxx                     ; 表示系統調用時的時刻(毫秒單位)
```

### valgrind

檢測內存洩漏, 非法內存訪問，未初始化訪問，二重delete, 釋放後訪問等

```
valgrind --leak-check=yes xxxx
```
