## Rotate List

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        N = 0
        ptr = head
        prev = None
        while ptr:
            N+=1
            prev = ptr
            ptr = ptr.next
        last_ptr = prev
        
        k = k%N
        # print(N, k, N-k)
        if k==0:
            return head
        
        idx=0
        ptr = head
        while idx<N-k-1 and ptr:
            idx+=1
            ptr = ptr.next
            
        # print(ptr)
        if ptr.next:
            last_ptr.next = head
            head, ptr.next = ptr.next, None            
            
        return head
        
        
        
        