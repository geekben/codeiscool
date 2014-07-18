#include<stdio.h>
#include<pthread.h>

int main()
{
    pthread_t td1, td2;
    void *thread1(void * arg);
    void *thread2(void * arg);

    pthread_create(&td1,NULL,thread1,NULL);
    pthread_create(&td2,NULL,thread2,NULL);

    pthread_join(td1,NULL);
    pthread_join(td2,NULL);
    printf("Exit main() %u!\n", (unsigned int)getpid());
}

void * thread1(void * arg)
{
    printf("Thread1 created, thread ID is %u, PID is %u, PPID is %u\n", 
            (unsigned int)pthread_self(), (unsigned int)getpid(), (unsigned int)getppid());
    pthread_exit(0);
}

void * thread2(void * arg)
{
    printf("Thread2 created, thread ID is %u, PID is %u, PPID is %u\n", 
            (unsigned int)pthread_self(), (unsigned int)getpid(), (unsigned int)getppid());
    pthread_exit(0);
}
