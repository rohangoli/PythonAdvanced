import time
import multiprocessing

def calc_sqrt(numbers,q):
    print("Calculate Square of Numbers:")
    for i in numbers:
        q.put(i*i)

if __name__ == '__main__':
    arr=[2,3,8,9]

    t=time.time()

    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=calc_sqrt,args=(arr,q))

    p1.start()
    p1.join()

    while q.empty() is False:
        print(q.get())

    print("Total time taken:",time.time()-t)