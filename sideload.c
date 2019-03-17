
#include <windows.h>

__declspec(dllexport) void sideload (void)
{
    MessageBox (0, "test", "From DLL", MB_ICONINFORMATION);
}
