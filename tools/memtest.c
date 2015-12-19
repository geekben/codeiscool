#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#define LEN 1024*1024*1024
int main()
{
        char *src = (char*)malloc(LEN);
        char *dest = (char*)malloc(LEN);
        int i = 0;
        struct timeval begin;
        struct timeval end;
        for (; i<LEN/4096; i++)
        {
                dest[i*4096] = 1;
                src[i*4096] = 1;
        }
        gettimeofday(&begin, NULL);
        for (i=0; i<10; i++)
        {
                memcpy((void*)dest, (void*)src, LEN);
        }
        gettimeofday(&end, NULL);
        int used = (end.tv_sec-begin.tv_sec)*1000000 + end.tv_usec - begin.tv_usec;
        printf("time used %d us\n", used);
        return 0;
}

