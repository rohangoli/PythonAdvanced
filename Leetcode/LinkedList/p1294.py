## Design Double Linked List

# Example 1:
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.debug = False
        if self.debug:  print('-'*25)

    def get(self, index: int) -> int:
        idx = 0      
        curr = self.head
        while idx<index and curr!=None:
            curr = curr.next
            idx+=1          
        if curr == None or idx!=index:
            return -1      
        return curr.val
    

    def addAtHead(self, val: int) -> None:
        
        newNode = ListNode(val)
        
        if self.head is not None:
            newNode.next = self.head
            self.head.prev = newNode
            
        self.head = newNode
        if self.debug:  self.printLinkedList("addAtHead")  
        return None

    def addAtTail(self, val: int) -> None:
        
        newNode = ListNode(val)
        
        curr=self.head
        while curr!=None and curr.next!=None:
            curr = curr.next
        
        if curr is not None:
            newNode.prev = curr
            curr.next = newNode
        else:
            self.head = newNode
        if self.debug:  self.printLinkedList("addAtTail")  
        return None


    def addAtIndex(self, index: int, val: int) -> None:        
        if self.head is None and index>0:
            return None
        
        if self.head is None or index==0:
            self.addAtHead(val)
            return None
        
        idx=0
        curr = self.head
        while curr.next!=None and idx<index:
            curr = curr.next
            idx+=1
            
        if curr.next==None and idx+1==index:
            self.addAtTail(val)
            return None
        
        newNode = ListNode(val)
        newNode.prev = curr.prev
        newNode.next = curr
        # print(id(newNode.prev), id(newNode.next))
        # print(newNode.prev.val, newNode.next.val)
        
        newNode.prev.next, newNode.next.prev = newNode, newNode
        if self.debug:  self.printLinkedList("addAtIndex({})".format(index))      
        return None

    def deleteAtIndex(self, index: int) -> None:
        if self.head==None or (self.head.next==None and index==0):
            self.head = None
            return None
        
        if self.head is None and index>0:
            return None
        
        if index==0 and self.head.next:
            self.head.next.prev = None
            self.head = self.head.next
            return None
        
        idx=0
        curr = self.head
        while curr.next!=None and idx<index:
            curr = curr.next
            idx+=1
            
        if index>idx:
            return None
            
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        if self.debug:  self.printLinkedList("deleteAtIndex({})".format(index))      
        return None

    
    def printLinkedList(self, action: str) -> None:
        print(action, end=" ::: [ ")
        curr = self.head
        while curr!=None:
            print(curr.val, end=" ")
            curr=curr.next
            if curr:
                print('<->', end=" ")
        print(']')
        return None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)