#Building and using DLLs in C
"""""""""""""""""""""""""""""
    At some point you might find that while higher level languages like C# are awesome and get
    the job done faster than regular C, the overhead of using C# libraries might cause issues
    when computing heavy loads. For example, if you wanted to write a bruteforcer or crypto 
    algorithm, you want the speed of C.

    1.Creating the DLL
    """"""""""""""""""
    In this tutorial i'll create a file named test_dll.c and test_dll.h.

        test_dll.c
                #include <stdio.h>
                #include "test_dll.h"

                EXPORT void message(){
                    printf("Hello World");
                }
    The code is pretty straight foward. I created a simple function that prints 'Hello World'. 
    The main thing to note is the use of this keyword EXPORT. It's a keyword I defined in test_dll.h

        test_dll.h
            #define EXPORT __declspec(dllexport)
            EXPORT void message (void);

    The EXPORT keyword is defined as __declspec(dllexport) which is a DLL export directive. 
    Using this directive basically tells the linker to expose the function for import to other DLLs or programs.

    This can be compiled like so:

            gcc -c test_dll.c
            gcc -shared -o TestDll.dll -Wl,--out-implib,libtstdll.a test_dll.o

    I'm compiling it such that the result is TestDll.dll.

    2.Creating the program
    """"""""""""""""""""""
    For this part, I just created a file main.c.
        main.c

            #include "test_dll.h"

            int main(){
                message();
                return 0;
            }

    I included the dll using the same name as its header file and then was able to simply call the function
    defined in it.

    It can be compiled like so:
        gcc -o testProg main.c -L. -lTestDll

    I just named my program 'testProg' because lack of creativity. The -L. part tells the linker to look in 
    the current directory for libs. The -lTestDll tells it to look for a lib named 'TestDll', which is our DLL.

    Conclusion
        Thats basically DLLs in a nutshell. They are very useful for making small libraries and APIs that you can use with C/C++ or C#.