## Flatten a Multilevel Doubly Linked List

# Example 1:
# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]
# Explanation: The multilevel linked list in the input is shown.
# After flattening the multilevel linked list it becomes:

# Example 2:
# Input: head = [1,2,null,3]
# Output: [1,3,2]
# Explanation: The multilevel linked list in the input is shown.
# After flattening the multilevel linked list it becomes:

# Example 3:
# Input: head = []
# Output: []
# Explanation: There could be empty list in the input.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ## Rohan's Implementation - Double Traversal
        if head is None:
            return None

        ptr1 = head
        #prev1 = None
        while ptr1 != None:
            if ptr1.child:
                ptr2 = ptr1.child
                prev2 = None
                while ptr2 !=None:
                    prev2 = ptr2
                    ptr2 = ptr2.next
                
                prev2.next = ptr1.next
                if ptr1.next:          
                    ptr1.next.prev = prev2
                
                ptr1.next = ptr1.child
                ptr1.child.prev = ptr1
                ptr1.child = None
            
            #prev = ptr1
            ptr1 = ptr1.next
        
        # curr = head
        # while curr:
        #     print(curr.val,' <-> ',end="")
        #     # print(curr.prev,curr,curr.next, curr.child,sep=' - ')
        #     curr = curr.next
        # print('\n','-'*25)
        
        return head
        
#         tempStack = []
        
#         temp = Node()
        
#         curr = head
#         prev = None
#         while curr:
#             temp.val = curr.val
#             temp.next = Node()
#             temp.prev = prev
#             prev = temp
#             temp = temp.next
#             if curr.child:
#                 tempStack.append(curr.next)
#                 curr = curr.child
#                 continue
            
#             if not curr.next and tempStack!=[]:
#                 curr = tempStack.pop()
#                 continue
            
#             curr = curr.next
                
#         return temp

    ## Single Traversal
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dummy = Node(-1, None, None, None)
        prev = dummy
        stack = [head]
        
        while stack:
            node = stack.pop()
            
            node.prev = prev
            prev.next = node
            if node.next:
                stack.append(node.next)
                node.next = None            
            if node.child:
                stack.append(node.child)
                node.child = None

            prev = node
        dummy.next.prev = None
        return dummy.next