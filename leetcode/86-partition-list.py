# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = ListNode()
        new_head.next = head
        tail = new_head
        p = head
        prev = None
        while p is not None and p.val < x:
            tail = p
            prev = p
            p = p.next
        while p is not None:
            while p is not None and p.val >= x:
                prev = p
                p = p.next
            if p:
                prev.next = p.next
                p.next = tail.next
                tail.next = p
                tail = p
                p = prev.next
            #r = []
            #rp = new_head.next
            #while rp:
            #    r.append(rp.val)
            #    rp = rp.next
            #print(r)
            
        return new_head.next
