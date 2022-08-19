## Insertion Sort List - Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        newH = ListNode()
        curr = head
        while curr:
            prev = newH
            while prev.next and prev.next.val<curr.val:
                prev = prev.next
                
            next = curr.next
            
            curr.next = prev.next
            prev.next  = curr
            
            curr = next
            
        return newH.next
        