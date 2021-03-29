from ctypes import *
import sys


try: 
    k32    = cdll.LoadLibrary('Graphics.dll')
    msvcrt = cdll.LoadLibrary(mFile)
except OSError as e:
    print("ERROR: %s" % e)
    sys.exit(1)

# do something...






#lib = ctypes.WinDLL('full/path/to/mylibrary.dll')
#func = lib['myFunc']#my func is double myFunc(double);
#func.restype = ctypes.c_double
#value = func(ctypes.c_double(42.0))
