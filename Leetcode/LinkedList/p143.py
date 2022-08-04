## Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        tempS = []
        while curr:
            tempS.append(curr)
            curr = curr.next
            
        flip = True
        curr = tempS.pop(0)
        while tempS:
            if flip:
                flip = False
                temp = tempS.pop()
                #print(curr.val, temp.val)
                curr.next = temp
                curr = temp
            else:
                flip = True
                temp = tempS.pop(0)
                #print(curr.val, temp.val)
                curr.next = temp
                curr = temp
        curr.next = None
                