#Threading - Python threads are used in cases where the execution of a task involves some waiting. Threading allows python to execute other code while waiting; this is easily simulated with the sleep function.

# import time

# def square(numbers):
#     print("calculate square of the numbers")
#     for n in numbers:
#         time.sleep(.5)
#         print("Square is", n*n)

# def cube(numbers):
#     print("calculate qube of the numbers")
#     for n in numbers:
#         time.sleep(.5)
#         print("Qube is", n*n*n)

# list = [2,3,4,5]
# t = time.time()
# square(list)
# cube(list)
# print("The execution time is", time.time()-t)

#-------------------------------------------------


# import time
# import threading

# def square(numbers):
#     print("calculate square of the numbers")
#     for n in numbers:
#         time.sleep(.5)
#         print("Square is", n*n)

# def cube(numbers):
#     print("calculate qube of the numbers")
#     for n in numbers:
#         time.sleep(.5)
#         print("Qube is", n*n*n)

# list = [2,3,4,5]
# t = time.time()
# t1 = threading.Thread(target=square, args=(list,))
# t2 = threading.Thread(target=cube, args=(list,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("The execution time is", time.time()-t)