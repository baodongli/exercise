# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        p = head
        length = 1
        while p.next is not None:
            length += 1
            p = p.next
        if length < n:
            return head
        
        if length == n:
            head = head.next
        elif length > n:
            i = 1
            p = head
            while i < length - n:
                p = p.next
                i += 1
            p.next = p.next.next
        return head
