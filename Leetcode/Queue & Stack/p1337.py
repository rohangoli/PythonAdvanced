## Design Circular Queue

# Example 1:
# Input
# ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 3, true, true, true, 4]

# Explanation
# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
# myCircularQueue.enQueue(1); // return True
# myCircularQueue.enQueue(2); // return True
# myCircularQueue.enQueue(3); // return True
# myCircularQueue.enQueue(4); // return False
# myCircularQueue.Rear();     // return 3
# myCircularQueue.isFull();   // return True
# myCircularQueue.deQueue();  // return True
# myCircularQueue.enQueue(4); // return True
# myCircularQueue.Rear();     // return 4

## Rohan's Implementation
class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [None for _ in range(k)]
        self.len = k
        self.head = None
        self.tail = None
        self.debug = False
        if self.debug:
            print('-'*35)
            print(self.arr)

    def enQueue(self, value: int) -> bool:
        if self.debug:
            print("Current Capacity: ",self.currCapacity())
            print("Head: {}, Tail: {}".format(self.head, self.tail))
        if self.isEmpty():
            self.head = 0
            self.tail = 0
            self.arr[self.tail] = value
        
        elif self.isFull():
            if self.debug:  print("enQueue: FULL\n")
            return False
        
        else:
            self.tail+=1
            if not self.tail < self.len:
                self.tail=0
            self.arr[self.tail] = value
        
        if self.debug:
            print("Head: {}, Tail: {}".format(self.head, self.tail)) 
            print("enQueue: ",self.arr)
            print()
        return True
        
    def deQueue(self) -> bool:
        if self.debug:
            print("Current Capacity: ",self.currCapacity())
            print("Head: {}, Tail: {}".format(self.head, self.tail))
        if self.isEmpty():
            self.head = None
            self.tail = None
            if self.debug:  print("deQueue: EMPTY\n")
            return False
        elif self.head==self.tail:
            self.arr[self.head] = None
            self.head = self.tail = None
        else:
            self.arr[self.head] = None
            self.head +=1
            if not self.head < self.len:
                self.head = 0
        if self.debug:
            print("Head: {}, Tail: {}".format(self.head, self.tail))
            print("deQueue: ",self.arr)
            print()
        return True

        
    def Front(self) -> int:
        if not self.isEmpty() and self.head!=None:
            return self.arr[self.head]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty() and self.tail!=None:
            return self.arr[self.tail]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.currCapacity()==0

    def isFull(self) -> bool:
        return self.currCapacity() == self.len

    def currCapacity(self) -> int:
        if self.tail==self.head==None:
            return 0
        elif self.tail>=self.head:
            return (self.tail - self.head + 1)
        else:
            return (self.len - self.head) + (self.tail + 1) 

## Better Leetcode Implementation
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.headIndex = 0
        self.count = 0
        self.capacity = k
        

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        self.queue[(self.headIndex + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]
        

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count - 1) % self.capacity]
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()