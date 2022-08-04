## Merge K Sorted Arrays

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        
        if len(lists)==1:
            return lists[0]
        
        def mergeLL(Node1, Node2):
            #print(Node1, Node2)
            ptr1 = Node1
            ptr2 = Node2
            
            head = ListNode(0)
            curr = head
            while ptr1 and ptr2:
                if ptr1.val >= ptr2.val:
                    curr.next = ptr2
                    ptr2 = ptr2.next
                else:
                    curr.next = ptr1
                    ptr1 = ptr1.next
                    
                curr = curr.next

                # if ptr1.val>=ptr2.val:
                #     temp = ptr2.next
                #     ptr2.next = ptr1
                #     ptr2 = temp
                # else:
                #     temp = ptr1.next
                #     ptr1.next = ptr2
                #     ptr1 = temp
                    
            if ptr1:
                curr.next = ptr1
                
            if ptr2:
                curr.next = ptr2
            
            #print(head)
            return head.next
        
        ll1 = lists.pop()
        while lists:
            ll2 = lists.pop()
            ll1 = mergeLL(ll1,ll2)
            
        return ll1
                
                    