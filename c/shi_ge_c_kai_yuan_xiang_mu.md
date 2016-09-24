# 十個C開源項目


代碼閱讀——十個C開源項目

## Webbench
Webbench是一個在linux下使用的非常簡單的網站壓測工具。它使用fork()模擬多個客戶端同時訪問我們設定的URL，測試網站在壓力下工作的性能，最多可以模擬3萬個並發連接去測試網站的負載能力。Webbench使用C語言編寫, 代碼實在太簡潔，源碼加起來不到600行。下載鏈接：Web Bench Homepage


## Tinyhttpd
tinyhttpd是一個超輕量型Http Server，使用C語言開發，全部代碼只有502行(包括註釋)，附帶一個簡單的Client，可以通過閱讀這段代碼理解一個 Http Server 的本質。下載鏈接：Tiny HTTPd | SourceForge.net


## CMockery
cmockery是google發佈的用於C單元測試的一個輕量級的框架。它很小巧，對其他開源包沒有依賴，對被測試代碼侵入性小。cmockery的源代碼行數不到3K，你閱讀一下will_return和mock的源代碼就一目瞭然了。

主要特點：

免費且開源，google提供技術支持；

輕量級的框架，使測試更加快速簡單；

避免使用複雜的編譯器特性，對老版本的編譯器來講，兼容性好;

並不強制要求待測代碼必須依賴C99標準，這一特性對許多嵌入式系統的開發很有用

下載鏈接：Downloads - cmockery - A lightweight library to simplify and generalize the process of writing unit tests for C applications.


## cJSON
cJSON是C語言中的一個JSON編解碼器，非常輕量級，C文件只有500多行，速度也非常理想。

cJSON也存在幾個弱點，雖然功能不是非常強大，但cJSON的小身板和速度是最值得讚賞的。其代碼被非常好地維護著，結構也簡單易懂，可以作為一個非常好的C語言項目進行學習。項目主頁:cJSON | SourceForge.net


## Libev
libev是一個開源的事件驅動庫，基於epoll，kqueue等OS提供的基礎設施。其以高效出名，它可以將IO事件，定時器，和信號統一起來，統一放在事件處理這一套框架下處理。基於Reactor模式，效率較高，並且代碼精簡（4.15版本8000多行），是學習事件驅動編程的很好的資源。下載鏈接：http://software.schmorp.de/pkg/libev.html

## Memcached
Memcached 是一個高性能的分佈式內存對象緩存系統，用於動態Web應用以減輕數據庫負載。它通過在內存中緩存數據和對象來減少讀取數據庫的次數，從而提供動態數據庫驅動網站的速度。Memcached 基於一個存儲鍵/值對的 hashmap。Memcached-1.4.7的代碼量還是可以接受的，只有10K行左右。下載地址：memcached - a distributed memory object caching system

## Lua
Lua很棒，Lua是巴西人發明的，這些都令我不爽，但是還不至於臉紅，最多眼紅。

讓我臉紅的是Lua的源代碼，百分之一百的ANSI C，一點都不摻雜。在任何支持ANSI C編譯器的平台上都可以輕鬆編譯通過。我試過，真是一點廢話都沒有。Lua的代碼數量足夠小，5.1.4僅僅1.5W行，去掉空白行和註釋估計能到1W行。下載地址：The Programming Language Lua

## SQLite
SQLite是一個開源的嵌入式關係數據庫，實現自包容、零配置、支持事務的SQL數據庫引擎。 其特點是高度便攜、使用方便、結構緊湊、高效、可靠。足夠小，大致3萬行C代碼，250K。 下載地址：SQLite Home Page 。

## Redis
Redis是一個用ANSI C 編寫的開源數據結構服務器。Redis的代碼非常容易讀懂，代碼寫的很整潔，並且代碼量相對較小（4.5w行，其實也不是很小）。大部分都是單線程的，幾乎不依賴其它庫。下載地址：redis.io/

## Nginx
Nginx("engine x") 是一個高性能的 HTTP 和反向代理服務器，也是一個 IMAP/POP3/SMTP 代理服務器 。Nginx 是由 Igor Sysoev 為俄羅斯訪問量第二的http://Rambler.ru站點開發的，它已經在該站點運行超過四年多了。Igor 將源代碼以類BSD許可證的形式發佈。自Nginx 發佈四年來，Nginx 已經因為它的穩定性、豐富的功能集、 示例配置文件和低系統資源的消耗而聞名了。

nginx的優秀除了體現在程序結構以及代碼風格上，nginx的源碼組織也同樣簡潔明了，目錄結構層次結構清晰，值得我們去學習。下載地址：nginx: download。

## UNIXv6
UNIX V6 的內核源代碼包括設備驅動程序在內 約有1 萬行，這個數量的源代碼，初學者是能夠充分理解的。有一種說法是一個人所能理解的代碼量上限為1 萬行，UNIX V6的內核源代碼從數量上看正好在這個範圍之內。看到這裡，大家是不是也有「如果只有1萬行的話沒準兒我也能學會」的想法呢？

另一方面，最近的操作系統，例如Linux 最新版的內核源代碼據說超過了1000 萬行。就算不是初學者，想完全理解全部代碼基本上也是不可能的。下載地址：http://minnie.tuhs.org/cgi-bin/utree.pl?file=V6

## NETBSD
NetBSD是一個免費的，具有高度移植性的 UNIX-like 操作系統，是現行可移植平台最多的操作系統，可以在許多平台上執行，從 64bit alpha 服務器到手持設備和嵌入式設備。NetBSD計畫的口號是："Of course it runs NetBSD"。它設計簡潔，代碼規範，擁有眾多先進特性，使得它在業界和學術界廣受好評。由於簡潔的設計和先進的特徵，使得它在生產和研究方面，都有卓越的表現，而且它也有受使用者支持的完整的源代碼。許多程序都可以很容易地通過NetBSD Packages Collection獲得。下載地址：The NetBSD Project