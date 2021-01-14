import time

# initial = time.time()       #time() is a function under time module it retures tic(meanse second)
# # print(initial)
# t = 0
# while(t<20):
#     print("This is example of time")
#     time.sleep(.5)
#     t=t+1
# print("The execution time of while loop is", time.time() - initial, "seconds")
#
# initial2 = time.time()
# for i in range (20):
#     print("This is example of time")
#     time.sleep(.5)
# print("The execution time of for loop is", time.time() - initial2, "seconds")

#------------------------------------------------------------------------

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

#time.time() - returns tic. It calculate time from an old time
#time.localtime - returns local time
#time.asctime - returns time in presentable format
