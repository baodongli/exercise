# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = tail = None
        h = []
        for l in lists:
            if l:
                heappush(h, (l.val, id(l), l))
        
        while h:
            val, _, l = heappop(h)
            node = ListNode(val)
            if head is None:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next
            if l.next:
                heappush(h, (l.next.val, id(l.next), l.next))
        return head

