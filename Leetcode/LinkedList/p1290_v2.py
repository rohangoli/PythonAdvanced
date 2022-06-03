class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        
        # print('-'*20)

    def get(self, index: int) -> int:
        idx=0
        curr=self.head
        
        while idx<=index and curr!=None:
            if idx == index:
                # self.printLinkedList("get({}) = {}".format(index,curr.val))
                return curr.val
            curr = curr.next
            idx+=1
        # self.printLinkedList("get({}) = -1".format(index))
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)

        if self.head==None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        # self.printLinkedList("addAtHead")
        return None

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        curr = self.head

        if curr==None:
            self.head = newNode
            # self.printLinkedList("addAtTail")
            return None
        
        while curr.next!=None:
            curr = curr.next

        curr.next = newNode
        # self.printLinkedList("addAtTail")
        return None

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)

        curr = self.head

        if index==0:
            newNode.next = self.head
            self.head = newNode
            # self.printLinkedList("addAtIndex({})".format(index))
            return None
        elif curr==None and index>0:
            return None

        idx=0
        prev=curr
        while idx<=index and curr!=None:
            if idx==index:
                newNode.next = prev.next
                prev.next = newNode
                # self.printLinkedList("addAtIndex({})".format(index))
                return None
            prev = curr
            curr = curr.next
            idx+=1
        if idx==index:
            prev.next = newNode
        # self.printLinkedList("addAtIndex({})".format(index))
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
        # self.printLinkedList("deleteAtIndex({})".format(index))
        return None
    
    def printLinkedList(self, action: str) -> None:
        print(action, end=" ::: [ ")
        curr = self.head
        while curr!=None:
            print(curr.val, end=" ")
            curr=curr.next
            if curr:
                print('->', end=" ")
        print(']')
        return None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)