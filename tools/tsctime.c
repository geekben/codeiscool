#include <stdio.h>
#include <sys/time.h>
#include <inttypes.h>

/*
* Read the 64-bit TSC (time stamp counter).
*/
static uint64_t rdtsc(void)
{
    unsigned long msw;
    unsigned long lsw;

    __asm__ __volatile__("rdtsc" : "=a" (lsw), "=d" (msw) :);
    return (((uint64_t) msw << 32) | lsw);
}

int
main(int argc, char *argv[])
{
    uint64_t start;
    uint64_t end;
    struct timeval tv_start;
    struct timeval tv_end;
    double sec;

    gettimeofday(&tv_start, NULL);
    start = rdtsc();
    while (1) {
        gettimeofday(&tv_end, NULL);
        if (tv_end.tv_sec > tv_start.tv_sec + 10)
            break;
    }
    end = rdtsc();
    printf("Total TSC ticks = %"PRIu64"\n", end - start);
    sec = (tv_end.tv_sec - tv_start.tv_sec) +
    (double) (tv_end.tv_usec - tv_start.tv_usec) / 1000000;
    printf("Time = %.3lf sec\n", sec);
    printf("TSC ticks per sec = %.0lf\n", (double) (end - start) / sec);
}
