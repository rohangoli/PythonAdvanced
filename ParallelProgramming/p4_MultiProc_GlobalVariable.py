import time
import multiprocessing

result=[]

def calc_sqrt(numbers):
    global result
    print("Calculate Square of Numbers:")
    for i in numbers:
        time.sleep(0.2)
        print("Square of %d: %d"%(i,i*i))
        result.append(i*i)
    print("Inner Process"),result

def calc_cube(numbers):
    print("Calculate Cube of Numbers:")
    for i in numbers:
        time.sleep(0.2)
        print("Cube of %d: %d"%(i,i*i*i))

if __name__ == '__main__':
    arr=[2,3,8,9]

    t=time.time()

    p1=multiprocessing.Process(target=calc_sqrt,args=(arr,))

    p1.start()

    p1.join()

    print("Outside Process:",result)
    print("Total time taken:",time.time()-t)