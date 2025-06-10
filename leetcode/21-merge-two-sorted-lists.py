# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        head = None
        tail = None

        while l1 or l2:
            addVal = 0
            if l1 and l2:
                if l1.val < l2.val:
                    addVal = l1.val
                    l1 = l1.next
                else:
                    addVal = l2.val
                    l2 = l2.next
            elif l1:
                addVal = l1.val
                l1 = l1.next
            else:
                addVal = l2.val
                l2 = l2.next
            if tail is None:
                head = tail = ListNode(addVal)
            else:
                tail.next = ListNode(addVal)
                tail = tail.next
        return head
