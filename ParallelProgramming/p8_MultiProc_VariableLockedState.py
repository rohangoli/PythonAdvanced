import time
import multiprocessing

def deposit(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value + 1

def withdraw(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value - 1 

if __name__ == "__main__":
    balance = multiprocessing.Value('i',400)
    proc1 = multiprocessing.Process(target=deposit,args=(balance,))
    proc2 = multiprocessing.Process(target=withdraw,args=(balance,))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

    print("End of Transactions: ",balance.value)