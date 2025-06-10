# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1p = l1
        l2p = l2
        c = 0
        r = ListNode()
        prev = r
        while l1p or l2p:
            node = ListNode()
            sum = c
            if l1p:
                sum += l1p.val
                l1p = l1p.next
            if l2p:
                sum += l2p.val
                l2p = l2p.next
            node.val = sum % 10
            c = sum // 10
            prev.next = node
            prev = node
        if c:
            node = ListNode(val=c)
            prev.next = node
        return r.next
