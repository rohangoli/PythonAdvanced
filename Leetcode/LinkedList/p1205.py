## Reverse Linked List

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        curr = head.next
        prev = head
        
        while curr!=None:
            prev.next = curr.next
            curr.next = head
            head = curr
            curr = prev.next
            
        return head