#   Using Shared Memory Array & Value

import time
import multiprocessing

def calc_sqrt(numbers,result,v):
    v.value=5.67
    print("Calculate Square of Numbers:")
    for i,j in enumerate(numbers):
        result[i]=j*j
    print("Inside Process:",result[:],v.value)
        

if __name__ == '__main__':
    arr=[2,3,8,9]
    t=time.time()

    result=multiprocessing.Array('i',4)
    v=multiprocessing.Value('d',0.0)
    p1=multiprocessing.Process(target=calc_sqrt,args=(arr,result,v))

    p1.start()

    p1.join()

    print("Outside Process:",result[:],v.value)
    print("Total time taken:",time.time()-t)