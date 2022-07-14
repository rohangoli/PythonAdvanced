## 1290. Convert Binary Number in a Linked List to Integer

# Example 1:
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# Example 2:
# Input: head = [0]
# Output: 0

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        if not head:
            return 0
        
        N = 0
        curr = head
        while curr:
            curr = curr.next
            N+=1
        
        #print(N)
        
        curr = head
        result = 0
        while curr:
            result+= (curr.val)*(2**(N-1))
            curr = curr.next
            N-=1
            
        return result
        