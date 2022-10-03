## Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempHead = ListNode(0, next=head)
        
        def helper(node, head):
            if not node or not node.next or not node.next.next:
                return head
            
            c0N = node
            c1N = node.next
            c2N = node.next.next
            
            c0N.next = c2N
            c1N.next = c2N.next
            c2N.next = c1N
            
            return helper(c0N.next.next, head)
        
        return helper(tempHead, tempHead).next