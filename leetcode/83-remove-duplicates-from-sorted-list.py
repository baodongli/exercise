# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        new_head = ListNode()
        new_head.next = head
        p = head.next
        while p is not None:
            if p.val == head.val:
                head.next = p.next
                p = head.next
            else:
                head = p
                p = p.next
        return new_head.next
