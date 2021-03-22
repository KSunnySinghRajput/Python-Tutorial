from ctypes import *
print(windll.kernel32) 
"<WinDLL 'kernel32', handle 7ffa9fbd0000 at 0x1beff6bc128"
print(cdll.msvcrt)
"<CDLL 'msvcrt', handle 7ffa9efa0000 at 0x240c09bc1d0>"
libc = cdll.msvcrt
