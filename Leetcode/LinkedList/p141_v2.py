# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:       
#         arr = []      
#         curr = head
#         while curr not in arr and curr!=None:
#             arr.append(curr)
#             curr = curr.next
            
#         if len(arr)>=1 and curr!=None:
#             return True
#         else:
#             return False
        if head is None:
            return False
        
        first = head
        second = head.next
        while first!=second:
            if not second or not second.next:
                return False
            
            first = first.next
            second = second.next.next
            
        return True