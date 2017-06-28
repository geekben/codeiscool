#include <stdio.h>
#include <sys/time.h>
#include <inttypes.h>
#include <unistd.h>

int
main(int argc, char *argv[])
{
    struct timeval tv_start;
    struct timeval tv_end;
    double sec;
	int c = 0;

    gettimeofday(&tv_start, NULL);
    while (1) {
		usleep(1000);
		c++;
        gettimeofday(&tv_end, NULL);
        if (tv_end.tv_sec > tv_start.tv_sec + 1) {
			printf("--%d--1000\n", c);
			c = 0;
    		gettimeofday(&tv_start, NULL);
		}
    }
}
