import py_compile
compileall.compile_dir('.')
py_compile.compile("hello1.py")
py_compile.compile(["hello1.py","hello2.py"])
