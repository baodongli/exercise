# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head
        l = 1
        last = head
        while last.next is not None:
            l += 1
            last = last.next
        nr = k % l

        ''' No need to perform the actual rotation
        for r in range(nr):
            last = head
            prev_last = None
            while last.next is not None:
                prev_last = last
                last = last.next
            prev_last.next = None
            last.next = head
            head = last
        '''
        new_last = head
        for r in range(l-nr-1):
            new_last = new_last.next
        last.next = head
        head = new_last.next
        new_last.next = None
                
        return head
