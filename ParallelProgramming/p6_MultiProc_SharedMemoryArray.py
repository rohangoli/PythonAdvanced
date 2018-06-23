import time
import multiprocessing

def calc_sqrt(numbers,result):
    print("Calculate Square of Numbers:")
    for i,j in enumerate(numbers):
        result[i]=j*j
    print("Inside Process:",result[:])
        

if __name__ == '__main__':
    arr=[2,3,8,9]
    t=time.time()

    result=multiprocessing.Array('i',4)
    p1=multiprocessing.Process(target=calc_sqrt,args=(arr,result))

    p1.start()

    p1.join()

    print("Outside Process:",result[:])
    print("Total time taken:",time.time()-t)