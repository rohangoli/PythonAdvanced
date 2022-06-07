## Odd Even Linked List

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# Example 2:
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        ptr1 = head
        ptr2 = head.next
        temp = ptr2
        
        while ptr1 and ptr2:
            if ptr1.next:
                ptr1.next = ptr1.next.next
                ptr1 = ptr1.next
                
            if ptr2.next:
                ptr2.next = ptr2.next.next
                ptr2 = ptr2.next
            
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = temp
        
#         even = head.next
#         odd = head
#         idx=0
#         curr = head
#         while curr!=None:
#             if idx%2==0:
#                 odd.next = curr
#                 odd = curr
#             else:
#                 even.next = curr
#                 even = curr
#             idx+=1
#             curr = curr.next
            
#         odd.next = even
        
        return head