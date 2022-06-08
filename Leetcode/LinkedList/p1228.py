## Add Two Numbers

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        temp = ListNode()
        ptr1 = l1
        ptr2 = l2
        ptr3 = temp
        
        ## For Sum till List1 and List2 are of same length
        while ptr1 and ptr2:
            ptr3.val+=(ptr1.val+ptr2.val)
            if ptr3.val>9:
                ptr3.next = ListNode(1)
                ptr3.val = ptr3.val%10
            else:
                ptr3.next = ListNode()
                
            ptr3 = ptr3.next
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        
        ## For remaining numbers in List1
        while ptr1:
            ptr3.val+=ptr1.val
            if ptr3.val>9:
                ptr3.next = ListNode(1)
                ptr3.val = ptr3.val%10
            else:
                ptr3.next = ListNode()
            ptr3 = ptr3.next
            ptr1 = ptr1.next
        
        ## For remaining numbers in List2
        while ptr2:
            ptr3.val+=ptr2.val
            if ptr3.val>9:
                ptr3.next = ListNode(1)
                ptr3.val = ptr3.val%10
            else:
                ptr3.next = ListNode()
            ptr3 = ptr3.next
            ptr2 = ptr2.next
        
        ## For trailing Zero
        ptr3 = temp
        prev=None
        while ptr3.next:
            prev=ptr3
            ptr3 = ptr3.next
            
        if ptr3.val==0:
            prev.next=None
        
        return temp