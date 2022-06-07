## Palindrome Linked List

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head is None or head.next is None:
            return head
        
        temp = ListNode()
        curr = head
        ptr2 = temp
        while curr!=None:
            ptr2.val = curr.val
            ptr2.next = ListNode()
            ptr2 = ptr2.next
            curr = curr.next
            
        curr=head.next
        prev=head
        while curr!=None:
            prev.next = curr.next
            curr.next = head
            head = curr

            curr = prev.next
            
        ptr1=head
        ptr2=temp
        while ptr1 and ptr2:
            if ptr1.val!=ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return True

    def isPalindrome_V2(self, head: Optional[ListNode]) -> bool:
        ## OPTIMIZED from leetcode/LinkedList/p1209.py
        rev = None
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        if fast:
            slow = slow.next
            
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
            
        return not rev
        