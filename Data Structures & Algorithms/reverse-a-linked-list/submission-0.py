# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        prev = None
        current = head
        nex = current.next

        while current is not None:
            current.next = prev
            prev=current
            current = nex

            if nex is not None:
                nex = nex.next

        return prev


        