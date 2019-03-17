#include <stdlib.h>

__declspec(dllexport) int __cdecl    _e (int x) { return x; }
__declspec(dllexport) int __cdecl    f (int x) { return x; }
__declspec(dllexport) int __stdcall  g (int x) { return x; }
__declspec(dllexport) int __fastcall h (int x) { return x; }
