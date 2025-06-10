# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        newhead = ListNode(next=head)
        knext_head = head
        ktail = newhead
        while knext_head is not None:
            p = knext_head
            pos = 1
            while p.next is not None and pos < k:
                pos += 1
                p = p.next
            if pos < k:
                ktail.next = knext_head
                break
            slhead = knext_head
            knext_head = p.next
            pos = 1
            p = slhead.next
            slhead.next = None
            next_ktail = slhead
            while pos < k:
                pos += 1
                next = p.next
                p.next = slhead
                slhead = p
                p = next
            ktail.next = slhead
            ktail = next_ktail
            
        return newhead.next
