## Copy List with Random Pointer

# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a linked list with random pointer.
class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return True
    
    def copyRandomList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        ptr = head
        while ptr:
            ptr2 = ListNode(ptr.val,ptr.next)
            ptr.next = ptr2
        
            ptr = ptr2.next
            
        ptr = head
        while ptr:
            if ptr.random == None:
                ptr.next.random = None
            else:
                ptr.next.random = ptr.random.next
            
            ptr = ptr.next.next
        
        ptr = head.next
        while ptr:
            if ptr.next:
                if ptr.next.next:
                    ptr.next = ptr.next.next
                else:
                    ptr.next = None
            ptr = ptr.next
        
        head = head.next
            
#         ptr = head
#         while ptr:
            
#             if ptr.random:
#                 print(ptr, ptr.val, ptr.random, ptr.random.val, sep=' - ', end =' ')
#             else:
#                 print(ptr, ptr.val, ptr.random, sep=' - ', end =' ')
#             print()
            
#             ptr = ptr.next

        
        return head