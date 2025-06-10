# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        prev = None
        while p:
            nn = None
            if p.next is not None:
                nn = p.next.next
                p.next.next = p
                if prev is None:
                    head = p.next
                else:
                    prev.next = p.next
                prev = p
                p.next = nn
            p = nn
        return head
