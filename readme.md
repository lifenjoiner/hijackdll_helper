## Intro
This is another tool helping to generate c file for dll hijack, besides AheadLib and AddExport.

这是 AheadLib 和 AddExport 之外的，另一种生成 DLL 劫持 C 源代码的辅助工具。

It is fully based on the function forwarding feature of the MSVC linker.

它完全使用 MSVC linker 的 DLL 函数重定向特性。

It's coded in python for easier change of the c file template.

使用 python 是为了便于修改生成的代码。

There are 2 tricks on the c files: 1, implement some functions yourself; 2, sideload extra codes by the dll entry.

操作点可以有 2 处：1，自己实现要修改的函数；2，从 dll 入口（旁路）加载额外的代码。

homepage: https://github.com/lifenjoiner/hijackdll_helper

AheadLib: https://github.com/Yonsm/AheadLib, https://github.com/strivexjun/AheadLib-x86-x64

AddExport: https://bbs.pediy.com/thread-154269.htm

## Dependencies
python3

pefile
