from ctypes import*
libc=CDLL("TestDll.dll")
print(libc.message)