# hw1

## fork + collatz

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

static void collatz(int n) {
    printf("%d ,", n);

    if (n == 1) return;
    else if (n % 2 == 0) collatz(n / 2);
    else collatz(3*n + 1);
}

int main()
{
    pid_t pid;
    int a = 100;

    pid = fork();

    if(pid<0) /*error occurred*/
    {
        fprintf(stderr, "Fork Failed");
        exit(-1);
    }
    else if(pid==0) /*child process*/
    {
        printf("child pid=%d\n", getpid());
        printf("a address%p a=%d\n", (void*)&a, a);
        printf("Child[+++]\n");
        collatz(8);
        printf("\nChild[---]\n");

    }
    else /*parent process*/
    {
        printf("parent pid=%d\n", getpid());
        a = 300;
        printf("a address%p a=%d\n", (void*)&a, a);
        printf("Parent[+++]\n");
        wait(NULL);
        printf("Child Complete\n");
        printf("Parent[---]\n");
        getchar();
        exit(0);
    }

    return 0;
}
```


## pipe + fork + read/write

```c
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>

#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define BUFFER_SIZE 80
#define READ_END 0
#define WRITE_END 1

int main(int argc, char *argv[]) {
    /* argc must be 3 to ensure the correct usage */
    if (argc != 3) {
        printf("The usage of this program is:\n");
        printf("FileCopy input.txt copy.txt\n");
        return 1;
    }
    else {
        int pid;
        /* initialize the pipe and fork variables */
        int fd[2];/* argv[0] is the program name, argv[1] and argv[2] are the file names */
        char *infile = argv[1];
        char *outfile = argv[2];
        /* create a pipe */
        if (pipe(fd) == -1) {
            fprintf(stderr, "Pipe failed");
            return 1;
        }

        printf("fd[0]=%d\n", fd[0]);
        printf("fd[1]=%d\n", fd[1]);

        /* fork */
        pid = fork();
        /* if pid < 0 there is an error */
        if (pid < 0) {
            fprintf(stderr, "Fork error");
            return 1;
        }
        /* parent code */
        if (pid > 0) {
            int  in;
            int  len;
            char buffer[BUFFER_SIZE];
            /* close the unused end of the pipe */
            close(fd[READ_END]);
            /* make a buffer to store input file information */
            /* open input file */
            in = open(infile, O_RDONLY);
            /* make sure it's not null */
            if (in == -1) {
                fprintf(stderr, "Error opening file %s\n", infile);
                return 1;
            }
            /* read from the file into the pipe thru the buffer */
            while ( 1 ) {
                memset( buffer, 0, sizeof(buffer));
                len = read(in, buffer, BUFFER_SIZE);
                printf("parent len=%d\n",len);
                if( len <= 0 ) break;
                write(fd[WRITE_END], buffer, len );
            }
            /* close the input file */
            close(in);
            close(fd[WRITE_END]);
            wait(NULL);
        }
        /* child process has pid == 0 */
        else {
            int out;
            int len;
            /* create a buffer to read from the pipe and store into the out file */
            char buffer[BUFFER_SIZE];
            /* close the unused end of the pipe */
            close(fd[WRITE_END]);
            /* initialize the output file */
            /* w+ means open a file for writing and create it if it doesn't exist */
            out = open(outfile, O_WRONLY | O_TRUNC | O_CREAT);
            while(1) {
                memset(buffer, 0, sizeof(buffer));
                len = read(fd[READ_END], buffer, BUFFER_SIZE) ;
                printf("child len=%d\n", len);
                if (len <= 0 ) break;
                write(out,buffer, len );
                printf("buf1:%s\n",buffer);
            }
            /* close the file and the pipe */
            close(out);
            close(fd[READ_END]);
        }
    }
    return 0;
}
```
