#include <stdlib.h>
#include <stdio.h>

int __cdecl    _e (int x);
int __cdecl    f (int x);
int __stdcall  g (int x);
int __fastcall h (int x);

int main(int argc, char **argv)
{
    printf("%d\n", _e(1));
    printf("%d\n", f(2));
    printf("%d\n", g(3));
    printf("%d\n", h(4));
    return 0;
}
