from ctypes import*


#Loading dynamic link libraries
#""""""""""""""""""""""""""""""
print(windll.kernel32)
#<WinDLL 'kernel32', handle 7ffd4ad50000 at 0x18523610d68>
print(cdll.msvcrt)
#<CDLL 'msvcrt', handle 7ffd4b5c0000 at 0x18523610dd8>



libc=cdll.msvcrt
print(libc)
#<CDLL 'msvcrt', handle 7ffd4b5c0000 at 0x18523610dd8>
print(libc.printf)
#<_FuncPtr object at 0x00000185235D45F8>
>>> print(windll.kernel32.GetModuleHandleA)
<_FuncPtr object at 0x00000185235D46C8>