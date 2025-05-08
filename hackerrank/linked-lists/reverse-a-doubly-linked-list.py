def reverse(llist):
    # Write your code here
    head = llist
    p = llist.next
    head.next = None
    while p is not None:
        new_head = p
        p = p.next
        new_head.next = head
        new_head.prev = None
        head.prev = new_head
        head = new_head
    return head
