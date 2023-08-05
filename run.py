from ctypes import *
import os

if os.system("bash build.sh") != 0:
    print("build error")
    exit(1)

lib = cdll.LoadLibrary("lib.so")
lib.func.argtypes = [
    c_int
]
lib.func.restype = c_int

print(lib.func(5))