helloworld.pyx
""""""""""""""
        print("Hello World")

setup.py
""""""""
        from setuptools import setup
        from Cython.Build import cythonize

        setup(
            ext_modules = cythonize("helloworld.pyx")
        )
cmd shell
"""""""""
    Which will leave a file in your local directory called:
        1.helloworld.so in unix
        2.helloworld.pyd in Windows
    
Now to use this file: start the python interpreter and simply import it as if it was a regular python module:
main.py
"""""""
        import helloworld
Hello World