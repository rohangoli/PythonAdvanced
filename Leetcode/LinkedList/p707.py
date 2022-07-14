## 707. Design Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        # self.printLinkedList()
        temp=0
        curr = self.head
        while temp!=index and curr!=None:
            curr = curr.next
            temp+=1
        if curr==None or temp!=index:
            return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        # self.printLinkedList()
        return None

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        curr = self.head
        prev=None
        while curr!=None:
            prev=curr
            curr=curr.next
            
        if prev==None:
            self.head = newNode
        else:
            prev.next = newNode
        # self.printLinkedList()
        return None

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        curr = self.head
        temp=0
        prev=None
        while temp!=index and curr!=None:
            prev = curr
            curr = curr.next
            temp+=1
        
        if prev==None:
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.next = prev.next
            prev.next = newNode
        # self.printLinkedList()
        return None
        

    def deleteAtIndex(self, index: int) -> None:
        temp = 0
        curr = self.head
        prev=None
        while temp!=index and curr!=None:
            prev = curr
            curr=curr.next
            temp+=1
            
        if temp!=index or curr==None:
            return None
            
        if prev == None:
            self.head=self.head.next
        else:
            prev.next=curr.next
        # self.printLinkedList()
        return None
    
    def printLinkedList(self) -> None:
        
        curr = self.head
        while curr!=None:
            print(curr.val,"->",end=" ")
            curr=curr.next
        print('\n','-'*20)
        return None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)