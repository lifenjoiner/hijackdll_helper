#!/usr/bin/python3
#coding=utf-8

import os
import sys
import pefile
import traceback

source_code_template = '''\
// Created by hijackdll-helper
/* There should be dll hijacking possible first! */
/* cl.exe /Os /GD /LD /Fe */
/* https://en.wikipedia.org/wiki/Name_mangling */

#include <windows.h>

/*  Don't forward to itself!
    "C:\\Windows\\System32\\version" is acceptable ;p
*/
#define HIJACKED_DLL_NAME "_DLL_NAME__"    //<--- modify

/* gcc does't support this. */
TEMPLATE_DLL_EXPORT

// Add your implementations here, and comment the forwarders <---

//extern int sideload();    //<---

/*  Less dependencies: _DllMainCRTStartup
    More functions: DllMain
    Take care of the core libs yourself: msvcrt, kernel32, ntdll, user32 */
BOOL WINAPI _DllMainCRTStartup(HMODULE hModule, DWORD dwReason, PVOID pvReserved)
{
	switch (dwReason) {
	case DLL_PROCESS_ATTACH:
		//sideload();    //<---
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
'''

'''
    cl.exe warning: export of "deleting destructor" may not run correctly
    msvcrt.dll: _adjust_fdiv
    是否是中转函数  如:KERNEL32.VerLanguageNameA
'''
def generate(outfile, new_dllname, symbols):
    export_text = ''
    for sym in symbols:
        export_text += '#pragma comment(linker, "/EXPORT:'
        if sym.name:
            """https://docs.microsoft.com/en-us/windows/desktop/Debug/pe-format#export-name-table"""
            name = sym.name.decode(encoding='ascii')
            """cl.exe, c: https://en.wikipedia.org/wiki/Name_mangling"""
            if name[0] == '_' and '@' not in name:
                export_text += '_'
            export_text += '%s="HIJACKED_DLL_NAME".%s,@%d")\n' % (name, name, sym.ordinal)
        else:
            export_text += 'fun_%d="HIJACKED_DLL_NAME".#%d,@%d,NONAME")\n' % (sym.ordinal, sym.ordinal, sym.ordinal)
    
    out = open(outfile, "w+")
    out.writelines(source_code_template
        .replace('_DLL_NAME_', new_dllname)
        .replace('TEMPLATE_DLL_EXPORT', export_text))
    
    out.close()

def usage():
    print('Usage: '+ sys.argv[0] +'[dll files]')
    sys.exit(0)

def run(filename):
    try:
        pe = pefile.PE(filename)
        symbols = pe.DIRECTORY_ENTRY_EXPORT.symbols
        (filename_base, fileext) = os.path.splitext(os.path.basename(filename))
        filename_out = filename_base + '~.c'

        print('[-] Processing '+ filename)
        print('    Output: '+ filename_out)
        print('    Symbols: %d' % len(symbols))

        generate(filename_out, filename_base, symbols)

    except Exception as e:
        traceback.print_exc()
        pass

def main():
    if len(sys.argv) == 1:
        usage()
    else:
        for arg in sys.argv[1:]:
            run(arg)


if __name__ == '__main__':
    main()
