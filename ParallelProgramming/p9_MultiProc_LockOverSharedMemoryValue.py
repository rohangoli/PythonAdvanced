import time
import multiprocessing

def deposit(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1 
        lock.release()

if __name__ == "__main__":
    balance = multiprocessing.Value('i',400)
    lock = multiprocessing.Lock()

    proc1 = multiprocessing.Process(target=deposit,args=(balance,lock,))
    proc2 = multiprocessing.Process(target=withdraw,args=(balance,lock,))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

    print("End of Transactions: ",balance.value)