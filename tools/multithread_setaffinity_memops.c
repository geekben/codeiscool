#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <sys/mman.h>
#ifndef __USE_GNU
#define __USE_GNU
#endif
#define _GNU_SOURCE
#include <pthread.h>
#include <sched.h>
 
#define NUM_THREADS 30
#define LEN 8192
#define COUNT 100000
#define PAGE 4096

 
/* create thread argument struct for thr_func() */
typedef struct _thread_data_t {
    int tid;
    double stuff;
} thread_data_t;

/* shared data between threads */
char temp;
pthread_mutex_t lock_x;
char buf[NUM_THREADS*PAGE];
 
/* thread function */
void *thr_func_1(void *arg) {
    thread_data_t *data = (thread_data_t *)arg;
    char *buf = NULL;
    int i = 0;
 
    printf("hello from thr_func, thread id: %d\n", data->tid);
    
    for(; i<COUNT; i++)
    {
        buf = (char*)malloc(LEN);
        *buf = i;
        *buf = *buf * *buf;
        pthread_mutex_lock(&lock_x);
        temp = *buf;
        *buf = ++temp;
        pthread_mutex_unlock(&lock_x);
        mprotect(buf, 4096, PROT_READ);

        free(buf);
    }
    pthread_mutex_lock(&lock_x);
    temp = data->tid;
    pthread_mutex_unlock(&lock_x);
 
    pthread_exit(NULL);
}

void *thr_func(void *arg) {
    thread_data_t *data = (thread_data_t *)arg;
    int i = 0, count = 0;
 
    printf("hello from thr_func, thread id: %d\n", data->tid);

    for (;i<COUNT;i++){
        pthread_mutex_lock(&lock_x);
        memset(buf,(char)data->tid,sizeof(buf));
        pthread_mutex_unlock(&lock_x);

        //sleep(1);
        count++;

        pthread_mutex_lock(&lock_x);
        mprotect(&buf[data->tid*4096], 4096, PROT_READ);
        pthread_mutex_unlock(&lock_x);
    }
    printf("Goodbye from thr_func, thread id: %d, count %d\n",
			data->tid, count);

    pthread_exit(NULL);
}
 
int main(int argc, char **argv) {
    struct timeval begin;
    struct timeval end;
    pthread_t thr[NUM_THREADS];
    int i, rc, j;
	cpu_set_t cpuset;
    /* create a thread_data_t argument array */
    thread_data_t thr_data[NUM_THREADS];

    memset(buf, 0, sizeof(buf));
    pthread_mutex_init(&lock_x, NULL);
 
    gettimeofday(&begin, NULL);
    /* create threads */
    for (i = 0; i < NUM_THREADS; ++i) {
        thr_data[i].tid = i;
        if ((rc = pthread_create(&thr[i], NULL, thr_func, &thr_data[i]))) {
            fprintf(stderr, "error: pthread_create, rc: %d\n", rc);
            return EXIT_FAILURE;
        }
		CPU_ZERO(&cpuset);
		CPU_SET(i%16, &cpuset);
		rc = pthread_setaffinity_np(thr[i], sizeof(cpu_set_t), &cpuset);
        if (rc != 0)
            printf("pthread_setaffinity_np error");
        rc = pthread_getaffinity_np(thr[i], sizeof(cpu_set_t), &cpuset);
	    if (rc != 0)
		    printf("pthread_getaffinity_np error");

	    printf("Set returned by pthread_getaffinity_np() contained:\n");
		for (j = 0; j < 16; j++)
            if (CPU_ISSET(j, &cpuset))
                printf("    CPU %d\n", j);
    }
    /* block until all threads complete */
    for (i = 0; i < NUM_THREADS; ++i) {
        pthread_join(thr[i], NULL);
    }
    gettimeofday(&end, NULL);
    int used = (end.tv_sec-begin.tv_sec)*1000000 + end.tv_usec - begin.tv_usec;
    printf("time used %d us\n", used);
    printf("TEMP = %d", (int)temp);
 
    return EXIT_SUCCESS;
}
