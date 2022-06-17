## Implement Queue using Stacks

# Example 1:
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

class MyQueue:

    def __init__(self):
        self.stack = []
        self.tempStack = []
        self.top = None

    def push(self, x: int) -> None:
        if not self.top:
            self.top = x
        self.stack.append(x)
        #print("push: ",self.stack)

    def pop(self) -> int:
        
        if self.empty():
            return None
        
        #print("popS: ", self.stack)
        while self.stack:
            self.tempStack.append(self.stack.pop())
        #print("popTS: ",self.tempStack)
        
        temp = self.tempStack.pop()
        
        if self.tempStack:
            self.top = self.tempStack[-1]
        else:
            self.top = None
            
        while self.tempStack:
            self.stack.append(self.tempStack.pop())
        #print("popS: ",self.stack)    
        return temp
        

    def peek(self) -> int:
        if not self.empty():
            return self.top
        else:
            return None

    def empty(self) -> bool:
        if len(self.stack)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()