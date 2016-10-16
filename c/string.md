# String


- strlen

```c
#include <stdio.h>

int my_strlen(char* src, int elements)
{
    int len = 0;

    while (*src++ != '\0') {
        if (len >= elements) {
            printf("Warning! bigger than max array size.\n");
            break;
        }

        len++;
    }

    return len;
}

int main(int argc, char* argv[])
{
    char str[10];

    scanf("%s", str);
    printf("len=%d\n", my_strlen(str, sizeof(str) / sizeof(str[0])));

    return 0;
}
```


- strcpy
- strcat
- atof
- atoi
- tolower
- isdigit
- isalpha
- strtok
