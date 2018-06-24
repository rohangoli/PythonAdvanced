# Multi Processing Pool -> Map & Reduce
import time
from multiprocessing import Pool

def calc_square(n):
    return n*n

def codebreaker(n):
    sum = 0
    for i in range(n):
        sum +=i*i
    return sum

if __name__ == "__main__":
    arr = [2,3,8,9]

    p=Pool()
    t=time.time()
    #result = p.map(calc_square,arr)
    result = p.map(codebreaker,range(10000))
    p.close()
    p.join()

    print("Parallel Processing Time taken: ",time.time()-t)

    t2=time.time()
    result2=[]
    for i in range(10000):
        result2.append(codebreaker(i))
    print("Serial Processing Time Taken: ",time.time()-t2)