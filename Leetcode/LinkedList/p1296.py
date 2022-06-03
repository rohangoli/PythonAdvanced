## Remove Nth Node From End of List

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = second = first = ListNode(0,head)
        
        i=0
        while i<n:
            first = first.next
            i+=1
            
        while first.next:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        
        return dummy.next
        
        # if head.next is None:
        #     return None
        
#         idx = head
#         follow = head
        
#         N=1
#         while idx.next != None:
#             print(idx.val, follow.val, sep='-')
#             if N>n:
#                 follow = follow.next
#             N+=1
#             idx = idx.next

#         print(follow.val, idx.val, sep='|')
#         follow.next=idx
#         print('-'*20)
#         return head
        
        
#         ptr = slwptr = head
#         N=1
#         prev2 = None
#         prev=None
#         while ptr!=None: 
#             if N>n:
#                 prev=slwptr
#                 slwptr = slwptr.next
#             N+=1
#             prev2 = ptr
#             ptr = ptr.next
        
#         if prev != None:
#             print(id(prev), prev.val)
#             print(id(prev2), prev2.val)
#             print('-'*15)
#             prev.next = prev2
#             return head
        
#         print(id(prev2), prev2.val)
#         print('-'*15)
        
#         return None
        