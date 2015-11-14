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


http://web2.clarkson.edu/class/cs444/labs/lab08/paging.html


- PagingReplacement.c

```c
/********************************************
  CS444 Operating System
  Lab08:
 
  Implementing FIFO and LRU page replacement algorithm

  Clarkson University 
  Name:
  ID:


 Date: Spring 2011
 *******************************************/

#include <stdio.h>
#include <stdlib.h>


/**************************************
 * The parameters of memory and disk pages 
 *
 * PageFrameList: The dynamically-allocated array representing memory pages
 * FrameNR: the number of page frames in memory
 * elementCout: Point to the next page to be replaced
 *
 * ReferenceString: The sequence of the demanding pages
 * ReferenceLength: The length of the randomized reference string
 * ReferenceSZ: the page number range in the reference string
 *
 */

#define ReferenceLength 100

typedef struct
{
    int *PageFrameList;
    int elementCount;	
}PageFrame;

int ReferenceSZ, FrameNR;

PageFrame memory;

int *ReferenceString;
 

/* Test driver sub functions */

void generateReferenceString();

void initializePageFrame();

void printReferenceString();

void printPageFrame();


/* Algorithm Functions */

int FIFO();

int LRU();

/* The possible algorithm subfunctions

int FIFOSearch(int PageNumber);

int FIFOInsert(int PageNumber);

int LRUSearch(int PageNumber);

int LRUInsert(int PageNumber);

void LRUupdatePageTable(int Findindex);

*/



/*******************************
 *
 * The main function is the test driver for FIFO & LRU algorithms
 *
 * 1. Initialize the system parameters
 * 2. Initialize the memory pages 
 * 3. Generate the randomized reference string
 * 4. Apply the FIFO algorithm, calculate the number of page faults
 * 5. Apply the LRU algorithm, calculate the number of page faults
 */


int main(int argc, char* argv[])
{


 
    if( argc != 3 )
    {
        printf("Command format: Test <reference string size> <number of page frames>");
    }


    ReferenceSZ = atoi(argv[1]);
    FrameNR = atoi(argv[2]);


   generateReferenceString();


   initializePageFrame();
   printf("page fault of FIFO: %d\n",FIFO());
   free(memory.PageFrameList);

   printf("\n");
   printf("\n");


   printReferenceString();

   initializePageFrame();
   printf("page fault of LRU: %d\n",LRU());
   free(memory.PageFrameList);


   free(ReferenceString);	

   return 0;

}


/**********************************
 **********************************
 *
 * The test driver functions implmentation details
 *
 **********************************
 */

void generateReferenceString()
{
   int i;
   srand(time(0));
   ReferenceString = (int *)malloc( sizeof(int) * ReferenceLength );
   printf("The randomized Reference String: ");
   for(i=0; i< ReferenceLength; i++)
   {
	ReferenceString[i] = rand() % ReferenceSZ;
        printf("%d ", ReferenceString[i]);       
   }
   printf("\n");
}


void initializePageFrame()
{
   int i;
   memory.PageFrameList = (int *)malloc( sizeof(int)* FrameNR );
   memory.elementCount =0;    
   for(i=0; i< FrameNR; i++)
   {
	memory.PageFrameList[i] = -1;       
   }

}

void printPageFrame()
{
   int i;
   for(i=0; i< FrameNR; i++)
   {
	printf("%2d ",memory.PageFrameList[i]);       
   }
   printf("\n");
}

void printReferenceString()
{
   int i;
   printf("The Same Reference String: ");
   for(i=0; i< ReferenceLength; i++)
   {
        printf("%d ", ReferenceString[i]);       
   }
   printf("\n");

}


/**********************************
 **********************************
 *
 * The skeleton code for FIFO & LRU algs
 * 
 * NOTE: you are not required to follow the skeleton code here 
 *       you can also write on your own, even different data structure
 *       BUT make sure your algorithm is correct!!!!!!
 *       It is strongly recommended to print out the PageFrames
 *       so that you can follow how the algorithm works and double check it.
 *
 **********************************
 */


int FIFO()
{
    int PagefaultCount=0;
    int i;

   for( i=0; i<ReferenceLength; i++ ) 
   {
       PagefaultCount+=FIFOInsert(ReferenceString[i]);
       printPageFrame();
   }


   return PagefaultCount;
}


/*  Some hints you can follow
int FIFOSearch(int PageNumber)
{



}

int FIFOInsert(int PageNumber)
{
    int Pagefault=0;
    if( 0==FIFOSearch(PageNumber) )
    {

      //Replace the page HERE

    }

    return Pagefault;      
}

*/


int LRU()
{
    int PagefaultCount=0;
    int i;

   for( i=0; i<ReferenceLength; i++ ) 
   {
       PagefaultCount+=LRUInsert(ReferenceString[i]);
       printPageFrame();
   }


   return PagefaultCount;

}

/*  Some hints you can follow
int LRUSearch(int PageNumber)
{


}

int LRUInsert(int PageNumber)
{
    int PageFault=0;

    int Findindex = -1;
    Findindex = LRUSearch(PageNumber);

    if ( -1 == Findindex ) 
    { 
        
      //Replace the page HERE

    }
    else
    {
       LRUupdatePageTable(Findindex);
    }
    return PageFault;

}

void LRUupdatePageTable(int Findindex)
{



}
*/
```
