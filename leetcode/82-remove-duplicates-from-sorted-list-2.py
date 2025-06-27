# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        p = head
        new_head = ListNode()
        new_head.next = head
        head = new_head
        p = head.next
        while p is not None:
            delp = False
            while p.next is not None and p.next.val == p.val:
                p.next = p.next.next
                delp = True
            if delp:
                head.next = p.next
            else:
                head = p
            p = head.next
        return new_head.next
