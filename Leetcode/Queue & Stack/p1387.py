## Implement Stack using Queues

# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False

class MyStack:

    def __init__(self):
        self.queue = []
        self.tempQ = []
        print('-'*25)
        
    def push(self, x: int) -> None:
        if self.empty():
            self.tempQ.append(x)
        else:
            self.queue.append(self.tempQ.pop(0))
            self.tempQ.append(x)
        #print("push: ", self.queue, self.tempQ)

    def pop(self) -> int:
        if self.empty():
            return None
        else:
            #print('popS: ', self.queue, self.tempQ)
            temp = self.tempQ.pop(0)
            #print('popI: ', self.queue, self.tempQ)
            i=0
            while self.queue:
                self.tempQ.append(self.queue.pop(0))
                i+=1
            #print('popI: ', self.queue, self.tempQ)
            j=0
            while j<i-1:
                self.queue.append(self.tempQ.pop(0))
                j+=1
            #print('popE: ', self.queue, self.tempQ)
            return temp

    def top(self) -> int:
        if self.empty():
            return None
        else:
            return self.tempQ[0]

    def empty(self) -> bool:
        if len(self.queue)+len(self.tempQ)==0:
            return True
        else:
            return False
        
## Better Implementation - LeetCode
class MyStack_V2:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.to = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.to = x
            

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.to = self.q1.pop(0)
            self.q2.append(self.to)
        num = self.q1.pop()
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        
        return num
        
        
    def top(self) -> int:
        return self.to

    def empty(self) -> bool:
        return not self.q1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()