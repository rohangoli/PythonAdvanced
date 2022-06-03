## Linked List Cycle II

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Example 2:
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Example 3:
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        slow=fast=head
        while fast.next and fast.next.next:
            print(slow.val, fast.val, sep=' - ')   
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                print(slow.val, fast.val, sep=' - ')  
                break
        print('-'*15)
                
        if not fast.next or not fast.next.next:
            return None
        
        fast2 = head
        while fast2!=slow:
            print(slow.val, fast2.val, sep=' - ')  
            fast2=fast2.next
            slow=slow.next
        print(slow.val, fast2.val, sep=' - ')
        print('='*15)   
        return fast2