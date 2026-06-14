# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        res = False

        p1=head
        p2=head.next

        while p1 and p2:
            if p1.val ==p2.val:
                res = True
                break
            p1 = p1.next
            p2= p2.next
            if not p2 or not p1:
                break
            p2=p2.next
        
        return res

        