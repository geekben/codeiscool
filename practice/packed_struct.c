#include <stdio.h>
#include <sys/mman.h>

#pragma pack(push, 1)
struct pack {
    char val;
    struct pack * next;
}__attribute__ ((__packed__));

struct unpack {
    int val;
    struct pack * next;
};
#pragma pack(pop)

int main() {

    printf("size of pack is %lu and upack is %lu\n",sizeof(struct pack),sizeof(struct unpack));
    printf("size of int is %lu\n",sizeof(int));
    printf("size of char is %lu\n",sizeof(char));

    int i = 0;

    struct pack pks[5];
    struct unpack upks[5];

    for(i = 0; i < 5; i++)
        printf("address of pks[%d] is %p\n",i, &pks[i]);
    for(i = 0; i < 5; i++)
        printf("address of upks[%d] is %p\n",i, &upks[i]);

    void * ptr = mmap(NULL, sizeof(struct unpack), PROT_READ|PROT_WRITE, MAP_ANONYMOUS|MAP_SHARED, -1, 0);
    if (ptr == MAP_FAILED) {
        perror("mmap");
    } else {
        struct unpack *upk;
        printf("Address of prt pointed: %p\n", ptr);
        upk = (struct unpack *)(ptr+1);
        upk->val = 0x123456;
        upk->next = &pks[1];
        printf("upk.val is: 0x%x\n", upk->val);
        printf("Address of upk.val is: %p\n", &(upk->val));
    }

    return 0;
}
