# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or left == right:
            return head
        new_head = ListNode()
        new_head.next = head
        lp = head
        head = new_head
        count = 1
        while count < left:
            head = lp
            lp = lp.next
            count += 1
        rp = lp.next
        while count < right:
            lp.next = rp.next
            rp.next = head.next
            head.next = rp
            rp = lp.next
            count += 1
        return new_head.next
