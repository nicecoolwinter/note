# hw3


```
Assume that a system has a 32-bit virtual address with a 4-KB page size. Write a 
C program that is passed a virtual address (in decimal) on the command line and 
have it output the page number and offset for the given address. 
```


```
As an example, your program would run as follows:

./a.out 19986

Your program would output:

The address 19986 contains:
page number=4
offset=3602
```

- page_number.c

```c
#include <stdio.h>
#include <stdlib.h>

#define PAGE_SIZE 4096

int main(int argc, char **argv) {

    unsigned int address;
    unsigned int page_number;
    unsigned int offset;

    if(argc<2) {
        printf("Enter the address: ");
        return -1;
    }

    address = atoi(argv[1]);
    page_number = address / PAGE_SIZE;
    offset = address % PAGE_SIZE;

    printf("The address=%u\nPage number = %u\noffset = %u\n", address, page_number, offset);

    return 0;
}
```

```c
./page_number 19986
```

