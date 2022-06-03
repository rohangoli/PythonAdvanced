# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA = headA
        tempB = headB
        
        while tempA!=tempB:
            if not tempA:
                tempA = headB
            else:
                tempA = tempA.next
                
            if not tempB:
                tempB = headA
            else:
                tempB = tempB.next
                
        return tempA
#         hashSet = set()
        
#         temp = headA
#         while temp!=None:
#             hashSet.add(id(temp))
#             temp = temp.next
            
#         temp = headB
#         while temp!=None:
#             if id(temp) in hashSet:
#                 return temp
#             temp = temp.next
            
#         return None