import time
import threading

def calc_sqrt(numbers):
    print("Calculate Square of Numbers:")
    for i in numbers:
        time.sleep(0.2)
        print("Square of %d: %d"%(i,i*i))

def calc_cube(numbers):
    print("Calculate Cube of Numbers:")
    for i in numbers:
        time.sleep(0.2)
        print("Cube of %d: %d"%(i,i*i*i))

arr=[2,3,8,9]

t=time.time()

t1=threading.Thread(target=calc_sqrt,args=(arr,))
t2=threading.Thread(target=calc_cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Total time taken:",time.time()-t)