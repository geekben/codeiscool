#include <stdio.h>

int main()
{
    int a = 0x01020304;
    char b = (char)a;
    printf("==%d==\n", b);

    if (b == (char)0x4)
        printf("Little Endian\n");
    else
        printf("Big Endian\n");
    return 0;
}
