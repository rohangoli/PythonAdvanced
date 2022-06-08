## Merge Two Sorted Linked Lists

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        temp = ListNode()
        
        ptr1 = list1
        ptr2 = list2
        ptr3 = temp
        while ptr1 and ptr2:
            
            if ptr1.val<= ptr2.val:
                ptr3.val = ptr1.val
                ptr1 = ptr1.next  
            else:
                ptr3.val = ptr2.val
                ptr2 = ptr2.next
                
            ptr3.next = ListNode()
            ptr3 = ptr3.next
            
        if ptr1:
            ptr3.val = ptr1.val
            ptr3.next = ptr1.next
        else:
            ptr3.val = ptr2.val
            ptr3.next = ptr2.next
            
        return temp
    
    def printList(self, listA: Optional[ListNode]) -> None:
        curr = listA
        while curr!=None:
            print(curr.val,'->',end ='')
            curr = curr.next
        print('')
        return None
                 