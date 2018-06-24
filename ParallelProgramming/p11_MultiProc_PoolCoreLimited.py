import time
from multiprocessing import Pool

def codebreaker(n):
    sum=0
    for i in range(n):
        sum+=i*i
    return sum

if __name__=="__main__":
    t=time.time()
    p=Pool(processes=1)
    #result=p.imap_unordered(codebreaker,[1,2,3,4,5])
    result=p.map(codebreaker,[1,2,3,4,5])
    p.close()
    p.join()
    print("Time Taken: ",time.time()-t)